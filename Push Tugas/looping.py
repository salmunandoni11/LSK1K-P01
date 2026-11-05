"""looping.py

Simple script that demonstrates a basic for-loop in Python.
It prints the numbers from 1 to 10 (inclusive) to the console.

Run the script directly:
    python looping.py

The script is deliberately minimal to serve as a clear example of
iteration and output handling.
"""

def main() -> None:
    """Print numbers from 1 to 10, each on its own line."""
    for i in range(1, 11):
        print(i)


if __name__ == "__main__":
    main()
