import python 
words =["words","python","programming","developer","coding"]
word=random.choice(words)
guessed_letters=[]
max_wrong_guesses=0
wrong_guesses=0
print("WELCOME TOM HUNGAMA")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")
while wrong_guesses < max_wrong_guesses:
 display_word=""
 for letter in word:
  if letter in guesses_letters:
   display_word += letter + " "
else:
 display_word += "_ "
print("\nWord:", display_word)
if all(letter in guessed_letters for letter in word):
 print("Congratulations! You guessed the word!")
 print("The word was:", word)
break
guess = input("Enter a letter: ").lower()
if len(guess) != 1 or not guess.isalpha():
 print(" Please enter only one letter.")
continue
if guess in guessed_letters:
 print("You already guessed that letter.")
continue
guessed_letters.append(guess)
if guess in word:
 print("Correct guess!")
else:
 wrong_guesses += 1
print("Incorrect guesses left:", max_wrong_guesses - wrong_guesses)
if wrong_guesses == max_wrong_guesses:
 print("\n Game Over!")
print("The correct word was:", word)
 
