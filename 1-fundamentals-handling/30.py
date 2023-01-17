days = int(input("Days: "))
years = days // 365
days_without_years = days % 365
months = days_without_years // 30
days_without_months_and_years = days_without_years % 30
print(f"{days} days is {years} year(s) {months} month(s) and {days_without_months_and_years} day(s)")