'''
CIS 122 Winter 2020 Assignment 5
Author: Rebecca Lee
Credit:
References: http://www.learningaboutelectronics.com/Articles/Escape-characters-in-Python.php
Description: Create a guessing game
'''
#Prompt the user for a guess word
#Prompt the user for a letter
#Empty word or letter input will exit the program
"""
After each letter guess, if all letters not found, display the guess
status (tabbed over on tab space):
    indicate if already guessed and already found
    indicate if already guessed and already not found
    indicate if guessed letter not found
    indicate if guessed letterr found
    follow the guess status with the complete list of letters guessed
    so far
Upon program exit, or when all letters have been guessed,
display results if any guesses were made
    Display original guess word
    Display matched letters
    Display unmatched letters
    display total number of guesses
Guess letters need only be entered once even if letters are repeated
in a guess word.
"""

"""Design specifications



Use accumulator variables for matched, umatched and total guesses variables
Use the tab escape character to indent guess status information (ie tabbed)
Guess status information must be preceded by ">" and have
the following format (where x is the guessed letter)
    >x not found
    >x already guessed
    >x already guessed and found
    >x found
After each guess status, display the complete list of guessed letters in the
    following format (where esta represents the matched and unmatched
    guessed letters combined:
    >Guesses so far: esta
If the letter entered is more than single character in length,
    display the following error message tabbed,
    and re-prompt the user for another letter
    >Only enter a single letter
Use the tab escape character to align final result information in columns
Word prompt must be: "Enter a guess word(blank to quit):"
Letter prompt must be: "Enter a guess letter (blank to quit):"
Separate the final results with a blank line
The first line of the results must be "***Results***"
The second line must be "Word:" followed by the original guess word,
    tabbed to align with the subsequent result line values
The third line must be "Matched:" followed by the matched guessed letters,
    tabbed to align with the subsequent result line values
The fourth line must be "Unmatched:" followed by the unmatched guessed
    letters, tabbed to align with the subsequent result line values
The fifth line must be "Guesses:" followed by the total
    number of letters guessed, tabbed to align with all
    the line values.
"""



#This code adds the option of breaking if space is entered for either word or letter
'''
guess_word = input("Enter a guess word(blank to quit):")


matched = ''
guesses = 0
all_guesses = ''
for guess_letter in guess_word:
    if guess_word == '\n':
        break
    else:
        if len(guess_letter)==len("a"):
            while matched != guess_word:
                guesses = guesses + 1
                guess_letter = input("Guess a letter (blank to quit):")
                all_guesses = all_guesses + guess_letter

                if guess_letter in guess_word:
                    print("\t >", guess_letter, "found")
                    print("\t > Guesses so far:", all_guesses)
                    matched = matched + guess_letter
                    
                elif guess_letter != len("a"):
                    print("Only enter a single letter")

                elif guess_letter in guess_word and all_guesses:
                    print("\t >", guess_letter, "already found")
                    
                
                    
                elif guess_letter not in guess_word:
                    print("\t >", guess_letter, "not found")
                    print("\t > Guesses so far:", all_guesses)
                    


            
        elif guess_letter == '\n':
            break
        
        
            

print("\t > All letters found \n") # \n leaves blank space after the printed lin

print("*** Results ***")
print("Word: \t \t", guess_word)
print("Matched: \t", matched) #TODO create variable that counts matched letters
print("Unmatched: \t")
print("guesses: \t", guesses)
'''

#TODO:
#add option when guess_letter already guessed
#fix bug so that matched words only appear once if guessed more than once
'''

guess_word = input("Enter a guess word(blank to quit):")


matched = ''
guesses = 0
all_guesses = ''
for guess_letter in guess_word:
    if guess_word == '\n':
        break
    else:
        if len(guess_letter)==len("a"):
            while matched != guess_word:
                guesses = guesses + 1
                guess_letter = input("Guess a letter (blank to quit):")
                all_guesses = all_guesses + guess_letter

                if guess_letter in guess_word:
                    print("\t >", guess_letter, "found")
                    print("\t > Guesses so far:", all_guesses)
                    matched = matched + guess_letter
                    
                elif guess_letter != len("a"):
                    print("Only enter a single letter")

                elif guess_letter in guess_word and all_guesses:
                    print("\t >", guess_letter, "already found")
                    
                
                    
                elif guess_letter not in guess_word:
                    print("\t >", guess_letter, "not found")
                    print("\t > Guesses so far:", all_guesses)
                    


            
        elif guess_letter == '\n':
            break
        
        
            

print("\t > All letters found \n") # \n leaves blank space after the printed lin

print("*** Results ***")
print("Word: \t \t", guess_word)
print("Matched: \t", matched) #TODO create variable that counts matched letters
print("Unmatched: \t")
print("guesses: \t", guesses)
'''
#DO NOT ERASE THIS CODE. BEST WORKING CODE YET
'''
guess_word = input("Enter a guess word(blank to quit):")


matched = ''
unmatched = ''
guesses = 0
all_guesses = ''
for guess_letter in guess_word:
    if guess_word == '\n':
        break
    else:
        if len(guess_letter)==1:
            while matched != guess_word:
                guesses = guesses + 1
                guess_letter = input("Guess a letter (blank to quit):")
                all_guesses = all_guesses + guess_letter

                if guess_letter in guess_word:
                    print("\t >", guess_letter, "found")
                    print("\t > Guesses so far:", all_guesses)
                    matched = matched + guess_letter

                elif guess_letter not in guess_word:
                    print("\t >", guess_letter, "not found")
                    print("\t > Guesses so far:", all_guesses)
                    unmatched = unmatched + guess_letter
                    
                else:
                    if len(guess_letter) != 1:
                        print("Only enter a single letter")
                
                    


            
        elif guess_letter == '\n':
            break
        
        
            

print("\t > All letters found \n") # \n leaves blank space after the printed lin

print("*** Results ***")
print("Word: \t \t", guess_word)
print("Matched: \t", matched) #TODO create variable that counts matched letters
print("Unmatched: \t", unmatched)
print("guesses: \t", guesses)
'''


#TO DO FIX if given a word with a repeating letter
#Fix if space if given then break does not print the ending results

guess_word = input("Enter a guess word(blank to quit):")


matched = ''
unmatched = ''
guesses = 0
all_guesses = ''
for guess_letter in guess_word:
    if guess_word == '\n':
        break
    else:
        if len(guess_letter)==1:
            while matched != guess_word:
                guesses = guesses + 1
                guess_letter = input("Guess a letter (blank to quit):")
                all_guesses = all_guesses + guess_letter

                
                if guess_letter in guess_word and (guess_letter not in matched):
                    print("\t >", guess_letter, "found")
                    print("\t > Guesses so far:", all_guesses)
                    matched = matched + guess_letter

                elif guess_letter in guess_word and (guess_letter in matched):
                    print("\t >", guess_letter, "already guessed and found")
                    print("\t > Guesses so far:", all_guesses)

                elif guess_letter not in guess_word and (guess_letter not in unmatched):
                    print("\t >", guess_letter, "not found")
                    print("\t > Guesses so far:", all_guesses)
                    unmatched = unmatched + guess_letter

                elif guess_letter not in guess_word and (guess_letter in unmatched):
                    print("\t >", guess_letter, "already guessed and not found")
                    print("\t > Guesses so far:", all_guesses)
                    
                else:
                    if len(guess_letter) != 1:
                        print("Only enter a single letter")
                
                    


            
        elif guess_letter == '\n':
            break
        
        
            

print("\t > All letters found \n") # \n leaves blank space after the printed lin

print("*** Results ***")
print("Word: \t \t", guess_word)
print("Matched: \t", matched) #TODO create variable that counts matched letters
print("Unmatched: \t", unmatched)
print("guesses: \t", guesses)
