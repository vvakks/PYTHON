WORDS = {"PAIR":4, "HAIR":4, "CHAIR":5}
def main():
    print("Your letters are A I P C R H G")
    while len(WORDS)>0:
        print(f"{len(WORDS)} words left")
        guess = input("Guess a word:")

        if guess in WORDS.keys():
            
            points = WORDS.pop(guess)
            print(f"Good job! You scored {points} points.")
main()


