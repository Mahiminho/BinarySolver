class module_task7:
    def task7(num):
        print("Тема: 7. НОРМАЛІЗУЙТЕ ДВІЙКОВІ ЧИСЛА У ФОРМАТІ З РУХОМОЮ КОМОЮ І ЗАПИШІТЬ ЇХ У НОРМАЛЬНІЙ ФОРМІ:")
        print("\nПОЯСНЕННЯ: Нормалізоване число - це неціле число, у якого перша цифра після коми - це 1. Якось так :/\n")
        bin_mass = {"0":0, "1":1, "10":2, "11":3, "100":4, "101":5, "110":6, "111":7} # массив для переведення чисел з бінарних в прості
        ten_mass = {0:"0", 1:"1", 2:"10", 3:"11", 4:"100", 5:"101", 6:"110", 7:"111"} # массив для переведення чисел з простих в бінарні
        num = num.split(" ") # розбиваю строку задану юзером на два числа
        a = num[0] # перше число
        b = num[1] # друге число



        # ДЛЯ НОРМАЛІЗАЦІЇ ПЕРШОГО ЧИСЛА
        i = 0
        while i < len(a): # в циклі перевіряю, чи степінь першого числа додатній чи від'ємний
            if a[i] == "-": # якщо від'ємний
                a1 = a.split("-") # розбиваю по мінусу
                numer = a1[0] # перша частинка це число
                numer1 = numer[:-3] # але прибираю зайву частинку (*10)
                power = a1[1] # початковий степінь (бінарний)
                power10 = bin_mass[power] # переводжу початковий степінь з бінарного в простий код

                numer2 = numer1.split(",") # саме число розбиваю по комі
                numer_before_coma = numer2[0] # число до коми
                numer_after_coma = numer2[1] # число після коми

                new_power = -1 * power10 + len(numer_before_coma) # створюю степінь, який буде у відповіді (множу старий степінь на -1, щоб було видно, що він від'ємний і додаю кількість символів до коми)

                res_num = "0," + numer_before_coma + numer_after_coma # створюю число, яке буде у відповіді, тобто фактично пересуваю частину, яка була перед комою, за кому

                value_before = numer1 + " * 10^(-" + power + ")" # початкове число, яке задав користувач, але в правильному форматі (замість, наприклад, "*10-10" буде " * 10^(-10)" і т.д.)

                if new_power < 0: # якщо степінь вийшов від'ємний
                    power_value = -1 * new_power # роблю його додатнім (тобто це величина самого степеня)
                    real_power = ten_mass[power_value] # по цій величині шукаю бінарний аналог
                    value_after = res_num + " * 10^(-" + real_power + ")" # число результат (з від'ємним степенем)
                    result = value_before + " = " + value_after # строка результат нормалізації
                else: # якщо степінь вийшов додатній
                    real_power = ten_mass[new_power] # шукаю бінарний аналог степеня
                    value_after = res_num + " * 10^(+" + real_power + ")" # число результат (з додатнім степенем)
                    result = value_before + " = " + value_after # строка результат нормалізації

                print(result) # вивід строки результату нормалізації для першого числа, якщо спочатку степінь спочатку був від'ємним

            elif a[i] == "+":
                a1 = a.split("+") # розбиваю по плюсу
                numer = a1[0] # перша частинка це число
                numer1 = numer[:-3] # але прибираю зайву частинку (*10)
                power = a1[1] # початковий степінь (бінарний)
                power10 = bin_mass[power] # переводжу початковий степінь з бінарного в простий код

                numer2 = numer1.split(",") # саме число розбиваю по комі
                numer_before_coma = numer2[0] # число до коми
                numer_after_coma = numer2[1] # число після коми

                new_power = power10 + len(numer_before_coma) # створюю степінь, який буде у відповіді (до початкового степеня додаю кількість символів до коми)

                res_num = "0," + numer_before_coma + numer_after_coma # створюю число, яке буде у відповіді, тобто фактично пересуваю частину, яка була перед комою, за кому

                value_before = numer1 + " * 10^(+" + power + ")" # початкове число, яке задав користувач, але в правильному форматі (замість, наприклад, "*10+10" буде " * 10^(+10)" і т.д.)

                real_power = ten_mass[new_power] # шукаю бінарний аналог степеня
                value_after = res_num + " * 10^(+" + real_power + ")" # число результат (з додатнім степенем)
                result = value_before + " = " + value_after # строка результат нормалізації

                print(result) # вивід строки результату нормалізації для першого числа, якщо спочатку степінь спочатку був додатнім

            else:
                pass

            i += 1

        print("")










        # ДЛЯ НОРМАЛІЗАЦІЇ ДРУГОГО ЧИСЛА
        i = 0
        while i < len(b): # в циклі перевіряю, чи степінь першого числа додатній чи від'ємний
            if b[i] == "+": # якщо додатній
                b1 = b.split(",") # розбиваю по комі
                b2 = b1[1] # беру все що після коми (а нуль, що був до коми посилаю за росіським кораблем)

                b3 = b2.split("+") # все що після коми розбиваю по плюсу
                numer = b3[0] # частина до плюса - це наше число, але з залишком (*10)
                numer = numer[:-3] # прибираю залишок (*10)
                power = b3[1] # частина після плюса (початковий степінь)

                n = 0
                while numer[n] == "0": # рахую, скільки є зайвих нулів після коми, які треба буде прибрати
                    n += 1

                new_numer = numer[n:] # прибираю нулі з початку числа

                new_power = bin_mass[power] - n # рахую новий степінь в десятковому коді

                if new_power < 0: # якщо новий степінь вийшов від'ємним
                    value_power = -1 * new_power # знаходжу його значення степеня
                    bin_new_power = ten_mass[value_power] # по його значенню знаходжу двійковий аналог
                    print("0," + numer + " * 10^(+" + power + ") = 0," + new_numer + " * 10^(-" + bin_new_power + ")") # складаю строку результат (число спочатку було з додатнім степенем, а стало з від'ємним)
                else: # якщо новий степінь вийшов додатнім
                    bin_new_power = ten_mass[new_power] # знаходжу двійковий аналог степеня
                    print("0," + numer + " * 10^(+" + power + ") = 0," + new_numer + " * 10^(+" + bin_new_power + ")") # складаю строку результат (число як було з додатнім степенем, так і залишилось)

            elif b[i] == "-":
                b1 = b.split(",")  # розбиваю по комі
                b2 = b1[1]  # беру все що після коми (а нуль, що був до коми посилаю за росіським кораблем)

                b3 = b2.split("-")  # все що після коми розбиваю по мінусу
                numer = b3[0]  # частина до мінуса - це наше число, але з залишком (*10)
                numer = numer[:-3]  # прибираю залишок (*10)
                power = b3[1]  # частина після мінуса (початковий степінь)

                n = 0
                while numer[n] == "0":  # рахую, скільки є зайвих нулів після коми, які треба буде прибрати
                    n += 1

                new_numer = numer[n:]  # прибираю нулі з початку числа

                new_power = -1 * bin_mass[power] - n  # рахую новий степінь в десятковому коді

                value_power = -1 * new_power  # знаходжу величину степеня
                bin_new_power = ten_mass[value_power]  # по його величині знаходжу двійковий аналог
                print("0," + numer + " * 10^(+" + power + ") = 0," + new_numer + " * 10^(-" + bin_new_power + ")")  # складаю строку результат (число як було з від'ємним степенем, так і залишилось)

            else:
                pass

            i += 1

        print("\n\n")