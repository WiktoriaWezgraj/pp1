def f(card_number):
    card_number = str(card_number)
    print(card_number[:2] + '*'*10 + card_number[-4:])
if __name__ =="__main__":
    f('5290312400019022')
