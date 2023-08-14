import numpy as np

class NumberProcessor:
    def __init__(self):
        self.N = 0
        self.points = []

    def read_N(self):
        self.N = int(input("Enter the number of points (N): "))

    def read_points(self):
        for i in range(self.N):
            x = float(input(f"Enter x-coordinate for point {i + 1}: "))
            y = float(input(f"Enter y-coordinate for point {i + 1}: "))
            self.points.append((x, y))

    def k_nn_regression(self, k, X):
        if k <= self.N:
            x_values = np.array([point[0] for point in self.points])
            y_values = np.array([point[1] for point in self.points])
            distances = np.abs(x_values - X)
            sorted_indices = np.argsort(distances)
            k_nearest_indices = sorted_indices[:k]
            k_nearest_y_values = y_values[k_nearest_indices]
            return np.mean(k_nearest_y_values)
        else:
            return "Error: k should be less than or equal to N"

def main():
    processor = NumberProcessor()
    processor.read_N()
    processor.read_points()

    k = int(input("Enter the value of k: "))
    X = float(input("Enter the value of X: "))

    result = processor.k_nn_regression(k, X)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
