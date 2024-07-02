# Helpers

## toDynamicFont.py

A python script that returns the environment-dependent [Font](https://developer.apple.com/documentation/swiftui/font) for a given font pt size.

### Usage

```zsh
$   python toDynamicFont.py 13

Footnote
--------
Weight: Regular
Size (points): 13
Leading (points): 18

Enter the size (point) or type 'exit' to quit:
```

## toFontWeight.py

### Usage

A python script that returns the [Font.Weight](https://developer.apple.com/documentation/swiftui/font/weight) for a given numeric value.

```zsh
$   python toFontWeight.py 400

Regular
-------
Font.Weight: regular
Numeric value: 400

Enter the numeric weight or type 'exit' to quit:
```
