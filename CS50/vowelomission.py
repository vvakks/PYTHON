def main():
    x= input("Enter tweet: ")
    vowels= ['a','e','i','o','u','A','E', 'I','O','U']
    y=""
    i=0
    for letter in vowels and i in range(len(x)):
        
        if(letter== x[i]):
            y=y+""
        else:
            y=y+x[i]
        i=i+1
    print(y)
main()
