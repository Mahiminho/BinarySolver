class module_task5:
    def task5(num):
        # ПЕРЕД ТИМ, ЯК НАДСИЛАТИ ЧИСЛА БОТУ, ТРЕБА ПРИБРАТИ ПРОБІЛИ БІЛЯ МІНУСА І ПЛЮСА (В СУМІ 4 ПРОБІЛА), ЩОБ ПРОБІЛ БУВ ЛИШЕ МІЖ ДВОМА ВИРАЗАМИ
        print("Тема: 5. У ПОДАНИХ АРИФМЕТИЧНИХ ВИРАЗАХ ДЕСЯТКОВІ ЧИСЛА БЕЗ ЗНАКІВ ПЕРЕТВОРІТЬ У ЇХ ДВІЙКОВІ ЕКВІВАЛЕНТИ І ВИКОНАЙТЕ ВІДПОВІДНІ ОПЕРАЦІЇ. ВИКОНАЙТЕ ПЕРЕВІРКУ ОТРИМАНИХ РЕЗУЛЬТАТІВ")
        print("\nПОПЕРЕДЖЕННЯ: Увага! У квадратних дужках позначається система числення! Не переписуйте квадратних дужок, просто система числення пишеться меншими цифрами!\n")
        nums = num.split(" ")
        a = nums[0]
        b = nums[1]




        # ДЛЯ ПЕРШОЇ ДІЇ
        # ДОДАВАННЯ
        print("1) Дія додавання " + a + ":")
        print("")
        a_divided = a.split("+") # розбиваю першу дію (додавання) на два числа
        a_first = int(a_divided[0]) # перше число
        a_second = int(a_divided[1]) # друге число

        for_user1 = [] # порожній масив де будуть числа ділені на 2, для виведення їх юзеру
        res1 = a_first % 2 # по модулю знаходжу останню цифру відповіді (тобто фінального двійкового першого числа першого виразу)
        res2 = a_first // 2 # ділю без остачі (для наступного ділення по модулю)
        for_user1.append(a_first) # додаю в масив число
        full_res1 = [] # створюю пустий масив з відповіддю (перевернутою)
        full_res1.append(str(res1)) # додаю останню цифру відповіді в масив
        while res2 >= 1: # повторюю дії до кінця
            for_user1.append(res2)
            res1 = res2 % 2
            res2 = res2 // 2
            full_res1.append(str(res1))

        for_user2 = [] # порожній масив де будуть числа ділені на 2, для виведення їх юзеру
        res3 = a_second % 2 # по модулю знаходжу останню цифру відповіді (тобто фінального двійкового другого числа першого виразу)
        res4 = a_second // 2 # ділю без остачі (для наступного ділення по модулю)
        for_user2.append(a_second) # додаю в масив число
        full_res2 = [] # створюю пустий масив з відповіддю (перевернутою)
        full_res2.append(str(res3)) # додаю останню цифру відповіді в масив
        while res4 >= 1: # повторюю дії до кінця
            for_user2.append(res4)
            res3 = res4 % 2
            res4 = res4 // 2
            full_res2.append(str(res3))

        i = 0
        while i < len(for_user1):  # створення виразів для користувача, які він записуватиме (з першим числом першого виразу)
            mid = "(" + str(full_res1[i]) + ")"
            print(str(for_user1[i]), ": 2 =", for_user1[i] // 2, mid)
            i += 1

        print("")

        full_res1.reverse() # перевертаю масив, щоб числа для відповіді були в правильному порядку
        full_res1 = ''.join(full_res1) # зробив з масива строку

        final = str(a_first) + "[10] = " + str(full_res1) + "[2]" # формую фінальну строку з відповіддю переведення
        print(final)
        print("")

        i = 0
        while i < len(for_user2):  # створення виразів для користувача, які він записуватиме (з другим числом першого виразу)
            mid = "(" + str(full_res2[i]) + ")"
            print(str(for_user2[i]), ": 2 =", for_user2[i] // 2, mid)
            i += 1

        print("")

        full_res2.reverse() # перевертаю масив, щоб числа для відповіді були в правильному порядку
        full_res2 = ''.join(full_res2) # зробив з масива строку

        final = str(a_second) + "[10] = " + str(full_res2) + "[2]" # формую фінальну строку з відповіддю переведення
        print(final)
        print("")

        summa = int(full_res1, 2) + int(full_res2, 2) # результат (десятковий) додавання двох двійкових чисел  (після коми стоїть система числення)
        res_bin = bin(summa)[2:] # переведення цього результату в двійкову систему

        # ВИВІД ВИРАЗУ ДОДАВАННЯ ДВІЙКОВИХ ЧИСЕЛ В СТОВПЧИК
        defin1 = len(res_bin) - len(full_res1)
        defin2 = len(res_bin) - len(full_res2)
        print(" " + " " * defin1 + full_res1)
        print("+")
        print(" " + " " * defin2 + full_res2)
        print(" __________")
        print(" " + res_bin)
        print("")

        # ПЕРЕВЕДЕННЯ НАЗАД В ДЕСЯТКОВУ СИСТЕМУ, ЩОБ ПЕРЕВІРИТИ ПРАВИЛЬНІСТЬ ВИКОНАННЯ ДОДАВАННЯ
        res_bin1 = res_bin # присвоюю значення двійкового результату іншій змінній
        res_bin1 = list(str(res_bin1)) # роблю масив (з цифр в виді рядків) з двійкового результату

        res_bin1 = [int(item) for item in res_bin1]  # переводжу масив двійкового результату в цифри з рядків
        res_bin1.reverse()  # перевернув список цифр результату, щоб виконати дії у правильному порядку

        # РАХУЮ СУМУ РЕЗУЛЬТАТУ (В ДЕСЯТКОВІЙ)
        res1 = 0
        i = 0
        while i < len(res_bin1):
            res1 += res_bin1[i] * 2 ** i
            i += 1

        res_bin1.reverse()  # ще раз перевернув список цифр результату, щоб записати в строку в правильному порядку
        str_full_res = ""

        # СТВОРЕННЯ ВИРАЗУ-ПЕРЕВЕДЕННЯ В ДЕСЯТКОВУ З ДВІЙКОВОЇ
        i = 0
        l = len(res_bin1) - 1
        while i < len(res_bin1):
            mid = str(res_bin1[i]) + "*2^" + "(" + str(l) + ")" + " + "
            str_full_res += mid
            i += 1
            l -= 1

        # ДОВЕРШЕННЯ ВИРАЗУ
        str_full_res = str_full_res[:-1]
        str_full_res = str_full_res[:-1]
        str_full_res = str(res_bin) + "[2] = " + str_full_res + "= " + str(res1) + "[10]"

        print(str_full_res)
        print("")





        # ДЛЯ ДРУГОЇ ДІЇ
        # ВІДНІМАННЯ
        print("2) Дія віднімання " + b + ":")
        print("")
        b_divided = b.split("–") # розбиваю другу дію (віднімання) на два числа
        b_first = int(b_divided[0]) # перше число
        b_second = int(b_divided[1]) # друге число

        for_user1 = [] # порожній масив де будуть числа ділені на 2, для виведення їх юзеру
        res1 = b_first % 2 # по модулю знаходжу останню цифру відповіді (тобто фінального двійкового першого числа першого виразу)
        res2 = b_first // 2 # ділю без остачі (для наступного ділення по модулю)
        for_user1.append(b_first) # додаю в масив число
        full_res1 = [] # створюю пустий масив з відповіддю (перевернутою)
        full_res1.append(str(res1)) # додаю останню цифру відповіді в масив
        while res2 >= 1: # повторюю дії до кінця
            for_user1.append(res2)
            res1 = res2 % 2
            res2 = res2 // 2
            full_res1.append(str(res1))

        for_user2 = [] # порожній масив де будуть числа ділені на 2, для виведення їх юзеру
        res3 = b_second % 2 # по модулю знаходжу останню цифру відповіді (тобто фінального двійкового другого числа першого виразу)
        res4 = b_second // 2 # ділю без остачі (для наступного ділення по модулю)
        for_user2.append(b_second) # додаю в масив число
        full_res2 = [] # створюю пустий масив з відповіддю (перевернутою)
        full_res2.append(str(res3)) # додаю останню цифру відповіді в масив
        while res4 >= 1: # повторюю дії до кінця
            for_user2.append(res4)
            res3 = res4 % 2
            res4 = res4 // 2
            full_res2.append(str(res3))

        i = 0
        while i < len(for_user1):  # створення виразів для користувача, які він записуватиме (з першим числом першого виразу)
            mid = "(" + str(full_res1[i]) + ")"
            print(str(for_user1[i]), ": 2 =", for_user1[i] // 2, mid)
            i += 1

        print("")

        full_res1.reverse() # перевертаю масив, щоб числа для відповіді були в правильному порядку
        full_res1 = ''.join(full_res1) # зробив з масива строку

        final = str(b_first) + "[10] = " + str(full_res1) + "[2]" # формую фінальну строку з відповіддю переведення
        print(final)
        print("")

        i = 0
        while i < len(for_user2):  # створення виразів для користувача, які він записуватиме (з другим числом першого виразу)
            mid = "(" + str(full_res2[i]) + ")"
            print(str(for_user2[i]), ": 2 =", for_user2[i] // 2, mid)
            i += 1

        print("")

        full_res2.reverse() # перевертаю масив, щоб числа для відповіді були в правильному порядку
        full_res2 = ''.join(full_res2) # зробив з масива строку

        final = str(b_second) + "[10] = " + str(full_res2) + "[2]" # формую фінальну строку з відповіддю переведення
        print(final)
        print("")

        # ОБЕРТАЮ ДРУГЕ ЧИСЛО
        full_res2a = full_res2 # присвоюю значення другого числа в двійковій формі іншій змінній, щоб не змінити значення full_res2
        full_res2a = list(full_res2a) # масив зі строки
        i = 0
        while i < len(full_res2a): # обертання (всі одиниці заміняю нулями і навпаки)
            if full_res2a[i] == '1':
                full_res2a[i] = '0'
            else:
                full_res2a[i] = '1'
            i += 1

        i = 0
        while full_res2a[i] == '0': # видаляю усі лишні нулі спочатку нового числа
            full_res2a.pop(i)
            i += 1
        full_res2b = ''.join(full_res2a) # складаю число докупи

        sum = int(full_res2b, 2) + int('1', 2) # додаю 1, щоб з оберненого числа вийшло інвертоване
        full_res2c = bin(sum)[2:]

        if len(full_res2) > len(full_res2c):
            v = len(full_res2) - len(full_res2c)
            full_res2c = v * "0" + full_res2c

        x = max(len(full_res2a), len(full_res2b), len(full_res2c)) # шукаю найдовшу строку-число, щоб знати, які відступи робити для інших чисел

        # ВИВІД ВИРАЗУ ІНВЕРТУВАННЯ
        print("Інвертація другого числа:")
        defin3 = x - len(full_res2)
        print(" " * defin3 + full_res2)
        print("________")
        defin4 = x - len(full_res2b)
        print(" " * defin4 + full_res2b)
        defin5 = x - 1
        print(" " * defin5 + "1")
        print("________")
        defin6 = x - len(full_res2c)
        print(" " * defin6 + full_res2c)
        print("")

        # ВИВІД ВИРАЗУ ДОДАВАННЯ
        print("Додавання до першого числа другого (інвертованого):")

        if len(full_res2c) < len(full_res1):
            p = len(full_res1) - len(full_res2c)
            full_res2c = p * "1" + full_res2c

        print(" 0," + full_res1)
        print("+")
        print(" 1," + full_res2c)
        print("_____________")

        summa = int(full_res1, 2) + int(full_res2c, 2) # результат (десятковий) додавання двох двійкових чисел  (після коми стоїть система числення)
        res_bin = bin(summa)[2:] # переведення цього результату в двійкову систему

        res_bin = res_bin[2:]
        res_bin = list(res_bin)
        if res_bin[0] == "1" and res_bin[1] == "0": # якщо перші два числа результату додавання (у двійковій системі) - це 1 і 0, то забираю їх, щоб дізнатись число результат
            res_bin.pop(0)
            res_bin.pop(1)
        else: # ІНАКШЕ ПІЗДЄЦ (програма розрахована на те, що число вийде додатнім)
            pass
        res_bin = ''.join(res_bin)

        if len(res_bin) < len(full_res1):
            t = len(full_res1) - len(res_bin)
            res_bin = "0" * t + res_bin

        print(" 0," + res_bin) # вивід результату
        print("")

        # ПЕРЕВЕДЕННЯ НАЗАД В ДЕСЯТКОВУ СИСТЕМУ, ЩОБ ПЕРЕВІРИТИ ПРАВИЛЬНІСТЬ ВИКОНАННЯ ДОДАВАННЯ
        res_bin1 = res_bin # присвоюю значення двійкового результату іншій змінній
        res_bin1 = list(str(res_bin1)) # роблю масив (з цифр в виді рядків) з двійкового результату

        res_bin1 = [int(item) for item in res_bin1]  # переводжу масив двійкового результату в цифри з рядків
        res_bin1.reverse()  # перевернув список цифр результату, щоб виконати дії у правильному порядку

        # РАХУЮ СУМУ РЕЗУЛЬТАТУ (В ДЕСЯТКОВІЙ)
        res1 = 0
        i = 0
        while i < len(res_bin1):
            res1 += res_bin1[i] * 2 ** i
            i += 1

        res_bin1.reverse()  # ще раз перевернув список цифр результату, щоб записати в строку в правильному порядку
        str_full_res = ""

        # СТВОРЕННЯ ВИРАЗУ-ПЕРЕВЕДЕННЯ В ДЕСЯТКОВУ З ДВІЙКОВОЇ
        i = 0
        l = len(res_bin1) - 1
        while i < len(res_bin1):
            mid = str(res_bin1[i]) + "*2^" + "(" + str(l) + ")" + " + "
            str_full_res += mid
            i += 1
            l -= 1

        # ДОВЕРШЕННЯ ВИРАЗУ
        str_full_res = str_full_res[:-1]
        str_full_res = str_full_res[:-1]
        str_full_res = str(res_bin) + "[2] = " + str_full_res + "= " + str(res1) + "[10]"

        print(str_full_res + "\n\n\n")