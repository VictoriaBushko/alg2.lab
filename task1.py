def min_time_to_paint(K, T, L):
    def can_paint_in_time(max_time):
        painters = 1
        current_time = 0

        for length in L:
            paint_time = length * T
            if paint_time > max_time:
                return False

            if current_time + paint_time > max_time:
                painters += 1
                current_time = paint_time
                if painters > K:
                    return False
            else:
                current_time += paint_time

        return True

    left, right = max(L) * T, sum(L) * T
    while left < right:
        mid = (left + right) // 2
        if can_paint_in_time(mid):
            right = mid
        else:
            left = mid + 1
    return left

if __name__ == "__main__":
    print(min_time_to_paint(5, 10, [15, 10, 5, 10, 15, 20, 20, 15, 20]))
    print(min_time_to_paint(1, 5, [10, 20, 30]))
    print(min_time_to_paint(3, 2, [5, 10, 15, 20]))
    print(min_time_to_paint(3, 10, [8, 1, 8, 10, 15]))
