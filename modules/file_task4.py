class module_task4:
    def task4(num):
        print("Тема: 4. ЗАЗНАЧТЕ МІНІМАЛЬНУ ОСНОВУ СИСТЕМИ ЧИСЛЕННЯ, ДО ЯКОЇ МОЖУТЬ НАЛЕЖАТИ ЗАДАНІ ЧИСЛА")
        print("\nПОЯСНЕННЯ: Для того, щоб знайти мінімальну основу системи числення, ми повинні знайти найбільшу цифру в числі і збільшити її на 1, як наприклад у двійкових числах найбільша цифра 1, у вісімкових 7 і т.д.\n")
        nums = num.split(" ")
        a = nums[0]
        b = nums[1]
        c = nums[2]
        d = nums[3]
        e = nums[4]



        # ДЛЯ ПЕРШОГО ЧИСЛА
        a_div = list(a)
        a_div.remove(",")

        i = 0
        while i < len(a_div):
            a_div[i] = int(a_div[i])
            i += 1
        n = max(a_div)
        x = n + 1

        final = "Число " + a + " належить до " + str(x) + "-ової системи числення, бо максимальна цифра в числі - це " + str(n) + "."
        print(final)





        # ДЛЯ ДРУГОГО ЧИСЛА
        b_div = list(b)
        b_div.remove(",")

        i = 0
        while i < len(b_div):
            b_div[i] = int(b_div[i])
            i += 1
        n = max(b_div)
        x = n + 1

        final = "Число " + b + " належить до " + str(x) + "-ової системи числення, бо максимальна цифра в числі - це " + str(n) + "."
        print(final)





        # ДЛЯ ТРЕТЬОГО ЧИСЛА
        c_div = list(c)
        c_div.remove(",")

        i = 0
        while i < len(c_div):
            c_div[i] = int(c_div[i])
            i += 1
        n = max(c_div)
        x = n + 1

        final = "Число " + c + " належить до " + str(x) + "-ової системи числення, бо максимальна цифра в числі - це " + str(n) + "."
        print(final)





        # ДЛЯ ЧЕТВЕРТОГО ЧИСЛА
        d_div = list(d)
        d_div.remove(",")

        i = 0
        while i < len(d_div):
            d_div[i] = int(d_div[i])
            i += 1
        n = max(d_div)
        x = n + 1

        final = "Число " + d + " належить до " + str(x) + "-ової системи числення, бо максимальна цифра в числі - це " + str(n) + "."
        print(final)





        # ДЛЯ П'ЯТОГО ЧИСЛА
        e_div = list(e)
        e_div.remove(",")

        i = 0
        while i < len(e_div):
            e_div[i] = int(e_div[i])
            i += 1
        n = max(e_div)
        x = n + 1

        final = "Число " + e + " належить до " + str(x) + "-ової системи числення, бо максимальна цифра в числі - це " + str(n) + "."
        print(final + "\n\n\n")