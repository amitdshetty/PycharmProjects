"""
Write a function that can take a string and return a list of bigrams.

Example:

sentence = "Have free hours and love children? Drive kids to school, soccer practice and other activities."

output = [('have', 'free'),
 ('free', 'hours'),
 ('hours', 'and'),
 ('and', 'love'),
 ('love', 'children?'),
 ('children?', 'drive'),
 ('drive', 'kids'),
 ('kids', 'to'),
 ('to', 'school,'),
 ('school,', 'soccer'),
 ('soccer', 'practice'),
 ('practice', 'and'),
 ('and', 'other'),
 ('other', 'activities.')]
"""

def find_bigrams(input_sentence):
    if len(input_sentence) <= 2:
        return input_sentence.lower()
    else:
        input_sentence = input_sentence.lower()
        input_sentence_list = input_sentence.split(' ')
        # print(input_sentence_list)
        result = []
        for i, word in enumerate(input_sentence_list):
            if i < len(input_sentence_list) - 1:
                temp = [input_sentence_list[i], input_sentence_list[i+1]]
                result.append(temp)
                temp = []
        return result


sentence = "Have free hours and love children? Drive kids to school, soccer practice and other activities."
result = find_bigrams(sentence)
print(result)