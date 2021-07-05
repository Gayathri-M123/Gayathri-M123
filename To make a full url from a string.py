To make a full url from a given string

Input Format

The input will be as a string.

Constraints

none

Output Format

The output will be as a url format.

Sample Input 0

www#hackkerrank#com#domains#python
Sample Output 0

https://www.hackkerrank.com/domains/python/
Sample Input 1

www#youtube#com#watch#python-tutorial
Sample Output 1

https://www.youtube.com/watch/python-tutorial/
  
  
  
  
  
PROGRAM
-------


s = ''
c = 0
k= '.'
j = '/'
m = list(map(str,input().split('#')))
for i in m:
    if c<3:
        s = s+i
        c+=1
        if c<3:
            s = s+k   
    elif len(m)>c:
        c += 1
        s = s+j
        s = s+i 
k = "https://" +s
print(k,end='/')
    
