from module5_mod import NumberProcessor

def main():
    processor = NumberProcessor()
    processor.read_N()
    processor.read_numbers()

    X = int(input("Enter the number to search (X): "))
    result = processor.find_index_of_x(X)

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
