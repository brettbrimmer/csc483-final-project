import collections
import math
import argparse

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

    def __init__(self, f):
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

        # calculate the tf for all documents
        for line in f:
            doc_terms = line.lower().split()  # removed lower() on 4/5/25
            doc_id = int(doc_terms[0])
            doc_wordcount = len(doc_terms)
            self.document_count += 1

            for term in set(doc_terms[1:]):
                if term != '-':
                    self.df[term] += 1
                    self.lnc[doc_id][term] = calculate_tf(term,
                                                          doc_terms)  # the l of the lnc. we can ignore n because it's 1. will multiply by c later

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
        top_10_results = sorted(cosine_similarity, key=cosine_similarity.get, reverse=True)

        # Return the top 10 results
        return top_10_results[:10]


def main(corpus):
    ir = IRSystem(open(corpus))

    while True:
        query = input('Query: ').strip()
        if query == 'exit':
            break
        results = ir.run_query(query)
        print(results)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("CORPUS",
                        help="Path to file with the corpus")
    args = parser.parse_args()
    main(args.CORPUS)