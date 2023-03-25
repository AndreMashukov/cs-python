def rotated_rect_sum(matrix, a, b):
    rows, cols = len(matrix), len(matrix[0])
    print("+++++")
    maxArea = float("-inf")
    # go through possible rectangles along both diagonals
    for w, h in [(a, b), (b, a)]:
        print(w, h)
        # go through possible "anchors", which is the left top coordinate of the rectangle candidate
        for i in range(w - 1, rows - h + 1):
            for j in range(0, cols - (h + w - 1) + 1):
                # print(f'i={i}; j={j}, {w-1}')
                area = 0
                # sum up the long diagonals
                for p in range(w): # go to next long diagonal
                    for q in range(h): # go down current diagonal
                        print(f'p={p}; q={q}')
                        area += matrix[i - p + q][j + p + q]
                
                # sum up the short diagonals
                k, l = i, j + 1 # note that short diagonals have one less element than long diagonals
                for p in range(w - 1):
                    for q in range(h - 1):
                        area += matrix[k- p + q][l + p + q]
                if (area > maxArea): maxArea = area
    return maxArea