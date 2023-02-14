'''
Chapter 11 of Think Python
Dictionaries
2/11/2023
'''
#11.1
def read_file_to_dict(file_name):
    with open(file_name, 'r') as file:
        # Split the contents of the file into words
        words = file.read().split()
        # Create a dictionary with the words as keys
        word_dict = {word: None for word in words}
        return word_dict
read_file_to_dict()