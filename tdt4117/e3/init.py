import t1
import t2
import t3
import t4

FOLDER = "./assets/"
TEXTFILE = FOLDER + "book_full.txt"
STOPWORDS = FOLDER + "stop_words.txt"

def main():
    
    # Run Task 1
    parapgraphs, stemmed_paragraphs = t1.main(TEXTFILE)

    # Run Task 2
    bags, dictionary = t2.main(STOPWORDS, stemmed_paragraphs)

    # Run Task 3
    tfidf_model, tfidf_corpus, matrix_sim, lsi_matrix, lsi_model = t3.main(bags, dictionary)

    # Run Task 4
    t4.main(dictionary, tfidf_model, tfidf_corpus, matrix_sim, lsi_matrix, lsi_model, parapgraphs)

if __name__ == "__main__":
    main()