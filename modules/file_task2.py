class module_task2:
    def task2(num):
        print("Тема: 2. ВИЗНАЧИТИ ДЕСЯТКОВІ ЗНАЧЕННЯ ЗАДАНИХ ЧИСЕЛ:")
        print("\nПОПЕРЕДЖЕННЯ: Увага! У квадратних дужках позначається система числення! Не переписуйте квадратних дужок, просто система числення пишеться меншими цифрами!")
        print("ПОЯСНЕННЯ: Щоб перевести число з будь-якої системи числення у десяткову, потрібно 'вагу' кожного розряду помножити на номер цього розряду.\n")
        nums = num.split(" ")
        a = nums[0]
        b = nums[1]
        c = nums[2]



        # ДЛЯ ПЕРШОГО ЧИСЛА
        a_divided = a.split(",") # розбиваю перше число з основою вісім на дві частини: цілу (до коми) і дробову (після коми)
        a_before_coma = list(a_divided[0]) # роблю масив з цілого числа
        a_after_coma = list(a_divided[1]) # роблю масив з дробового числа

        a_before_coma = [int(item) for item in a_before_coma] # переводжу масив з чисел до коми в числа з рядків
        a_after_coma = [int(item) for item in a_after_coma] # переводжу масив з чисел після коми в числа з рядків
        a_before_coma.reverse() # перевернув список чисел до коми, щоб виконати дії у правильному порядку

        # розрахунок суми до коми
        res1 = 0
        i = 0
        while i < len(a_before_coma):
            res1 += a_before_coma[i] * 8 ** i
            i += 1

        # розрахунок суми після коми
        res2 = 0
        i = 0
        p = -1
        while i < len(a_after_coma):
            res2 += a_after_coma[i] * 8 ** p
            i += 1
            p -= 1

        # розрахунок повної суми
        full_res = res1 + res2

        a_before_coma.reverse()  # реверс списоку чисел до коми, щоб записати в строку в правильному порядку
        str_full_res = ""

        # створення першої частини виразу (ДО КОМИ)
        i = 0
        l = len(a_before_coma) - 1
        while i < len(a_before_coma):
            mid = str(a_before_coma[i]) + "*8^" + "(" + str(l) + ")" + " + "
            str_full_res += mid
            i += 1
            l -= 1

        # створення другої частини виразу (ПІСЛЯ КОМИ)
        s = -1
        i = 0
        while i < len(a_after_coma):
            mid = str(a_after_coma[i]) + "*8^" + "(" + str(s) + ")" + " + "
            str_full_res += mid
            i += 1
            s -= 1

        # довершення виразу
        str_full_res = str_full_res[:-1]
        str_full_res = str_full_res[:-1]
        str_full_res = a + "[8] = " + str_full_res + "= " + str(full_res) + "[10]"

        print(str_full_res, "\n")





        # ДЛЯ ДРУГОГО ЧИСЛА
        b_divided = b.split(",")  # розбиття другого числа з основою п`ять на дві частини: цілу (до коми) і дробову (після коми)
        b_before_coma = list(b_divided[0])  # створення масиву з цілого числа
        b_after_coma = list(b_divided[1])  # створення масиву з дробового числа

        b_before_coma = [int(item) for item in b_before_coma]  # переведення масиву з чисел до коми в числа з рядків
        b_after_coma = [int(item) for item in b_after_coma]  # переводення масиву з чисел після коми в числа з рядків
        b_before_coma.reverse()  # реверс списоку чисел до коми, щоб виконати дії у правильному порядку

        # сума до коми
        res1 = 0
        i = 0
        while i < len(b_before_coma):
            res1 += b_before_coma[i] * 5 ** i
            i += 1

        # сума після коми
        res2 = 0
        i = 0
        p = -1
        while i < len(b_after_coma):
            res2 += b_after_coma[i] * 5 ** p
            i += 1
            p -= 1

        # повна сума
        full_res = res1 + res2

        b_before_coma.reverse()  # реверс списоку чисел до коми, щоб записати в строку в правильному порядку
        str_full_res = ""

        # створення першої частини виразу (ДО КОМИ)
        i = 0
        l = len(b_before_coma) - 1
        while i < len(b_before_coma):
            mid = str(b_before_coma[i]) + "*5^" + "(" + str(l) + ")" + " + "
            str_full_res += mid
            i += 1
            l -= 1

        # створення другої частини виразу (ПІСЛЯ КОМИ)
        s = -1
        i = 0
        while i < len(b_after_coma):
            mid = str(b_after_coma[i]) + "*5^" + "(" + str(s) + ")" + " + "
            str_full_res += mid
            i += 1
            s -= 1

        # довершення вриазу
        str_full_res = str_full_res[:-1]
        str_full_res = str_full_res[:-1]
        str_full_res = b + "[5] = " + str_full_res + "= " + str(full_res) + "[10]"

        print(str_full_res, "\n")





        # ДЛЯ ТРЕТЬОГО ЧИСЛА
        c_divided = c.split(",")  # розбиття третього числа з основою два на дві частини: цілу (до коми) і дробову (після коми)
        c_before_coma = list(c_divided[0])  # створення масиву з цілого числа
        c_after_coma = list(c_divided[1])  # створення масиву з дробового числа

        c_before_coma = [int(item) for item in c_before_coma]  # переведення масиву з чисел до коми в числа з рядків
        c_after_coma = [int(item) for item in c_after_coma]  # переведення масиву з чисел після коми в числа з рядків
        c_before_coma.reverse()  # реверс списоку чисел до коми, щоб виконати дії у правильному порядку

        # сума до коми
        res1 = 0
        i = 0
        while i < len(c_before_coma):
            res1 += c_before_coma[i] * 2 ** i
            i += 1

        # сума після коми
        res2 = 0
        i = 0
        p = -1
        while i < len(c_after_coma):
            res2 += c_after_coma[i] * 5 ** p
            i += 1
            p -= 1

        # повна сума
        full_res = res1 + res2

        c_before_coma.reverse()  # реверс списоку чисел до коми, щоб записати в строку в правильному порядку
        str_full_res = ""

        # створення першої частини виразу (ДО КОМИ)
        i = 0
        l = len(c_before_coma) - 1
        while i < len(c_before_coma):
            mid = str(c_before_coma[i]) + "*2^" + "(" + str(l) + ")" + " + "
            str_full_res += mid
            i += 1
            l -= 1

        # створення другої частини виразу (ПІСЛЯ КОМИ)
        s = -1
        i = 0
        while i < len(c_after_coma):
            mid = str(c_after_coma[i]) + "*2^" + "(" + str(s) + ")" + " + "
            str_full_res += mid
            i += 1
            s -= 1

        # довершення виразу
        str_full_res = str_full_res[:-1]
        str_full_res = str_full_res[:-1]
        str_full_res = c + "[2] = " + str_full_res + "= " + str(full_res) + "[10]"

        print(str_full_res + "\n\n\n")