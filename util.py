def print_column(name, style):
    print(f"\n{name}\n{'-' * len(name)}")
    for k, v in style.items():
        print(f"{k}: {v}")
