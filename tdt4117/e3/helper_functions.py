import string
from nltk.stem.porter import PorterStemmer
import codecs

stemmer = PorterStemmer()


def get_paragraphs(file):
    """
    Reads lines from a given file and splits them into paragraphs which are
    places in an array which is then returned.
    :param file: file object
    :return: list of paragraphs
    """
    paragraph = ""
    paragraphs = []
    for line in file.readlines():
        if line.isspace():
            if paragraph != "":
                paragraphs.append(paragraph)
            paragraph = ""
            continue
        paragraph += line
    return paragraphs


def remove(word, paragraphs):
    """
    Removes any paragraphs containing a given word
    :param word: single word string
    :param paragraphs: array of paragraphs
    :return: list of paragraphs
    """
    for p in paragraphs:
        if p.__contains__(word):
            paragraphs.remove(p)
    return paragraphs


def tokenize(paragraphs):
    """
    Loops over an array of paragraphs and calls a helper method
    to tokenize each string of words
    :param paragraphs: array of paragraphs
    :return: list of paragraphs
    """
    for i, p in enumerate(paragraphs):
        paragraphs[i] = tokenize_string(p)
    return paragraphs


def tokenize_string(words):
    """
    Returns an array of words split by space
    :param words: string of words
    :return: list of words
    """
    return words.split(" ")


def remove_punctuations(paragraphs):
    """
    Loops over an array of paragraphs and call a helper method
    to remove punctuations.
    :param paragraphs: array of paragraphs
    :return: list of paragraphs
    """
    for i, word_list in enumerate(paragraphs):
        words = remove_punctuations_in_list(word_list)
        paragraphs[i] = words
    return paragraphs


def remove_punctuations_in_list(list):
    """
    Iterates over every word in a given list, generating a new list
    of words without any punctuations.
    This list is then returned
    :param list: list of words
    :return: list of words
    """
    words = []
    for word in list:
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
    """
    takes a list of paragraphs, which are lists of words and
    calls a helper method to stem each word in every list.
    :param paragraphs: list of paragraphs
    :return: list of stemmed paragraphs
    """
    for i, p in enumerate(paragraphs):
            paragraphs[i] = stem_list(p)
    return paragraphs


def stem_list(list):
    """
    Takes a list of words and runs a helper method to stem each word.
    :param list: list of words
    :return: list of stemmed words
    """
    for i, word in enumerate(list):
        list[i] = stemmer.stem(word.lower())
    return list


def get_stop_words(file):
    """
    Takes a file and creates an array of words.
    :param file: file object
    :return: list of words
    """
    stopwords = []
    for line in file.readlines():
        for word in line.split("\n"):
            stopwords.append(word)
    return stopwords


def get_stop_wordids(stopwords, dictionary):
    """
    Based on a given dictionary, this will find the word-indexes of every stopword
    which exists in the dictionary.
    :param stopwords: list of words
    :param dictionary: dictionary object
    :return: list of indexes
    """
    stopIds = []
    for word in stopwords:
        try:
            stopIds.append(dictionary.token2id[word])
        except:
            pass
    return stopIds


def process(query):
    """
    Processes a query. The query is tokenized, rid of punctuations and stemmed.
    :param query: string
    :return: string
    """
    query = tokenize_string(query)
    query = remove_punctuations_in_list(query)
    query = stem_list(query)
    return query


def show_topics(topics, lsi_model):
    """
    Displays topics on a given format.
    :param topics: list of topic objects
    :param lsi_model: lsi model object
    """
    for topic in enumerate(topics):
        t = topic[1][0]
        print("\n[Topic " + t.__str__() + "]")
        print(lsi_model.show_topics()[t])


def show_docs(docs, paragraphs):
    """
    Displays documents on a given format.
    :param docs: list of lsi matrix elements
    :param paragraphs: list of paragraphs
    """
    for doc in docs:
        p = doc[0]
        print("\n[Paragraph " + p.__str__() + "]")
        print(paragraphs[p])