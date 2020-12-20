import random

content = ("car,man,home,door,table,computer")
word_list = content.split(",")

while True:
    chance = 5

    word = random.choice(word_list)

    known = list()

    for i in range(len(word)):
        known.append("_")

    while known.count("_") > 0:
        print(known)
        print("chance:", chance)
        letter = input("Enter a letter: ")

        if word.find(letter) == -1:
            chance -= 1
            if chance < 0:
                print("You lose")
                exit()

        else:
            for i in range(len(word)):
                if letter == word[i]:
                    known[i] = letter

    print(known)
    print("Congratulations")
