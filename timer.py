import time
current_version = "0.0.9"

# intro
print("Добро пожаловать в таймер обратного отсчёта")
time.sleep(1)
print("Текущая версия приложения - " + current_version)

#main body
timer = (input("Сколько минут поставить на таймер? "))
timer_value = (int(timer)) * 60

print(timer_value)
while timer_value != 0:
    time.sleep(1)
    timer_value = timer_value -1
    print(timer_value)
    # здесь в след. версии можно попробовать добавить формулу с минутами. 
    # то есть брать число секунд, делить на 60 и выводить как " осталось X минут и Y секунд"
print("Time is out")