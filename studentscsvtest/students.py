import csv

name = input("whats your name? ")
home = input("Where is your home? ")

with open("students.csv", "a") as file:
        writer= csv.DictWriter(file, fieldnames=["name", "home"])
        writer.writerow({"name":name,"home":home})