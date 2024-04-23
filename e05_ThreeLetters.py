'''

Write a function solution that, given two integers A and B, returns a string containing exactly A letters 'a' and exactly B letters 'b' with no three consecutive letters being the same (in other words, neither "aaa" nor "bbb" may occur in the returned string).

Examples:

1. Given A = 5 and B = 3, your function may return "aabaabab". Note that "abaabbaa" would also be a correct answer. Your function may return any correct answer.

2. Given A = 3 and B = 3, your function should return "ababab", "aababb", "abaabb" or any of several other strings.

3. Given A = 1 and B = 4, your function should return "bbabb", which is the only correct answer in this case.

Assume that:

A and B are integers within the range [0..100];
at least one solution exists for the given A and B.
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
'''
def solution(A, B):
    # Implement your solution here
    N = A + B
    if(A == 0 and B == 0) return ''
    if(A == 0):
      res = ['b'] * B
      return ''.join(res)
    if(B == 0):
      res = ['a'] * A
      return ''.join(res)
    sel = 'a'
    if(B > A): sel = 'b'
    if(sel == 'a'): A -= 1
    else: B -= 1
    dp = [''] * (N + 1)
    dp[0] = sel
    for i in range(1, N):
      sel = 'a'
      if(B > A): sel = 'b'
      if(i >= 2):
        if(dp[-2:] == 'aa'): sel = 'b'
        elif(dp[-2:] == 'bb'): sel = 'a'
      if(sel == 'a'): A -= 1
      else: B -= 1
      dp[i] = dp[i-1] + sel
    return dp[N-1]
