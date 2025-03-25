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

    painters = []
    current_time = 0
    current_painter = []

    for length in L:
        paint_time = length * T
        if current_time + paint_time > left:
            painters.append(current_painter)
            current_painter = [length]
            current_time = paint_time
        else:
            current_painter.append(length)
            current_time += paint_time

    painters.append(current_painter)

    result = [f"Мінімальний час: {left} хвилин"]
    for i, p in enumerate(painters, start=1):
        result.append(f"Маляр {i} малює щити: {', '.join(map(str, p))}")

    print("\n".join(result))
    return left


if __name__ == "__main__":
    min_time_to_paint(5, 10, [15, 10, 5, 10, 15, 20, 20, 15, 20])
    print("-")
    min_time_to_paint(1, 5, [10, 20, 30])
    print("-")
    min_time_to_paint(3, 2, [5, 10, 15, 20])
    print("-")
    min_time_to_paint(3, 10, [8, 1, 8, 10, 15])
