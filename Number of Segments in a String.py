You are given a string s, return the number of segments in the string.

A segment is defined to be a contiguous sequence of non-space characters.

Input Format

Hello, my name is John

Constraints

0 <= s.length <= 300 s consists of lower-case and upper-case English letters, digits or one of the following characters "!@#$%^&*()_+-=',.:". The only space character in s is ' '.

Output Format

5

Sample Input 0

Hello, my name is John
Sample Output 0

5
Explanation 0

The five segments are ["Hello,", "my", "name", "is", "John"]

Sample Input 1

love live! mu'sic forever
Sample Output 1

4
Explanation 1

The five segments are ["love", "live!", "mu'sic", "forever",]





PROGRAM
-------
c=0
a = list(map(str,input().split()))
for i in a:
    c+=1
print(c)    
