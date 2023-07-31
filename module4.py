def main():
    N = int(input("Enter the number of elements (N): "))
    numbers = []

    for i in range(N):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    X = int(input("Enter the number to search (X): "))

    if X in numbers:
        index = numbers.index(X) + 1
        print(f"The number {X} was found at index {index}.")
    else:
        print("-1")

if __name__ == "__main__":
    main()
