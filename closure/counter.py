def counter(start=0):
    value = start - 1

    def increase():
        nonlocal value
        value += 1
        return value
    
    return increase

cnt = counter()
