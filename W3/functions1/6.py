def reversed_sentence(sentence):
    words = sentence.split(' ')
    reverse_sentence = ' '.join(reversed(words))
    return reverse_sentence
sentence = input()
print(reversed_sentence(sentence))