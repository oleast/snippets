import string
from nltk.stem.porter import PorterStemmer
import codecs

stemmer = PorterStemmer()

def get_paragraphs(f):
    
    # This function takes a file object (f), reads the lines and splits it into paragraphs.
    # The paragraphs are then returned as an array
    
    paragraph = ""
    paragraphs = []
    for line in f.readlines():
        if line.isspace():
            if paragraph != "":
                paragraphs.append(paragraph)
            paragraph = ""
            continue
        paragraph += line
    #print("get_paragraphs: {}".format(len(paragraphs)))
    return paragraphs


def remove_containing_word(word, strings):

    # This method removes a string from an array of strings if the string contains a given word.
    # It then returns the array.

    for s in strings:
        if s.__contains__(word):
            strings.remove(s)
    #print("remove: {}".format(len(strings)))
    return strings

def tokenize(paragraphs):

    # This method iterates over an array of paragraphs, and splits every paragraph into an array of its words.abs
    # It the returns the paragraphs

    for i, p in enumerate(paragraphs):
        paragraphs[i] = p.split(" ")
        #print(paragraphs[i])
    #print("tokenize: {}".format(len(paragraphs)))
    return paragraphs

def remove_punctuations(paragraphs):

    # This function removes puctuation from a two-dimentional array of strings.
    # It then reuturns the array.

    for i, word_list in enumerate(paragraphs):
        words = remove_punctuations_in_list(word_list)
        paragraphs[i] = words
    return paragraphs


def remove_punctuations_in_list(word_list):

    # This method iterates over an array of strings, removing all puctuation.
    # It then returns the array.

    words = []
    for word in word_list:
        w = ""
        for letter in word:
            if (string.punctuation + "\n\r\t").__contains__(letter):
                if w != "":
                    words.append(w.lower())
                    w = ""
                continue
            w += letter
        if w != "":
            words.append(w.lower())
    return words


def stem(paragraphs):

    # This function takes a two-dimentional array of strings, and stems each string (word).
    # It then returns the array.

    for i, p in enumerate(paragraphs):
        paragraphs[i] = stem_list(p)
    return paragraphs


def stem_list(words):

    # This function takes an array and stems every string (word) in it.
    # It then returns the array.

    for i, word in enumerate(words):
        words[i] = stemmer.stem(word.lower())
        #print(words[i])
    return words


def get_stop_words(f):

    # This function takes a file object and returns an array containing each line in the file.

    stop_words = []
    for word in f.readlines():
        stop_words.append(word.rstrip("\n"))
    #print("get_stop_words: {}".format(len(stop_words)))
    return stop_words


def get_stop_wordids(stop_words, dictionary):

    # Based on a given dictionary, this will find the word-indexes of every stopword
    # which exists in the dictionary.

    ids = []
    for word in stop_words:
        try:
            ids.append(dictionary.token2id[word])
        except:
            pass
    return ids


def process(query):

    # This function processes a query.
    # The query is tokenized,
    # rid of punctuations
    # and then stemmed before it is returned.

    query = query.split(" ")
    query = remove_punctuations_in_list(query)
    query = stem_list(query)
    return query


def show_topics(topics, lsi_model):

    # This function displays topics on a given format.

    for topic in enumerate(topics):
        t = topic[1][0]
        print("\n[Topic " + t.__str__() + "]")
        print(lsi_model.show_topics()[t])


def show_docs(docs, paragraphs):

    # This function displays documents on a given format.

    for doc in docs:
        p = doc[0]
        print("\n[Paragraph " + p.__str__() + "]")
        print(paragraphs[p])
