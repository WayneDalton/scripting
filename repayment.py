import argparse

# Set up the argument parser
parser = argparse.ArgumentParser(
    description="Calculate monthly loan repayments based on amount, interest rate, and term."
)

# Define the expected CLI arguments
parser.add_argument(
    "--amount", 
    type=float, 
    required=True, 
    help="The total loan amount (e.g., 150000)"
)
parser.add_argument(
    "--rate", 
    type=float,  # Changed from int to float to accept decimal interest rates
    required=True, 
    help="The annual interest rate as a percentage (e.g., 7.5 for 7.5%%)"
)
parser.add_argument(
    "--term", 
    type=int, 
    required=True, 
    help="The number of months to repay the loan"
)

# Parse the arguments
args = parser.parse_args()

# Perform the calculation using the parsed arguments
PV = args.amount
i = args.rate / 100 / 12  # Works perfectly with float values now
n = args.term

# Formula math
t = (1 + i) ** n
PMT = (PV * i * t) / (t - 1)

# Give the answer to the user
print(f"Loan repayment: R{PMT:.2f} per month.")