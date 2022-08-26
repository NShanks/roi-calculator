def camelCase(x):
    newWord = ''
    for word in x.split():
        newWord += word.strip().capitalize()
        newWord = newWord.replace(newWord[0], newWord[0].lower(), 1)
    return newWord
# newItem = camelCase(input("enter a few words: "))
# print(newItem)
# print(camelCase(input("hello sir how are you today")))
# print(camelCase(newItem))
# print(newItem)

def unCamelCase(x):
    newWord = ''
    for letter in range(len(x)):
        if x[letter].isupper() == True:
            newWord += (f" {x[letter]}")
        else:
            newWord += (x[letter])
    return newWord.capitalize()

print(unCamelCase("asdfAsdf"))

monthlyCashFlow = 390
downPayment = 40000
closingCosts = 3000
rehabBudget = 7000
misc = 0
totalInvestment = int(downPayment) + int(closingCosts) + int(rehabBudget) + int(misc)

roi = (monthlyCashFlow*12) / totalInvestment

print(roi)