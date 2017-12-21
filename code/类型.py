# -*- coding: utf-8 -*-

print('1.3 的类型: %s' % type(1.3))

print('1 的类型: %s' % type(1))

print('\'I\\\'m jack\' 的类型: %s' % type('I\'m jack'))

print('u\'我\'的类型: %s' % type(u'我'))

print('我'*3)

print('我是超人'[1:2])
print('我是超人'[:2])
print('我是超人'[3:])

print(r'\r我是超人')
print('\t我是超人')

a = 2

print('%e' % 1.3)

print("{0} {1}, 你好!".format("hello", "world"))

print(str.capitalize('jack'))

print('[jack]'.center(20, '-'))

print('1233211'.count('1'))

print('\'你好啊\'的utf-8编码: %s' % '你好啊'.encode("UTF-8"))

print('111'.endswith('0'))
print('1110'.endswith('0'))

print('你好\t哈哈'.expandtabs(tabsize=4))

print('46452534634'.index('3'))

try:
	print('46452534634'.index('a'))
except Exception as e:
	print(e)

print('你好啊'.isalnum())
print('你好啊1'.isalnum())
print('你好啊1，'.isalnum())
print()
print('你好啊'.isalpha())
print('你好啊，'.isalpha())

print('hello world'.title())
print()
print('11Hello World11'.strip('11'))

print('hello world'.upper())

l = ['item', 'item1']

print('[\'item\', \'item1\'] 的类型: %s' % type(l))

print("len list: ", l.__len__())
print("len list: ", len(l))

print()


class My:
	def __len__(self):
		return 3432543

nmy = My()
print('len(nmy): %d' % len(nmy))
print()

print("list[0]: ", l[0])
l[0] = 'change item'
print("list[0]: ", l[0])

del l[0]

print(l)


l2 = ['item', 'item1', 'item2']
print('l2[1:]: ', l2[1:])
l3 = l2
l4 = l2.copy()
print('l3: ', l3)
print('l4: ', l4)
l2.clear()
print('l2: ', l2)
print('l3: ', l3)
print('l4: ', l4)


tup1 = ('Google', 'Runoob', 1997, 2000)

print('tup1', tup1)

try:
	tup1[1] = 'hello'
except Exception as e:
	print(e)

tup2 = (1,)

tup3 = tup1 + tup2

print('tup3', tup3)

dict1 = {'Alice': 2341, 'Beth': '9102', 'Cecil': '3258'}

print(dict1)
print('dict1[\'Alice\']: ',dict1['Alice'])

c=True

if c:
	print('c is True')
elif "11":
	print('111')
else:
	print('C is False')

if "11":
	print('11 is True')

count = 0
while count < 5:
	print(count, " 小于 5")
	count = count + 1
else:
	print(count, " 大于或等于 5")


for i in range(5):
	print("range 5: ", i)

for i in range(5, 10):
	print("range 5, 10: ", i)

for i in range(5):
	if i == 2:
		break
	print("range 5: ", i)
