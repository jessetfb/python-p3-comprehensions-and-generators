#!/usr/bin/env python3

def return_evens(num_list):
    num_list = [num for num in num_list if num%2 == 0]

    return num_list

def make_exclamation(sentence_list):
    sentence_list = [(string + "!") for string in sentence_list]
    return sentence_list