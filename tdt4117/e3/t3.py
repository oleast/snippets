import gensim

def main(bags, dictionary):

    # Task 3.1
    tfidf_model = gensim.models.TfidfModel(bags)

    # Task 3.2
    tfidf_corpus = tfidf_model[bags]

    # Task 3.3
    matrix_sim = gensim.similarities.MatrixSimilarity(tfidf_corpus)

    # Task 3.4
    lsi_model = gensim.models.LsiModel(tfidf_corpus, id2word=dictionary, num_topics=100)
    lsi_corpus = lsi_model[bags]
    lsi_matrix = gensim.similarities.MatrixSimilarity(lsi_corpus)

    # Task 3.5
    print(lsi_model.show_topics(3, 3))

    return tfidf_model, tfidf_corpus, matrix_sim, lsi_matrix, lsi_model