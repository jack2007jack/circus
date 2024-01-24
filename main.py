# Specifikācija
# - 1pt Spelētāji sāk no lauciņa nr. 1, vispār 100 lauciņu. Ir divi spēlētāji. Vinē tas kurš pirmais sasniedz pēdējo lauciņu
# - 1pt Maksimāli - 25 raundi, ja beidzas raundi - neizšķirts
# - 1pt Viens pēc otra met kauliņu (ar nejauša ciparu ģenerātora palidzību) un iet uz priekšu
# - 1pt Ja trāpa uz lauciņu ar kāpnem:
# -- zilas kāpnes ved uz leju, 18 -> 7, 67 -> 46 , 80 -> 69, 74 -> 63
# -- sarkanas kāpnes ved uz augšu, 15 -> 24, 39 -> 48, 33 -> 52, 87 -> 96 
# - 1pt Katrā raundā tik drukāta informācija kur atrodas spēlētājs, dators un vai ir uzkāpts uz kāpnem

# Koda vertēšanas kritēriji
# - 1pt Kodā izmanto mainīgus, ciklus (for vai while), zarošanu (if)
# - 1pt Kods strādā bez kļūdam
# - 1pt Mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# - 1pt Kodam ir jēdzīgi komentāri, pirms "if, for" koda konstrukcijam
# - 1pt Izmaiņas saglabātas versiju vadības sistēmā Git

# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Nejauša skaitļa generēšana - https://www.w3schools.com/python/ref_random_randint.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git

from random import randint

lauciņa2 = 1

lauciņa1 = 1

while True: 

    if lauciņa1 >= 100:
        print(f"spelētājs 1 won with: {lauciņa1}")
        break
    elif int(lauciņa2) >= 100:
        print(f"spelētājs 2 won with: {lauciņa2}")
        break
    kauliņu1 = [randint(1, 6) for i in range(1)]
    
    lauciņa1 += sum(kauliņu1)
    
    print('spelētājs 1',kauliņu1, lauciņa1)
    
    kauliņu2 = [randint(1, 6) for i in range(1)]
    
    lauciņa2 += sum(kauliņu2)
    
    print('spelētājs 2',kauliņu2, lauciņa2) 
 
    if lauciņa1 == 18:
        lauciņa1=lauciņa1 - 11 and print("zilas kāpnes18.1")
    if lauciņa2 == 18:
        lauciņa2=lauciņa2 - 11 and print("zilas kāpnes18.2")

    if lauciņa1 == 67:
        lauciņa1=lauciņa1 - 21 and print("zilas kāpnes67.1")
    if lauciņa2 == 67:
        lauciņa2=lauciņa2 - 21 and print("zilas kāpnes67.2")
