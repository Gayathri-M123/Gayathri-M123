Obtain the domain name from the url

Input Format

The input will be a string. For Eg: 'https://www.youtube.com'

Constraints

none

Output Format

The Output format should be in string. For Eg: youtube.com

Sample Input 0

http://www.google.com
Sample Output 0

google.com



PROGRAM
-------


n = list(map(str,input().split("/")))
a = n[2][4:]    
    
print(a)
