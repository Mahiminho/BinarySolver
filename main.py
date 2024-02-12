import sys
from modules.file_task1 import module_task1
from modules.file_task2 import module_task2
from modules.file_task3 import module_task3
from modules.file_task4 import module_task4
from modules.file_task5 import module_task5
from modules.file_task6 import module_task6
from modules.file_task7 import module_task7
from modules.file_task8 import module_task8
from modules.file_task9 import module_task9



if __name__ == "__main__":
    original_stdout = sys.stdout # збереження поточного виводу консолі у змінну

    with open('OOFK_RGR.txt', 'w', encoding='utf-8') as f: # вказання файлу, в який буде записуватися вивід
        sys.stdout = f # перенаправлення виводу у файл
        
        # Варіант 2
        module_task1.task1("Що прийнято називати основою системи числення:")
        module_task2.task2("2712,663 134,223 110001110010101,10111001")
        module_task3.task3("56,455 2343167,64")
        module_task4.task4("315,783 317712,56 123321,21 1010,10201 3456,345609")
        module_task5.task5("275+333 426–222")
        module_task6.task6("295,4301")
        module_task7.task7("1010,11011*10+11 0,00001001*10+101")
        module_task8.task8("А=-0,101010 В=+0,000111")
        module_task9.task9("А=-0,101010*10-101 В=-0,000111*10-011")

        sys.stdout = original_stdout # повернення виводу консолі на місце

    print("Файл з готовим варіантом: OOFK_RGR.txt")



# Варіант 18
# module_task1.task1("Яка максимальна кількість розрядів необхідна для представлення результату додавання двох 10-розрядних чисел?")
# module_task1.task2("2756,475 433,334 110110111101011,01111101")
# module_task1.task3("89,642 4765442,273")
# module_task1.task4("352144,21521 346327,33 324223,821 21111,211 327452,295")
# module_task1.task5("353+254 392–276")
# module_task1.task6("299,1405")
# module_task1.task7("1101,10001*10-101 0,0011011*10+110")
# module_task1.task8("А=-0,111011 В=+0,001110")
# module_task1.task9("А=-0,111011*10+101 В=-0,101001*10-010")