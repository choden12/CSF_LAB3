import random


# =========================
# Generate Sorted Array
# =========================

def generate_array(n):
    array = [random.randint(1, 1000) for _ in range(n)]
    array.sort()
    return array


# =========================
# Binary Search
# =========================

def binary_search(array, key):
    low = 0
    high = len(array) - 1
    comparisons = 0

    while low <= high:

        mid = (low + high) // 2

        comparisons += 1

        if array[mid] == key:
            return mid, comparisons

        elif key < array[mid]:
            high = mid - 1

        else:
            low = mid + 1

    return -1, comparisons


# =========================
# Ternary Search
# =========================

def ternary_search(array, key):
    low = 0
    high = len(array) - 1
    comparisons = 0

    while low <= high:

        third = (high - low) // 3

        mid1 = low + third
        mid2 = high - third

        comparisons += 1

        if array[mid1] == key:
            return mid1, comparisons

        comparisons += 1

        if array[mid2] == key:
            return mid2, comparisons

        if key < array[mid1]:
            high = mid1 - 1

        elif key > array[mid2]:
            low = mid2 + 1

        else:
            low = mid1 + 1
            high = mid2 - 1

    return -1, comparisons


# =========================
# Best Case
# =========================

def binary_best_case(array):
    if len(array) == 0:
        return 0

    return 1


def ternary_best_case(array):
    if len(array) == 0:
        return 0

    return 1


# =========================
# Worst Case
# =========================

def binary_worst_case(array):
    if len(array) == 0:
        return 0

    key = 1001

    position, comparisons = binary_search(array, key)

    return comparisons


def ternary_worst_case(array):
    if len(array) == 0:
        return 0

    key = 1001

    position, comparisons = ternary_search(array, key)

    return comparisons


# =========================
# Main Menu
# =========================

array = []


while True:

    print()
    print("===== SEARCH MENU =====")
    print("1. Generate sorted random numbers")
    print("2. Display Array")
    print("3. Binary Search")
    print("4. Ternary Search")
    print("5. Best Case Step Count")
    print("6. Worst Case Step Count")
    print("7. Comparison Table")
    print("8. Exit")

    choice = input("Enter your choice: ")


    # =========================
    # Option 1
    # =========================

    if choice == "1":

        n = int(input("Enter the number of elements: "))

        array = generate_array(n)

        print("Array generated successfully!")


    # =========================
    # Option 2
    # =========================

    elif choice == "2":

        if len(array) == 0:

            print("Please generate the array first.")

        else:

            print("Sorted Array:")
            print(array)


    # =========================
    # Option 3
    # =========================

    elif choice == "3":

        if len(array) == 0:

            print("Please generate the array first.")

        else:

            key = int(input("Enter the key to search: "))

            position, comparisons = binary_search(array, key)

            if position != -1:

                print("Binary Search: Key found!")
                print("Index:", position)

            else:

                print("Binary Search: Key not found.")

            print("Number of comparisons:", comparisons)


    # =========================
    # Option 4
    # =========================

    elif choice == "4":

        if len(array) == 0:

            print("Please generate the array first.")

        else:

            key = int(input("Enter the key to search: "))

            position, comparisons = ternary_search(array, key)

            if position != -1:

                print("Ternary Search: Key found!")
                print("Index:", position)

            else:

                print("Ternary Search: Key not found.")

            print("Number of comparisons:", comparisons)


    # =========================
    # Option 5 - Best Case
    # =========================

    elif choice == "5":

        if len(array) == 0:

            print("Please generate the array first.")

        else:

            binary_count = binary_best_case(array)
            ternary_count = ternary_best_case(array)

            print()
            print("===== BEST CASE =====")
            print("Binary Search comparisons:", binary_count)
            print("Ternary Search comparisons:", ternary_count)


    # =========================
    # Option 6 - Worst Case
    # =========================

    elif choice == "6":

        if len(array) == 0:

            print("Please generate the array first.")

        else:

            binary_count = binary_worst_case(array)
            ternary_count = ternary_worst_case(array)

            print()
            print("===== WORST CASE =====")
            print("Test key:", 1001)
            print("Binary Search comparisons:", binary_count)
            print("Ternary Search comparisons:", ternary_count)


    # =========================
    # Option 7 - Comparison Table
    # =========================

    elif choice == "7":

        print()
        print("===== COMPARISON TABLE =====")
        print("n\tBinary\tTernary")

        test_sizes = [10, 20, 50, 100, 200, 500, 1000]

        for n in test_sizes:

            # Generate a new sorted array
            array = generate_array(n)

            # Key 1001 is guaranteed to be absent
            key = 1001

            # Binary Search
            binary_position, binary_count = binary_search(
                array, key
            )

            # Ternary Search
            ternary_position, ternary_count = ternary_search(
                array, key
            )

            print(n, "\t", binary_count, "\t", ternary_count)


    # =========================
    # Option 8 - Exit
    # =========================

    elif choice == "8":

        print("Program ended.")
        break


    else:

        print("Invalid choice. Please try again.")