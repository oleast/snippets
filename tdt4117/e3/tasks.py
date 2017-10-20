import codecs
import helper_functions as hf
import gensim
import copy

ASSETS = "./assets/"
TEXTFILE = ASSETS + "book_full.txt"
STOPWORDS = ASSETS + "stop_words.txt"

class Tasks:

    stopWords = []
    stemmed_paragraphs = []
    paragraphs = []
    dictionary = None
    stopIds = []
    tfidf_model = None
    bags = []
    matrixSim = None
    lsi_model = None
    lsi_corpus = None
    lsi_matrix = None

    def task_one(self):
        # 1.1
        file = codecs.open(TEXTFILE, "r", "utf-8")

        # 1.2
        self.stemmed_paragraphs = hf.get_paragraphs(file)

        # 1.3
        self.stemmed_paragraphs = hf.remove("Gutenberg", self.stemmed_paragraphs)
        self.paragraphs = copy.copy(self.stemmed_paragraphs)

        # 1.4
        self.stemmed_paragraphs = hf.tokenize(self.stemmed_paragraphs)

        # 1.5
        self.stemmed_paragraphs = hf.remove_punctuations(self.stemmed_paragraphs)

        # 1.6
        self.stemmed_paragraphs = hf.stem(self.stemmed_paragraphs)

    def task_two(self):
        # 2.1
        # Read the file of stopwords
        file = codecs.open(STOPWORDS, "r", "utf-8")

        # get an array of stopwords
        self.stopWords = hf.get_stop_words(file)
        # generate a dictionary of the words in the paragraph
        self.dictionary = gensim.corpora.Dictionary(self.stemmed_paragraphs)
        # get an array of ids based on stopwords and the dictionary
        self.stopIds = hf.get_stop_wordids(self.stopWords, self.dictionary)
        # Filtering out the stopwords in the dictionary
        self.dictionary.filter_tokens(self.stopIds)

        # 2.2
        # Create a bag of words of every paragraph
        for p in self.stemmed_paragraphs:
            self.bags.append(self.dictionary.doc2bow(p))

    def task_three(self):
        # 3.1
        self.tfidf_model = gensim.models.TfidfModel(self.bags)

        # 3.2
        tfidf_corpus = self.tfidf_model[self.bags]

        # 3.3
        self.matrixSim = gensim.similarities.MatrixSimilarity(tfidf_corpus)
        # 3.4
        self.lsi_model = gensim.models.LsiModel(tfidf_corpus, id2word=self.dictionary, num_topics=100)
        self.lsi_corpus = self.lsi_model[self.bags]
        self.lsi_matrix = gensim.similarities.MatrixSimilarity(self.lsi_corpus)

        # 3.5
        print(self.lsi_model.show_topics(3, 3))

    def task_four(self):
        # 4.1
        #query = "What is the function of money?".lower()
        query = "How taxes influence economics".lower()
        query = hf.process(query)
        query = self.dictionary.doc2bow(query)

        # 4.2
        tfidf_index = self.tfidf_model[query]

        # 4.3
        docsim = enumerate(self.matrixSim[tfidf_index])
        docs = sorted(docsim, key=lambda kv: -kv[1])[:3]
        print(docs)

        # 4.4
        lsi_query = self.lsi_model[query]
        topics = sorted(lsi_query, key=lambda kv: -abs(kv[1]))[:3]
        hf.show_topics(topics, self.lsi_model)
        docsim = enumerate(self.lsi_matrix[lsi_query])
        docs = sorted(docsim, key=lambda kv: -kv[1])[:3]
        hf.show_docs(docs, self.paragraphs)