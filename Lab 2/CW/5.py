def date(day):
  yr = day // 365
  mnth = (day - (yr * 365)) // 30
  days = (day - (yr * 365)) - (mnth * 30)
  return f"{yr} years, {mnth} months and {days} days"

d = int(input(""))
print(date(d))