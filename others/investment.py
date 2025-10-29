def investment():
    initialInvest = float(input("Enter initial investment: "))
    annualInterest = float(input("Enter the annual interest rate: "))
    
    monthlyInterest = annualInterest / 1200
    balance = initialInvest
    months = 0
    
    while balance < 2 * initialInvest:
        balance += balance * monthlyInterest
        months += 1
    
    years = months // 12
    remainingMonths = months % 12
    balance = round(balance, 2)
    print()
    print(f"After {years} years and {remainingMonths} months, balance is $ {balance}")
def main():
    investment()
main()
    
    