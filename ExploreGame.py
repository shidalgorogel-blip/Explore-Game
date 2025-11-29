import random


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.score = 0
        self.inventory = []
    
    def add_item(self, item):
        self.inventory.append(item) #inventory
        print(f"{item} has been added to your inventory.")

    def use_potion(self, item):
        if "Health Potion" in self.inventory: #one of the items that can be used in inventory
            self.health += 20
            self.inventory.remove("Health Potion")
            print("You used a Health Potion. Health increased by 20.")
        else:
            print("You don't have a Health Potion in your inventory.")
    def use_sword(self, item):
        if "Silver Sword" in self.inventory: # Another item that can be used in inventory
            self.health += 5
            self.inventory.remove("Silver Sword")
            print("You have an increased health due to protection +5 ")
    def show_status(self):
        print(f"Name: {self.name}, Health: {self.health}, Score: {self.score}, Inventory: {self.inventory}")


name = input("Enter your name, adventurer: ")
player = Player(name)

print(f"Welcome, {player.name}! Your journey begins...")

locations = ["forest", "castle"]
Winning_score = 50

def random_treasure():
    return random.choice(["Silver Sword", "Health Potion"]) #gives random items 


def random_encounter():
    battle = random.choice(["goblin", "dragon"]) #the different creatures that will be encountered
    if battle == "goblin":
        print("A goblin appears!")
        battle_action = input("Do you [fight] or [flee]? ")
        if battle_action.lower() == "fight":
            print("You defeated the goblin!")
            damage = 10
            player.score += 10
            player.health -= damage 
            treasure = random_treasure()
            player.add_item(treasure)
            print(f"You took {damage} damage but gained 10 score.")

        elif battle_action.lower() == "flee":
            print("You fled from the goblin!")
        else:
            print("The goblin attacks you because you hesitate!")
            damage = 5
            player.health -= damage
            print(f"You took {damage} damage")

    elif battle == "dragon":
        print("A dragon appears!")
        battle_action = input("Do you [fight] or [flee]? ")
        if battle_action.lower() == "fight":
            print("You bravely fought the dragon and won!")
            damage = 30
            player.score += 50 # will change player score
            player.health -= damage
            treasure = random_treasure()
            player.add_item(treasure)
            print(f"You took {damage} but gaine 50 score.")

        elif battle_action.lower() == "flee":
            print("You fled from the dragon!")
        else:
            print("The dragon engulfs you in flames because you hesitate!")
            damage = 15
            player.health -= damage
            print(f"You took {damage} damage.")

    print(f'Current Health: {player.health}, Score: {player.score}\n')

def explore(location): #Finds a random location with random encounters
    print(f"You walk into the {location}.") # This 
    if player.health <= 0: #checks if plahyers health is above zero 
        print("You're not strong enough")
        return
    random_encounter()
    if location in locations:                             #This makes sure if all locations have been explored
        locations.remove(location)
    
    if len(locations) == 0:
        if player.score >= Winning_score:
            print(f"Congrats {player.name} You win!")
        else:
            print(f"You did not win!")
        exit()
    
def check_win():
    if locations_played >=2: # Checks if player has played two locations and if so decided if they won or not
        print(f'You have completed {locations_played} adventures!')
        if player.score >= Winning_score:
            print(f'Congrats, {player.name}! You won with a score of {player.score}!')
        else:
            print(f'Sorry! You did not win because you had a score of {player.score}!')
        print("Game over!")
        exit()
    else:
        print("Choose your next adventure\n")

    

def main():
    print("Type 'explore forest', 'explore castle', quit to exit, or 'status' to view your status.")
    # TODO: Add a 'status' command to show health, inventory, and score
    while True:
        if locations:
            print("Available locations:", ", ".join(locations))
        command = input("> ").lower()
        
        if command.startswith("explore "):
            loc = command.replace("explore ", "")
            if loc in locations:
                explore(loc)
            else:
                print("You have already explored that location")
        elif command == "quit":
            print("Thanks for playing!")
        elif command == "status":
            player.show_status()
            break
        else:
            print("Invalid command. Try 'explore forest', explore castle 'status', or 'quit'")
            # TODO: Suggest valid commands when input is invalid

if __name__ == "__main__":
    main()
