import random
from words import word_list

def get_word():
  word = random.choice(word_list)
  return word.upper()


def play(word):
  word_completion = "_" * len(word)
  guessed = False
  guessed_letters = []
  guessed_words = []
  tries = 6
  print("Welkom bij galgje!")
  print(display_hangman(tries))
  print(word_completion)
  print("\n")
  while not guessed and tries > 0:
    guess = input("kies een letter:").upper()
    if len(guess) == 1 and guess.isalpha():
      if guess in guessed_letters:
        print("Je hebt", guess, "al geraden!")
      elif guess not in word:
        print(guess, "zit helaas niet in het woord...")
        tries -= 1
        guessed_letters.append(guess)
      else:
        print("Goed gedaan", guess, "zit in het woord!")
        guessed_letters.append(guess)
        word_as_list = list(word_completion)
        indices = [i for i, letter in enumerate(word) if letter == guess]
        for index in indices:
          word_as_list[index] = guess
        word_completion = "".join(word_as_list)
        if "_" not in word_completion:
          guessed = True
    elif len(guess) == len(word) and guess.isalpha():
      if guess in guessed_words:
        print("Je hebt het woord", guess, "al geraden!")
      elif guess != word:
        print(guess, "is niet het juiste woord.")
        tries -= 1
        guessed_words.append(guess)
      else:
        guessed = True
        word_completion = word

    else:
      print("Geen geldige invoer")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
  if guessed:
    print("Goed gedaan! Je hebt gewonnen!")
  else:
    print("Helaas... je hebt het woord niet geraden. Het woord was:" + word + ". Volgende keer beter!")


def display_hangman(tries):
    stages = [
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
  word = get_word()
  play(word)
  while input("Wil je opnieuw spelen? (Y/N)").upper() == "Y":
    word = get_word()
    play(word)


if __name__ == "__main__":
  main()