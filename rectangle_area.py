# rectangle_area.py

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
    - length (float): The length of the rectangle.
    - width (float): The width of the rectangle.

    Returns:
    - float: The area of the rectangle.
    """
    area = length * width
    return area


# Let's test the function with user input
if __name__ == "__main__":
    try:
        # Get user input
        l = float(input("Enter the length of the rectangle: "))
        w = float(input("Enter the width of the rectangle: "))
        
        # Call the function
        result = calculate_area(l, w)
        print(f"The area of the rectangle is: {result}")
    
    except ValueError:
        print("Please enter valid numeric values.")
