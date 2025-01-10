def sort(width=None, height=None, length=None, mass=None):
    """
    Function to sort packages based on their dimensions and mass.

    Args:
    width (int): Width of the package in cm.
    height (int): Height of the package in cm.
    length (int): Length of the package in cm.
    mass (int): Mass of the package in kg.

    Returns:
    str: The category of the package ('STANDARD', 'SPECIAL', 'REJECTED').
    """
    if width is None or height is None or length is None or mass is None:
        raise ValueError("All four arguments (width, height, length, mass) must be provided.")

    try:
        # Inputs must be integers
        width = int(width)
        height = int(height)
        length = int(length)
        mass = int(mass)
    except ValueError:
        raise ValueError("All inputs must be integers.")

    # Dimensions positive
    if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        raise ValueError("All dimensions and mass must be positive.")
    # volume of package
    volume = width * height * length

    # Bulky package
    is_bulky = volume > 1_000_000 or width >= 150 or height >= 150 or length >= 150

    # Heavy package
    is_heavy = mass >= 20

    # category
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

# Example input
if __name__ == "__main__":
    while True:
        user_input = input("Enter width, height, length, and mass separated by spaces (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Exiting the program.")
            break
        try:
            width, height, length, mass = user_input.split()
            result = sort(width, height, length, mass)
            print(result)
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter exactly four space-separated positive integers for width, height, length, and mass.")
