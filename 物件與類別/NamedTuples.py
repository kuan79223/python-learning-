from collections import namedtuple

Sky = namedtuple('Da','top down')

fa = Sky('上面','下面')
print(fa)
print(fa.top)
print(fa.down)

'----------------------------'
#
dict1 = {'top':'上面','down':'下面'}

fa1 = Sky(**dict1)
print(fa1)
print(fa1.top)
print(fa1.down)
#更改內容
fa2 = fa1._replace(top='蒼天',down='大地')
print(fa2)
#創建
dict1['上面'] = '天空'
print(fa1)