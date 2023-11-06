def no_words(sen):
    count = 1
    for i in sen:
        if i == ' ':
            count += 1
    return count


sen = input("Enter a sentence : ")
print(no_words(sen))
