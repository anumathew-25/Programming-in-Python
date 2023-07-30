#import the pandas library and aliasing as pd
import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve the first element
print(s[0])

#retrieve the first three element
print(s[:3])

#retrieve the last three element
print (s[-3:])



