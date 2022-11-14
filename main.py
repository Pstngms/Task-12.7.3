per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму, которую планируете положить под проценты: "))
TKB = per_cent.get('ТКБ') * money
SKB = per_cent.get('СКБ') * money
VTB = per_cent.get('ВТБ') * money
SBER = per_cent.get('СБЕР') * money
deposit = [int(TKB), int(SKB), int(VTB), int(SBER)]
print(deposit)
print("Максимальная сумма, которую вы можете заработать — %d" % (max(deposit)))
