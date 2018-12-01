# Mini-Search-Engine
A program that creates an inverted index for a given set of documents. A program that can evaluate conjunctive queries with two operands. That is, queries of the form: Term1 AND Term2

A program that creates an inverted index for a given set of documents. A program that can evaluate conjunctive queries with two operands. That is, queries of the form: Term1 AND Term2

Files: Part1.py Part2.py Part3b.py Part3a.txt Part3b.txt

I have built an inverted index for 10 documents and implemented the boolean query evaluation using the provided algorithm.

In order to run the program you will required to have NLTK packages for the python

For mac users it can be installed as following:

Install NLTK: run sudo pip install -U nltk Install Numpy (optional): run sudo pip install -U numpy Test installation: run python then type import nltk

I have simply used the Sublimetext and command + b to run the code and for testing usage.

You will also need the documents.txt file.

Part 1: Construct Inverted Index

I used tokenizer to find stop words and remove them. Then I used stemmer and lemmer to sort out similar words. Inverted Index for all 10 documents.

Part 2: Boolean Query Evaluation Algorithm

So I loaded the stored inverted_token_file from Part 1. Then added the check to see if the queries words are in the index or not. After that used it to check the of the two and queries.

Part3b.py: Mini Search Engine Code (This generated the result for Part3b)
