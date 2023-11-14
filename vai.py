'''
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.171 Safari/537.36
         Windows NT 5.1,
        "Windows NT 6.0.
        'Windows NT 6.1',
        "Windows NT 6.2",
        'Windows NT 6.3",
        
'''
import random
usen=[]
for x in range(1000):
  a='Mozilla/5.0 (Windows NT'
  b=random.choice(['10.0','5.1','6.0','6.1','6.2','6.3'])
  c='Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
  d=random.randrange(73,127)
  e='0'
  f=random.randrange(3000,6000)
  g=random.randrange(40,150)
  i='Safari/537.36'
  ua=f'{a} {b};{c}{d}.{e}.{f}.{g} {i}.{f}'
 ugen.append(ua)
  
print(ugen)