from time import sleep
import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
    print("")

def dots(x):
    for z in range(x):
        print('.', end=' ', flush=True)
        time.sleep(0.5)
    print("")

def camelCase(x):
    newWord = ''
    for word in x.split():
        newWord += word.strip().capitalize()
        newWord = newWord.replace(newWord[0], newWord[0].lower(), 1)
    return newWord
def unCamelCase(x):
    newWord = ''
    for letter in range(len(x)):
        if x[letter].isupper() == True:
            newWord += (f" {x[letter]}")
        else:
            newWord += (x[letter])
    return newWord.capitalize()

class MainClass():
    def __init__(self):
        self.incomeSourceDict = {}
        self.expenseDict = {}
        self.monthlyCashFlow = 0
        self.roi = 0

    def incomeSources(self):
        delay_print("What is your rental income? ")
        self.incomeSourceDict['rentalIncome'] = int(input(""))

        delay_print("What is your laundry income? ")
        self.incomeSourceDict['laundryIncome'] = int(input(""))

        delay_print("What is your storage income? ")
        self.incomeSourceDict['storageIncome'] = int(input(""))

        delay_print("What is your misc income? ")
        self.incomeSourceDict['miscIncome'] = int(input(""))

        while True:# giving the user an option to add to the dictionary of income
            delay_print("Do you want to add any more income sources? ")
            response = input("Please type Y or N: ")
            if response.lower() == 'y' or response.lower() == 'yes':
                delay_print("What is the new income source? ")
                newItem = camelCase(input(""))

                delay_print(f"How much do you get from {unCamelCase(newItem)} monthly? Please enter a number: ")
                newMoney = int(input(""))
                camelCase(newItem)
                self.incomeSourceDict[newItem] = newMoney
            elif response.lower() == 'n' or response.lower() == 'no':
                delay_print("Okay, we won't add any others.")
                break
            else:
                delay_print("Invalid input. Please try again!")
        self.incomeSourceDict['totalMonthlyIncome'] = sum(self.incomeSourceDict.values())
            
        delay_print("Here's how we're looking with your current income sources:\n")
        for key, value in self.incomeSourceDict.items():
            print(unCamelCase(key), value)
            sleep(0.5)
        sleep(2)

    def expenseSources(self):
        delay_print("How much do you pay monthly in taxes? ")
        self.expenseDict['tax'] = int(input(""))

        delay_print("How much do you pay monthly in insurance? ")
        self.expenseDict['insurance'] = int(input(""))

        delay_print("How much do you pay monthly in utilities? ")
        self.expenseDict['utilities'] = int(input(""))

        delay_print("How much do you pay monthly in HOI Fees? ")
        self.expenseDict['hoiFees'] = int(input(""))

        while True:# giving the user an option to add to the dictionary of expenses
            delay_print("Do you want to add any more expenses? ")
            delay_print("Please type Y or N: ")
            response = input("")
            if response.lower() == 'y' or response.lower() == 'yes':
                delay_print("What is the expense? ")
                newItem = camelCase(input(""))

                delay_print(f"How much does {unCamelCase(newItem)} cost monthly? Please enter a number: ")
                newMoney = int(input(""))
                camelCase(newItem)
                self.expenseDict[newItem] = newMoney
            elif response.lower() == 'n' or response.lower() == 'no':
                delay_print("Okay, we won't add any others.")
                break
            else:
                delay_print("Invalid input. Please try again!")
        self.expenseDict['totalMonthlyExpense'] = sum(self.expenseDict.values())
        delay_print("Here's how we're looking with your current expenses:\n")
        for key, value in self.expenseDict.items():
            print(unCamelCase(key), value)
            sleep(0.5)
        sleep(2)
    
    def cashFlow(self):
        self.monthlyCashFlow = self.incomeSourceDict['totalMonthlyIncome'] - self.expenseDict['totalMonthlyExpense']
        delay_print(f"Cash flow is calculated by subtracting your monthly expenses, {self.expenseDict['totalMonthlyExpense']}, from your monthly income, {self.incomeSourceDict['totalMonthlyIncome']}")
        sleep(3)
        delay_print("Your monthly cash flow is")
        dots(3)
        delay_print(f"${self.monthlyCashFlow}")
        sleep(1)

    def returnOnInvestment(self):
        delay_print("What was your down payment? ")
        downPayment = input("")
        delay_print("What were your closing costs? ")
        closingCosts = input("")
        delay_print("What was your rehab budget? ")
        rehabBudget = input("")
        delay_print("If there were any miscellaneous expenses, how much did they total to? ")
        misc = input("")
        totalInvestment = int(downPayment) + int(closingCosts) + int(rehabBudget) + int(misc)
        if totalInvestment > 0:
            self.roi = (self.monthlyCashFlow*12) / totalInvestment
        else:
            self.roi = self.monthlyCashFlow
        delay_print(f"Your total return on investment is {(self.roi)*100}%")
        delay_print("Generally speaking, a good return on investment is about 5-10%")
        if self.roi >= 0.05 and self.roi <= 0.1:#between 5% and 10%
            delay_print("It looks like your property could be a good investment.")
        elif self.roi < 0.05 and self.roi >= 0:#between 0% and 5%
            delay_print("This property might be a little difficult to earn your money back efficiently.")
        elif self.roi < 0:#less than zero
            delay_print("You will lose money on this property. You can go light the money on fire instead if you want.")
            delay_print("Might be less of a headache")
        elif self.roi > 0.1 and self.roi <= 1:#between 10% and 100%
            delay_print("This is a great investment. You should make your money back in no time.")
            delay_print("Next step is to buy another house (and use this calculator again).")
        elif self.roi > 1:#greater than 100%
            delay_print("This uhhh.... property is no good.")
            sleep(2)
            delay_print("Whats the address?")
            sleep(2)
            delay_print("I'm not going to STEAL your investment property. No.")
            sleep(2)
            delay_print("I might buy it for myself.")
            dots(3)
            delay_print("Fair and square.")


invest = MainClass()
while True:
    delay_print(f"\nHello! Welcome to the investment calculator!\n")
    sleep(0.5)
    delay_print("Let's start by calculating your income sources.")
    sleep(1)
    invest.incomeSources()
    delay_print("\nLet's calculate your expenses next.")
    sleep(1)
    invest.expenseSources()
    delay_print("\nNow, we will figure out your monthly cash flow.")
    sleep(1)
    invest.cashFlow()
    delay_print("\nFinally, let's get the total return on investment you can expect.")
    delay_print("Now we can decide if this rental property is worth it or not.\n")
    # dots(5)
    invest.returnOnInvestment()
    break

