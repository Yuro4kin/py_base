

# 3. Написать программу вывода чисел 0; -100; 5.6; -3 в виде столбца:
#	0
#	-100
#	5.6
#	-3
#    в котором все строки выровнены по правому краю (подсказка: воспользуйтесь методом rjust)

numStr = " 1; -100; 2; -200"
dig2 = numStr.split(";")
for z in dig2:
    dig3 = z.rjust(5)
    print(z.rjust(5))
   #print("Программа вывода чисел 0; -100; 5.6; -3 в виде столбца: ", dig3)
    

st = "3; -300; 4; -400"
st = st.split(";")
for x in st:
 print(x.rjust(5))

num = '5; -500; 6; -600'.split(';')
for i in num:
    print(i.rjust(5))


