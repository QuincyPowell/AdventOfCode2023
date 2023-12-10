import sys

input_data = []

with open(sys.argv[1], 'r', encoding="utf-8") as file:
    for line in file:
        data_line = []
        for item in line.strip().split():
            data_line.append(int(item))

        input_data.append(data_line)

def is_all_zero(integer_series):
    for integer in integer_series:
        if integer != 0:
            return False
    return True

def difference_integer_series(integer_series):
    difference_series = []
    cursor = 0
    end = len(integer_series) - 1
    while cursor < end:
        difference_series.append(integer_series[cursor + 1] - integer_series[cursor])
        cursor += 1
    return difference_series

def predict_next_int_for_series(integer_series):
    integer_series_stack = []
    next_series = integer_series.copy()

    while not is_all_zero(next_series):
        integer_series_stack.append(next_series)
        next_series = difference_integer_series(next_series)

    current_series = integer_series_stack.pop()
    next_integer = current_series[-1]
    while integer_series_stack:
        current_series = integer_series_stack.pop()
        next_integer = current_series[-1] + next_integer

    return next_integer

sum_of_predicted_values = 0
for series in input_data:
    print(series)
    predicted_value = predict_next_int_for_series(series)
    print(predicted_value)
    sum_of_predicted_values += predicted_value

print("Sum of predicted values: " + str(sum_of_predicted_values))
