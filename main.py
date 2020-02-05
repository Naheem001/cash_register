from time import ctime
def get_number_input(prompt):
    value = None
    while type(value) != float:
        try:
            value = float(input(prompt))
            return value
        except KeyboardInterrupt:
            exit()
        except ValueError as e:
            print('Invalid input!')
            print(ctime(), e, file = ERROR_FILE)


def main():
    while True:
        client_name = input('What is the customer\'s name?: ')
        if not client_name:
            break
        while True:
            product_name = input('what is the product name? ')
            if not product_name:
                break
            product_qty = get_number_input('How many {} purchased? '.format(product_name))
            product_price = get_number_input('How much is {}? '.format(product_name))

            print(client_name, product_name, product_qty, product_price, file = REGISTER)


if __name__ == '__main__':
    #superglobals
    ERROR_FILE = open('error_log.txt', 'a')
    REGISTER = open('register.txt', 'a')
    main()
    ERROR_FILE.close()
    REGISTER.close()