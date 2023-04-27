base_rates = {'uah_usd':36.50,'uah_eur':40.80}
output_header = '''... Welcome to Exchanger !!! ...
Please choose your base currency, type corresponding number 
1) UAH
2) USD
3) EUR'''
print(output_header)

type_of_currency = input('Your choice: ')
amount_of_money = int(input('Amount of money: '))

output_footer = ''

if type_of_currency == '1':
    uah = amount_of_money
    usd = amount_of_money / base_rates.get('uah_usd')
    eur = amount_of_money / base_rates.get('uah_eur')
    output_footer += f' {uah} UAH = {usd:.2f} USD\n {uah} UAH = {eur:.2f} EUR'
elif type_of_currency == '2':
    uah = amount_of_money * base_rates.get('uah_usd')
    usd = amount_of_money
    eur = amount_of_money * ( base_rates.get('uah_usd') / base_rates.get('uah_eur') )
    output_footer += f' {usd} USD = {uah:.2f} UAH\n {usd} USD = {eur:.2f} EUR'
elif type_of_currency == '3':
    uah = amount_of_money * base_rates.get('uah_eur')
    usd = amount_of_money * (base_rates.get('uah_eur') / base_rates.get('uah_usd'))
    eur = amount_of_money
    output_footer += f' {eur} EUR = {uah:.2f} UAH\n {eur} EUR = {usd:.2f} USD'
else:
    print("Oops, invalid currency number. Try it again )")
    exit()

print('Result:',output_footer,sep='\n')
