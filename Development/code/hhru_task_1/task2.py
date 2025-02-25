def longest_monotone_segment(arr):
    n = len(arr)
    if n == 1:
        return (0, 0)

    max_length = 1
    start = 0
    best_start, best_end = 0, 0

    # Check for increasing and decreasing sequences
    for i in range(1, n):
        if arr[i] > arr[i - 1]:  # Increasing
            if i - start + 1 > max_length:
                max_length = i - start + 1
                best_start, best_end = start, i
        elif arr[i] < arr[i - 1]:  # Decreasing
            if i - start + 1 > max_length:
                max_length = i - start + 1
                best_start, best_end = start, i
        else:
            start = i  # Reset segment on equal elements

    return best_start, best_end  # 0-based indexing as per your example

# Example usage:
input_str = input("Enter numbers separated by ', ': ")
input_list = [x.strip() for x in input_str.split(",") if x.strip().lstrip('-').isdigit()]
arr = list(map(int, input_list))

print(longest_monotone_segment(arr))
