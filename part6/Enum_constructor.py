import enum
class Gender(enum.Enum):
    MALE = '男','阳刚之力'
    FEMAL = '女','柔顺之美'
    def __init__(self,cn_name, desc):
        self._cn_name = cn_name
        self._desc = desc
    @property
    def desc(self):
        return self._desc
    @property
    def cn_name(self):
        return self._cn_name
#访问FEMALE的name
print("FEMALE的name：", Gender.FEMAL.name)
#访问Female的Vlaue
print("FEMALE的Value：", Gender.FEMAL.value)
#访问自定义的cn_name属性
print("FEMALE的cn_name：",Gender.FEMAL.cn_name)
#访问自定义的desc属性
print("FEMALE的desc：",Gender.FEMAL.desc)