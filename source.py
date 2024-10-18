def insertion_sort(v: list):
    for i in range(1, len(v)):
        x = v[i]
        j = i-1
        while j >= 0 and v[j] > x:
            v[j+1] = v[j]
            j -= 1
        v[j+1] = x
    return v

def bubble_sort(v: list):
    n = len(v)
    for i in range(n):
        for j in range(n-i-1):
            if v[j+1] < v[j]:
                v[j], v[j+1] = v[j+1], v[j]
    return v

def selection_sort(v: list):
    n = len(v)
    for i in range(n):
        minj = i
        minx = v[i]
        for j in range(i+1, n):
            if v[j] < minx:
                minj = j
                minx = v[j]
        v[minj] = v[i]
        v[i] = minx

    return v
