def countA(w):
    total = 0

    for i in range(0, len(w)):
        total = total * i
        if w[0] == "a":
            return total

countA("alphabet")

