import argparse
import repo
import util

lookup_col = 'Numeric value'
table = repo.WEIGHT

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Print Font.Weight based on numeric value')
    parser.add_argument('size', type=int, nargs='?', help='font weight')
    args = parser.parse_args()

    if args.size is None:
        size = input("Enter the numeric weight or type 'exit' to quit: ")
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
            util.print_column_with_closest_property_in(table.items(), lookup_col, size)
        size = input("\nEnter the numeric weight or type 'exit' to quit: ")
