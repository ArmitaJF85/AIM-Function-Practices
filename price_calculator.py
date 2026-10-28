#https://github.com/ArmitaJF85/AIM-Function-Practices.git

def calculate_price(price, tax_rate=0.1):
    return price * (1 + tax_rate)

def main():
    price = float(input())
    try:
        tax_rate = float(input())
    except EOFError:
        tax_rate = 0.1

    print(calculate_price(price, tax_rate))

if __name__ == "__main__":
    main()
