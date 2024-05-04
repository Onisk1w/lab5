def find_missing_number(nums, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
sequence = [1, 2, 4, 5]  # ожидаемый диапазон от 1 до 5
N = 5
print(find_missing_number(sequence, N))  # Выводит 3, так как 3 удалено из последовательности
