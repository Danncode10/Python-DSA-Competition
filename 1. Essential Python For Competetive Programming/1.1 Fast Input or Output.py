import sys

# # For integers
# n = int(sys.stdin.readline().strip())
#
# print(n)
#
# # For array
# arr = list(map(int, sys.stdin.readline().split()))
#
# print(arr)


# Example 3:
# n = int(sys.stdin.readline().strip())  # Number of lines
# for _ in range(n):
#     line = sys.stdin.readline().strip()
#     print(line)  # Process each line


# Example 4:
data = sys.stdin.read().splitlines()  # Reads entire input and splits by lines
for line in data:
    print(line)
