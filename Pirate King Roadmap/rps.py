import random

class RPS:
    def __init__(self):
        self.choices = ("rock", "paper", "scissors")
        self.cpu_choice = self.choices[random.randint(0, 2)]

    def randomize(self):
        self.cpu_choice = self.choices[random.randint(0, 2)]

    def get_choice(self):
        player_choice = input("Enter a choice (rock, paper, scissors): ").lower()

        while player_choice not in self.choices:
            player_choice = input("Invalid input. Enter a choice (rock, paper, scissors): ")

        return player_choice
    
    def play(self):
        print("Welcome to rock, paper, scissors!")

        #while True:
        opponent = input("Go against CPU or player: ").lower()

        if opponent == "cpu":
            p1 = input("Enter a choice (rock, paper, scissors): ")

            print(f"\nPlayer: {p1}")
            print(f"Computer: {self.cpu_choice}\n")

            if p1 == self.cpu_choice:
                print("It's a tie!")
            elif p1 == "rock" and self.cpu_choice == "scissors":
                print("You win!")
            elif p1 == "paper" and self.cpu_choice == "rock":
                print("You win!")
            elif p1 == "scissors" and self.cpu_choice == "paper":
                print("You win!")
            else:
                print("You lose!")

rps = RPS()
rps.play()