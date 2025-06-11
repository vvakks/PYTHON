def main():
    amtdue=50
    flag=0
    while True:
        x = int(input("Enter coin : "))
        if not(x==25 or x==10 or x==5):
            continue
        else:
            amtdue=amtdue-x
            print(f"amount due is {amtdue}")
            if(amtdue<0):
                break
            elif(amtdue==0):
               
                flag=1
                break
            else:
                continue
    if(flag==0):
        print(f"Your change is {abs(amtdue)}")
    else:
        print("Thank you")
main()