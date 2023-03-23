# Найдите сумму цифр трехзначного числа.

n = int(input("Введите трехзначное число -> "))
sum = 0
i = 0

if n > 99 and n < 1000:
    while n > 0:
        i = int(n % 10)
        sum = sum + i
        n = n / 10
else:
    print("Число не трёхзначиное")

print(sum)