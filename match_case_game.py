import random

def play_game():
    secret_number = random.randint(1, 10)
    guess_count = 0

    print("🎯 I'm thinking of a number between 1 and 10. Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("❗ Please enter a valid number.")
            continue

        guess_count += 1

        match guess:
            case number if number == secret_number:
                print("🎉 Congratulations, you guessed it!")
                print(f"✅ You got it in {guess_count} guess{'es' if guess_count > 1 else ''}!")
                break
            case number if number > secret_number:
                print("📈 Oops, your guess is a bit high. Try again!")
            case number if number < secret_number:
                print("📉 Nope, your guess is a bit low. Give it another shot!")

while True:
    play_game()
    again = input("\n🔁 Play again? (yes/no): ").strip().lower()

    match again:
        case "yes" | "y":
            print("\n🎮 Starting a new game...\n")
            continue
        case "no" | "n":
            print("👋 Thanks for playing! Goodbye.")
            break
        case _:
            print("🤔 Invalid response. Exiting game.")
            break
