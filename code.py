temp = []

for i in range(7):
    t = float(input("Enter temperature: "))
    temp.append(t)

print("Temperatures:")
for t in temp:
    print(t)

print("Highest:", max(temp))
print("Lowest:", min(temp))

average = sum(temp) / 7
print("Average:", average)

print("Temperatures above average:")
for t in temp:
    if t > average:
        print(t)

temp.sort()
print("Ascending order:", temp)