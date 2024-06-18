def display_word(secret_word, suggested_letters):
    secret_word_list  =[]
    display_word = []
    for letter in secret_word:
        secret_word_list.append(letter)
        display_word.append("_")
    for i in range(len(secret_word_list)):
      if secret_word_list[i] == suggested_letters:
        display_word[i] = suggested_letters
    print(display_word)


word = "Becode"
suggested_letters = input("Give letter")
display_word(word, suggested_letters)