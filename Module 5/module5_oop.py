class NumberProcessor:
    def __init__(self):
        self.N = 0
        self.numbers = []

    def read_N(self):
        self.N = int(input("Enter the number of elements (N): "))

    def read_numbers(self):
        for i in range(self.N):
            num = int(input(f"Enter number {i + 1}: "))
            self.numbers.append(num)

    def find_index_of_x(self, X):
        if X in self.numbers:
            return self.numbers.index(X) + 1
        else:
            return -1

def main():
    processor = NumberProcessor()
    processor.read_N()
    processor.read_numbers()

    X = int(input("Enter the number to search (X): "))
    result = processor.find_index_of_x(X)

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
