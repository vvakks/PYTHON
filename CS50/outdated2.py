def main():
    monthsew = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    while True:
        try:
            x=input("Enter shit")
            if("/" in x):
                months, days , years= x.split("/")
                if int(months)>12 or int(days)>31:
                    continue
                months=months.zfill(2)
                days=days.zfill(2)
                print(f"{years}-{months}-{days}")
                break
            else:
                month_temp, day_temp, year = x.split(" ")
                month=str(monthsew.index(month_temp)+1).zfill(2)
                day=day_temp[:1].zfill(2)
                print(f"{year}-{month}-{day}")
                break
        except(ValueError, IndexError):
            continue
main()
                
                