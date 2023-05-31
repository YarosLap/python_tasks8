import os
import re

data = open('/Users/yaroslav/Desktop/GB/Python/dz8.nosync/log.txt', mode='r', encoding='utf-8')
text = data.readline()
quest = text.split(':')[1]
data.close()
answer = input(f'{quest}? Ваш ответ:')
print(answer)

data2 = open('/Users/yaroslav/Desktop/GB/Python/dz8.nosync/ans.txt', mode='a', encoding='utf-8')
data2.write(answer)
data.close()
