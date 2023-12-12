def reverse_words(text):
    splitedText = text.split(' ')
    newText = []
    for word in splitedText:
        reverseWord = word[::-1]
        newText.append(reverseWord)
    return ' '.join(newText)