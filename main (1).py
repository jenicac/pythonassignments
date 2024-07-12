def is_list_mult10(my_list):
  for num in my_list:
    #identify multiples of 10
    if num % 10 != 0:
      return False
    return True
def is_list_no_mult10(my_list):
  for num in my_list:
    #identify non-multiples of 10
    if num % 10 == 0:
      return False
    return True
def main():
  size = int(input())
  values = []
  for i in range(size):
    value = int(input())
    values.append(value)
  if is_list_mult10(values):
        print('all multiples of 10')
  elif is_list_no_mult10(values):
        print('no multiples of 10')
  else:
        print('mixed values')
      
if __name__ == '__main__':
    main()
    
#not printing mixed value