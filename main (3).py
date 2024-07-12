#Use these functions
def GetStartNum():
  while True:
    try:
      num_organisms = int(input("Starting number of organisms: "))
      if num_organisms >= 2:
        return num_organisms
      else:
        print("The starting number of organisms must be at least 2.")
    except ValueError:
      print("Invalid input. Please enter a valid integer.")
    #num_organisms = int(input("Starting number of organisms: "))
    #return num_organisms


def GetDailyInc():
  while True:
    try:
      daily_increase = float(input('Average daily increase:'))   
      if 0 < daily_increase < 1:
        return daily_increase * 100
      elif daily_increase >= 1:
        return daily_increase
      else:
        print('Average daily increase must be a positive number:')
    except ValueError:
      print("Invalid input. Please enter a valid number.")
    #daily_increase = float(input())
    #return daily_increase

def GetNumOfDays():
  while True:
    try:
      num_days = int(input('Number of days to multiply: '))
      if num_days >= 1:
        return num_days
      else:
        print('Number of days must be at least 0.')
    except ValueError:
      print("Invalid input. Please enter a valid integer.")
    #num_days = int(input('Number of days to multiply: '))
    #return num_days


def CalcAndPrint(num_organisms, daily_increase, num_days):
  print('Day Approximate\t\t Population')
  print("-" * 28)
  for day in range(1, num_days + 1):
    if day == 1:
      print(day, '\t\t\t\t\t', num_organisms)
    else:
      num_organisms += num_organisms * (daily_increase/100)
      print(day, '\t\t\t\t\t', num_organisms)
    
  

def main():
  num_organisms = GetStartNum()
  daily_increase = GetDailyInc()
  num_days = GetNumOfDays()
  CalcAndPrint(num_organisms, daily_increase, num_days)

if __name__ == "__main__":
  main()