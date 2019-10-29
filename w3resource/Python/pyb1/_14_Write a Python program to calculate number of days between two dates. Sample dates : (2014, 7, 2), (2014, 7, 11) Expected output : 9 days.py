from datetime import date
startDate = date(2019, 5, 25)
endDate = date(2019,5, 5)
result = startDate - endDate
print(result.days)