# the mortgage calculations is:
# P = L[c(1 + c)n]/[(1 + c)n - 1]
# where
# L = Loan amount
# P = Monthly payment
# n = Month when the balance is paid in full (30 years * 12 months)
# c = monthly interest rate (5% yearly rate means c = 0.05 / 12)
L = 300000
length = 30.0
rate = 5.0
c = (rate / 100.0) / 12.0
n = length * 12.0
c1 = (1 + c) ** n
print("A mortgage of", L , "at", rate, "percent for", length, "years")
print("Monthly Payment is", L * ((c * c1) / (c1 - 1)))