n= input("Enter your greeting").lower().strip()
money=100
if(n[0]=="h"):
    money=20
if(n.find("hello")>-1):
    money=0
print(money,"$")
