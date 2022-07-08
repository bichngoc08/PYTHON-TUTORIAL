"""
 Nhập vào một ngày (ngày, tháng, năm). Tìm ngày kế sau ngày vừa nhập (ngày/tháng/năm).
"""

day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))

if day > 31 and month > 12:
    print(" Ngày và tháng không hợp lệ!")
else:
    # Xét qua năm
    if day == 31 and month == 12:
        year += 1
        day = 1
        month = 1
        print("{}" "/" "{}" "/" "{}".format(day, month, year))
    # Xét qua tháng
    elif month in {1, 3, 5, 7, 8, 10, 12}:
        if day == 31:
            day = 1
            month += 1
            print("{}" "/" "{}" "/" "{}".format(day, month, year))
        elif day >= 31:
            print("Ngày không hợp lệ!")
        else:
            day += 1
            print("{}" "/" "{}" "/" "{}".format(day, month, year))
    elif month in {4, 6, 9, 11}:
        if day == 30:
            day = 1
            month += 1
            print("{}" "/" "{}" "/" "{}".format(day, month, year))
        elif day > 30:
            print("Ngày không hợp lệ!")
        else:
            day += 1
            print("{}" "/" "{}" "/" "{}".format(day, month, year))
    elif month in {2}:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            if day == 29:
                day = 1
                month += 1
                print("{}" "/" "{}" "/" "{}".format(day, month, year))
            elif day > 29:
                print("Ngày không hợp lệ!")
            else:
                day += 1
                print("{}" "/" "{}" "/" "{}".format(day, month, year))
        else:
            if day == 28:
                day = 1
                month += 1
                print("{}" "/" "{}" "/" "{}".format(day, month, year))
            elif day > 28:
                print("Ngày không hợp lệ!")
            else:
                day += 1
                print("{}" "/" "{}" "/" "{}".format(day, month, year))
    else:
        print("Tháng không hợp lệ!")
