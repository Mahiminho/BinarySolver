class module_task9:
    def task9(num):
        print("Тема: 9. ДОДАТИ У МОДИФІКОВАНОМУ ДОПОВНЯЛЬНОМУ КОДІ ДВІЙКОВІ ЧИСЛА У ФОРМАТІ З РУХОМОЮ КОМОЮ З ОСНОВОЮ d=2:")
        print("\nПОПЕРЕДЖЕННЯ: Увага! У цьому завданні у квадаратних дужках позначається, у якому коді подане число:\nпр - прямий;\nоб - обернений;\nдоп - доповняльний.\nКвадратних дужок переписувати не потрібно, просто вкажіть тип двійкового коду трохи меншими буквами.\n")
        bin_mass = {"0":0, "1":1, "10":2, "11":3, "100":4, "101":5, "110":6, "111":7}  # массив для переведення чисел з бінарних в прості
        ten_mass = {0:"0", 1:"1", 2:"10", 3:"11", 4:"100", 5:"101", 6:"110", 7:"111"}  # массив для переведення чисел з простих в бінарні
        num = num.split(" ") # розбиваю задану користувачем строку на дві частини
        a = num[0]
        b = num[1]

        a1 = a.split(",") # кожне число розбиваю по комі, і беру лише те, що після коми
        b1 = b.split(",")
        a1 = a1[1]
        b1 = b1[1]

        a1 = a1.split("*10") # тепер розбиваю по таким трьом символам, щоб розділити степінь і число
        b1 = b1.split("*10")
        a2 = a1[0] # число
        b2 = b1[0]
        a3 = a1[1] # степінь
        b3 = b1[1]

        print("Задані числа:")
        print("A = -0," + a2 + " * 10^(" + a3 + ")")
        print("B = -0," + b2 + " * 10^(" + b3 + ")")

        a4 = a3[1:] # величина степеня
        b4 = b3[1:]

        if a4[0] == "0": # якщо степінь записаний в умові так: 010, то прибираю перший нуль, бо інакше не знайду його десяткову величину в масиві
            a4 = a4[1:]
        if b4[0] == "0":
            b4 = b4[1:]

        if a3[0] == "+": # якщо степінь додатній у двійковому, то додатній і в десятковому, якщо від'ємний, то від'ємний
            a5 = bin_mass[a4]
        else:
            a5 = -1 * bin_mass[a4]

        if b3[0] == "+":
            b5 = bin_mass[b4]
        else:
            b5 = -1 * bin_mass[b4]



        if a5 > b5: # найважливіша частина: визначення більшого з двох степенів (тут перевіряю чи а більше b)
            dis = a5 - b5 # на скільки більший більший степінь
            new_b = "0" * dis + b2 # посуваю число, так би мовити, вправо

            print("ПОЯСНЕННЯ: Щоб зрозуміти, на скільки посунути число з меншим степенем вправо, треба знайти, на скільки його степінь менший за степінь другого числа.")

            print(" (" + a3 + ")") # виводжу вираз знаходження різниці степенів
            print("-")
            print(" (" + b3 + ")")
            print(" ______")
            print(" (+" + ten_mass[dis] + ")")
            print("")

            print("B = -0," + new_b + " * 10^(" + a3 + ")") # виводжу нову В
            print("")

            print("Переведення чисел в доповняльний код:")

            i = 0 # переведення в доповняльний код А
            a6 = []
            while i < len(a2):
                if a2[i] == "0":
                    a6.append("1")
                else:
                    a6.append("0")
                i += 1
            a6 = ''.join(a6)

            sum = int(a6, 2) + int("1", 2)
            a6 = bin(sum)[2:]

            if len(a6) < 6: # якщо результат вийшов довжино менше 6, то додаю наперід потрібну кількість нулів
                n = 6 - len(a6)
                a6 = "0" * n + a6



            i = 0 # переведення в доповняльний код В
            b6 = []
            while i < len(new_b):
                if new_b[i] == "0":
                    b6.append("1")
                else:
                    b6.append("0")
                i += 1
            b6 = ''.join(b6)

            sum = int(b6, 2) + int("1", 2)
            b6 = bin(sum)[2:]



            print("A[доп] = 11," + a6)
            print("B[доп] = 11," + b6)
            print("")



            a7 = "11" + a6 + "0" * dis # підготовка чисел для додавання
            b7 = "11" + b6
            sum = int(a7, 2) + int(b7, 2) # додавання
            result = bin(sum)[2:]

            result_aft_coma = result[:3] # розбиваю результат на знак і саме число
            result_bef_coma = result[3:]

            print("Додавання чисел у доповняльних кодах:")
            print("A[доп] + B[доп] = C[доп]")
            print("")
            print("  11," + a6)
            print("+")
            print("  11," + b6)
            print(" __________" + "_" * dis)
            print(" " + result_aft_coma + "," + result_bef_coma)
            print("")
            print("C[доп] = " + result_aft_coma + "," + result_bef_coma)
            print("")
            print("Переведення результату додавання у прямий код:")

            if result_aft_coma == "110": # якщо результат вийшов додатнім, то одразу виводжу, бо пр = доп
                new_res = result_bef_coma
                print("C[пр] = 11," + new_res)
            else: # якщо результат вийшов від'ємним
                i = 0
                new_res = []
                while i < len(result_bef_coma): # переводжу з доповняльного в прямий код
                    if result_bef_coma[i] == "0":
                        new_res.append("1")
                    else:
                        new_res.append("0")
                    i += 1
                new_res = ''.join(new_res)

                sum = int(new_res, 2) + int("1", 2)
                new_res = bin(sum)[2:]

                print("C[пр] = 11," + new_res) # а тоді виводжу

            print("Відповідь:")
            print("C = -0," + new_res + " * 10^(" + a3 + ")")



        else: # всі ті самі дії, що вище, але для протилежного випадку, тобто, якщо степінь В більший
            dis = b5 - a5
            new_a = "0" * dis + a2

            print("ПОЯСНЕННЯ: Щоб зрозуміти, на скільки посунути число з меншим степенем вправо, треба знайти, на скільки його степінь менший за степінь другого числа.")

            print(" (" + a3 + ")")
            print("-")
            print(" (" + b3 + ")")
            print(" ______")
            print(" (+" + ten_mass[dis] + ")")
            print("")

            print("А = -0," + new_a + " * 10^(" + b3 + ")")
            print("")

            print("Переведення чисел в доповняльний код:")

            i = 0
            b6 = []
            while i < len(b2):
                if b2[i] == "0":
                    b6.append("1")
                else:
                    b6.append("0")
                i += 1
            b6 = ''.join(b6)

            sum = int(b6, 2) + int("1", 2)
            b6 = bin(sum)[2:]

            if len(b6) < 6:
                n = 6 - len(b6)
                b6 = "0" * n + b6

            i = 0
            a6 = []
            while i < len(new_a):
                if new_a[i] == "0":
                    a6.append("1")
                else:
                    a6.append("0")
                i += 1
            a6 = ''.join(a6)

            sum = int(a6, 2) + int("1", 2)
            a6 = bin(sum)[2:]

            print("A[доп] = 11," + a6)
            print("B[доп] = 11," + b6)
            print("")

            b7 = "11" + b6 + "0" * dis
            a7 = "11" + a6
            sum = int(b7, 2) + int(a7, 2)
            result = bin(sum)[2:]

            result_aft_coma = result[:3]
            result_bef_coma = result[3:]

            print("Додавання чисел у доповняльних кодах:")
            print("A[доп] + B[доп] = C[доп]")
            print("")
            print("  11," + a6)
            print("+")
            print("  11," + b6)
            print(" __________" + "_" * dis)
            print(" " + result_aft_coma + "," + result_bef_coma)
            print("")
            print("C[доп] = " + result_aft_coma + "," + result_bef_coma)
            print("")
            print("Переведення результату додавання у прямий код:")

            if result_aft_coma == "110":
                new_res = result_bef_coma
                print("C[пр] = 11," + new_res)
            else:
                i = 0
                new_res = []
                while i < len(result_bef_coma):
                    if result_bef_coma[i] == "0":
                        new_res.append("1")
                    else:
                        new_res.append("0")
                    i += 1
                new_res = ''.join(new_res)

                sum = int(new_res, 2) + int("1", 2)
                new_res = bin(sum)[2:]

                print("C[пр] = 11," + new_res)

            print("Відповідь:")
            print("C = -0," + new_res + " * 10^(" + b3 + ")")