# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

n = int(input("Введите длинну шоколадки ->"))
m = int(input("Введите ширину шоколадки ->"))
k = int(input("Введите количество долек ->"))

if k > n or k == 0:
    print("Стольок долек нет :С")
    exit()
if k % n == 0 or k % m == 0:
     print("yes")
else:
    print("no")