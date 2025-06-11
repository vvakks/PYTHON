def main():
    x= input("enter word")
    shorten(x)
    
def shorten(word):
    return(word.replace('a','e'))


if __name__=="__main__":
    main()