import csv
def get_investment_return(start_year, end_year, investment_type, csv_file_path):
    total_return = 1.0

    with open(csv_file_path, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)  
        start_index = headers.index(str(start_year))
        end_index = headers.index(str(end_year)) + 1  
        if investment_type.lower() == 'crypto' and start_year < 2011:
                    return 1.0

        for row in reader:
            if row[0].strip().lower() == investment_type.strip().lower():
                for i in range(start_index, end_index):
                    annual_change_str = row[i].replace('%', '').strip()
                    annual_change = float(annual_change_str) if annual_change_str else 0.0
                    total_return *= (1 + annual_change)
                break

    return total_return


def calculate_final_investment_value(principal_amt, total_return):
    return principal_amt * total_return

def main():
    start_year = 1990
    end_year = 2020
    principal_amt = 1000
    csv_file_path = "S&P 500.csv"  

    investment_types = [
        'S&P 500 (includes dividends)',
        '3-month T.Bill',
        'US T. Bond',
        'Baa Corporate Bond',
        'Real Estate',
        'Gold',
        'Crypto'
    ]

    for investment_type in investment_types:
      
            total_return = get_investment_return(start_year, end_year, investment_type, csv_file_path)
            final_value = calculate_final_investment_value(principal_amt, total_return)
            if principal_amt != final_value:
                print(f"Final Value of ${principal_amt} invested in {investment_type} from {start_year} to {end_year}: ${final_value:.2f}")

if __name__ == "__main__":
    main()
