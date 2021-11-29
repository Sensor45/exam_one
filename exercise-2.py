deposit = int(input('Введите сумму депозита :'))
accumulated_deposit = int(input('Введите сумму накопления :'))
interest_rate = int(input('Введите годовую ставку в процентах :'))

month=0

while deposit < accumulated_deposit:
    month=month+1
    deposit = (deposit*(interest_rate/100)/12)+deposit

print(f'Количество месяцев накопления нужной суммы :{month}')

