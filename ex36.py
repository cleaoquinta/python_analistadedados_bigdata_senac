#t += i significa: t recebe a soma de t (ele mesmo) + i.
#for é um somatório (?)
#Range de (1,50) pega do número 1 até o 10.
t=0
for i in range(1,50):
    t += i
if t % 2 == 0:
    print(f"{t} é par!")
else:
    print(f"{t} é impar!")