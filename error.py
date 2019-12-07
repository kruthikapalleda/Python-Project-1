print('how many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
       print('thats lot many of cats.')
    else:
       print('this is not that many cats.')
except ValueError:
    print('you did not enter a number.')




    #def div42by(divideBy):
    #try:
     #   return 42 / divideBy
    #except: ZeroDivisionError:
     #   print('Error : You tried to divide by zero.')
        
    #return 42 / divideBy

#print(div42by(2))
#print(div42by(12))
#print(div42by(0))
#print(div42by(1))



