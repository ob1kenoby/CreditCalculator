import math
import argparse


def overpayment(o):
    print(f"\nOverpayment = {o}")


def calculate_periods(p, a, i):
    n = math.ceil(math.log((a / (a - i * p)), (1 + i)))
    if n == 1:
        text = f"1 month"
    elif n < 12:
        text = f"{n} months"
    elif n == 12:
        text = f"1 year"
    elif n == 13:
        text = f"1 year and 1 month"
    elif n % 12 == 1:
        text = f"{n // 12} years and 1 month"
    else:
        text = f"{n // 12} years and {n % 12} months"
    print(f"You need {text} to repay this credit")
    overpayment(a * n - p)


def calculate_annuity(p, n, i):
    a = math.ceil(p * ((i * pow(1 + i, n)) / (pow(1 + i, n) - 1)))
    print(f"Your annuity payment = {a}")
    overpayment(a * n - p)


def calculate_principal(a, n, i):
    p = math.ceil(a / ((i * pow(1 + i, n)) / (pow(1 + i, n) - 1)))
    print(f"Your credit principal - {p}!")
    overpayment(a * n - p)


def calculate_difference(p, n, i):
    total_paid = 0
    for m in range(1, n + 1):
        d = math.ceil(p / n + i * (p - (p * (m - 1)) / n))
        total_paid += d
        print(f"Month {m}: paid out {d}")
    overpayment(total_paid - p)


parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--principal', type=int)
parser.add_argument('--payment', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
args = parser.parse_args()
error_argument = False
number_of_parameters = 0
for arg in vars(args):
    if getattr(args, arg):
        number_of_parameters += 1
        if arg != "type" and getattr(args, arg) < 0:
            error_argument = True
        elif args.interest is None:
            error_argument = True
        else:
            interest = args.interest / (12 * 100)
if (args.type is None) or (args.type not in ('diff', 'annuity')) or (
        number_of_parameters < 4) or error_argument or (
        args.type == 'diff' and args.payment is not None):
    print("Incorrect parameters")
elif args.type == "diff":
    if args.payment is None:
        calculate_difference(args.principal, args.periods, interest)
elif args.type == 'annuity':
    if args.periods is None:
        calculate_periods(args.principal, args.payment, interest)
    elif args.payment is None:
        calculate_annuity(args.principal, args.periods, interest)
    elif args.principal is None:
        calculate_principal(args.payment, args.periods, interest)
