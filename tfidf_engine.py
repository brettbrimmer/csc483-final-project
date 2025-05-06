import collections
import math
import argparse
import os
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

def calculate_tf(term, document):
    result = 1 + math.log(document.count(term), 10)
    return result


def calculate_idf(document_count, df):
    if (df != 0):
        result = math.log(document_count / df)
    else:
        result = 0

    return result;

class IRSystem:

    def __init__(self, folder_path):
        # Use lnc to weight terms in the documents:
        #   l: logarithmic tf
        #   n: no df
        #   c: cosine normalization

        # Store the vecorized representation for each document
        #   and whatever information you need to vectorize queries in _run_query(...)

        # YOUR CODE GOES HERE
        ## we'll keep track of:
        ## df: how many documents each term appears in at least once
        ## lnc: the score for a term in a specific document
        ## c_sum: denominator for cosine normalization
        self.df = collections.defaultdict(int)  # term -> document frequency(float)
        self.document_count = 0
        self.lnc = collections.defaultdict(lambda: collections.defaultdict(float))  # doc_id -> term -> lnc(float)
        self.c_sum = collections.defaultdict(
            float)  # doc_id -> sum of all ltn weights in a document # this will be the denominator for the cosine normalization. square root of (weight of all sums squared)
        total_weight = collections.defaultdict(float) # just for calculating total weight of a term across all documents for written HW

        #### Work Area ####
        ## TODO: We must allow this area to parse documents in this format:
        """
        
        [[Nugent, Texas]]

        CATEGORIES: Unincorporated communities in Jones County, Texas, Unincorporated communities in Texas, Abilene metropolitan area
        
        Nugent is an unincorporated community in Jones County, Texas, United States. According to the Handbook of Texas, the community had an estimated population of 41 in 2000.[tpl]cite web | url = http://www.tshaonline.org/handbook/online/articles/NN/hnn42.html | title = Nugent, Texas | work = | publisher = The Handbook of Texas online | date =  | accessdate = 2009-11-11[/tpl] It is part of the Abilene, Texas Metropolitan Statistical Area.
        The Lueders-Avoca Independent School District serves area students.
        
        ==Climate==
        
        The climate in this area is characterized by hot, humid summers and generally mild to cool winters.  According to the Köppen Climate Classification system, Nugent has a humid subtropical climate, abbreviated "Cfa" on climate maps.Climate Summary for Nugent, Texas
        
        ==References==
        
        """
        ## TODO: Iterate through files from enwiki-20140602-pages-articles.xml-0005.txt to enwiki-20140602-pages-articles.xml-1259.txt
        ## (instead of just one file.)
        ## For each file, set its docid tp the string in [[brackets]] instead of an integer
        ## We can just consume the rest of it as text, then when we reach [[brackets]] again we know that's a new document
        ## when we reach EOF, obviously we just go to the next file

        doc_id = "" # keeps track of which wikipedia doc we are adding terms to

        print("About to enter file loop")

        # calculate the tf for all documents



        """
        for i in range(5,1260):
            ## Create file path with correct number of leading zeros so the number is 4 digits
            file_path = os.getcwd() + "\\" + folder_path + "\\" + "enwiki-20140602-pages-articles.xml-"
            digit_count = len(str(i))
            zeros_to_add = 4 - digit_count

            for i in range(zeros_to_add):
                file_path += "0"

            file_path += str(i)

            print("going to try to open file at " + file_path)
            """
        # open the file
        try:

            for filename in sorted(os.listdir(folder_path)):
                file_path = os.path.join(folder_path, filename)


                print("Going to try to open file now")

                # f = open(file_path)
                f = open(file_path, 'r', encoding='utf-8')

                print(f"file {file_path} opened successfully!!")

                # new_doc_started = False # lets us know whether to add to df later on

                doc_terms = []

                for line in f:
                    # print("Looking at line" + line)
                    # print("next line")

                    # if(len(line) > 4):
                        # print("This line ends with " + line[-4])

                    # if line.startswith('[[') and line.endswith(']]'):
                    # if(line.startswith('[[') and ']]' in line):
                    if (line.startswith('[[') and ']]' in line[-4:] and "Image:" not in line): # some images start with [[ and end in ]], we don't want to count that as a document title
                        # print("Found a line that starts with [[ and ends with ]]")
                        
                        # Calculate df and lnc for previous doc_id and its terms
                        if doc_id != "": # skip for first iteration
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
                        line = line[2:len(line)-2]
                        doc_id = line

                        # print("Next doc_id: " + doc_id)

                        # Increase doc count
                        self.document_count += 1

                        # Reset doc terms
                        doc_terms = []
                    else:
                        doc_terms += line.lower().split()
                        # doc_terms = line.lower().split()  # removed lower() on 4/5/25
                        # doc_id = int(doc_terms[0])
                        # doc_wordcount = len(doc_terms)
                        # self.document_count += 1

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
                if (self.c_sum[doc_id] != 0): # if this term has a weight of 0, its c_sum will be 0, so we don't want to divide by 0
                    self.lnc[doc_id][key] = self.lnc[doc_id][key] / self.c_sum[doc_id]
                else:
                    self.lnc[doc_id][key] = 0
                total_weight[key] += self.lnc[doc_id][key]

    def run_query(self, query):
        print("In run_query!")
        terms = query.lower().split()  # removed lower(). on 4/5/25
        return self._run_query(terms)

    def _run_query(self, terms):
        # Use ltn to weight terms in the query:
        #   l: logarithmic tf
        #   t: idf
        #   n: no normalization

        # Return the top-10 document for the query 'terms'
        result = []

        # YOUR CODE GOES HERE
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
        top_50_results = sorted(cosine_similarity, key=cosine_similarity.get, reverse=True)

        print(f"Items for {terms}: ")

        for i in range(len(top_50_results)):
            if(i < 50):
                print(f"Item {i}: {top_50_results[i]}")

        # Return the top 10 results
        return top_50_results[:50]


def main(corpus):
    ir = IRSystem(corpus) ## passes along the path to the folder of wikisubset files

    print("In main!")

    while True:
        query = input('Query: ').strip()
        if query == 'exit':
            break
        results = ir.run_query(query)
        print(results)

    ## the corpus is selected in test_boolean_queries.py on this line:
    ## ir = tfidf_engine.IRSystem(open("wiki-small.txt"))
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("CORPUS",
                        help="Path to file with the corpus")
    args = parser.parse_args()
    main(args.CORPUS)