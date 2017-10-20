import gensim
from sklearn import preprocessing
import codecs
import helper_functions as hf
from tasks import Tasks

"""

# get paragraphs and stopwords
paragraphs = hf.get_paragraphs(codecs.open("./text", "r", "utf-8"))
stopwords = hf.get_stop_words(codecs.open("./stopWords.txt", "r", "utf-8"))

# Remove paragraphs with gutenberg
paragraphs = hf.remove("Gutenberg", paragraphs)

# Remove punktuation
paragraphs = hf.remove_punctuations(paragraphs)

copy = list(map(list, paragraphs))

# stemming the words
paragraphs = hf.stem(paragraphs)

dictionary = gensim.corpora.Dictionary(paragraphs)

# get stopwords
stopIds = hf.get_stop_wordids(stopwords, dictionary)

dictionary.filter_tokens(stopIds)
bags = []
for p in paragraphs:
    bags.append(dictionary.doc2bow(p))

tfidf_model = gensim.models.TfidfModel(bags)
tfidf_corpus = tfidf_model[bags]
idf_matrix = gensim.similarities.MatrixSimilarity(tfidf_corpus)

lsi_model = gensim.models.LsiModel(tfidf_corpus, id2word=dictionary, num_topics=100)
lsi_corpus = lsi_model[bags]
lsi_matrix = gensim.similarities.MatrixSimilarity(lsi_corpus)

print(lsi_model.show_topics())

"""
t = Tasks()
t.task_one()
t.task_two()
t.task_three()
t.task_four()
