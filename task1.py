def main():
    with open('career.in', 'r') as f_in:
        lines = f_in.read().strip().splitlines()

    L = int(lines[0].strip())

    triangle = []
    for i in range(1, L+1):
        parts = lines[i].split()
        row = [int(x) for x in parts]
        triangle.append(row)

    for i in range(L-2, -1, -1):
        for j in range(i+1):
            left = triangle[i+1][j]
            right = triangle[i+1][j+1]
            triangle[i][j] += left if left > right else right

    with open('career.out', 'w') as f_out:
        f_out.write(str(triangle[0][0]))
        f_out.write('\n')

if __name__ == "__main__":
    main()
