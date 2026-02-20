'''
# Project Creation Date: 3:03:25 PM, 2/19/2026
'''

monthly = 1000
yearly_interest = 1.05
years = 30
wallet = 0

def calculate(wallet, monthly, yearly_interest, years):
    for i in range(years):
        wallet += (monthly * 12)
        wallet *= yearly_interest
        print(f"Year {i+1}: {round(wallet, 2)}")

print(f"Initial: {round(wallet, 2)}")
calculate(wallet, monthly, yearly_interest, years)