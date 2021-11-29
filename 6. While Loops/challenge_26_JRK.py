print("\nWelcome to the factor generator app.")
condicion = True
while condicion:
    user_input = int(input("\nEnter a number to determine all factors of that number: "))
    factors = []
    for i in range(1,user_input+1):
        if user_input % i == 0:
            factors.append(i)
    print(f"\nFactors of {user_input} are:\n")
    for i in factors:
        print(f"{i}")
    print(f"\nIn summary:")
    for i in range(int(len(factors)/2)):
        print(f"{factors[i]} * {factors[-i-1]} = {factors[i] * factors[-i-1]} ")
    stop = input("\nRun again (y/n): ").lower()
    if stop.startswith("n"):
        condicion = False
        print("Thank you for using the program. Have a great day.")