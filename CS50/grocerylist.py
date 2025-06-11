def main():
    y={}
    
    while True:
        try:
            x = input("Enter grocery list").strip().title()
            
            if x in y:
                y[x]= y[x]+1
                print(y.keys())
            else:
                y[x]=1
                print(y.keys())
        except EOFError:
            print()
            break
    for item, count in sorted(y.items()):
        print(f"{count} {item}")
main()
    
        