def brute_force():
    password = int(input("Input a password: "))
    guesses = [0, 0, 0, 0, 0, 0]
    attempts = 0
 
    while attempts < 50:
        guesses[0] = guesses[0] + 1
        guesses[1] = guesses[1] + 2
        guesses[2] = guesses[2] + 3
        guesses[3] = guesses[3] + 4
        guesses[4] = guesses[4] + 5
        guesses[5] = guesses[5] + 6
        attempts = attempts + 1
        
        print(f"Attempt {attempts}: Bots are trying numbers {guesses}")
        
        found = False
        
        if guesses[0] == password:
            print(f"Bot 1 has cracked the password on attempt {attempts}!")
            found = True
        if guesses[1] == password:
            print(f"Bot 2 has cracked the password on attempt {attempts}!")
            found = True
        if guesses[2] == password:
            print(f"Bot 3 has cracked the password on attempt {attempts}!")
            found = True
        if guesses[3] == password:
            print(f"Bot 4 has cracked the password on attempt {attempts}!")
            found = True
        if guesses[4] == password:
            print(f"Bot 5 has cracked the password on attempt {attempts}!")
            found = True
        if guesses[5] == password:
            print(f"Bot 6 has cracked the password on attempt {attempts}!")
            found = True
            
        if found == True:
            break
            
    else:
        print(f"Too many attempts! You have been locked out! Attempts: {attempts}")

brute_force()
