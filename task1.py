def is_monotonic(arr):
    increasing = decreasing = True
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        elif arr[i] < arr[i - 1]:
            increasing = False
    return increasing or decreasing

if __name__ == "__main__":
    arr = list(map(int, input("Введіть масив чисел через пробіл: ").split()))
    print(is_monotonic(arr))
