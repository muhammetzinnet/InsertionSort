


def insertion_Sort(dizi):
    for i in range(1, len(dizi)):
        key = dizi[i]
        j = i-1

        while j>= 0 and key<dizi[j]:
            dizi[j+1] = dizi[j]
            j = j - 1

        dizi[j+1] = key

dizi = [7,3,5,8,2,9,4,15,6]
insertion_Sort(dizi)
print(dizi)