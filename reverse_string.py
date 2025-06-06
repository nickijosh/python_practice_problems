def reverse_string(text):
    """
    This function takes a string and returns it reversed.
    """
    return text[::-1] # Slice the string in reverse

# Test code (runs only when you execute the script directly)
if __name__ == "__main__":
    input_text = input("Enter a string to reverse: ")
    reversed_text = reverse_string(input_text)
    print(f"Reversed string: {reversed_text}")