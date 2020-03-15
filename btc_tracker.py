from datetime import datetime as dt
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
        first_rate = previous_rate
        print('[!] - Tracking from CoinDesk -')
        print(f"[-] INITIAL: ${first_rate:,} {currency}   ====   {dt.now().strftime('%a %d-%m-%Y %H:%M:%S%f %Z')}\n\n")
        _flag = True
        counter = 0
        previous_rate_percentage = 1
        while(_flag):
            obj = btc_tracker.get_currency_price(currency)
            increase_rate_percentage = rate_diff_percentage(previous_rate, obj['rate'], percentage=True)
            first_rate_percentage = rate_diff_percentage(first_rate, obj['rate'], percentage=True)
            if increase_rate_percentage != 0 and increase_rate_percentage != previous_rate_percentage:
                updown_indicator = lambda x: '+' if x >= 0 else '-'
                updown = updown_indicator(increase_rate_percentage)
                print(f"[{updown}] {obj['timestamp'].strftime('%a %d-%m-%Y %H:%M:%S%f %Z')}\n")
                print(f"[{updown}] INITIAL RATE: ${first_rate:,} {currency}")
                print(f"[{updown}] CURRENT RATE: ${obj['rate']:,} {currency}")
                print(f"[{updown}] CURRENT PROFIT: ${(obj['rate'] - previous_rate):,} {currency}")
                print(f"[{updown}] GLOBAL PROFIT: ${(obj['rate'] - first_rate):,} {currency}")
                print(f"[{updown}] CURRENT BALANCE  % {increase_rate_percentage:,}")
                print(f"[{updown}] GLOBAL BALANCE  % {first_rate_percentage:,}")
                print('·········································································')
                if increase_rate_percentage < 0 and min_rate is not None:
                    if abs(abs(first_rate_percentage) - abs(min_rate)) <= rate_window:
                        print(f'\n===== [!] Alert!!! BTC has DECREASED  % {first_rate_percentage:,} since {first_rate:,} =====\n')
                if increase_rate_percentage > 0 and max_rate is not None:
                    if abs(abs(first_rate_percentage) - abs(max_rate)) <= rate_window:
                        print(f'\n===== [!] Alert!!! BTC has INCREASED  % {first_rate_percentage:,} since {first_rate:,}  =====\n')
            previous_rate = obj['rate']
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