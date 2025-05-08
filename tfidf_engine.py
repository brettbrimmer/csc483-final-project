import collections
import math
import argparse
import os
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.tokenize import PunktTokenizer
import time
from openai import OpenAI
# from openai.error import RateLimitError
from openai import RateLimitError

my_api_key = os.getenv("OPENAI_API_KEY")

ps = PorterStemmer()

client = OpenAI(api_key=my_api_key)

# queries OpenAI with a question (a string), and asks it to determine the answer from the results list (a list of strings)
# returns the string of the result picked by openai
def query_openai(question, results):
    prompt = (
        f"Give me the answer to the question with one of the strings from the following list. "
        f"Only give one answer. Only give the answer itself as a response, don't say anything else at all. Here is the question: {question} "
        f"and here is the list: {results}"
    )

    try:
        response = client.responses.create(
            model="gpt-4.1",
            # model="gpt-3.5-turbo",
            input=prompt
        )
        return response.output_text
    except RateLimitError:
        print("Rate limit hit. Waiting 10 seconds...")
        time.sleep(10)
        return query_openai(question, results)

# performs porter-stemmer on a string 'token'. if the string was all-non-alphanumeric, turns that token into an empty string
# returns the modified string
def stem_token(token):
    my_token = ps.stem(token)

    # these stop words were removed as they were inefffective at improving the results
    """
    if(len(my_token) == 1
        or token.lower() == "the"
        or token.lower() == "an"
        or token.lower() == "and"
        or token.lower() == "in"
        or token.lower() == "to"
        or token.lower() == "is"
        or token.lower() == "are"
        or token.lower() == "was"
        or token.lower() == "were"
        or token.lower() == "it"
        or token.lower() == "that"
        or token.lower() == "this"
        or token.lower() == "with"
        or token.lower() == "as"
        or token.lower() == "for"
        or token.lower() == "by"
        or token.lower() == "be"
        or token.lower() == "at"
        or token.lower() == "don"       # terms with apostrophes that will be weird when stemmed
        or token.lower() == "won"
        or token.lower() == "she"
        or token.lower() == "he"
        or token.lower() == "we"
        or token.lower() == "you"
        or token.lower() == "it"
        or token.lower() == "they"
        or token.lower() == "hasn"
        or token.lower() == "hadn"
    ):
        my_token = ""
        """

    # if it's all non-alphanumeric, turn it into an empty string
    if all(not char.isalnum() for char in my_token):
        my_token = ""

    return my_token;

# calculates term frequency formula given a term and document
def calculate_tf(term, document):
    result = 1 + math.log(document.count(term), 10)
    return result

# calculates idf formula given a document count and a document frequency
def calculate_idf(document_count, df):
    if (df != 0):
        result = math.log(document_count / df)
    else:
        result = 0

    return result;

# information retrieval system
class IRSystem:

    def __init__(self, folder_path):
        # Use lnc to weight terms in the documents:
        #   l: logarithmic tf
        #   n: no df
        #   c: cosine normalization

        # Store the vecorized representation for each document
        #   and whatever information you need to vectorize queries in _run_query(...)

        ## we'll keep track of:
        ## df: how many documents each term appears in at least once
        ## lnc: the score for a term in a specific document
        ## c_sum: denominator for cosine normalization
        self.df = collections.defaultdict(int)  # term -> document frequency(float)
        self.document_count = 0
        self.lnc = collections.defaultdict(lambda: collections.defaultdict(float))  # doc_id -> term -> lnc(float)
        self.c_sum = collections.defaultdict(
            float)  # doc_id -> sum of all ltn weights in a document # this will be the denominator for the cosine normalization. square root of (weight of all sums squared)
        total_weight = collections.defaultdict(
            float)  # just for calculating total weight of a term across all documents for written HW

        doc_id = ""  # keeps track of which wikipedia doc we are adding terms to

        print("About to enter file loop")

        # open the file
        try:
            for filename in sorted(os.listdir(folder_path)):
                file_path = os.path.join(folder_path, filename)

                print("Going to try to open file now")
                with open("printstatements.txt", "a") as newFile: newFile.write("Opening a file...\n\n")

                f = open(file_path, 'r', encoding='utf-8')

                print(f"file {file_path} opened successfully!!")

                doc_terms = []

                for line in f:
                    if (line.startswith('[[') and ']]' in line[
                                                          -4:] and "Image:" not in line):  # some images start with [[ and end in ]], we don't want to count that as a document title
                        # Calculate df and lnc for previous doc_id and its terms
                        if doc_id != "":  # skip for first iteration
                            for term in set(doc_terms[1:]):
                                if term != '-':
                                    # add to doc frequency
                                    # if new_doc_started == True:
                                    self.df[term] += 1
                                    # new_doc_started = False

                                    self.lnc[doc_id][term] = calculate_tf(term,
                                                                          doc_terms)  # the l of the lnc. we can ignore n because it's 1. will multiply by c later

                        # set the new doc_id to the title of the wikipedia article
                        line = line.strip()
                        line = line[2:len(line) - 2]
                        doc_id = line

                        # Increase doc count
                        self.document_count += 1

                        # Reset doc terms
                        doc_terms = []
                    else:
                        tokens = word_tokenize(line.lower())  # ps
                        stemmed_tokens = [stem_token(token) for token in tokens]  # ps
                        doc_terms += stemmed_tokens  # ps

                print("closing file...")

                f.close()
        except FileNotFoundError:
            print(f"File not found at {file_path}")
        except PermissionError:
            print(f"Permission denied to read the file at {file_path}.")
        except OSError:
            print(f"An error occurred: {e}")

        # calculate c_sum
        for doc_id in self.lnc.keys():
            for weight in self.lnc[doc_id].values():  # iterate over all lnc values for all terms
                # Add weights
                self.c_sum[doc_id] += math.pow(weight, 2)

            # square root c_sum
            self.c_sum[doc_id] = math.sqrt(self.c_sum[doc_id])

        for doc_id in self.lnc.keys():  # iterate over all doc_ids in the doc_id hashmap
            for key in self.lnc[doc_id].keys():  # iterate over all terms in the lnc hashmap
                if (self.c_sum[
                    doc_id] != 0):  # if this term has a weight of 0, its c_sum will be 0, so we don't want to divide by 0
                    self.lnc[doc_id][key] = self.lnc[doc_id][key] / self.c_sum[doc_id]
                else:
                    self.lnc[doc_id][key] = 0
                total_weight[key] += self.lnc[doc_id][key]

    # run a query for a string 'query'
    def run_query(self, query):
        print("In run_query!")
        tokens = word_tokenize(query.lower())  # ps
        terms = [stem_token(token) for token in tokens]  # ps

        return self._run_query(terms, query)

    # helper function that actually performs the query
    def _run_query(self, terms, query):
        # Use ltn to weight terms in the query:
        #   l: logarithmic tf
        #   t: idf
        #   n: no normalization

        # Return the top-10 document for the query 'terms'
        result = []

        ## each query term will have an ltn value, based on its tf (term frequency) and idf (inverse document frequency) value
        doc_wordcount = len(terms)
        ltn = collections.defaultdict(float)

        ## calculate ltn
        for term in terms:
            if term != '-':
                temp_tf = calculate_tf(term, terms)  # the l in ltn
                temp_idf = calculate_idf(self.document_count, self.df[term])  # the t in ltn
                ltn[term] = temp_tf * temp_idf  # the ltn. ignore n because it's 1

        cosine_similarity = collections.defaultdict(float)

        ## now we calculate the cosine similarity for each query term against the same term in each document
        ## we add them up for each document, giving each document its cosine similarity score
        for term in ltn.keys():  # for each term
            for doc_id in self.lnc.keys():  # for each doc_id
                cosine_similarity[doc_id] += ltn[term] * self.lnc[doc_id][term]

        # Sort the cosine similarity values in descending order
        top_850_results = sorted(cosine_similarity, key=cosine_similarity.get, reverse=True)

        top_850_results = top_850_results[:850]

        final_answer = ""
        final_answer = query_openai(query, top_850_results)

        return final_answer

# main method that passes along the corpus to the IRSystem class and runs the query
def main(corpus):
    ir = IRSystem(corpus)  ## passes along the path to the folder of wikisubset files

    with open("printstatements.txt", "a") as newFile: newFile.write("In main!\n\n")

    while True:
        query = input('Query: ').strip()
        if query == 'exit':
            break
        results = ir.run_query(query)
        print(results)

# calls main with corpus
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("CORPUS",
                        help="Path to file with the corpus")
    args = parser.parse_args()
    main(args.CORPUS)