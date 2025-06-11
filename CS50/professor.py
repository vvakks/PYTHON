import random
import math

def main():
    level = get_level()
    count=0
    wrongcount=0
    for i in range(10):
        
        if wrongcount==0:
            a=generate_integer(level)
            b=generate_integer(level)
        companswer=a+b
        usanswer= int(input(f"{a}+{b}="))
        if(companswer==usanswer):
            count=count+1
            wrongcount=0
            continue
        else:
            print("EEE")
            wrongcount=wrongcount+1
            if(wrongcount==3):
                print(a,"+",b,"=",companswer)
                wrongcount=0
                continue
    print(f"You got {count} correct AAAA")
        
    


def get_level():
    while True:
        level= int(input("Enter level"))
        if(0<level<4):
            return(level)
        continue
    


def generate_integer(level):
    numrange=[]
    for i in range(int(math.pow(10,level))):
        numrange.append(i)
    return(random.choice(numrange))
        
        


if __name__ == "__main__":
    main()

# import random
# import math

# def main():
#     level = get_level()
#     count = 0

#     for i in range(10):
#         a = generate_integer(level)
#         b = generate_integer(level)
#         correct_answer = a + b
#         wrongcount = 0  # Reset for each question

#         while wrongcount < 3:
#             try:
#                 user_answer = int(input(f"{a} + {b} = "))
#                 if user_answer == correct_answer:
#                     count += 1
#                     break
#                 else:
#                     print("EEE")
#             except ValueError:
#                 print("EEE")
#             wrongcount += 1

#         if wrongcount == 3:
#             print(f"{a} + {b} = {correct_answer}")

#     print(f"You got {count} correct AAAA")


# def get_level():
#     while True:
#         try:
#             level = int(input("Enter level (1, 2, or 3): "))
#             if 1 <= level <= 3:
#                 return level
#         except ValueError:
#             continue


# def generate_integer(level):
#     if level == 1:
#         return random.randint(0, 9)
#     elif level == 2:
#         return random.randint(10, 99)
#     else:
#         return random.randint(100, 999)


# if __name__ == "__main__":
#     main()
