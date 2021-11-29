print("\nWelcome to the Even Odd Number App")
condicion = True
while condicion :
    user_input = input("\nEnter in a string of numbers separated by a comma (.) : ").replace(" ","").split(",")
    evens = []
    odds = []
    print(f"\n----Result Summary----")
    for i in user_input:
        if int(i) % 2 == 0:
            print(f"\t{i} is even!")
            evens.append(int(i))
        else:
            print(f"\t{i} is odd!")
            odds.append(int(i))  
    odds = sorted(odds)
    evens = sorted(evens)   
    print(f"\nThe following {len(evens)} numbers are evens:")
    for i in evens:
        print(f"\t{i}")   
    print(f"\nThe following {len(odds)} numbers are odds:")
    for i in odds:
        print(f"\t{i}")  
    stop = input("\nWould you like to run the program again (y/n):").lower().strip()
    if stop.startswith("n"):
        condicion = False
        print("Thank you for using the program. Goodbye.")
#[JRK]