def sqrt(x):
    if x == 0:
        return 0.0
    guess = x
    for _ in range(20):
        guess = (guess + x / guess) / 2
    return guess

def max_wire_length(w, heights):
    n = len(heights)
    dp = [0.0] * heights[0]

    for i in range(1, n):
        new_dp = [0.0] * heights[i]
        for h2 in range(1, heights[i] + 1):
            max_len = 0.0
            for h1 in range(1, heights[i - 1] + 1):
                dist = sqrt(w * w + (h2 - h1) * (h2 - h1))
                if dp[h1 - 1] + dist > max_len:
                    max_len = dp[h1 - 1] + dist
            new_dp[h2 - 1] = max_len
        dp = new_dp

    return round(max(dp), 2)

def main():
    with open('input.txt', 'r') as f:
        w = int(f.readline())
        heights = list(map(int, f.readline().split()))

    result = max_wire_length(w, heights)

    with open('output.txt', 'w') as f:
        f.write("{:.2f}\n".format(result))

if __name__ == "__main__":
    main()
