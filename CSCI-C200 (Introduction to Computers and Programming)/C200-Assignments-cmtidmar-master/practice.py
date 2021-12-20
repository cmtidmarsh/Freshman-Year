from datetime import datetime

now = datetime.now()
today = now.strptime(now, "%m-%d-%Y")
print(now.date())