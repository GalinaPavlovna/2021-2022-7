def cez(s,n,l):
    par1 = [64, 91, 96, 123, 26]
    par2 = [ord('а') - 1, ord('я') + 1, ord('А') - 1, ord('Я') + 1, 32]
    if l == 'en':
        p = par1
    else:
        p = par2
    s1=list(s)
    for i in range (len(s1)):
        if p[0]<ord(s1[i])<p[1]:
            s1[i]=chr(ord(s1[i])+n) if ord(s1[i])+n<p[1] else chr(ord(s1[i])+n-p[4])
        elif p[2]<ord(s1[i])<p[3]:
            s1[i]=chr(ord(s1[i])+n) if ord(s1[i])+n<p[3] else chr(ord(s1[i])+n-p[4])
    return ''.join(s1)

#Основная программа
l=input('Введите язык. руский - ru, английский - en:  ')
v=input ('Расшифровываем - 1, зашифровываем -2  ')
if v=='2':
    n=int(input('Введите сдвиг: '))
    s=input('Введите фразу: ')
    print (cez(s,n,l))
else:
    k=26
    if l=="ru": k=32
    n = int(input('Введите сдвиг; если не известен, введите 0 '))
    s = input('Введите фразу: ')
    if n!=0: print (cez(s,k-n,l))
    else:
        d=0
        i=1
        while d==0:
            print(cez(s,k-i,l))
            d=int(input('Фраза осмысленна? Если да - нажмите 1, если нет - 0 '))
            print (d)
            i+=1
