principal = 1000  # initial amount
rate = 0.05  # interest rate
numyrs = 5
year = 1

while year <= numyrs:
    principal = principal * (1 + rate)
    print(f"{year:>3d} {principal:0.2f}")
    year += 1



