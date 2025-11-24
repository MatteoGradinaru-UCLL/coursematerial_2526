# def spellcheck(document, valid_words):
#     valid_set = set(valid_words)
#     current_word = ""
#     misspelled = set()

#     for char in document:
#         if char == ' ' or char == "\n":
#             if current_word:
#                 lowercase_word = current_word.lower()
#                 if lowercase_word not in valid_set:
#                     misspelled.add(lowercase_word)
#                 current_word = ""
#         else:
#             current_word += char

#     if current_word:
#         lowercase_word = current_word.lower()
#         if lowercase_word not in valid_set:
#             misspelled.add(lowercase_word)
#     return misspelled

def spellcheck(document, valid_words):
    valid_set = set(valid_words)
    words = document.split()
    
    misspelled = set()
    for word in words:
        lowercase_word = word.lower()
        if lowercase_word not in valid_set:
            misspelled.add(lowercase_word)
    
    return misspelled


valid_words = [ 'cat', 'mat', 'sat', 'the' ]
document = """
The cat
sat on
the mat
"""

print(spellcheck(document, valid_words))