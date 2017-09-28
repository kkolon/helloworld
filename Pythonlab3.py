fruit_basket = ['grapefruit', 'raspberry', 'blackberry', 'pomelo', 'orange']

def guess_fruit(basket):
    basket = fruit_basket

def main():
    i= 0
    while i < 5:
        guess = raw_input("Guess a fruit!")

        if guess in fruit_basket:
            print("You guessed correctly")
            i = 5
        else:
            print("The fruit is not in the fruit basket!")
            i += 1


main()
