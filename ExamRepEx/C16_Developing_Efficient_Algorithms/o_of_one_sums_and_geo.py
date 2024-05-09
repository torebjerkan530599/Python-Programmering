import time

# An O(1) time algorithm for computing the sum of numbers from n1 to n2 for (n1 < n2)
def On_time1_summation(n1,n2):
  sum = n2 * (n2 + 2) / 2 - n1 * (n1 + 2) / 2
  return sum

def On_time2_summation(n1,n2):
  sum = n2 * (n2 + 1) / 2 - n1 * (n1 + 1) / 2
  return sum

print(On_time1_summation(10,20))  
print(On_time2_summation(10,20))

def On_time3_geometric(a, n1):
  sum = (1 - a ** (n1+1)) / (1-a)
  sum = -1 + 2 ** (n1+1)
  return sum

print(On_time3_geometric(2,10))

# 16.3.5

def iterative_exponentiation(a, n):
  function_time_start = time.time()
  result = a
  i = 2
  
  startTime = time.time()
  while i <= n:
      result *= result # i.e result = 2: 2*2=4, 4*4 = 16, 16*16 = 256  
      i *= 2 # doubling 1 every iteration, meaning: 4,8,16

  
  endtime = time.time()
  print(f'Execution of the while loop:  {endtime - startTime}')
  
  startTime = time.time()
  
  for _ in range(i // 2 + 1, n + 1):
      result *= a # 265 * 2 = 512, 512 * 2 = 1024
  
  endtime = time.time()
  
  print(f'Execution of the for loop:  {endtime - startTime}')
  
  function_time_end = time.time()
  print(f'Execution iterative exponentiation:  {function_time_end - function_time_start}')
  
  return result
  
# Assume that 2k-1 <= n < 2k. 
# The while loop is executed k-1 times. 
# The for loop is executed at most 2k-2k-1=2k-1 times. 
# So, the total complexity is O(n). Consider another implementation:

def recursive_exponentiation(a, n):
    if n == 1:
        return a
    else:
        temp = recursive_exponentiation(a, n // 2)
        if n % 2 == 0:
            return temp * temp
        else:
            return a * temp * temp

# Test the functions
iterative_exponentiation(2, 700000)  # Example usage
function_time_start = time.time()
recursive_exponentiation(2, 700000)   # Example usage
function_time_end = time.time()
print(f'Execution recursive exponentiation:  {function_time_end - function_time_start}')