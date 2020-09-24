def jack(net, m, p):
    print('OPay'.center(m + p))
    print('Merchant'.center(m + p))
    print()
    for k, v in net.items():
        print(k.ljust(m) + str(v).rjust(p))
winner = {'Merchant ID:': 'Merchant name:', '156619102220269920': 'God\'s Time multi-purpose', ' ': ' ', 'Merchant address:': ' ', '  ': '  ', 'Terminal ID:':'205/88JB'}
jack(winner, 20, 25)

print()
def POS(find, x, y):
    print('PURCHASE'.center(x + y))
    for k, v in find.items():
        print(k.ljust(x) + str(v).rjust(y))
let = {'STAN:': '003867', 'DATE/TIME:': '04/08/2020 13:18:41', 'AMOUNT:': 'NGN 3100.00', 'MASTER': '539941******9210', 'EXPIRY DATE:': '05/23', 'AUTHORIZATION:': '95EC1B', 'CVMR:': '440302'}
POS(let, 12, 19)

print()
def mine(select, x, y):
    print('TRANSACTION APPROVED'.center(x + y))
    print()
    for k, v in select.items():
        print(k.ljust(x) + str(v).rjust(y))
be = {'RESPONSE CODE': '00', 'AID': 'A0000000041010', 'RRN': '200804131841', 'Access': 'PIN', 'OPay POS:': '2.0.9','pos.support opay.team merchant':' '}
mine(be, 20, 9)


