# 34. TO‘LOV TIZIMI
bal = 0
hist = []

while True:
    c = input()
    if c == "in":
        x = int(input()); bal += x; hist.append(x)
    if c == "out":
        x = int(input()); bal -= x; hist.append(-x)
    if c == "bal":
        print(bal, hist)
    if c == "exit":
        break
