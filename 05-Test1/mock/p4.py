'''
The credit card number consists of 16 digits. Define a function f(card_number) that masks the card number. The function returns a character string in which only the first two and the last four digits of the card number are visible. The remaining digits of the card number are replaced with an asterisk. Sample result:
f("5290312400019022") returns "52**********9022"
'''
def f(card_number):
    return card_number[:2]+ '*'*10 + card_number[-4:]

