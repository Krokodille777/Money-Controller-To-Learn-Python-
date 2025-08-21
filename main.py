
def buy_item(items, inventory, balance):
    item = input("Enter the item you want to buy: ")
    if item in items:
        if balance >= items[item]:
            inventory.append(item)
            balance -= items[item]
            print(f"You bought a {item} for {items[item]}.")
        else:
            print("You don't have enough money.")
    else:
        print("Item not found.")
    return inventory, balance

def main():
    myInventory = []
    startMoney = 100
    items ={
        "banana": 2,
        "sack_of_sugar": 10,
        "pair_of_gloves": 35,
        "ticket_to_circus":50,
        "dress": 90,
        "cat": 200,
        "car" : 500,
        "house":1000,
        "diamond":1000000
    }
    print("Select a command: buy_item, sell_item, check_balance, work, inventory, exit")