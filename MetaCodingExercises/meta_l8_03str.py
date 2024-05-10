'''
Minimum Length Substrings
You are given two strings s and t. You can select any substring of string s and rearrange the characters of the selected substring. Determine the minimum length of the substring of s such that string t is a substring of the selected substring.
Signature
int minLengthSubstring(String s, String t)
Input
s and t are non-empty strings that contain less than 1,000,000 characters each
Output
Return the minimum length of the substring of s. If it is not possible, return -1
Example
s = "dcbefebce"
t = "fd"
output = 5
Explanation:
Substring "dcbef" can be rearranged to "cfdeb", "cefdb", and so on. String t is a substring of "cfdeb". Thus, the minimum length required is 5.
'''
'''
We first count the occurrences of characters in string t and store them in a dictionary t_count.
We use a sliding window approach to iterate over string s.
At each step, we update the count of characters in the window and try to minimize the window by moving the start pointer.
Finally, we return the minimum length found. If no valid substring is found, we return -1.
'''
def minLengthSubstring(s, t):
    # Count the occurrences of characters in string t
    t_count = {}
    for char in t:
        t_count[char] = t_count.get(char, 0) + 1
    
    # Initialize variables for the sliding window
    min_length = float('inf')
    start = 0
    missing = len(t)
    
    # Iterate over the string s using a sliding window
    for end in range(len(s)):
        # Update the count of the current character
        if s[end] in t_count:
            t_count[s[end]] -= 1
            if t_count[s[end]] >= 0:
                missing -= 1
        
        # If all characters of t are found in the window, try to minimize the window
        while missing == 0:
            min_length = min(min_length, end - start + 1)
            if s[start] in t_count:
                t_count[s[start]] += 1
                if t_count[s[start]] > 0:
                    missing += 1
            start += 1
    
    # If no valid substring found, return -1
    if min_length == float('inf'):
        return -1
    return min_length
'''
'''
import math
# Add any extra import statements you may need here
from itertools import permutations

# Add any helper functions you may need here
def getPositions(S):
  mp = {}
  for i in range(len(S)):
    prev = mp.get(S[i], [])
    mp[ S[i] ] = prev + [i]
  return mp
def getLenSubstr(l_positions):
  if(len(l_positions) < 1): return 0;
  l_positions.sort()
  return (l_positions[-1] - l_positions[0] + 1)
def min_length_substring(s, t):
  # Write your code here
  # check total size
  if(len(s) < len(t)): return -1
  
  # list number, position of letters in s and t
  s_positions = getPositions(s)
  t_positions = getPositions(t)
  #print('s_positions', s_positions)
  #print('t_positions', t_positions)
  # list possible permutations of target letters
  t_perms_total = []
  for let_t in t_positions:
    # check every letter in target
    n_t = len( t_positions.get(let_t, []) )
    n_s = len( s_positions.get(let_t, []) )
    if( n_t > n_s ): return -1   # impossible
    elif( n_t == n_s ):
      if(len(t_perms_total) < 1):
        t_perms_total.append(s_positions.get(let_t, []))
        
      else:
        # all are put into list
        for a_perm in t_perms_total:
          a_perm += s_positions[let_t]
    else: # there are many possibilities
      t_perms = list( permutations(s_positions[let_t], n_t) )
      for i in range(len(t_perms)) :
        if(i == 0): continue # will be added later
        n_perms = len(t_perms_total)
        for j in range(n_perms):  # expand the list so the length will be len(t_perms) times
          t_perms_total.append(t_perms_total[j] + list(t_perms[i]) )
      # add or append the first one
      if(len(t_perms) > 0 ):
        if(len(t_perms_total) < 1):
          t_perms_total.append( list(t_perms[0]) )
        else:
          for a_perm in t_perms_total:
            a_perm += list(t_perms[0]) 
    #print(let_t, n_t, n_s, t_perms_total)      
  # get minimum substing from t_perms_total
  min_len = float('inf')
  for t_perms in t_perms_total:
     min_len = min(getLenSubstr(t_perms),min_len)
    
  # select min substring
  if(min_len == float('inf')): return -1
  return min_len











# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  s1 = "dcbefebce"
  t1 = "fd"
  expected_1 = 5
  output_1 = min_length_substring(s1, t1)
  check(expected_1, output_1)

  s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
  t2 = "cbccfafebccdccebdd"
  expected_2 = -1
  output_2 = min_length_substring(s2, t2)
  check(expected_2, output_2)

  # Add your own test cases here
  s1 = "dcbefebcedd"
  t1 = "fdd"
  expected_1 = 10
  output_1 = min_length_substring(s1, t1)
  check(expected_1, output_1)

  
