def main():
    x = input("Enter tweet: ")
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    y = ""
    for letter in x:
        if letter not in vowels:
            y = y + letter
    print(y)

main()