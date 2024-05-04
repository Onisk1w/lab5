def roman_to_int(s):
    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    prev_value = 0
    for char in s:
        value = roman_map[char]
        if value > prev_value:
            result += value - 2 * prev_value
        else:
            result += value
        prev_value = value
    return result

print("введите римское число ")
roman_number = input()
print(roman_to_int(roman_number))
