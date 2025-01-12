def calculate_room():
    print("Room Calculator")
    print("1. Rectangle (2D - Area and Perimeter)")
    print("2. Square (2D - Area and Perimeter)")
    print("3. Cuboid (3D - Volume and Surface Area)")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        print("\n--- Rectangle ---")
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
        perimeter = 2 * (length + width)
        print(f"Area: {area} square units")
        print(f"Perimeter: {perimeter} units")

    elif choice == '2':
        print("\n--- Square ---")
        side = float(input("Enter the side of the square: "))
        area = side ** 2
        perimeter = 4 * side
        print(f"Area: {area} square units")
        print(f"Perimeter: {perimeter} units")

    elif choice == '3':
        print("\n--- Cuboid ---")
        length = float(input("Enter the length of the cuboid: "))
        width = float(input("Enter the width of the cuboid: "))
        height = float(input("Enter the height of the cuboid: "))
        volume = length * width * height
        surface_area = 2 * (length * width + width * height + length * height)
        print(f"Volume: {volume} cubic units")
        print(f"Surface Area: {surface_area} square units")

    else:
        print("Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    calculate_room()
