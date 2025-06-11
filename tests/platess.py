def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(s):
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    if(len(s)>6 or len(s)<2):
        return False
    flag=0
    count=0
    for i in range(len(s)):
        if(s[i].isdigit()):
            flag=flag+1
            if(flag==1):
                count=i+1
            
        
    if(flag==(len(s)-count) and not s[count]== "0"):
        return True
    else:
        return False
if __name__ == "__main__":
    main()