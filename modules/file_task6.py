class module_task6:
    def task6(num):
        print("Тема: 6. ПЕРЕТВОРІТЬ ПОСЛІДОВНО ЗА ВКАЗАНОЮ СХЕМОЮ ДЕСЯТКОВЕ ЧИСЛО З ОДНІЄЇ СИСТЕМИ ЧИСЛЕННЯ ДО ІНШОЇ З ТОЧНІСТЮ ДО d^(-4) (d –ОСНОВА СИСТЕМИ ЧИСЛЕННЯ).")
        print("\nПОПЕРЕДЖЕННЯ: Увага! У квадратних дужках позначається система числення! Не переписуйте квадратних дужок, просто система числення пишеться меншими цифрами!\n")
        b = num

        # ДЛЯ ПЕРШОГО ПЕРЕВЕДЕННЯ
        # ДЛЯ ПЕРЕВЕДЕННЯ В ВІСІМКОВУ СИСТЕМУ ЧИСЛЕННЯ
        print("1) Переведення числа з десяткової системи числення у вісімкову:\n")
        b_divided = b.split(",") # розбиваю число з основою десять на дві частини: цілу (до коми) і дробову (після коми)
        b_before_coma = int(b_divided[0]) # роблю ціле число, з числа до коми
        b_after_coma = int(b_divided[1]) # роблю ціле число з числа після коми

        for_user1 = [] # порожній масив де будуть числа ділені на 8, для виведення їх юзеру
        res1 = b_before_coma % 8 # по модулю знаходжу останню цифру відповіді (тобто фінального вісімкового числа до коми)
        res2 = b_before_coma // 8 # ділю без остачі (для наступного ділення по модулю)
        for_user1.append(b_before_coma) # додаю в масив число
        full_res1 = [] # створюю пустий масив з відповіддю (перевернутою)
        full_res1.append(str(res1)) # додаю останню цифру відповіді в масив
        while res2 >= 1: # повторюю дії до кінця
            for_user1.append(res2)
            res1 = res2 % 8
            res2 = res2 // 8
            full_res1.append(str(res1))

        half_res = "0." + str(b_after_coma) # роблю дробове число після коми строкою
        half_res = float(half_res) # переводжу його в НЕ цілочисельний формат

        for_user2 = [] # порожній масив де будуть числа множені на 8, для виведення їх юзеру
        for_user2.append(round(half_res, 3)) # заокруглення (до трьох знаків після коми) чисел, множених на 8 і додання їх в масив
        i = 0
        full_res2 = [] # створюю масив для відповіді
        res3 = half_res * 8 # виконую першу дію множення

        if res3 >= 1: # і першу перевірку: якщо число більше рівне за 1, то:
            res_half = str(res3) # переводжу його в строку
            res_half = res_half.split(".") # розбиваю по крапці на дві частини: до і після крапки
            first = int(res_half[0]) # першу частину (до крапки (тобто цілу)) переводжу в цілочисельний формат
            res3 -= first # віднімаю від основного так би мовити числа (яке множиться) цілу частину
            full_res2.append(str(first)) # додаю в масив строкою
        else: # протилежний варіант першої перевірки
            full_res2.append('0')

        while i < 3: # продовжую перевірки, заповнюючи масив числами
            for_user2.append(round(res3, 3))
            res3 = res3 * 8

            if res3 >= 1:
                res_half = str(res3)
                res_half = res_half.split(".")
                first = int(res_half[0])
                res3 -= first
                full_res2.append(str(first))
            else:
                full_res2.append('0')
            i += 1

        i = 0
        while i < len(for_user1): # створення виразів для користувача, які він записуватиме (з числом до коми)
            mid = "(" + str(full_res1[i]) + ")"
            print(str(for_user1[i]), ": 8 =", for_user1[i] // 8, mid)
            i += 1

        print("")

        i = 0
        while i < len(for_user2): # створення виразів для користувача, які він записуватиме (з числом після коми)
            res = for_user2[i] * 8

            if res >= 1:
                res_half = str(res)
                res_half = res_half.split(".")
                first = int(res_half[0])
                res -= first
            else:
                pass

            mid = str(for_user2[i]) + " * 8 = " + str(round(res, 3)) + " (" + str(full_res2[i]) + ")"
            print(mid)
            i += 1

        print("")

        full_res1.reverse() # перевертаю масив, щоб числа для відповіді були в правильному порядку
        full_res1 = ''.join(full_res1) # зробив з масива строку до коми
        full_res2 = ''.join(full_res2) # зробив з масива строку після коми
        full_res = full_res1 + "," + full_res2 # формую фінальне число результат

        final = b + "[10] = " + str(full_res) + "[8]" # формую фінальну строку з відповіддю переведення
        print(final)
        print("")





        # ДЛЯ ДРУГОГО ПЕРЕВЕДЕННЯ
        # ДЛЯ ПЕРЕВЕДЕННЯ В ДВІЙКОВУ СИСТЕМУ ЧИСЛЕННЯ
        print("2) Переведення числа з вісімкової системи числення у двійкову:\n")

        b = full_res
        bin_mass = {"0":"000", "1":"001", "2":"010", "3":"011", "4":"100", "5":"101", "6":"110", "7":"111"}

        b_divided = b.split(",") # розбиваю число з основою десять на дві частини: цілу (до коми) і дробову (після коми)
        b_before_coma = list(b_divided[0]) # роблю масив чисел (строкових) з числа до коми
        b_after_coma = list(b_divided[1]) # роблю масив чисел (строкових) з числа після коми
        b_before_coma1 = list(b_divided[0]) # роблю масив чисел (строкових) з числа до коми (щоб зробити з них двійкові)
        b_after_coma1 = list(b_divided[1]) # роблю масив чисел (строкових) з числа після коми (щоб зробити з них двійкові)

        # ПЕРЕВОДЖУ ЧИСЛА ДО КОМИ В ДВІЙКОВІ
        i = 0
        while i < len(b_before_coma):
            b_before_coma1[i] = bin_mass[b_before_coma[i]]
            i += 1

        # ПЕРЕВОДЖУ ЧИСЛА ПІСЛЯ КОМИ В ДВІЙКОВІ
        i = 0
        while i < len(b_after_coma):
            b_after_coma1[i] = bin_mass[b_after_coma[i]]
            i += 1

        # ВИВІД ПРОЦЕДУРИ ПЕРЕВЕДЕННЯ ДО КОМИ
        i = 0
        while i < len(b_before_coma):
            print(b_before_coma[i] + "[10] = " + b_before_coma1[i] + "[2]")
            i += 1
        print("")

        # ВИВІД ПРОЦЕДУРИ ПЕРЕВЕДЕННЯ ПІСЛЯ КОМИ
        i = 0
        while i < len(b_after_coma):
            print(b_after_coma[i] + "[10] = " + b_after_coma1[i] + "[2]")
            i += 1
        print("")

        # СКЛАДАЮ ПЕРЕВЕДЕНІ МАСИВИ ДОКУПИ
        b_before_coma1 = ''.join(b_before_coma1)
        b_after_coma1 = ''.join(b_after_coma1)

        # ТАК ЯК З ТОЧНІСТЮ ДО d^(-4) ТРЕБА ПЕРЕВЕСТИ, ТО ВИДАЛЯЮ ВСІ ЛИШНІ ЕЛЕМЕНТИ ПІСЛЯ КОМИ ПІСЛЯ ЧЕТВЕРТОГО
        b_after_coma2 = list(b_after_coma1)
        while len(b_after_coma2) > 4:
            b_after_coma2.pop(4)
        b_after_coma1 = ''.join(b_after_coma2)

        full_res = b_before_coma1 + "," + b_after_coma1 # результат в виді строки

        # РЕЗУЛЬТАТ ВИВОДУ РЕЗУЛЬТАТУ...
        print("Результат з точністю до d^(-4):")
        print(b + "[8] = " + full_res + "[2]") # результат дія
        print("")





        # ДЛЯ ТРЕТЬОГО ПЕРЕВЕДЕННЯ
        # ДЛЯ ПЕРЕВЕДЕННЯ В ШІСТНАДЦЯТКОВУ СИСТЕМУ ЧИСЛЕННЯ
        print("3) Переведення числа з двійкової системи числення у шістнадцяткову:\n")

        b = full_res
        bin_mass = {"0000":"0", "0001":"1", "0010":"2", "0011":"3", "0100":"4", "0101":"5", "0110":"6", "0111":"7", "1000":"8", "1001":"9", "1010":"A", "1011":"B", "1100":"C", "1101":"D", "1110":"E", "1111":"F"}

        b_divided = b.split(",") # розбиваю число з основою два на дві частини: цілу (до коми) і дробову (після коми)
        b_before_coma = b_divided[0] # частина до коми
        b_after_coma = b_divided[1] # частина після коми

        while len(b_before_coma) % 4 != 0: # якщо довжина числа не кратна 4, то додаємо наперід нулі, доки не буде кратна 4 (при цьому величина числа не змінюється)
            b_before_coma = "0" + b_before_coma

        print(b_before_coma + "," + b_after_coma) # вивід цього числа кратного 4
        print("")

        x = len(b_before_coma) / 4 # кількість тетрад у числі
        # СКЛАДНА ПРОЦЕДУРА РОЗБИТТЯ ДВІЙКОВОГО ЧИСЛА НА ТЕТРАДИ
        i = 0
        y1 = 0
        y2 = 4
        res_before_coma = []
        while i < x:
            p = b_before_coma[y1:y2]
            res_before_coma.append(p)
            i += 1
            y1 += 4
            y2 += 4

        # ПЕРЕВОДЖУ ВСІ ТЕТРАДИ З ДВІЙКОВИХ У ШІСТНАДЦЯТКОВІ СИМВОЛИ
        i = 0
        res_before_coma1 = []
        while i < len(res_before_coma):
            res_before_coma1.append(bin_mass[res_before_coma[i]])
            i += 1

        res_after_coma = bin_mass[b_after_coma] # переводжу одну двійкову тетраду після коми у шістнадцятковий символ

        # ВИВІД ПЕРЕВЕДЕННЯ ДВІЙКОВИХ ТЕТРАД У ШІСТНАДЦЯТКОВІ СИМВОЛИ
        i = 0
        while i < len(res_before_coma):
            print(res_before_coma[i] + "[2] = " + res_before_coma1[i] + "[16]")
            i += 1
        print("")
        print(b_after_coma + "[2] = " + res_after_coma + "[16]")
        print("")

        # СКЛАДАННЯ ЧИСЛА-РЕЗУЛЬТАТУ ДО КУПИ
        full_res1 = ''.join(res_before_coma1)
        full_res = full_res1 + "," + res_after_coma

        print(b + "[2] = " + full_res + "[16]")  # результат дія
        print("")





        # ДЛЯ ЧЕТВЕРТОГО ПЕРЕВЕДЕННЯ
        # ДЛЯ ПЕРЕВЕДЕННЯ В ДЕСЯТКОВУ СИСТЕМУ ЧИСЛЕННЯ
        print("4) Переведення числа з шістнадцяткової системи числення у десяткову:\n")

        b = full_res
        bin_mass = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "A":10, "B":11, "C":12, "D":13, "E":14, "F":15}

        b_divided = b.split(",") # розбиваю число з основою шістнадцять на дві частини: цілу (до коми) і дробову (після коми)
        b_before_coma = list(b_divided[0]) # частина до коми
        b_after_coma = b_divided[1] # частина після коми

        # РАХУЮ ДЕСЯТКОВЕ ЧИСЛО ДО КОМИ (ОБЕРТАЮ МАСИВ І ДОДАЮ ПРОМІЖНІ РЕЗУЛЬТАТИ (ЧИСЛА ПОМНОЖЕНІ НА 16 В ПЕВНОМУ СТЕПЕНІ))
        b_before_coma.reverse()
        i = 0
        res1 = 0
        while i < len(b_before_coma):
            res1 += bin_mass[b_before_coma[i]] * 16**i
            i += 1

        # РАХУЮ ТАКОЖ РЕЗУЛЬТАТ ПІСЛЯ КОМИ, ОКРУГЛЮЮЧИ ЙОГО ДО 4 ЗНАКИ ПІСЛЯ КОМИ. ДОДАЮ РЕЗУЛЬТАТ ДО І ПІСЛЯ КОМИ І ОТРИМУЮ ФІНАЛЬНИЙ РЕЗУЛЬТАТ
        res2 = bin_mass[b_after_coma] * 16**(-1)
        res2 = round(res2, 4)
        full_res = res1 + res2

        # ОБЕРТАЮ МАСИВ НАЗАД І СТВОРЮЮ СТРОКУ, ЯКУ ОТРИМАЄ КОРИСТУВАЧ (В ЦИКЛІ СТРОКА З СИМВОЛАМИ ДО КОМИ І ЩЕ ПОТІМ ЧАСТИНКА ПІСЛЯ КОМИ)
        b_before_coma.reverse()
        l = len(b_before_coma) - 1
        i = 0
        res_str = ""
        while i < len(b_before_coma):
            res_str += b_before_coma[i] + "*16^(" + str(l) + ") + "
            i += 1
            l -= 1
        res_str += b_after_coma + "*16^(-1) = " + str(full_res)

        # ВИВІД І ПОПЕРЕДЖЕННЯ
        print(res_str)
        print("")
        print("ПОЯСНЕННЯ: Результат подано з точністю до d^(-4). Результат не збігся повністю з початковим числом, бо в процесі переведень, ми подавали число з точністю до d^(-4).\n\n\n")