# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 18:59:55 2023

@author: payal
"""

def most_frequent(input_string):
    # created an empty dictionary to store letter frequencies
    
    letter_count = {}
    # Removing space and convert the input string to lowercase
    input_string = input_string.replace(" ","").lower()
   # Iterate through each character in the input string 
    for char in input_string:
        # checking if the character is a letter 
        if char.isalpha():
            #Update the frequency count for the character
            letter_count[char] = letter_count.get(char, 0) + 1
            
    # sort the dictionary by values (frequencies) in decreasing order
    sorted_letters = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)
    
    # Printing the letters and their frequencies
    for letter, frequency in sorted_letters:
        print(f"{letter} = {frequency:02d}", end=" ")

# Input string
input_string = "Entrepreneur"

#Calling the most_frequent function  
most_frequent(input_string)      
        