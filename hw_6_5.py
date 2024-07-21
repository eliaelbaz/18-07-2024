
numbers = [10, 20, 30, 40]
while True:
    try:
        index = int(input("Enter an index (enter -999 to stop): "));
        if index == -999:
            break
        print("Value at index", index, ":", numbers[index]);
    except ValueError:
        print("Error: You must enter an integer.");
    except IndexError:
        print("Error: Index out of range. Please enter a valid index (0-3).");
