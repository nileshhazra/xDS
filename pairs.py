def pairs(elements):
    result = []

    for i in range(0, len(elements)):
        for j in range(i + 1, len(elements)):
            pair = [elements[i], elements[j]]
            result.append(pair)

    return result
