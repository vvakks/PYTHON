import requests
import emoji
import inflect
p= inflect.engine()
from pyfiglet import Figlet
figlet= Figlet()
def main():
    joinedword=[]
    while True:
        try:
            name = input("name")
            joinedword.append(name)
        except EOFError:
            print(p.join(joinedword))
            break
                
main()
    