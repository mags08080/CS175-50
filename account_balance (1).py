# -*- coding: utf-8 -*-
"""account_balance

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ScwGXJop3BbJL5APMoysxlcQWqheCmw4
"""

# CS175
# Maggie Volker

#inital balance
initalBalance = 1000.00

#interest per year
interestRate = 0.05

#first year balance
balanceAfterFirstYear = initalBalance * (1 + interestRate)
print(f"The balance after the first year is ${balanceAfterFirstYear}")

#second year balance
balanceAfterSecondYear = balanceAfterFirstYear * (1 + interestRate)
print(f"The balance after the second year is ${balanceAfterSecondYear}")

#third year balance
balanceAfterThirdYear = balanceAfterSecondYear * (1 + interestRate)
print(f"The balance after the third year is ${balanceAfterThirdYear}")