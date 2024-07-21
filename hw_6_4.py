import random
# a
numbers_95_105 = [x for x in range(95, 106)];
# b
even_numbers_10_20 = [x for x in range(10, 21) if x % 2 == 0];
# c
random_bools = [random.choice([True, False]) for _ in range(5)];
# d
random_numbers = [random.randint(1, 100) for _ in range(10)];
# e
numbers_above_50 = [x for x in random_numbers if x > 50];
# f
random_numbers_above_50 = [x for x in [random.randint(1, 100) for _ in range(10)] if x > 50];
# g
input_string = input("Enter a string: ");
filtered_chars = [char for char in input_string if char != 't' and char != ' '];

print(numbers_95_105, even_numbers_10_20, random_bools, random_numbers, numbers_above_50, random_numbers_above_50, filtered_chars, sep='\n');
