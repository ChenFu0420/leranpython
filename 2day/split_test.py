s = 'crazyit.org is a good site'
#使用空白字符分割
print(s.split())
#使用空白字符分割最，最多之分割前两个单词
print(s.split(None, 2))
#使用.进行分割
print(s.split('.'))
mylist = s.split()
#使用‘/'作为分隔符，将mylist连接成字符串
print('/'.join(mylist))
#使用‘,'作为分隔符，将mylist连接成字符串
print(','.join(mylist))