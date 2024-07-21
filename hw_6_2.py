# a
temperatures = [];
# b
while True:
    temp = float(input("Enter a temperature (enter -999 to stop): "));
    if temp == -999:
        break
    if -50 <= temp <= 50:
        temperatures.append(temp);
# c
temperatures.extend([18.5, 39.1, -20.0]);
# d
print("Highest temperature:", max(temperatures));
# e
print("Lowest temperature:", min(temperatures));
# f
print("Average temperature (using sum and len):", sum(temperatures) / len(temperatures));
# g
del temperatures[0];
# h
temperatures.remove(18.5);
# i
last_temp = temperatures.pop();
print("Last temperature removed:", last_temp);
# j
sorted_temperatures = temperatures.copy();
sorted_temperatures.sort();
print("Sorted temperatures:", sorted_temperatures);
# k
reversed_sorted_temperatures = temperatures.copy();
reversed_sorted_temperatures.sort(reverse=True);
print("Reversed sorted temperatures:", reversed_sorted_temperatures);
# l
reversed_temperatures = list(reversed(temperatures));
print("Reversed list of temperatures:", reversed_temperatures);
