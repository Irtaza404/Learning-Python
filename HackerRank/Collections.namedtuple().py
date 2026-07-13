# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
cols = input().split()
mi=cols.index("MARKS")
print(f"{sum(int(input().split()[mi]) for _ in range(n))/n:.2f}")
