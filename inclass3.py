def sum_even_numbers(*args):
    
 total=0
 
 for num in args:
     if num%2==0:
      total+=num

 return total

def my_fun():
    
     a = sum_even_numbers(2,4,6,8,10)
     print('sum_even_numbers:', a )
     
my_fun()

