import functions

def main(dictionary, tfidf_model, tfidf_corpus, matrix_sim, lsi_matrix, lsi_model, paragraphs):

    # Task 4.1
    query = "How taxes influence economics".lower()
    query = functions.process(query)
    query = dictionary.doc2bow(query)

    # Task 4.2
    tfidf_index = tfidf_model[query]

    # Task 4.3
    docsim = enumerate(matrix_sim[tfidf_index])
    docs = sorted(docsim, key=lambda kv: -kv[1])[:3]
    print(docs)

    # Task 4.4
    lsi_query = lsi_model[query]
    topics = sorted(lsi_query, key=lambda kv: -abs(kv[1]))[:3]
    functions.show_topics(topics, lsi_model)
    docsim = enumerate(lsi_matrix[lsi_query])
    docs = sorted(docsim, key=lambda kv: -kv[1])[:3]
    functions.show_docs(docs, paragraphs)
