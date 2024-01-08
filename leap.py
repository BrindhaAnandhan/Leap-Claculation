def leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print ("This is leap year")
    else:
        print("This is not a leap year")

if __name__ == "__main__":
    leap(int(input("Enter year: ")))