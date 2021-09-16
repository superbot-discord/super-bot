import re
import datetime as dt
userDate = input("DT: ")

dateParts = {
  m[-1]: int(m[:-1])
  for m in re.findall(r'([\d]{1,4}[yMdhms]{1})', userDate)
}
now = dt.datetime.now()

dObj1 = dt.datetime(1970,1,1,0,0,0)

dObj2 = dt.datetime(
  dateParts.get('y', now.year), dateParts.get('m', now.month),
  dateParts.get('d', now.day), dateParts.get('h', now.hour),
  dateParts.get('M', now.minute), dateParts.get('s', now.second)
)

print(dObj1)
print(dObj2)
print((dObj2-dObj1).total_seconds())