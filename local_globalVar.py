def spam():
    global eggs  #refer to global eggs
    eggs =' KP ' #assignment statments = Local var
                 #else no assign statements =global var
    print(eggs)  
eggs = 42  

    #eggs = 99
    #bacon()
    #print(eggs) #def bacon():
    #ham = 101
    #eggs = 0  #local cant use local var in other scopes,ie: local variables of one fuction is completly different from other local function and they are not the same.

spam()
print(eggs)
#print(eggs) #local var cant be used in global scopes.



#spam = 42 #global variable

#def eggs():
    #spam = 42 #local variable

#print('some code here.')
#print('some more code.')
