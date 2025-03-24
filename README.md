# Mortgage Calculator

This Python script calculates mortgage payments, remaining loan balances, and provides a full amortization schedule. It is useful for home buyers, financial analysts, and anyone interested in understanding loan repayment structures.

## Features
- **Fixed Monthly Payment Calculation**
- **Remaining Balance Calculation** (after a specified number of months)
- **Amortization Schedule** (breakdown of principal, interest, and remaining balance for each month)

## How It Works
The script consists of three core functions:

### 1. Mortgage Payment Calculation
Calculates the monthly payment using the formula:
```python
A = (L * monthly_rate) / (1 - (1 + monthly_rate) ** -n)
```
Where:
- `L` = Loan amount
- `monthly_rate` = Monthly interest rate (annual rate / 12)
- `n` = Number of months (loan term)

### 2. Remaining Balance Calculation
Determines the balance after `j` months:
```python
R_j = L * (alpha**n - alpha**j) / (alpha**n - 1)
```
Where:
- `alpha = 1 + monthly_rate`
- `j` = Number of months passed

### 3. Amortization Schedule
Generates a breakdown of payments, showing:
- Payment number
- Monthly payment amount
- Interest portion
- Principal portion
- Remaining balance

## Example Usage
```python
L = 100000  # Loan amount
monthly_rate = 0.006  # Monthly interest rate (0.6%)
n = 180  # Number of months (15 years)
j = 84  # Month for remaining balance calculation

A = mortgage_payment(L, monthly_rate, n)
R_j = remaining_balance(L, monthly_rate, n, j)
breakdown = payment_breakdown(L, monthly_rate, n)
```

### Sample Output
```
Monthly Payment: $843.86
Remaining Balance after 84 months: $58,326.57
Interest Paid in Month 84: $350.00
Principal Paid in Month 84: $493.86

Month | Payment | Interest | Principal | Remaining Balance
------------------------------------------------------------
  1   | $843.86 |  $600.00 |  $243.86  | $99,756.14
  2   | $843.86 |  $598.54 |  $245.32  | $99,510.82
...
180   | $843.86 |  $4.21   |  $839.65  | $0.00
```

## Requirements
- Python 3.x

## Installation
Clone the repository:
```sh
git clone https://github.com/KennethTebogo/mortgage-calculator.git
cd mortgage-calculator
```

## Running the Script
Run the Python script:
```sh
python mortgage_calculator.py
```

## Future Enhancements
- Add user input for loan parameters
- Improve output formatting with `tabulate`
- Export amortization schedule to CSV/Excel

## License
This project is licensed under the MIT License.

## Author
[Kenneth Tebogo Khondowe](https://github.com/KennethTebogo)

