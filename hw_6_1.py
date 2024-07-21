# a
numbers = [];
for i in range(80, 100):
    numbers.append(i);
# b
print("First element:", numbers[0]);
# c
print("Last element:", numbers[-1]);
# d
print("Number of elements:", len(numbers));
# e
print("Elements from index 3 to 12:", numbers[3:13]);
# f
print("Elements from index 3 to the end:", numbers[3:]);
# g
print("Elements from the start to index 9:", numbers[:10]);
# h
middle_index = len(numbers) // 2
numbers.insert(middle_index, 999);
print("List after inserting 999 in the middle:", numbers);
# i
print("List in reverse order:", numbers[::-1]);
# j
print("Elements at odd indices:", numbers[1::2]);
