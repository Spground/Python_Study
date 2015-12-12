#Data Struct in python

#list list can be modified, but string and tuple can't
#-----------------------------list’s usage--------------------------------------

#append
mList = [1, 2, 3, 4];
mList.append(5);
print(mList);

#extend
temp = [6, 7, 8];
mList.extend(temp);
print(mList, "the length of mList is ", len(mList));

#insert
mList = [0,1, 2, 3, 4];
mList.insert(0, 0);
print(mList);

#remove
print("origin list is ", mList);
mList.remove(0);#only remove the firt 0(if 0 appears more than once)
#mList.remove(9); if elemen is not existed, it will throw a exception
print("removed mList is ", mList);

#pop pop([i]), i is a optional arg
mList = [1, 2, 3, 4, 5];
#this will pop the last elemnt in list, and remove it from list
pValue = mList.pop();
print("The result of pop() is ", pValue);
print(mList);

pValue = mList.pop(0);
print("The result of pop(0) is ", pValue);
print(mList);

#clear equal to del a[:]
#two methods used to clear list
mList = [1, 2, 3, 4, 5];
mList.clear();
print(mList);

mList = [1, 2, 3, 4, 5];
del mList[:];
print(mList);

#index(x) return the position where the element firstly appear
mList = [1, 1, 2, 3, 5, 5];
print("The position where 5 appears firstly is ", mList.index(5));

#count(x)
print("The count of 5 is ", mList.count(5));

#sort
mList = [52, 56, 0, -2.0,63, 11, 36, 7];
print("THe orignal list is ", mList);
mList.sort();
print("The sorted list is ", mList);

#reverse
mList = [52, 56, 0, -2.0,63, 11, 36, 7];
print("THe orignal list is ", mList);
mList.reverse();
print("The reversed list is ", mList);

#copy
mList = [1, 2, 3, 4, 5];
mList0 = mList;
mListCopy = mList.copy();
print("mList is ", mList);
print("mList0 is ", mList0);
print("mListCopy is ", mListCopy);

mList.append(6);
print("mList has appended a elment\n");
print("mList is ", mList);
print("mList0 is ", mList0);
print("mListCopy is ", mListCopy);

#use list to built Stack Data Struct

stack = [];

def push(e):
        stack.append(e);
        return;

def pop():
        return stack.pop();

#push some element
print("The push order is ", end = ":");
i = 5;
while i :
        push(i);
        print(i, end=", ");
        i = i - 1;

#print the pop order
print("The pop order is ", end = ": ");
while len(stack):
        print(stack.pop(), end = ", ")

#queue
from collections import deque
queue = deque(["H", 1, "G"]);
queue.append(6);
print(queue);
print("Pop is ", queue.popleft());

#列表推导式
vec = [2, 4, 6];
vec = [3*x for x in vec];
print(vec);

vec = [[x, x ** 2] for x in vec];
print(vec);

vec = [2, 4, 6];
vec = [x for x in vec if x > 3];
print(vec);

vecX = [1, 2, 4, 8];
vecY = [-1, -2, -4, -8];
#vecX + vecY
v = [vecX[i] + vecY[i] for i in range(len(vecX))];
print("vecX + vecY is ", v);

v = [x + y for x in vecX for y in vecY];
print(v);

#嵌套列表解析
#矩阵的转置
#方式一
martrix = [
        [1, 2, 3 ,4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
        ]
martrix = [[row[i] for row in martrix] for i in range(len(martrix))];
print(martrix);

#tuple & sequence
t = (123, 54321, "hello");
print(t[0]);
print(t);
u = (t, t);
print(u);

#set
basket = {"apple", "orange", "apple", "pear"};
print(basket);
print("apple" in basket);

a = set("abgfagregrwaegrega");
print(a);

#集合也支持推导模式
a = {x for x in 'abjbjufbnhsdeiufhui' if x not in 'abc'};
print(a);

#字典
tel = {"Tom":15123, "Tony":123, "Lincon":5456, 110:120};
print("TEl type is ", type(tel), "tel is ", tel);

print(tel[110]);

#keys
keys = tel.keys();
print(keys);

keysList = list(keys);
print(keysList);
print(keysList[0]);

