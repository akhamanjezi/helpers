import argparse
import repo
import util

lookup_col = 'Size (points)'
table = repo.FONT

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Print font information based on size')
    parser.add_argument('size', type=int, nargs='?', help='font size')
    args = parser.parse_args()

    if args.size is None:
        size = input("Enter the size (point) or type 'exit' to quit: ")
    else:
        size = args.size

    while True:
        if size == 'exit':
            break
        try:
            size = int(size)
        except ValueError:
            size = input("\nInvalid input. Please enter a number or 'exit': ")
            continue
        if size in [value[lookup_col] for value in table.values()]:
            for key, value in table.items():
                if value[lookup_col] == int(size):
                    util.print_column(key, value)
                    break
        else:
            print(
                f"Size {size} not found. Please enter a valid size or 'exit'.")
        size = input("\nEnter the size (point) or type 'exit' to quit: ")
