#序列封包：将10、20、30分装成元组后赋值给vals
vals = 10, 20, 30
print(vals)
print(type(vals))
print(vals[1])
a_tuple = tuple(range(1, 10, 2))
#序列解包：将a_tuple元组的各元素依次赋值给a、b、c、d、e变量
a, b, c, d, e = a_tuple
print(a, b, c, d, e)
a_list = ['fkit', 'crazyit']
#序列解包：将a_list 序列的各元素依次赋值给a_str、b_str变量
a_str, b_str = a_list
print(a_str, b_str)