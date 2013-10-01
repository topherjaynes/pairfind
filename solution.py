#!/usr/bin/env python
# encoding: utf-8

from sys import argv, getsizeof
from itertools import combinations
import codecs

def find_pair_frequency(file_of_artists, num_appearances):
    """ Takes a file and reades line by line. Each line is a turned
         into a list of pairs, which are added to a dictionary counting
         the frequency of occurances.


         Keyword arguments:
          file_of_artists: A txt file where each line is a list of up
                                 to 50 artist can be UTF-8
          num_appearances: integer of the list the pairs
                                        have to occur in to be successful
    """
    dict_of_pairs = {}
    dict_of_pairs_frequency = {}

    file_of_artists = codecs.open(file_of_artists, 'rb', encoding="UTF-8")

    for line in file_of_artists:
        # spliting the playlist on the comma
        # generate a list of unique pairs on the current list
        pairs_list = find_unique_pairings(line.strip('\n').split(','), 2)

        for pair in pairs_list:
            # Create new sorted tuple and add to dict countring freq
            sorted_pair = tuple(sorted([pair[0], pair[1]]))

            # checks if the tuple is in dictionary  and increments count
            if sorted_pair in dict_of_pairs_frequency:
                dict_of_pairs_frequency[sorted_pair] += 1
            else:
                try:
                    dict_of_pairs[sorted_pair] += 1

                    # check to see if the is larger than number sorting for
                    # if so then drop add to other dictionary
                    if dict_of_pairs[sorted_pair] >= num_appearances:
                        dict_of_pairs_frequency[sorted_pair] = dict_of_pairs.pop(sorted_pair)

                except:
                    dict_of_pairs[sorted_pair] = 1

    print_dictionary_of_artist(dict_of_pairs_frequency)


def print_dictionary_of_artist(unique_artists):
    """ function to print  key based on frequency (num_appearances)"""
    for key,value in unique_artists.iteritems():
        #print utf-f key of artist
        print key[0].encode("utf-8") + ", " + key[1].encode("utf-8")


def sytems_stats(dict_to_find_stats):
    """ Takes a dictionary tells us length and size in memory """
    print "Size of  dictionary: %d" % getsizeof(dict_to_find_stats)
    print "Length : %d" % len(dict_to_find_stats)


def find_unique_pairings(list_of_uniques, tuple_length):
    """
    Relying on the itertools combinations method here
    Passing the value of 2 we get
    tuples of length 2, in sorted order, no repeated elements

    The returned list doesn't take into account alphabetical order,
    so tuples that are generated in this might have (artist1, artis2)
    while another like might contain (artist2, artist1), which aren't
    comparable, but equal

    args:
        tuple_length
        list_of_uniques
    """
    return list(combinations(list_of_uniques, tuple_length))

def main(filename, number_of_occurances):
    if filename =="":
        return "Please enter a file name"
    elif filename.find('.txt') == False:
        return "Please make sure file is a .txt"
    elif number_of_occurances < 1:
        return "Please make sure your number of list is greater than 1"
    else:
        find_pair_frequency(filename, number_of_occurances)

if __name__ == '__main__':
    main(argv[1], int(argv[2]))
