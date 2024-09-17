def month_name(month):
    months = {1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель", 5: "Май", 6: "Июнь",
              7: "Июль", 8: "Август", 9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}
    return months[month] if month in months else None

print(month_name(4)) # april
print(month_name(13)) # None