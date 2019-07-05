a =1
b=2
n=3
print('{a}{b}{n}')
import chardet
import  urllib.request
TestData = urllib.request.urlopen('http://www.163.com/').read()
print(chardet.detect(TestData))
