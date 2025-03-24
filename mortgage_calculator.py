def mortgage_payment(L, monthly_rate, n):
    A = (L * monthly_rate) / (1 - (1 + monthly_rate) ** -n)  # Monthly payment formula
    return A

def remaining_balance(L, monthly_rate, n, j):
    alpha = 1 + monthly_rate
    R_j = L * (alpha**n - alpha**j) / (alpha**n - 1)
    return R_j

def payment_breakdown(L, monthly_rate, n):
    A = mortgage_payment(L, monthly_rate, n)
    balance = L
    breakdown = []
    
    for j in range(1, n + 1):
        interest = monthly_rate * balance
        principal = A - interest
        balance -= principal
        breakdown.append((j, round(A, 2), round(interest, 2), round(principal, 2), round(balance, 2)))
    
    return breakdown

# Example usage
L = 100000  # Loan amount
monthly_rate = 0.006  # Monthly interest rate (0.6%)
n = 180  # Number of months (15 years)
j = 84  # Month for remaining balance calculation

A = mortgage_payment(L, monthly_rate, n)
R_j = remaining_balance(L, monthly_rate, n, j)

# Retrieve interest and principal after month j
breakdown = payment_breakdown(L, monthly_rate, n)
interest_j, principal_j = breakdown[j - 1][2], breakdown[j - 1][3]

print(f"Monthly Payment: ${A:.2f}")
print(f"Remaining Balance after {j} months: ${R_j:.2f}")
print(f"Interest Paid in Month {j}: ${interest_j:.2f}")
print(f"Principal Paid in Month {j}: ${principal_j:.2f}\n")

print("Month | Payment | Interest | Principal | Remaining Balance")
print("-" * 60)
for month, pay, interest, principal, balance in breakdown:  # Display all 180 months
    print(f"{month:5d} | ${pay:7.2f} | ${interest:8.2f} | ${principal:9.2f} | ${balance:16.2f}")
