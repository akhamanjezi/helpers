import argparse
import repo

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
        if size in [value['Numeric value'] for value in table.values()]:
            for key, value in table.items():
                if value['Numeric value'] == int(size):
                    print(f"\n{key}\n{'-' * len(key)}")
                    for k, v in value.items():
                        print(f"{k}: {v}")
        else:
            print(
                f"Size {size} not found. Please enter a valid weight value or 'exit'.")
        size = input("\nEnter the numeric weight or type 'exit' to quit: ")
