def print_column(name, style):
    print(f"\n{name}\n{'-' * len(name)}")
    for k, v in style.items():
        print(f"{k}: {v}")

def print_column_with_closest_property_in(table: dict[str, dict[str, any]], lookup_col: str, target_value: int):
    closest_smaller = None
    closest_larger = None
    min_smaller_diff = float('inf')
    min_larger_diff = float('inf')

    for name, style in table:
        size_diff = style[lookup_col] - target_value

        if size_diff < 0 and abs(size_diff) < min_smaller_diff:
            closest_smaller = (name, style)
            min_smaller_diff = abs(size_diff)
        elif size_diff > 0 and size_diff < min_larger_diff:
            closest_larger = (name, style)
            min_larger_diff = size_diff

    if closest_smaller:
        print_column(*closest_smaller)

    if closest_larger:
        print_column(*closest_larger)
