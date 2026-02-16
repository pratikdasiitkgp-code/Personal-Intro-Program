# Personal Introduction Program
# Week 1 Internship Task – Python Basics

def main():
    print("=== Welcome to the Personal Introduction Program ===\n")

    # Taking user input
    name = input("Enter your name: ").strip()
    
    # Age validation
    while True:
        try:
            age = int(input("Enter your age: "))
            if age <= 0:
                print("Age must be a positive number. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number for age.")

    hobby = input("Enter your hobby: ").strip()

    # Displaying friendly message
    print("\n--- Introduction Summary ---")
    print(f"Hello {name}! 👋")
    print(f"You are {age} years old and you enjoy {hobby}.")
    print("That's awesome! Keep learning and growing 🚀")


if __name__ == "__main__":
    main()
