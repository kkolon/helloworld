#frut basket game

fruit_basket = ['grapefruit', 'apple', 'tree sap', 'pear', 'dirt']

def guess_fruit(basket):
    basket = fruit_basket

def main():
    i= 0
    while i < 5:
        guess = raw_input("Pick a fruit for my fruit basket . . .")

        if guess in fruit_basket:
            print("Yay! You are correct!")
            i = 5
        else:
            print("Not my kind of fruit!")
            i += 1


main()
