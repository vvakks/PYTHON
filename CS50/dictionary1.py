WORDS = {"BEAR":12, "GEAR":10, "WEAR":5, "CHARMANDER":11}
def main():
    while len(WORDS)>0:
        guess = input("INPUt guess")
        print(f"There are {len(WORDS)} left")
        if guess in WORDS.keys():
            points = WORDS.pop(guess)
            print(f"You have scored{points} points")
main()



