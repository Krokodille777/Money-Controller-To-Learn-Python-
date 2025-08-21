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

def do_action(balance, action):
    cost = actions.get(action, None)
    if cost is None:
        print ("Invalid action")
        return balance
    if balance < cost:
        print ("Insufficient funds")
        return balance
    
    if action == "buy_groceries":
        print ("You bought groceries. You saved yourself for a couple of days. Enjoy!! 🥦")
        balance -= cost
        return balance
    if action == "visit_a_doctor":
        print ("You visited a doctor. He found out you have ebola, just kidding! 😂")
        balance -= cost
        return balance
    if action == "buy_a_new_outfit":
        print ("You bought a new outfit. Now all your friends will be jealous! 👗")
        balance -= cost
        return balance
    if action == "buy_a_circus_ticket":
        print ("You bought a circus ticket. Hope you aren't scared of clowns! 🤡")
        balance -= cost
        return balance
    if action == "rent_an_apartment":
        print ("You rented an apartment. Feel comfortable in your small vault until the next paycheck! 🏠")
        balance -= cost
        return balance
    if action == "buy_a_car":
        print ("You bought a car. Remember: no drunk driving! 🚗")
        balance -= cost
        return balance
    if action == "wedding":
        print ("The sweetest day of your life! Hope your bride feels the same way! 💍")
        balance -= cost
        return balance
    if action == "birthday_gift":
        print ("You bought a birthday gift. You're so thoughtful! But who is the lucky recipient? 🎁")
        balance -= cost
        return balance
def exit():
    print("Exiting the game. Are you sure? 😢")
    confirmation = input("Type 'yes' to confirm: ")
    if confirmation == "yes":
            print("It was a pleasure playing with you! 😊")
    else:
            print("Don't think you can escape that easily, sugar! 😏")
startMoney = 100
actions={
        "buy_groceries" : 50,
        "visit_a_doctor": 25,
        "buy_a_new_outfit": 200,
        "buy_a_circus_ticket": 50,
        "rent_an_apartment": 500,
        "buy_a_car": 20000,
        "wedding":  10000,
        "birthday gift": 30
    }
while True:
    command = input("Select a command: /check_balance, /work, /do_action, /show_actions, /exit \n")
    if command != "/exit":
        if command == "/check_balance":
            startMoney = check_balance(startMoney)
        elif command == "/work":
            startMoney = work(startMoney)
        elif command == "/show_actions":
            print("Available actions:")
            for action in actions.keys():
                print(f" - {action.replace('_', ' ')}")
        elif command == "/do_action":
            action = input("Enter the action you want to do: ")
            startMoney = do_action(startMoney, action)


    
    if command == "/exit":
        exit()
        break