import re
from collections import Counter
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "texto.txt")

# Read the input text from the file
with open(file_path, 'r') as f:
    lines = f.read()

# Preprocess the text: lowercased and remove non-alphabetic characters (letters only)
text = re.sub(r'[^a-zA-ZñÑ]', '', lines).lower()

# Count the frequency of each letter
letter_counts = Counter(text)

# Define the letter frequencies (percentage) in the language
zerrendaLetra = ['E', 'A', 'O', 'L', 'S', 'N', 'D', 'R', 'U', 'I', 'T', 'C', 'P', 'M', 'Y', 'Q', 'B', 'H', 'G', 'F', 'V', 'J', 'Ñ', 'Z', 'X', 'K', 'W']
zerrendaPortzentaia = [16.78, 11.96, 8.69, 8.67, 7.88, 7.01, 6.87, 4.94, 4.80, 4.15, 3.31, 2.92, 2.776, 2.12, 1.54, 1.53, 0.92, 0.89, 0.73, 0.52, 0.39, 0.30, 0.29, 0.15, 0.06, 0.00, 0.00]

# Calculate the percentage of each letter in the message
total_letters = sum(letter_counts.values())
ekibalentzia = sorted(letter_counts, key=letter_counts.get, reverse=True)

# Create a mapping between the most frequent letters in the message and the predefined frequency list
hiztegi = dict(zip(ekibalentzia, zerrendaLetra[:len(ekibalentzia)]))

# decypher function: translates the original message based on the current letter mapping
def decypher(lines, hiztegi):
    """
    Apply the current letter mapping (hiztegi) to the original text.
    Non-alphabetic characters remain unchanged.
    """
    return ''.join(hiztegi.get(char, char) if char.isalpha() else char for char in lines.lower())

# modify_alphabet function: swaps two letters in the current mapping
def modify_alphabet(hiztegi, char1, char2):
    """
    Swap two letters in the current letter mapping (hiztegi).
    char1 and char2 are the letters to be swapped.
    """
    # Reverse the mapping (letter -> frequency letter)
    inverse_hiztegi = {v: k for k, v in hiztegi.items()}
    
    if char1 in inverse_hiztegi and char2 in inverse_hiztegi:
        # Swap the letters in the dictionary
        key1, key2 = inverse_hiztegi[char1], inverse_hiztegi[char2]
        hiztegi[key1], hiztegi[key2] = char2, char1  # Perform the swap in hiztegi
    
    return hiztegi

# Interactive loop to improve the decrypted text through letter swaps
def interactive_swapping(hiztegi, lines):
    mezuItzulia = decypher(lines, hiztegi)
    while True:
        # Display the current state of the text
        print("\nCurrent message:\n")
        print(mezuItzulia)
        
        # Get user input for letters to swap
        char1 = input("\nEnter the first letter to swap (or 0 to exit): ").upper()
        if char1 == "0":
            break
        
        char2 = input("Enter the second letter to swap: ").upper()
        
        # Perform the letter swap
        hiztegi = modify_alphabet(hiztegi, char1, char2)
        
        # Re-decrypt the message using the updated mapping
        mezuItzulia = decypher(lines, hiztegi)
        
        # Provide feedback after the swap
        print(f"\nSwapped '{char1}' with '{char2}'. Here is the updated text:")
        print(mezuItzulia)
    
    return hiztegi, mezuItzulia

# Run the interactive swapping function
hiztegi, final_text = interactive_swapping(hiztegi, lines)

# Save the translated message and mapping to a file
output_path = os.path.join(script_dir, "../output.txt")
with open(output_path, "w") as f:
    f.write("Final translated message:\n")
    f.write(final_text + "\n\n")
    f.write("Letter mappings (original -> swapped):\n")
    for key, value in hiztegi.items():
        f.write(f"{key} -> {value}\n")

print("\nTranslation saved to 'output.txt'.")