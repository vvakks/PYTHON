def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        try:
            date = input("Date: ").strip()

            # Case 1: MM/DD/YYYY
            if "/" in date:
                month, day, year = date.split("/")
                
                month = month.zfill(2)
                day = day.zfill(2)
                if int(month)>12 or int(day)>31:
                    continue
                print (month,day,year)
                print(f"{year}-{month}-{day}")
                break

            # Case 2: Month D, YYYY
            else:
                month_str, rest = date.split(" ", 1)
                day, year = rest.replace(",", "").split(" ")
                month_index = months.index(month_str.title()) + 1
                month = str(month_index).zfill(2)
                day = day.zfill(2)
                if int(month)>12 or int(day)>31:
                    continue
                print(f"{year}-{month}-{day}")
                break

        except (ValueError, IndexError):
            # Catch bad formats and prompt again
            continue

main()
