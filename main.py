from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)

class DiceGame:
    def __init__(self):
        self.die1 = Die()
        self.die2 = Die()

    def play_round(self):
        roll1 = self.die1.roll()
        roll2 = self.die2.roll()
        total = roll1 + roll2
        result = self.evaluate_roll(total)
        return roll1, roll2, total, result

    def evaluate_roll(self, total):
        if total in [7, 11]:
            return "Win"
        elif total in [2, 3, 12]:
            return "Lose"
        else:
            return "Roll Again"
        
def main():
    while True:
        print("1. Play a round")
        print("2. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                game = DiceGame()
                roll1, roll2, total, result = game.play_round()
                print(f"Die 1: {roll1}, Die 2: {roll2}, Total: {total}, Result: {result}")
            elif choice == 2:
                break
            else:
                print("Invalid input. ")
        except:
            print("Invalid input. ")

#no idea why this works but it looked cool in the other file
if __name__ == "__main__":
    main()