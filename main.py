import time

def check_balance(balance):
    print(f"Your balance is {balance} dollars.")
    return balance
def work(balance):
    work_type = input("What type of work do you want to do this time? (full_time, part_time)")
    time.sleep(1)
    print("Working...")
    time.sleep(1)

    if work_type == "full_time":
        balance += 500
        print("You worked full time and earned 500 dollars.")
    elif work_type == "part_time":
        balance += 250
        print("You worked part time and earned 250 dollars.")
    else:
        print("Invalid work type.")
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

command = input("Select a command: /check_balance, /work, /do_action, /exit")
if command != "/exit":
    if command == "/check_balance":
        startMoney = check_balance(startMoney)
    elif command == "/work":
        startMoney = work(startMoney)
