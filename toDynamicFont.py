import argparse

if __name__ == "__main__":
    table = {
        'Large Title': {'Weight': 'Regular', 'Size (points)': 34, 'Leading (points)': 41},
        'Title 1': {'Weight': 'Regular', 'Size (points)': 28, 'Leading (points)': 34},
        'Title 2': {'Weight': 'Regular', 'Size (points)': 22, 'Leading (points)': 28},
        'Title 3': {'Weight': 'Regular', 'Size (points)': 20, 'Leading (points)': 25},
        'Headline': {'Weight': 'Semibold', 'Size (points)': 17, 'Leading (points)': 22},
        'Body': {'Weight': 'Regular', 'Size (points)': 17, 'Leading (points)': 22},
        'Callout': {'Weight': 'Regular', 'Size (points)': 16, 'Leading (points)': 21},
        'Subhead': {'Weight': 'Regular', 'Size (points)': 15, 'Leading (points)': 20},
        'Footnote': {'Weight': 'Regular', 'Size (points)': 13, 'Leading (points)': 18},
        'Caption 1': {'Weight': 'Regular', 'Size (points)': 12, 'Leading (points)': 16},
        'Caption 2': {'Weight': 'Regular', 'Size (points)': 11, 'Leading (points)': 13}
    }

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
