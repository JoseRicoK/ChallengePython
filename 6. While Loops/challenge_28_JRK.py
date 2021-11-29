import time

print("\nWelcome to the prime number app")

condicion=True

while condicion:
    print(f"\nEnter 1 to determinate if a specific number is prime.")
    print(f"Enter 2 to determinate all prime numbers within a set range.")
    eleccion = input("Enter your choice (1/2): ")
    if eleccion == "1":
        prime_number = int(input("\nEnter a number to determine if it is prime or not: "))
            
            # Ponemos el número cómo primo de forma predeterminada y analizamos si es primo o no buscando sus divisores
        isPrime=True
        for i in range(2,prime_number):
            if prime_number%i == 0:
                isPrime=False
                break
        if isPrime:
            print(f"\n{prime_number} is prime.\n")    
        else:
            print(f"\n{prime_number} is not prime.\n")    
    elif eleccion == "2":
        star_range = int(input("Enter the lower bound of your range:\t"))
        stop_range = int(input("Enter the upper bound of your range:\t"))        
        primes = []   
        time_start = time.time()
        for i in range(star_range, stop_range+1):
            if i > 1:
                isPrime=True
                for j in range(2,i):
                    if i % j == 0:
                        isPrime=False
                        break     
            else:
                isPrime=False
            if isPrime:
                primes.append(i)
        end_time = time.time()
        delta_time = round(end_time - time_start,4)
        print(f"Calculations took a total of {str(delta_time)} seconds")
        print(f"The following numbers between {str(star_range)} and {str(stop_range)} are prime: ")
        input("Press enter to continue")
        for prime in primes:
            print(f"{prime}")
    else:
        print("That is not a valid option.")
    continue_program = input("Would you like to run the program again (y/n):").lower().strip()
    if continue_program.startswith("n"):
        condicion = False
        print("\nThank you for using the program. Have a nice day.")
#[JRK]