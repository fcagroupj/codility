'''
Given digitals [123456789], you can insert + or - in any position in order to get the sum of 100
for example:
123+45-67+8-9 = 100
123-45-67+89  = 100
Print all possible ways as example string
expained as:
1 [100, 20, 3, 40, 5, -60, -7, 8, -9]
1 [100, 20, 3, -40, -5, -60, -7, 80, 9]
1 [100, 20, 3, 4, -5, 60, 7, -80, -9]
1 [100, 20, 3, -4, -5, -6, -7, 8, -9]
1 [10, 2, 3, 4, 5, -6, -7, 80, 9]
1 [10, 2, 3, -4, 5, 60, 7, 8, 9]
1 [10, 2, -3, -4, 5, -6, 7, 80, 9]
1 [1, 20, 3, -4, 50, 6, 7, 8, 9]
1 [1, 20, 3, -4, 5, 6, 70, 8, -9]
1 [1, 2, 30, 4, -5, 60, 7, -8, 9]
1 [1, 2, 3, -4, 5, 6, 70, 8, 9]
1 [-1, 2, -3, 4, 5, 6, 70, 8, 9] 
'''
def printSumString(l_digi):
    print(l_digi)
def getTarget(digits, d_target, target):
   
    lt = len(d_target)
    if(lt== 9 and sum(d_target) ==  target):
        printSumString(d_target)
        return 
    
    if(lt >= 9):
        return 
    #print(2, lt, 8 -lt, d_target)
    # each number can be from highest digital to single
    for j in range(8 -lt, -1, -1):
        # if it is not single, the following is decreasing
        for k in range(j+1):
            value = digits[k+lt] * pow(10, j-k)
            d_target.append(value)
        # recursively check
        getTarget(digits, d_target, target)
        for k in range(j+1):
            d_target.pop()
        # can be negative
        for k in range(j+1):
            value = digits[k+lt] * pow(10, j-k)
            d_target.append(-value)    
        getTarget(digits, d_target, target)
        for k in range(j+1):
            d_target.pop()

    return 

digits = [i for i in range(1, 10)]
operation = [10, 1, -1]
target = 100
d_target = []

getTarget(digits, d_target, target)
  
