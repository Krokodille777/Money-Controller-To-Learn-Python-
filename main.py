def check_balance(balance):
    print(f"Your balance is {balance} dollars.")
    return balance

myInventory = []
startMoney = 100
actions={
        "buy groceries" : 50,
        "visit a doctor": 25,
        "buy a new outfit": 200,
        "buy a circus ticket": 50,
        "rent an apartment": 500,
        "buy a car": 20000,
        "wedding":  10000,
        "birthday gift": 30
    }

command = input("Select a command: check_balance, work, do_action, exit")
if command != "exit":
    