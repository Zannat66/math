x = []
y = []
sumX = 0
sumX2 = 0
sumY = 0
sumXY = 0

n = int(input("Enter n:  "))

print("Enter value: ")
print("\n")

for i in range(n):
    print("x[" + str(i) + "]=")
    x.append(float(input()))
    print("y[" + str(i) + "]=")
    y.append(float(input()))

for i in range(n):
    sumX = sumX + x[i]
    sumX2 = sumX2 + x[i] * x[i]
    sumY = sumY + y[i]
    sumXY = sumXY + x[i] * y[i]

b = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX * sumX)
a = (sumY - b * sumX) / n

result_y = a + b * 86
print("Result: " + str(result_y))