## program to extract Strings between HTML
import re

test_str = '<b>Reddy Prasad</b> is <b>Best</b>. I love <b>Technology Enabler Machine Learning Algorithm</b> <b>Reading CS</b> from it.<b>Machine Learing Researcher</b>'
print("The original string is : " + str(test_str))
  
tag = "b"  # brack tag in html
  
# regex to extract required strings
reg_str = "<" + tag + ">(.*?)</" + tag + ">"
res = re.findall(reg_str, test_str)
  
# printing result
print("The Strings extracted : " + str(res))