def dec2bin(x):
    c = ''
    while x >= 1:
        a = x % 2
        x = x // 2
        c = c +str(a)
    return(c[::-1])
print('请输入十进制数：',end = '')
temp = input()
num = int(temp)
print('%d的二进制为：'%num,end = '')
print(dec2bin(num))
