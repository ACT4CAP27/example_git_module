import os
import sys

try:
    import pyfiglet
except ImportError:
    print("The 'pyfiglet' library is needed for the fancy ASCII art.")
    print("Please install it by running: pip install pyfiglet")
    sys.exit(1)

def main():
    # Retrieve the environment variables
    param1 = os.environ.get('PARAMETER1')
    param2 = os.environ.get('PARAMETER2')

    # Check if both parameters are provided
    if param1 is None or param2 is None:
        print("Error: Please set both PARAMETER1 and PARAMETER2 environment variables.")
        print("\nExample usage:")
        print("  export PARAMETER1='First'")
        print("  export PARAMETER2='Second'")
        print("  python fancy_print.py")
        sys.exit(1)

    # Generate and print the ASCII art
    print("~" * 60)
    print(" PARAMETER 1:")
    print("~" * 60)
    print(pyfiglet.figlet_format(param1, font="slant"))

    print("~" * 60)
    print(" PARAMETER 2:")
    print("~" * 60)
    print(pyfiglet.figlet_format(param2, font="slant"))

if __name__ == "__main__":
    main()
