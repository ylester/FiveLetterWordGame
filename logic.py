import random
DATA_STORE = {}


def create_word_bank():
    f=open("words.txt", "r")
    f2 = open("valid_words.txt","w")
    for word in f:
        word = word.split()[0]
        if len(set(word)) == 5:
            f2.write(word + "\n")
    f2.close()


def pick_word():
    word_bank = open("valid_words.txt").readlines()
    return random.choice(word_bank).split()[0]


def guessed(guess_word, word):
    guess_word = guess_word.lower()
    if len(guess_word) > 5 or len(guess_word) < 5:
        print("Word must be 5 letters long, try again! \n")
        return 0
    if len(set(guess_word)) <= 3:
        print("Are you sure that's a real word? Try again!\n")
        return 0
    if guess_word.isalpha():
        correct = 0
        letters = [l for l in word]
        guess = set(guess_word)
        for val in guess:
            if val in letters:
                correct += 1
        print("Number of Correct Letters: {} \n".format(correct))
        return guess_word, correct
    else:
        print("Invalid Characters, try again")
        return 0


def counter(count):
    count -= 1
    if count == 3:
        print("3 Guesses Remaining \n")
        return count
    if count == 2:
        print("2 Guesses Remaining \n")
        return count
    if count == 1:
        print("1 Guess Remaining \n")
        return count
    return count


def store_data(guess_data):
    key = guess_data[0]
    value = guess_data[1]
    DATA_STORE[key] = value
    print(DATA_STORE)
    print()


def final_guess(word):
    final = input('Final Guess, What is the word?: \n')
    if final.lower() == word:
        print("Congrats!!! You Won!!")
    else:
        print("Sorry! Game Over! You Lose.")


def main():
    word = pick_word()
    count = 8
    while count != 0:
        guess = input('Guess a 5 letter word: \n')
        input_answer = guessed(guess, word)
        if input_answer == 0:
            continue
        else:
            store_data(input_answer)
            count = counter(count)
    final_guess(word)


if __name__ == "__main__":
    main()
