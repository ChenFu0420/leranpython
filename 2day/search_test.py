s = 'crazyit.org is good site'
#判断s是否已crazyit 开头
print(s.startswith('crazyit'))
#判断s是否已site结尾
print(s.endswith('site'))
#查找s中org出现的位置
print(s.find('org')) #8
#从索引9出开始查找org出现的位置
print(s.find('org', 9)) #-1
#将字符串中所有it替换成xxxx
print(s.replace('it', 'xxxx'))
#将字符串中1个it替换成xxxx
print(s.replace('it', 'xxxx', 1))
#定义翻译映射表：97 (a)->945 (α), 98(b)-> 945（β）, 116(t) -> 964(τ)
table = {97: 945, 98: 946, 116: 964}
print(s.translate(table))