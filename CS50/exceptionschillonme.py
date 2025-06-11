def main():
    dictionary= {"balls":"100", "sigma":"5 m","dogma":"40"}
    x =input("Enter part to measure")
    try:
        au= float(dictionary[x])*100
    except ValueError:
        print("The value attached to the key could not be converted to float")
    except KeyError:
        print("The value inputted is not founds")
    else:
        print(f"The value in m is {au}")
main()