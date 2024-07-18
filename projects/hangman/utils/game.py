import random as rd 

class HangmanGame:
    def __init__(self):
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions', 'python', 'programming', 'developer']
        self.word_to_find = list(rd.choice(self.possible_words).upper())
        self.lives = 5
        self.correctly_guessed_letters = ["_" for i in range(len(self.word_to_find))]
        self.wrongly_guessed_letters= []
        self.error_count = 0
        self.turn_count = 0
    
    def play(self):
        while True:
            guess = input("Try a letter: ").upper()
            if len(guess) != 1:
                print("Only one letter")
                continue
            elif not guess.isalpha():
                print("This is not a letter")
                continue
            elif guess in self.correctly_guessed_letters:
                print("Already tried that letter")
                continue
            elif guess in self.wrongly_guessed_letters:
                print("Already tried that letter")
                continue
            elif guess in self.word_to_find:
                for i in range(len(self.word_to_find)):
                    if self.word_to_find[i] == guess:
                        self.correctly_guessed_letters[i] = guess
            else:
                self.wrongly_guessed_letters.append(guess)
                self.error_count +=1
                self.lives -=1
            self.turn_count	+=1    
            break
    def game_over(self):
        if self.lives == 0:
            print("Game over! You lost!")
            return True

    def well_played(self):
        if self.correctly_guessed_letters == list(self.word_to_find):
            print(f"Congrats! You found the word:{self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!")
            return True
        
    def start_game(self):
        print(self.correctly_guessed_letters)
        while self.lives >= 0:
            self.play()
            if self.game_over():
                break
            if self.well_played():
                break
            print(self.correctly_guessed_letters)
            print(f"Bad Guesses: {self.wrongly_guessed_letters}, Lives left:  {self.lives}, Error count: {self.error_count},Turn count: {self.turn_count}")


game = HangmanGame()
game.start_game()
       
