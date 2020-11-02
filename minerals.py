import requests

qwe = []
count = 1
all_id = {'Tritanium': '34',
          'Pyerite': '35',
          'Mexallon': '36',
          'Isogen': '37',
          'Nocxium': '38',
          'Zydrine': '39',
          'Megacyte': '40',
          'Morphite': '11399'}

def all_items():
    buy_prices_list = {}
    sell_prices_list = {}
    global count
    for item_id in all_id:
        buy_link = 'https://esi.evetech.net/latest/markets/10000002/orders/?' \
                   'datasource=tranquility&order_type=buy&page=1&type_id={id}'.format(id=all_id.get(item_id))
        sell_link = 'https://esi.evetech.net/latest/markets/10000002/orders/?' \
                    'datasource=tranquility&order_type=sell&page=1&type_id={id}'.format(id=all_id.get(item_id))
        buy_response = requests.get(buy_link).json()
        sell_response = requests.get(sell_link).json()
        for i in buy_response:
            if i['system_id'] == int('30000142'):
                qwe.append(i['price'])
        buy_prices_list.update({item_id: max(qwe)})
        qwe.clear()
        count += 1
        for i in sell_response:
            if i['system_id'] == int('30000142'):
                qwe.append(i['price'])
        sell_prices_list.update({item_id: min(qwe)})
        qwe.clear()
        count += 1
    return buy_prices_list, sell_prices_list


if __name__ == "__main__":
    all_items()
    print('minerals.py')
