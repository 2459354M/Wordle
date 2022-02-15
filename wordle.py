from operator import length_hint
import random


def readfile():
    with open("Data/words.txt") as file:
        data = file.read()
        data = data.split("\n")
        filtered_data = []
        remove = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ.!£$%^&*()-_=';[];'#./`¬"
        for i in data:
            bad_word = False
            for j in i:
                if j in remove:
                    bad_word = True
                    break
            if not bad_word:
                filtered_data.append(i)
    return filtered_data

def play_game(words, lettercount, attempts=5):
    words = [i for i in words if len(i) == lettercount]
    target_word = random.choice(words)
    target_word_as_list = list(target_word)
    winner = False
    while attempts >= 0:
        attempt = input("Enter a word: ")
        if attempt == target_word:
            print("Congratulations you have guessed the word correctly")
            winner = True
            break
        elif len(attempt) == lettercount:
            attempt = list(attempt)
            feedback_word = ["X" for i in range(lettercount)]
            for i in range(lettercount):
                if attempt[i] in target_word:
                    if attempt[i] == target_word_as_list[i]:
                        feedback_word[i] = "@"
                    else:
                        feedback_word[i] = "-"
            print(attempt)
            print(str(feedback_word))
            print("{} attempts remaining".format(attempts))
            attempts -= 1
        else:
            print(attempt)
            print("invalid word!")
    if not winner:
        print("the word was {}!".format(target_word))
        print("try again")


def main():
    words = readfile()
    letter_count = int(input("Enter letter count: "))
    play_game(words,letter_count)




if __name__ == "__main__":
    main()