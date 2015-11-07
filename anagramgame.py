from random import randint
from getpass import getpass
from functions1 import InputInt
while True:
    print("ANAGRAM GAME")
    scores = [0,0]
    # ask user for number of rounds
    rounds = InputInt("How many rounds do you want to play? ")
    # loop for number of rounds user has entered
    for i in range(rounds):
        # loop twice (once for each player)
        for j in range(2):
            thisplayer = "Player " + str(j + 1)
            otherplayer = "Player " + str(2 - j)
            letters1 = []
            letters2 = []
            numbers = []
            print(thisplayer.upper())
            # ask user for word
            word = getpass("Enter a word for {0} to guess: ".format(otherplayer))
            length = len(word)
            # add each letter of word to list
            for k in range(length):
                letters1.append(word[k])
            for k in range(length):
                while True:
                    # pick random number
                    random1 = randint(0,length - 1)
                    numberexists = False
                    # check if random number is already in array by
                    # comparing it to each number already in array
                    for l in range(len(numbers)):
                        if random1 == numbers[l]:
                            numberexists = True
                    if numberexists == False:
                        break
                # add random number to array
                numbers.append(random1)
                letters2.append(letters1[random1])
            anagram = ""
            for k in range(length):
                anagram += letters2[k]
            print("Anagram generated")
            input("Press enter to continue...")
            print()
            print(otherplayer.upper())
            print("Solve this anagram: " + anagram)
            print("Answer is case-sensitive - make sure you use the correct case!")
            answer = input("Answer: ")
            if answer == word:
                print("Correct! {0} gains 1 point".format(otherplayer))
                scores[1 - j] += 1
            else:
                print("Incorrect! {0} gains 1 point".format(thisplayer))
                print("Correct answer is: " + word)
                scores[j] += 1
            print()
            print("Player 1 score: {0}".format(scores[0]))
            print("Player 2 score: {0}".format(scores[1]))
            if i != rounds - 1 or j != 1:
                input("Press enter to continue...")
            print()
    print("Game over")
    if scores[0] > scores[1]:
        print("Player 1 wins!")
    elif scores[0] < scores[1]:
        print("Player 2 wins!")
    else:
        print("Draw!")
    option = input("Play again? Enter y or n: ")
    if option.lower() != "y":
        break
    print()
