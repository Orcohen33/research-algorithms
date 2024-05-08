"""
Author: Or Cohen
Date: 21/04/2024
"""
if __name__ == '__main__':
    try:
        a, b = map(int, input("Enter two numbers with a space between each number:\n(Example: '3 5')\n").split())
        print(f"a * b = {a * b}")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")