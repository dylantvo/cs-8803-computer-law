def divide(x, y):
    result = x / y
    return result

def main():
    for i in range(5, -1, -1):
        print(f"Dividing 10 by {i}")
        result = divide(10, i)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
