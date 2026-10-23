def brute_force():
    password = int(input("Enter a password..."))
    attempted_password = 0
    attempts = 0
    max_attempts = 100
    bot_amount = 0
    found = False 
    bots = [0] * bot_amount
    while attempted_password != password:
        attempted_password = attempted_password + 1
    if attempted_password == password:
        print(f"Password cracked! Password : {password}")
brute_force()