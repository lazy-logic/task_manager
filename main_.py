# Interactive CLI game where the player makes decisions that affect their budget and inventory.

# 1. Print welcome message
print("Welcome to the the GROW C6_Adventure Game!")
# 2. Ask for player name
player_name = input("Enter your Nickname (make it fancy): ")
# 3. Ask for starting budget 
while True: 
    try:
        starting_budget = int(input("Enter your starting budget: "))
        break
    except ValueError:
        print("Please enter a valid integer for your budget.")
# 4. Create inventory list
inventory = {"Fruit": [], "Wood": [], "Tools": [],}

# 5. Display starting location
print(f"{player_name} is in a small village.")
# 6. Decision 1: Shop or farm
decision_1 = input("Choose a direction (Shop/Farm): ").strip().lower()
if decision_1 == "shop":
    starting_budget -= 10
    inventory["Fruit"].append("Apple")
elif decision_1 == "farm":
    starting_budget += 20
    inventory["Wood"].append("Oak")
# 7. Move to Second Scene

# --- Second Scene ---
# 8. Decision 2: 
#    - Sell items or keep them
decision_2 = input("Do you want to sell your items or keep them? (Sell/Keep): ").strip().lower()
if decision_2 == "sell":
    starting_budget += 30
    for key in inventory:
        inventory[key] = []
elif decision_2 == "keep":
    pass 

# 8.1 Display current budget and inventory
print(f"Current Budget: {starting_budget}")
print(f"Current Inventory: {inventory}")


# 10. Decision 3: Enter tournament or skip
decision_3 = input("Do you want to enter the tournament or skip? (Enter/Skip): ").strip().lower()
if decision_3 == "enter":
    starting_budget -= 20
    if starting_budget > 50:
        starting_budget += 100
        if "Tools" not in inventory:
            inventory["Tools"] = []
        inventory["Tools"].append("Trophy")
    else:
        pass
elif decision_3 == "skip":
    pass
# 11. Display current budget and inventory after tournament decision
print(f"Current Budget: {starting_budget}")
print(f"Current Inventory: {inventory}")

# 12. Decision 4: Go home or continue adventure
decision_4 = input("Do you still want to continue or exit? (exit/continue): ").strip().lower()
if decision_4 == "exit":
    print("You have chosen to go home. Safe travels!")
elif decision_4 == "continue":
    print("You have chosen to continue your adventure. Be brave!")
# 13. Show final budget and inventory
print(f"Final Budget: {starting_budget}")
print("You are now in the village square.")
# 14. If budget >= 100: win ending, else: survival ending 
print("You have collected the following items:")
print("Final Inventory:")
for category, items in inventory.items():
    print(f"{category}: {', '.join(items)}")
if starting_budget >= 100:
    print("Congratulations! You have achieved a win ending.")
else:
    print("You have reached a survival ending.")



