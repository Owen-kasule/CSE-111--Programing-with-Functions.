def main():
    # Open the file and read the contents into a list
    with open("provinces.txt", "rt") as file:
        provinces = [line.strip() for line in file]

    # Print the entire list
    print("Original List:")
    print(provinces)

    # Remove the first element
    provinces.pop(0)

    # Remove the last element
    provinces.pop(-1)

    # Replace all occurrences of "AB" with "Alberta"
    provinces = ["Alberta" if province == "AB" else province for province in provinces]

    # Count the occurrences of "Alberta"
    alberta_count = provinces.count("Alberta")

    # Print the modified list
    print("\nModified List:")
    print(provinces)

    # Print the count of "Alberta"
    print(f"\n'Alberta' occurs {alberta_count} times in the modified list.")

if __name__ == "__main__":
    main()
