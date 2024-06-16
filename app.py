from calc_func import do_addition,do_substraction,do_division
from multiply import do_multiplication


def main():
    print("welcome to the calculator app!")
    print(""" select the function
          1.add
          2.substract
          3.multiplication
          4.division
          """)
    user_input = input('Select the function')
    a = int(input('Value of A : '))
    b = int(input('Value of B: '))

    if user_input == '1':
        result = do_addition(a,b)
    elif user_input == '2':
        result = do_substraction(a,b)
    elif user_input=='3':
        result = do_multiplication(a,b)
    elif user_input=='4':
        result = do_division(a,b)
    
    print(result)


if __name__ == '__main__':
    main()


