def main():
    print("You stand before an old hospital, rain pouring down, you feel a chill.")

    choice = input("Would you like to Enter the hospital? (y/n) ").strip().lower()
    if choice == "y":
        print("You step inside…")

        door = input("Would you like to go Left or right? (l/r) ").strip().lower()
        if door == "l":
            print("Cold air. A whisper: 'Welcome'. Then you woke up from your dream with unexplainable fear.")
            print("Thank You for playing")
            return

        elif door == "r":
            print("Footsteps above. The lights die, everything is dark and you suddenly feel weird. You pass out and wake up outside again.")
            again = input("Play again? (y/n): ").strip().lower()
            if again == "y":
                main()
            else:
                print("Thank you for playing!")
                return
        else:
            print("You freeze. Something watches.")

    elif choice == "n":
        print("You walk away. The rain follows anyway.")
    else:
        print("Silence answers your hesitation.")

if __name__ == "__main__":
    main()
