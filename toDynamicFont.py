import argparse
import repo

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
        if size in [value['Size (points)'] for value in table.values()]:
            for key, value in table.items():
                if value['Size (points)'] == int(size):
                    print(f"\n{key}\n{'-' * len(key)}")
                    for k, v in value.items():
                        print(f"{k}: {v}")
        else:
            print(
                f"Size {size} not found. Please enter a valid size or 'exit'.")
        size = input("\nEnter the size (point) or type 'exit' to quit: ")
