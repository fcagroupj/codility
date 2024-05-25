'''
Given digitals [123456789], you can insert + or - in any position in order to get the sum of 100
for example:
123+45-67+8-9 = 100
123-45-67+89  = 100
123+4-5+67-89
123-4-5-6-7+8-9
12+3+4+5-6-7+89
12+3-4+5+67+8+9
12-3-4+5-6+7+89
1+23-4+56+7+8+9
1+23-4+5+6+78-9
1+2+34-5+67-8+9
1+2+3-4+5+6+78+9
-1+2-3+4+5+6+78+9
Print all possible ways as example string

'''
def getSum(s_in):
    sum_n = 0
    sign_n = 1
    str_d = ''
    for s in s_in:        
        if(s == '+'):
            if(len(str_d) > 0):
                sum_n += int(str_d) * sign_n
                str_d = ''
            sign_n = 1
        elif(s == '-'):
            if(len(str_d) > 0):
                sum_n += int(str_d) * sign_n
                str_d = ''
            sign_n = -1
        else:
            str_d += s
    if(len(str_d) > 0):
        sum_n += int(str_d) * sign_n
    return sum_n    
def find_combinations(current, remaining, target_sum):
    if not remaining:
        if getSum(current) == target_sum:
            return [current]
        return []
    target_set = []
    for i in range(1, len(remaining) + 1):
        num_str = remaining[:i]
        
        # Concatenate without an operator
        ret = find_combinations(current + num_str, remaining[i:], target_sum)
        for a in ret:
            if(a not in target_set): target_set.append(a)
        # Add with +
        if(current):
            ret = find_combinations(current + '+' + num_str, remaining[i:], target_sum)
            for a in ret:
                if(a not in target_set): target_set.append(a)
        # Add with -
        ret = find_combinations(current + '-' + num_str, remaining[i:], target_sum)
        for a in ret:
            if(a not in target_set): target_set.append(a)
    return target_set
def main():
    digits = "123456789"
    target_sum = 100
    set_target = set()
    ret1 = find_combinations("", digits, target_sum)
    print(ret1)
###############################################################
# this is a little complicated
def getDigitals(n):
    i = 0
    while(n  > 0):
        i += 1
        n = n // 10
    return i
def printSumString(l_digitals):
    #print(l_digitals)
    sum_s = ''
    i = 0
    while(i < len(l_digitals)):
        j = getDigitals( abs(l_digitals[i]) )
        if(j < 1): 
            i += 1
            continue
        sum1 = 0
        for k in range(j):
            sum1 += l_digitals[i+k]
        
        if(i>0 and sum1 > 0): sum_s += '+'
        elif(sum1 < 0): sum_s += '-'
        sum_s += str( abs(sum1) )
        i += j
    print(sum_s)
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

if __name__ == "__main__":
    
    digits = [i for i in range(1, 10)]
    operation = [10, 1, -1]
    target = 100
    d_target = []

    getTarget(digits, d_target, target)
