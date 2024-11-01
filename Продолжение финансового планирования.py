import math
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0
for i in range (months):
    delta = spend - salary
    money_capital += delta
    spend *= 1+increase

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", math.ceil(money_capital))
