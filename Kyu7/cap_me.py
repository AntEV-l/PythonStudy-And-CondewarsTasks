arrays = ["jo", "nelson", "jurie"]
def cap_me(arr):
    for index, item in enumerate(arr):
        arr[index] = arr[index][:1].upper() + arr[index][1:].lower()
    return arr

print(cap_me(arrays))