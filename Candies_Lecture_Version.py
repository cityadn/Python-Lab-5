candies = [4,2,1,1,2]
extraCandies = 1
maximum = max(candies)
print(maximum)

for i in range(0, len(candies)):
    value = candies[i]+extraCandies
    print(value)
    if value >= maximum:
        print(True)
    elif value < maximum:
        print(False)
