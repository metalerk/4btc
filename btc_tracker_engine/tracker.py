import dateutil.parser
import json
import requests as req

class CoinDeskTracker:
    def __init__(self):
        self.endpoint = 'https://api.coindesk.com/v1/bpi/'

    def get_currency_price(self, currency, just_rate=False):
        try:
            r = req.get('{}currentprice/{}.json'.format(self.endpoint, currency))
            obj = r.json()
            if just_rate:
                return {'rate': float(obj['bpi'][currency]['rate'].replace(',', '')),}
            return {
                'currency_code': obj['bpi'][currency]['code'],
                'currency_description': obj['bpi'][currency]['code'],
                'rate': float(obj['bpi'][currency]['rate'].replace(',', '')),
                'timestamp': dateutil.parser.parse(obj['time']['updatedISO'])
            }
        except KeyError as e:
            return {'error': f'Invalid key {e}'}
    
    def get_available_currencies(self):
        return self.__load_currency_map()

    def is_valid_currency(self, currency):
        currency_map = self.__load_currency_map()
        return currency in [c['currency'] for c in currency_map]

    def __load_currency_map(self):
        try:
            r = req.get('{}supported-currencies.json'.format(self.endpoint))
            return r.json()
        except:
            return {}