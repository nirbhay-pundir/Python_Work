startPoint = int(input("Enter starting point of interval: "))
endPoint = int(input("Enter ending point of interval: "))

for num in range(startPoint,endPoint):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                break
        else:
            print(num)
