
def get_word():
    while True:
      word= input("Give me a word: ").upper()
      if word.isalpha():
         return word
      else:
         print("Please enter an answer with only letters")

def get_lives():
    while True:
      lives = input("Enter the Number of lives")
      if lives.isdigit():
         return int(lives) 
      else: 
         print("Not a number")

def get_guess(suggested_letters):
    while True:
        guess = input("Try a letter").upper()
        if len(guess) != 1:
            print("Only one letter")
            continue
        elif not guess.isalpha():
           print("This is not a letter")
           continue
        elif guess in suggested_letters:
            print("Already tried that letter")
            continue
        else:
          return guess
    
def assess_guess(secret_word, guessed_letter, lives_left):
    if guessed_letter in secret_word:
        print("Correct! This letter is in the secret word!") 
        print(f"Tries left: {lives_left}")
       
    else:
        print("Wrong! This letter is not in the secret word!")
        lives_left -=1
        print(f"Tries left: {lives_left}")
    return lives_left

def display_word(displayed_word, secret_word_list):
  print(" ".join(displayed_word))    
  if secret_word_list == displayed_word:
    print("Congrats! You found the word!")
    return True     
  else: 
    return False

def main():
    secret_word = get_word()
    lives = get_lives()
    guessed_letters = [] 
    secret_word_list = []
    displayed_word = []
    for letter in secret_word:
        secret_word_list.append(letter)
        displayed_word.append("_")


    while lives > 0 :
      guess_letter = get_guess(guessed_letters)      
      for i in range(len(secret_word_list)):
        if secret_word_list[i] == guess_letter:
          displayed_word[i] = guess_letter
      guessed_letters.append(guess_letter)
      lives = assess_guess(secret_word_list, guess_letter, lives)
      if lives == 0:
         print("You lost")
         break
      if display_word(displayed_word,secret_word_list):
         break
      else:
         continue
         


main()
      
