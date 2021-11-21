def is_size_difference_valid(key):
    # checks the dictionaries created in OneEnzyme.py and TwoEnzyme.py
    # if the resulting bands are suitable for Southern Blot

    # bands must be bigger than 1000 bp and smaller than 8000 bp
    # the difference between bands must be at least 500 bp
    # in case one band is bigger than 3000 bp at least 1000 bp
    # in case one band is bigger than 6000 bp at least 2000 bp

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
