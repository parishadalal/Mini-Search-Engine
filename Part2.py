import pickle

from nltk.stem.porter import *

#this will load the saved the inverted_token_file
def open_inverted_index(source_file):
    with open(source_file, 'rb') as input_file:
        download = pickle.load(input_file)
    return download

#finds targeted words
def posting_list(term1, term2, index):
    porter_stemmer = PorterStemmer()
    word1=porter_stemmer.stem(term1)
    word2=porter_stemmer.stem(term2)
    if word1 not in index:
        raise ValueError("First term not found")
    elif word2 not in index:
        raise ValueError("Second term not found")
    else:
        return index[word1], index[word2]

#finds the intersection of the two list
def intersection(parsing1, parsing2):
    intersects = []
    data1 = parsing1[0]
    data2 = parsing2[0]
    index1 = 1
    index2 = 1
    while index1 <= data1 and index2 <= data2:
        if parsing1[index1] == parsing2[index2]:
            intersects.append(parsing1[index1])
            index1 += 1
            index2 += 1
        elif parsing1[index1] < parsing2[index2]:
            index1 += 1
        else:
            index2 += 1
    return intersects


def boolean_query(tokens_file_name, query1, query2):
    index = open_inverted_index(tokens_file_name)
    target = posting_list(query1, query2, index)
    result = intersection(target[0], target[1])
    print (query1, 'and', query2, 'sets are', target[0][1:], target[1][1:])
    print 'Intersection for the  query is {}'.format(result)


if __name__ == '__main__':
    boolean_query('inverted_token_file', 'via', 'yes')
