import csv

def calculate_simple_interest(amount, year, rate):
        return (amount * year * rate) / 100

def calculate_compound_interest(principal, rate, times_compounded, years):
        return principal * (pow((1 + rate / times_compounded), times_compounded * years))

def calculate_compound_interest(principal, rate, times_compounded, years):
        return principal * (pow((1 + rate / times_compounded), times_compounded * years))

def adjust_for_inflation(start_year, end_year, principal_amount, csv_file_path):
        adjusted_amount = principal_amount
        with open(csv_file_path, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                for year in range(int(start_year), int(end_year)-1):
                    str_year = str(year)
                    if str_year in row:
                        inflation_rate = float(row[str_year])/100
                        adjusted_amount *= (1 + inflation_rate)
        return adjusted_amount
def depreciated_value_due_to_inflation(start_year, end_year, principal_amount, csv_file_path):
    adjusted_amount = principal_amount
    with open(csv_file_path, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            for year in range(int(start_year), int(end_year)):
                str_year = str(year)
                if str_year in row:
                    inflation_rate = float(row[str_year]) / 100
                    adjusted_amount /= (1 + inflation_rate)
    return adjusted_amount
start_year = 1990#nput("Enter the starting year: ")
end_year = 2002#input("Enter the ending year: ")
principal_amt = 1000#float(input("Enter the principal amount: "))

rate = 3 #float(input("Enter the annual interest rate (in %): "))
years = 12#float(input("Enter the number of years: "))
times_compounded = 2#float(input("Enter the number of times interest is compounded per year: "))
if __name__ == "__main__":
    csv_file_path = "merica.csv"  

    adjusted_amount = depreciated_value_due_to_inflation(start_year, end_year, principal_amt, csv_file_path)
    print(f"The amount adjusted for inflation is: {adjusted_amount:.2f}")

    simple_interest = calculate_simple_interest(principal_amt, years, rate)
    print(f"The simple interest is: {simple_interest:.2f}")
    principal_amt=simple_interest
    Inflation_simple_interest = depreciated_value_due_to_inflation(start_year, end_year, principal_amt, csv_file_path)
    print(f"The inflation adjusted simple interest is: {Inflation_simple_interest}")
    compound_interest = calculate_compound_interest(principal_amt, rate/100, times_compounded, years)
    print(f"The compound interest is: {compound_interest:.2f}")
    principal_amt=compound_interest
    Inflation_simple_interest = depreciated_value_due_to_inflation(start_year, end_year, principal_amt, csv_file_path)
    print(f"The inflation adjusted compound interest is: {Inflation_simple_interest}")




