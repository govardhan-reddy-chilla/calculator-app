from calc_func import do_addition,do_substraction

def main():
    print("welcome to the calculator app!")
    print("""n select the function
          1.add
          2.substract
          """)
    user_input = input('Select the function')
    a = int(input('Value of A : '))
    b = int(input('Value of B: '))

    if user_input == '1':
        result = do_addition(a,b)
    elif user_input == '2':
        result = do_substraction(a,b)
    
    print(result)


if __name__ == '__main__':
    main()


