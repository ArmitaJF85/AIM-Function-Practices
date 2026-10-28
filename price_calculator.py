#https://github.com/ArmitaJF85/AIM-Function-Practices.git
import sys

def calculate_price(price, tax_rate=0.1):
    return price * (1 + tax_rate)

def main():
    lines = sys.stdin.read().splitlines()
    price = float(lines[0])

    if lrn(lines) > 1 and
lines[1].strip():
         tax_rate = float(lines[1])
        print(calculate_price(price, tax_rate))
else:
    print(calculate_price(price))

if __name__ == "_main_":
    main()
