# potential problems:
# large pdf's load slowly and thier analysis takes time ==> do async processing to avoid overheads


import slate3k as slate
import re

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer,WordNetLemmatizer
from nltk.tokenize import word_tokenize,sent_tokenize
from textblob import TextBlob as tb
import math

stop_words=set(stopwords.words("english"))
print(stop_words)


# here strings denotes to the array of strings extracted by the return_strings_info file
# a very crude implementation
# try to use NLTK and text processing concepts
# sort the words in the files based on the Noun count in the file
# if the top k words are filed return the list
# else go for the VERBS in the sentences and fill up the remainin k words
# byy k here I mean the accuracy
# stem/lemmentize every search keyword and match it to the DB tags to find appropriate files
# aslo create a deep search for matching every word in a document!


# if the backend where to be weak and cant handle DB stores implement these methods!!
def return_tag_info():
    pass

def save_tag():
    pass

# def important_word_finder():


def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)


def create_tag(strings,accuracy=10):
    dic={}
    for x in strings:
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1
    print(dic)
    val=[x for x in dic.keys()]
    lis=filter(lambda x:x not in stop_words,val )
    lis=[x for x in lis]
    print("lis is ",lis)

    ps=PorterStemmer()
    lammenter=WordNetLemmatizer()
    stemmed=[ps.stem(x) for x in lis]
    lament=[lammenter.lemmatize(x) for x in lis]
    print("Stemmed list is ",stemmed)
    print("Lammentizied list is ",lament)
    val.sort()
    return {'tags':val}


# filepath => downloaded file from a remote java-backend url
# returns a JSON object to the path
def return_whole_doc(path):
    with open(path, 'rb') as f:
        doc = slate.PDF(f)
    print("Returning ",''.join(doc))
    return ''.join(doc)

def return_strings_info(filepath,delimiter="\n",accuracy=10):
    with open(filepath, 'rb') as f:
        doc = slate.PDF(f)
    print(doc)
    print(len(doc))

    strings=[]

    # for x in doc:
    #     for y in re.split(',|.|\n|:',x):
    #         strings.append(y)
    # s = "\n"  # for splitting as sentence based on '.'
    # s=" " # splitting of word based on " "

    # note the delimiter must be a RE but as single delimiters are RE it's fine
    for x in doc:
        lis=re.split(delimiter, x)
        for y in lis:
            strings+=y.split(' ')

    print("After splitting based on '.'", strings)
    print("Total lines extracted ", len(strings))

    # prints the full document as a list of strings
    # each element of the list is a page in the document
    # print(doc[0])
    # # prints the first p
    # print("Printing line by line")
    # for x in strings:
    #     print("line: ", x)
    # return (create_tag(strings))
    print("returning ",' '.join(strings))
    return (' '.join(strings))

    # create as function
    # create a function to match similarity!!
# print(return_strings_info("C:\\Users\\Balarubinan\\Desktop\\important shits\\recipt for exam fee.pdf"))
# ans=return_strings_info("C:\\Users\\Balarubinan\\Desktop\\important shits\\recipt for exam fee.pdf")
# ans2=return_strings_info("C:\\Users\\Balarubinan\\Desktop\\cheatsheets\\sql cheatsheet.pdf")
# print("Top words in document:")
# scores = {word: tfidf(word,tb(ans),ans2) for word in ans}
# sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
# for word, score in sorted_words[:3]:
#     print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))

document1 = tb(return_strings_info("C:\\Users\\Balarubinan\\Desktop\\important shits\\recipt for exam fee.pdf"))

document2 = tb(return_strings_info("C:\\Users\\Balarubinan\\Desktop\\Random files\\TNEB Online Payment.pdf"))

document3= tb(return_strings_info("C:\\Users\\Balarubinan\\Desktop\\important shits\\hhopcorft chap 2 practice.pdf"))


bloblist = [document1, document2, document3]
for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:10]:
        print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))