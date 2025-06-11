def main():
    history = []
    while True:
        action = input("Action")
        if(action== "Undo"):
            undone = history.pop()
            print(undone)
            continue
        history.append(action)
        print(history)
        
        if(action== "Restart"):
            history.clear()
        elif(action== "Stop"):
            break
main()
