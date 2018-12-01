import Part1
import Part2


def SearchEngine():
    sourceFile = 'documents.txt'
    invertedList = 'Part3a.txt'
    invertedTokens = 'inverted_token_file'
    Part1.run_inverted_index(sourceFile, invertedList, invertedTokens)
    Part2.boolean_query(invertedTokens,'asus','google')
    Part2.boolean_query(invertedTokens,'screen','bad')
    Part2.boolean_query(invertedTokens,'great','tablet')

if __name__ == '__main__':
    SearchEngine()
