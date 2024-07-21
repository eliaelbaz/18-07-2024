import random

bool_list = [random.choice([True, False]) for _ in range(3)];
print(all(bool_list), any(bool_list), not any(bool_list), any(not x for x in bool_list), sep='\n');
num_list = [random.randint(-2, 2) for _ in range(5)];
print(all(num_list), any(num_list), not any(num_list), any(x == 0 for x in num_list), sep='\n');
