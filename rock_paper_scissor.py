import random

computer_win=0

user_win=0
round_count = 1

while round_count <= 5:

    print("\n---Rock-Paper-Scissors Game---")
    print(f"--- Round {round_count} ---")
    print()
    print("1-rock")
    print("2-paper")
    print("3-scissors")

    try:
        choice=int(input("enter your choice(1-3):"))
        if choice==1:
            uchoice="rock"
        elif choice==2:
            uchoice="paper"
        elif choice==3:
            uchoice="scissors"
        else:
            print("Invalid choice! Try again.")
            continue
            
        print("\nyou choose:",uchoice)

        computer=random.choice([1,2,3])
        if computer==1:
            cchoice="rock"
        elif computer==2:
            cchoice="paper"
        else:
            cchoice="scissors"
        print("computer choose:",cchoice)

        if(uchoice==cchoice):
            print("\nIt's a draw!")
        elif(uchoice=="rock" and cchoice=="paper"):
            print("\ncomputer won")
            computer_win+=1
        elif(uchoice=="rock" and cchoice=="scissors"):
            print("\nyou won")
            user_win+=1
        elif(uchoice=="paper" and cchoice=="rock"):
            print("\nyou won")
            user_win+=1
        elif(uchoice=="paper" and cchoice=="scissors"):
            print("\ncomputer won")
            computer_win+=1
        elif(uchoice=="scissors" and cchoice=="rock"):
            print("\ncomputer won")
            computer_win+=1
        elif(uchoice=="scissors" and cchoice=="paper"):
            print("\nyou won")
            user_win+=1

        round_count+=1
    except Exception as e:
        print(f"error occured:{e}")

print("\n--- Final Score ---\n")
print("computers win count:",computer_win)
print("yours win count:",user_win)

if user_win > computer_win:
    print("\n🎉 Congratulations! You are the overall winner!")
elif user_win < computer_win:
    print("\n💻 Computer is the overall winner!")
else:
    print("\n🤝 It's a tie overall!")