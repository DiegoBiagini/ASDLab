from timeit import default_timer as timer

from ngram import *


def main():
    # Words that will be tested
    n_words = 100

    dict_name = "../dict_nomi_95000.txt"

    # The thresholds for closest_word_ngram_ed_jacc that will be tested
    jacc_thresholds = [0.2, 0.5, 0.8]
    n_grams_lenght = [2, 3, 4]

    dictionary = file_to_list(dict_name)
    dictionary_spaces = add_spaces(dictionary)

    random_words = random.sample(dictionary, n_words)

    mistyped_list = mistype_list(random_words)
    mistyped_list_spaces = [(" " + el[0] + " ", " " + el[1] + " ") for el in mistyped_list]

    list_to_file(mistyped_list, "data/in_words.txt")


    # SIMPLE EDIT DISTANCE
    times = []
    n_hit = 0

    # Data that will be written to file
    # List of tuples with the time it took and the word it found
    out_data = []

    for word_query in mistyped_list:
        elapsed_time = timer()
        result = closest_word(word_query[1], dictionary)
        elapsed_time = timer() - elapsed_time

        out_data.append((elapsed_time, result[0]))
        times.append(elapsed_time)
        # Check if it guessed it correctly
        if result[0] == word_query[0]:
            n_hit += 1

    list_to_file(out_data, "data/out_simple_ed.txt")
    print("Simple edit distance\n Average time: ", sum(times) / n_words)
    print("Hit rate: ", n_hit / n_words, "\n\n")


    for n_gram in n_grams_lenght:

        n_gram_dictionary = dictionary_ngram(dictionary_spaces, n_gram)

        # EDIT DISTANCE ON JACCARD > THRESHOLD

        for jacc in jacc_thresholds:
            times = []
            n_hit = 0

            out_data = []

            for word_query in mistyped_list_spaces:
                elapsed_time = timer()
                result = closest_word_ngram_ed_jacc(word_query[1], n_gram, n_gram_dictionary, jacc)
                elapsed_time = timer() - elapsed_time

                out_data.append((elapsed_time, result[0]))
                times.append(elapsed_time)
                # Check if it guessed it correctly
                if result[0] == word_query[0]:
                    n_hit += 1

            list_to_file(out_data, "data/out_jacc_" + str(jacc) + "_" + str(n_gram) + "n.txt")
            print("Edit distance with jaccard >= " + str(jacc) +" and ngram of size " +str(n_gram))
            print("Average time: ", sum(times) / n_words)
            print("Hit rate: ", n_hit / n_words, "\n\n")


        # EDIT DISTANCE ON AT LEAST 1 NGRAM
        times = []
        n_hit = 0

        out_data = []
        for word_query in mistyped_list_spaces:
            elapsed_time = timer()
            result = closest_word_ngram_ed_1gram(word_query[1], n_gram, n_gram_dictionary)
            elapsed_time = timer() - elapsed_time

            out_data.append((elapsed_time, result[0]))
            times.append(elapsed_time)
            # Check if it guessed it correctly
            if result[0] == word_query[0]:
                n_hit += 1

        list_to_file(out_data, "data/out_1gram_" + str(n_gram) + "n.txt")
        print("Edit distance on words with at least 1 common ngram of size " + str(n_gram))
        print("Average time: ", sum(times) / n_words)
        print("Hit rate: ", n_hit / n_words, "\n\n")


if __name__ == '__main__':
    main()
