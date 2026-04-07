import sys
from pathlib import Path

# import time

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            k = int(file.readline())

            alphabet = {}

            for i in range(k):
                x, v = file.readline().split()
                alphabet[x] = int(v)
            
            A = file.readline().strip()
            B = file.readline().strip()

            # start_time = time.perf_counter()

            n, m = len(A), len(B)
            values = [[0] * (m + 1) for _ in range(n + 1)]

            max_val = 0
            end = 0

            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if A[i - 1] == B[j - 1]:
                        values[i][j] = values[i - 1][j - 1] + alphabet[A[i - 1]]

                        if values[i][j] > max_val:
                            max_val = values[i][j]
                            end = i
                    else:
                        values[i][j] = 0

            length = 0
            i = end - 1
            temp = max_val
            while i >= 0 and temp > 0:
                temp -= alphabet[A[i]]
                length += 1
                i -= 1

            substring = A[end - length : end]

            # end_time = time.perf_counter()
            # runtime = end_time - start_time
            # print(f"Runtime: {runtime:.8f} seconds")

            print(max_val)
            print(substring)



            out = Path(sys.argv[1]).with_suffix(".out")

            with open(out, 'w') as fileOut:
                fileOut.write(str(max_val) + '\n' + substring)

                fileOut.close()
        
        file.close()

    return 0

if __name__ == "__main__":
    main()