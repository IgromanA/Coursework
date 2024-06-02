def main():
    Flag = True

    choise = int(input("Which action will you choose?\n ▷ 1 ― x+2\n ▷ 2 ― x*2\n ▷ 3 ― x²\n"))
    keys = list(map(int, input("Enter your numbers: ").split()))
    while Flag:
        if choise == 1:
            print(f"\033[H\033[JResults:\n")
            for key in keys:
                print(f" ({key}): {key + 2}")
            Flag = False
        elif choise == 2:
            print(f"\033[H\033[JResults:\n")
            for key in keys:
                print(f" ({key}): {key * 2}")
            Flag = False
        elif choise == 3:
            print(f"\033[H\033[JResults:\n")
            for key in keys:
                print(f" ({key}): {key ** 2}")
            Flag = False
        else:
            print(f"\033[H\033[JIncorrect value!")
            Flag = False
    cont = input('\nDo u want continue? (y/n): ')
    if cont == "y":
        print("\033[H\033[J", end="")
        main()
    else:
        print(f'\033[H\033[JHave a good day! ;)')
        
    
if __name__ == "__main__":
    main()