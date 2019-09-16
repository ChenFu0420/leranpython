#导入traceback模块
import traceback
class SelfException(Exception): pass
def main():
    firstMethod()
def firstMethod():
    secondMethod()
def secondMethod():
    thridmethod()
def thridmethod():
    raise SelfException("自定义异常信息")
try:
    main()
except:
    #捕获异常，并将异常传播信息输出到控制台
    traceback.print_exc()
    #捕获异常，并将异常传播信息输出到指定文件中
    traceback.print_exc(file=open('log.txt','a'))