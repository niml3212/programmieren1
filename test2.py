import random
def RPS():
        choice = input("Enter your choice (Rock(1), Paper(2), Scissors(1)): ")
        #list = {"Rock", "Paper", "Scissors"}
        bot = random.randint(1,3)
        print(bot)
        if choice == 1 and bot == 2:
                print("Paper covers Rock, you lose!")
        elif choice == 2 and bot == 3:
                print("Scissors cuts Paper, you lose!")
        elif choice == 3 and bot == 1:
                print("Rock crushes Scissors, you lose!")
        elif choice == 1 and bot == 3:
                print("Rock crushes Scissors, you win!")
        elif choice == 2 and bot == 1:
                print("Paper covers Rock, you win!")
        elif choice == 3 and bot == 2:
                print("Scissors cuts Paper, you win!")
        elif choice == 1 and bot == 1:
                print("It's a tie!")
            

            
RPS()