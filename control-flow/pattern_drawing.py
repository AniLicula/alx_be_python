# pattern_drawing.py

def main():
    while True:
        try:
            size = int(input("Enter the size of the pattern: "))
            if size > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    row = 0
    while row < size:
        for col in range(size):
            print("*", end="")
        print()  # Newline after each row
        row += 1

if __name__ == "__main__":
    main()

