def main():
    x = input("Enter camel case: ")
    print(snake_case(x))
def snake_case(x):
    x1=""
    for i in range(len(x)):
        if(ord(x[i])<97 and i>0):
            x1=x1+"_"+x[i].lower()
        else:
            x1=x1+x[i]
    return x1
main()