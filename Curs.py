import random
print('='*80)
print("Тема: применение циклов\nАвтор: Кирилл Ломовской")
print('='*80)
print("***********ТРЕНИРУЕМ НАВЫКИ СЛОЖЕНИЯ, ВЫЧИТАНИЯ, УМНОЖЕНИЯ И ДЕЛЕНИЯ************")
print('-'*80)
print("\t\tЭтот тест, для проверки знаний на арифметические операции.\n\nТы можешь проверить себя, на задачах любой сложности.\nВыбрать любой диапазон значений или количество примеров.\nОднако результат никогда не будет отрицательным или дробным.\n\n\tПроверь себя! Брось вызов программе! И ты получишь свой результат!\n\nРезультат будет указан после завершения каждой операции и в конце по всем.\nРезультат представлен относительно всего количества вопросов и в процентах.")
print('-'*80)
i,j,x,y,z,inp,rightAnswer1,rightAnswer2,rightAnswer3,rightAnswer4,rez=0,0,0,0,0,0,0,0,0,0,0
percent1,percent2,percent3,percent4=0,0,0,0
ide1,ide2,ide3,ide4=False,False,False,False
settings = ''
oper = input("\t\t\tКакую операцию вы хотите тренировать: \n1 - Сложение \n2 - Умножение \n3 - Вычитание \n4 - Деление\n5 - Выход\n")
while not(oper == '1' or oper == '2' or oper == '3' or oper == '4' or oper == '5'):
    oper = input("\t\t\tКакую операцию вы хотите тренировать: \n1 - Сложение \n2 - Умножение \n3 - Вычитание \n4 - Деление\n5 - Выход\n")
oper = int(oper)
if oper != 5:
    coltry,span = 10,100
    print("\n\tПо умолчению тест содержит",coltry,"заданий с диапазоном чисел от 0 до",span)
    print('-'*80)
    settings = input("Хотите изменить настройки y/n ? ")
    settings = settings.lower()
    while not(settings == 'y' or settings == 'n'):
        settings = input("Хотите изменить настройки y/n ? ")
        settings = settings.lower()
    if settings == 'y':
        coltry = input("Сколько примеров подряд вы хотели бы получить - ")
        while (coltry.isdigit()==False):
            coltry = input("Сколько примеров подряд вы хотели бы получить - ")
        coltry = int(coltry)
        span = input("В каком диапазоне вы хотели бы получать числа: от 0 до ")
        while (span.isdigit()==False):
            span = input("В каком диапазоне вы хотели бы получать числа: от 0 до ")
        span = int(span)
    print('-'*80)
while oper != 5:
    if oper == 1:
        print("\n"+"*"*36+"CЛОЖЕНИЕ"+"*"*36)
        ide1 = True
        while i < coltry:
            x = random.randint(0,span) 
            y = random.randint(0,span)
            z = x + y
            print(x,"+",y,"=",end=" ")
            inp = input()
            while (inp.isdigit()==False):
                print(x,"+",y,"=",end=" ")
                inp = input()
            inp = int(inp)
            if inp == z:
                print("\t\t\t\tОтвет правильный!")
                rightAnswer1 += 1
            else:
                print("\t\t\tОтвет неверный, правильный ответ - ",int(z))
            i += 1
            print('-'*80)
        percent1 = rightAnswer1 /(coltry /100)
        print('\\'*80)
        print("\t\tКоличество правильных ответов",rightAnswer1,"из",coltry,"-",int(percent1),"%")
        print('\\'*80)
        i = 0
        rez = input("\n\t\t   Хотите улучшить свой результат y/n ? ")
        rez = rez.lower()
        while not(rez== 'y' or rez == 'n'):
            rez = input("\n\t\t   Хотите улучшить свой результат y/n ? ")
            rez = rez.lower()
        if rez == "y":
            rightAnswer1,coltry = 0, 0
            coltry,span = 10,100
            print("\t\nПо умолчению тест содержит",coltry,"заданий с диапазоном чисел от 0 до",span)
            print('-'*80)
            settings = input("Хотите изменить настройки y/n ? ")
            settings = settings.lower()
            while not(settings == 'y' or settings == 'n'):
                settings = input("Хотите изменить настройки y/n ? ")
                settings = settings.lower()
            if settings == 'y':
                coltry = input("Сколько примеров подряд вы хотели бы получить - ")
                while (coltry.isdigit()==False):
                    coltry = input("Сколько примеров подряд вы хотели бы получить - ")
                coltry = int(coltry)
                span = input("В каком диапазоне вы хотели бы получать числа: от 0 до ")
                while (span.isdigit()==False):
                    span = input("В каком диапазоне вы хотели бы получать числа: от 0 до ")
                span = int(span)
            print('-'*80)
        elif rez == "n":
            print('_'*80)
            oper = input("\n\t\t\tКакую операцию вы хотите тренировать: \n1 - Сложение \n2 - Умножение \n3 - Вычитание \n4 - Деление\n5 - Выход\n")
            while not(oper == '1' or oper == '2' or oper == '3' or oper == '4' or oper == '5'):
                oper = input("\t\t\tКакую операцию вы хотите тренировать: \n1 - Сложение \n2 - Умножение \n3 - Вычитание \n4 - Деление\n5 - Выход\n")
            oper = int(oper)
            if oper != 5:
                coltry,span = 10,100
                print("\tПо умолчению тест содержит",coltry,"заданий с диапазоном чисел от 0 до",span)
                print('-'*80)
                settings = input("Хотите изменить настройки y/n ? ")
                settings = settings.lower()
                while not(settings == 'y' or settings == 'n'):
                    settings = input("Хотите изменить настройки y/n ? ")
                    settings = settings.lower()
                if settings == 'y':
                    coltry = input("Сколько примеров подряд вы хотели бы получить - ")
                    while (coltry.isdigit()==False):
                        coltry = input("Сколько примеров подряд вы хотели бы получить - ")
                    coltry = int(coltry)
                    span = input("В каком диапазоне вы хотели бы получать числа: от 0 до ")
                    while (span.isdigit()==False):
                        span = input("В каком диапазоне вы хотели бы получать числа: от 0 до ")
                    span = int(span)
                print('-'*80)
    if oper == 2:
        print("\n"+"*"*35+"УМНОЖЕНИЕ"+"*"*36)
        ide2 = True
        while i < coltry:
            x = random.randint(0,span) 
            y = random.randint(0,span)
            z = x * y
            print(x,"*",y,"=",end=" ")
            inp = input()
            while (inp.isdigit()==False):
                print(x,"*",y,"=",end=" ")
                inp = input()
            inp = int(inp)
            if inp == z:
                print("\t\t\t\tОтвет правильный!")
                rightAnswer2 += 1
            else:
                print("\t\t\tОтвет неверный, правильный ответ - ",int(z))
            i += 1
            print('-'*80)
        percent2 = rightAnswer2 /(coltry /100)
        print('\\'*80)
        print("\t\tКоличество правильных ответов",rightAnswer2,"из",coltry,"-",int(percent2),"%")
        print('\\'*80)        
        i = 0
        rez = input("\n\t\t   Хотите улучшить свой результат y/n ? ")
        rez = rez.lower()
        while not(rez== 'y' or rez == 'n'):
            rez = input("\n\t\t   Хотите улучшить свой результат y/n ? ")
            rez = rez.lower()
        if rez == "y":
            rightAnswer2,coltry = 0, 0
            coltry,span = 10,100
            print("\t\nПо умолчению тест содержит",coltry,"заданий с диапазоном чисел от 0 до",span)
            print('-'*80)
            settings = input("Хотите изменить настройки y/n ? ")
            settings = settings.lower()
            while not(settings == 'y' or settings == 'n'):
                settings = input("Хотите изменить настройки y/n ? ")
                settings = settings.lower()
            if settings == 'y':
                coltry = input("Сколько примеров подряд вы хотели бы получить - ")
                while (coltry.isdigit()==False):
                    coltry = input("Сколько примеров подряд вы хотели бы получить - ")
                coltry = int(coltry)
                span = input("В каком диапазоне вы хотели бы получать числа: от 0 до ")
                while (span.isdigit()==False):
                    span = input("В каком диапазоне вы хотели бы получать числа: от 0 до ")
                span = int(span)
            print('-'*80)
        elif rez == "n":
            print('_'*80)
            oper = input("\n\t\t\tКакую операцию вы хотите тренировать: \n1 - Сложение \n2 - Умножение \n3 - Вычитание \n4 - Деление\n5 - Выход\n")
            while not(oper == '1' or oper == '2' or oper == '3' or oper == '4' or oper == '5'):
                oper = input("\t\t\tКакую операцию вы хотите тренировать: \n1 - Сложение \n2 - Умножение \n3 - Вычитание \n4 - Деление\n5 - Выход\n")
            oper = int(oper)
            if oper != 5:
                coltry,span = 10,100
                print("\tПо умолчению тест содержит",coltry,"заданий с диапазоном чисел от 0 до",span)
                print('-'*80)
                settings = input("Хотите изменить настройки y/n ? ")
                settings = settings.lower()
                while not(settings == 'y' or settings == 'n'):
                    settings = input("Хотите изменить настройки y/n ? ")
                    settings = settings.lower()
                if settings == 'y':
                    coltry = input("Сколько примеров подряд вы хотели бы получить - ")
                    while (coltry.isdigit()==False):
                        coltry = input("Сколько примеров подряд вы хотели бы получить - ")
                    coltry = int(coltry)
                    span = input("В каком диапазоне вы хотели бы получать числа: от 0 до ")
                    while (span.isdigit()==False):
                        span = input("В каком диапазоне вы хотели бы получать числа: от 0 до ")
                    span = int(span)
                print('-'*80)
    if oper == 3:
        print("\n"+"*"*35+"ВЫЧИТАНИЕ"+"*"*36)
        ide3 = True
        while i < coltry:
            x = random.randint(0,span) 
            y = random.randint(0,x)
            z = x - y
            print(x,"-",y,"=",end=" ")
            inp = input()
            while (inp.isdigit()==False):
                print(x,"-",y,"=",end=" ")
                inp = input()
            inp = int(inp)
            if inp == z:
                print("\t\t\t\tОтвет правильный!")
                rightAnswer3 += 1
            else:
                print("\t\t\tОтвет неверный, правильный ответ - ",int(z))
            i += 1
            print('-'*80)
        percent3 = rightAnswer3 /(coltry /100)
        print('\\'*80)
        print("\t\tКоличество правильных ответов",rightAnswer3,"из",coltry,"-",int(percent3),"%")
        print('\\'*80)        
        i = 0
        rez = input("\n\t\t   Хотите улучшить свой результат y/n ? ")
        rez = rez.lower()
        while not(rez== 'y' or rez == 'n'):
            rez = input("\n\t\t   Хотите улучшить свой результат y/n ? ")
            rez = rez.lower()
        if rez == "y":
            rightAnswer3,coltry = 0, 0
            coltry,span = 10,100
            print("\t\nПо умолчению тест содержит",coltry,"заданий с диапазоном чисел от 0 до",span)
            print('-'*80)
            settings = input("Хотите изменить настройки y/n ? ")
            settings = settings.lower()
            while not(settings == 'y' or settings == 'n'):
                settings = input("Хотите изменить настройки y/n ? ")
                settings = settings.lower()
            if settings == 'y':
                coltry = input("Сколько примеров подряд вы хотели бы получить - ")
                while (coltry.isdigit()==False):
                    coltry = input("Сколько примеров подряд вы хотели бы получить - ")
                coltry = int(coltry)
                span = input("В каком диапазоне вы хотели бы получать числа: от 0 до ")
                while (span.isdigit()==False):
                    span = input("В каком диапазоне вы хотели бы получать числа: от 0 до ")
                span = int(span)
            print('-'*80)
        elif rez == "n":
            print('_'*80)
            oper = input("\n\t\t\tКакую операцию вы хотите тренировать: \n1 - Сложение \n2 - Умножение \n3 - Вычитание \n4 - Деление\n5 - Выход\n")
            while not(oper == '1' or oper == '2' or oper == '3' or oper == '4' or oper == '5'):
                oper = input("\t\t\tКакую операцию вы хотите тренировать: \n1 - Сложение \n2 - Умножение \n3 - Вычитание \n4 - Деление\n5 - Выход\n")
            oper = int(oper)
            if oper != 5:
                coltry,span = 10,100
                print("\tПо умолчению тест содержит",coltry,"заданий с диапазоном чисел от 0 до",span)
                print('-'*80)
                settings = input("Хотите изменить настройки y/n ? ")
                settings = settings.lower()
                while not(settings == 'y' or settings == 'n'):
                    settings = input("Хотите изменить настройки y/n ? ")
                    settings = settings.lower()
                if settings == 'y':
                    coltry = input("Сколько примеров подряд вы хотели бы получить - ")
                    while (coltry.isdigit()==False):
                        coltry = input("Сколько примеров подряд вы хотели бы получить - ")
                    coltry = int(coltry)
                    span = input("В каком диапазоне вы хотели бы получать числа: от 0 до ")
                    while (span.isdigit()==False):
                        span = input("В каком диапазоне вы хотели бы получать числа: от 0 до ")
                    span = int(span)
                print('-'*80)
    if oper == 4:
        print("\n"+"*"*36+"ДЕЛЕНИЕ"+"*"*37)
        ide4 = True
        while i < coltry:
            x = random.randint(0,span) 
            y = random.randint(1,x+1)
            z = x / y
            while (z != int(z)):
                x = random.randint(0,span) 
                y = random.randint(1,x+1)
                z = x / y
            print(x,"/",y,"=",end=" ")
            inp = input()
            while (inp.isdigit()==False):
                print(x,"-",y,"=",end=" ")
                inp = input()
            inp = int(inp)
            if inp == z:
                print("\t\t\t\tОтвет правильный!")
                rightAnswer4 += 1
            else:
                print("\t\t\tОтвет неверный, правильный ответ - ",int(z))
            i += 1
            print('-'*80)
        percent4 = rightAnswer4 /(coltry /100)
        print('\\'*80)
        print("\t\tКоличество правильных ответов",rightAnswer4,"из",coltry,"-",int(percent4),"%")
        print('\\'*80)
        i = 0
        rez = input("\n\t\t   Хотите улучшить свой результат y/n ? ")
        rez = rez.lower()
        while not(rez== 'y' or rez == 'n'):
            rez = input("\n\t\t   Хотите улучшить свой результат y/n ? ")
            rez = rez.lower()
        if rez == "y":
            rightAnswer4,coltry = 0, 0
            coltry,span = 10,100
            print("\t\nПо умолчению тест содержит",coltry,"заданий с диапазоном чисел от 0 до",span)
            print('-'*80)
            settings = input("Хотите изменить настройки y/n ? ")
            settings = settings.lower()
            while not(settings == 'y' or settings == 'n'):
                settings = input("Хотите изменить настройки y/n ? ")
                settings = settings.lower()
            if settings == 'y':
                coltry = input("Сколько примеров подряд вы хотели бы получить - ")
                while (coltry.isdigit()==False):
                    coltry = input("Сколько примеров подряд вы хотели бы получить - ")
                coltry = int(coltry)
                span = input("В каком диапазоне вы хотели бы получать числа: от 0 до ")
                while (span.isdigit()==False):
                    span = input("В каком диапазоне вы хотели бы получать числа: от 0 до ")
                span = int(span)
            print('-'*80)
        elif rez == "n":
            print('_'*80)
            oper = input("\n\t\t\tКакую операцию вы хотите тренировать: \n1 - Сложение \n2 - Умножение \n3 - Вычитание \n4 - Деление\n5 - Выход\n")
            while not(oper == '1' or oper == '2' or oper == '3' or oper == '4' or oper == '5'):
                oper = input("\t\t\tКакую операцию вы хотите тренировать: \n1 - Сложение \n2 - Умножение \n3 - Вычитание \n4 - Деление\n5 - Выход\n")
            oper = int(oper)
            if oper != 5:
                coltry,span = 10,100
                print("\tПо умолчению тест содержит",coltry,"заданий с диапазоном чисел от 0 до",span)
                print('-'*80)
                settings = input("Хотите изменить настройки y/n ? ")
                settings = settings.lower()
                while not(settings == 'y' or settings == 'n'):
                    settings = input("Хотите изменить настройки y/n ? ")
                    settings = settings.lower()
                if settings == 'y':
                    coltry = input("Сколько примеров подряд вы хотели бы получить - ")
                    while (coltry.isdigit()==False):
                        coltry = input("Сколько примеров подряд вы хотели бы получить - ")
                    coltry = int(coltry)
                    span = input("В каком диапазоне вы хотели бы получать числа: от 0 до ")
                    while (span.isdigit()==False):
                        span = input("В каком диапазоне вы хотели бы получать числа: от 0 до ")
                    span = int(span)
                print('-'*80)
if (ide1 == True or ide2 == True or ide3 == True or ide4 == True):
    print('/'*80)
    print("\t\tКоличество правильных ответов по всем операциям: \n")
    if ide1 == True:
        print("\tКоличество правильных ответов по сложению - ",rightAnswer1,"из",coltry,"-",int(percent1),"%")
    if ide2 == True:
        print("\tКоличество правильных ответов по умножению - ",rightAnswer2,"из",coltry,"-",int(percent2),"%")
    if ide3 == True:
        print("\tКоличество правильных ответов по вычитанию - ",rightAnswer3,"из",coltry,"-",int(percent3),"%")
    if ide4 == True:
        print("\tКоличество правильных ответов по делению - ",rightAnswer4,"из",coltry,"-",int(percent4),"%")
    print('/'*80)
print("\n********************************КОНЕЦ ПРОГРАММЫ*********************************")
input("\n\t\t    Для завершения нажмите Enter")
