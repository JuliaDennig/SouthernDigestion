def isSizeDifferenceValid(key):
    if len(key) == 1:
        if 1000 <= key[0] <= 8000:
            return True
        else:
            return False

    for i in range(len(key)-1):
        if key[i] >= 8000 or key[i] <= 1000:
            return False
        if (key[i + 1] > 6000 or key[i] > 6000) and not key[i] - key[i + 1] >= 2000:
            return False
        if (key[i + 1] > 3000 or key[i] > 3000) and not key[i] - key[i + 1] >= 1000:
            return False
        if (key[i + 1] < 3000 or key[i] < 3000) and not key[i] - key[i + 1] >= 500:
            return False

    return True
