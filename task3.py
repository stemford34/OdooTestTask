def sumList(digit, suma):
    """Сounts the amount of elements, compares with the given amount, returns True or False

    digit: list[]
    suma: int

    """
    currentSum = 0
    for dig in digit:
        currentSum += dig
    
    if suma == currentSum:
        return True
    else:
        return False


lineInput = list(map(int, input().split()))

N = lineInput[0]
suma = lineInput[1]/2
digit = [0] * N
count = 0

current = N-1

while 1:
    if digit[current] < 9:
        digit[current] += 1
    else:
        while digit[current] == 9:
            current -= 1
            if current < 0:
                break
        if current < 0:
                break
        digit[current] += 1
        i = current + 1
        current = N-1
        while i < N:
            digit[i] = 0
            i += 1
    if sumList(digit, suma):
        count += 1

#found the number of combinations of half the ticket, squared, to get all the combinations
count **= 2
print(count)