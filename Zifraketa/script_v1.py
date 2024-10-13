import re
from collections import Counter
import random
import os
import shutil

def esAlphPerc():
    # Define the Spanish alphabet
    spanish_alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
        'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    
    # Define the percentage of usage of each letter in the Spanish language
    placeholder_values = [
        0.1196, 0.9200, 0.0331, 0.0687, 0.1678, 0.0052, 0.0073, 0.0089, 
        0.0415, 0.0030, 0.0000, 0.0837, 0.0212, 0.0701, 0.0029, 0.0869,
        0.0278, 0.0153, 0.0494, 0.0788, 0.0331, 0.0480, 0.0039, 0.0000,
        0.0006, 0.0154, 0.0015
    ]

    # Create a dictionary to store the usage values of each letter
    letter_frequencies = {}
    
    # Assign usage values to the corresponding letters
    for i, letter in enumerate(spanish_alphabet):
        letter_frequencies[letter] = placeholder_values[i]
    
    return letter_frequencies 

def decypher(file_path, usage_alphabet):
    with open(file_path, 'r') as f:
        lines = f.read()
    
    text = re.sub(r'[^a-zA-ZñÑ]', '', lines).lower() # Text to lowercase, excluding non-alphabetic characters
    letter_counts = Counter(text)
    ranked_letters = [letter for letter, _ in letter_counts.most_common()]
    letter_mapping = {ranked_letters[i]: usage_alphabet[i] for i in range(len(ranked_letters))} # Map the most common letters to the most used letters
    new_text = ''.join(letter_mapping.get(char, char) for char in lines.lower()) # Replace the original letters with the mapped letters
    
    return new_text, letter_mapping

def modify_alphabet(usage_alphabet, letter1, letter2):
    # Find the indices of the letters to swap
    index1 = usage_alphabet.index(letter1)
    index2 = usage_alphabet.index(letter2)
    
    # Swap the letters in the usage_alphabet
    new_alphabet = usage_alphabet.copy()
    new_alphabet[index1], new_alphabet[index2] = new_alphabet[index2], new_alphabet[index1]
    
    return new_alphabet

def loop():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'texto.txt')
    new_file_path = os.path.join(script_dir, 'texto_decyphered.txt')
    shutil.copyfile(file_path, new_file_path)
    
    # Read the file
    with open(file_path, 'r') as f:
        lines = f.read()
    
    usage_alphabet = sorted(esAlphPerc().keys(), key=lambda x: esAlphPerc()[x], reverse=True) # For first iteration
    correct = False

    while not correct:
        new_text, letter_mapping = decypher(new_file_path, usage_alphabet)

        # Write the new_text to the new_file_path
        with open(new_file_path, 'w') as f:
            f.write(new_text)

        print(new_text)

        # Define the Spanish alphabet
        spanish_alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
        'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]

        while True:
            user_input = input("Enter two letters which position will swap (separated by a comma) or 0 to exit: ").strip()
            
            if user_input == '0':
                print("Final usage alphabet:", ' '.join(usage_alphabet))
                correct = True
                continue
            
            letters = user_input.split(',')
            
            if len(letters) == 2 and all(letter.isalpha() for letter in letters):
                letter1, letter2 = letters[0].strip(), letters[1].strip()
                if letter1 in spanish_alphabet and letter2 in spanish_alphabet:
                    usage_alphabet = modify_alphabet(usage_alphabet, letter1, letter2)
                    break
                else:
                    print("Invalid input. Please enter exactly two valid letters from the alphabet.")
            else:
                print("Invalid input. Please enter exactly two letters separated by a comma.")
        
loop()