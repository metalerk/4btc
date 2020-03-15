import sys
import time
import click
from btc_tracker_engine import (
    CoinDeskTracker,
    rate_diff_percentage,
)

def show_banner():
    banner = """                        
        ,d8    88                                
      ,d888    88             ,d                 
    ,d8" 88    88             88                 
  ,d8"   88    88,dPPYba,   MM88MMM   ,adPPYba,  
,d8"     88    88P'    "8a    88     a8"     ""  
8888888888888  88       d8    88     8b          
         88    88b,   ,a8"    88,    "8a,   ,aa  
         88    8Y"Ybbd8"'     "Y888   `"Ybbd8"'


    http://luisesteban.mx/      © Powered by 4MLabs                                                                                                                                      
"""
    print(banner)

@click.command()
@click.argument('currency')
@click.option('--interval', type=float, default=0, help='Time interval of tracking in seconds.')
@click.option('--alert/--no-alert', default=True, help='Alert fluctuation.')
@click.option('--min-rate', type=float, help='Minimum rate percentage of alert.')
@click.option('--max-rate', type=float, help='Maximum rate percentage of alert.')
@click.option('--rate-window', type=float, default=5, help='Rate percentage window range.')
@click.option('--times', default=-1, help='Watch n times.')
def main(currency, interval, alert, min_rate, max_rate, rate_window, times):
    """4btc Bitcoin tracker tool   By ©4MLabs"""
    try:
        show_banner()
        currency = currency.upper()
        btc_tracker = CoinDeskTracker()
        print('\t\t****** Tr4ck3r ******\n\n')
        if not btc_tracker.is_valid_currency(currency):
            print(f'[-] Invalid currency \'{currency}\'.\n')
            sys.exit(1)
        previous_rate = btc_tracker.get_currency_price(currency, just_rate=True)['rate']
        _flag = True
        counter = 0
        previous_rate_percentage = 1
        while(_flag):
            obj = btc_tracker.get_currency_price(currency)
            increase_rate_percentage = rate_diff_percentage(previous_rate, obj['rate'], percentage=True)
            previous_rate = obj['rate']
            if increase_rate_percentage != 0 and increase_rate_percentage != previous_rate_percentage:
                updown_indicator = '+' if increase_rate_percentage >= 0 else '-'
                increase_decrease_indicator = 'INCREASE' if updown_indicator == '+' else 'DECREASE'
                print(f"[{updown_indicator}] {obj['timestamp'].strftime('%a %d-%m-%Y %H:%M:%S%f %Z')} --- 1 BTC => ${obj['rate']:,} {obj['currency_code']} - {increase_decrease_indicator} RATE  % {increase_rate_percentage}")
                print('·····························································································')
                if increase_rate_percentage < 0 and min_rate is not None:
                    if abs(abs(increase_rate_percentage) - abs(min_rate)) <= rate_window:
                        print(f'\n=============== [!] Alert!!! BTC has DECREASED   % {increase_rate_percentage} ===============\n')
                if increase_rate_percentage > 0 and max_rate is not None:
                    if abs(abs(increase_rate_percentage) - abs(min_rate)) <= rate_window:
                        print(f'\n=============== [!] Alert!!! BTC has INCREASED   % {increase_rate_percentage} ===============\n')
            previous_rate_percentage = increase_rate_percentage
            if times > -1:
                if counter < times - 1:
                    counter += 1
                else:
                    _flag = False
            time.sleep(interval)
    except KeyboardInterrupt:
        print('Bye!')
    except KeyError as e:
        print(f'[-] Error: {e}')

if __name__ == "__main__":
    main()