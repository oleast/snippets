import codecs
import functions
import gensim

def main(stop_words_file, stemmed_paragraphs):
    
    bags = []
    # Task 2.1
    # Read the file of stopwords
    f = codecs.open(stop_words_file, "r", "utf-8")

    # get an array of stopwords
    stop_words = functions.get_stop_words(f)

    #print("t2.stopwords:len: {}".format(len(stop_words)))
    #print("t2.stemmed_paragraphs:len {}".format(len(stemmed_paragraphs)))
    # generate a dictionary of the words in the paragraph
    dictionary = gensim.corpora.Dictionary(stemmed_paragraphs)

    #print("t2.dict:len: {}".format(len(dictionary)))
    # get an array of ids based on stopwords and the dictionary
    stop_ids = functions.get_stop_wordids(stop_words, dictionary)

    # Filtering out the stopwords in the dictionary
    dictionary.filter_tokens(stop_ids)

    # Task 2.2
    # Create a bag of words of every paragraph
    for p in stemmed_paragraphs:
        bags.append(dictionary.doc2bow(p))
    
    return bags, dictionary
