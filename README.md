# 4btc Tr4ck3r

Bitcoin tracker tool

![4btc_logo](https://user-images.githubusercontent.com/13503868/76696448-56a10a00-6651-11ea-845d-7a09f3f2960b.png)

## Requirements

- Python 3.7 or later

## Setup

Create virtualenv and activate it

```sh
$ virtualenv -p python3 env
$ source env/bin/activate
```

Install dependencies

```sh
$ pip install -r requirements.txt
```

## Run

```sh
$ python btc_tracker.py --help
Usage: btc_tracker.py [OPTIONS] CURRENCY

  4btc Bitcoin tracker tool   By ©4MLabs

Options:
  --interval FLOAT      Time interval of tracking in seconds.
  --alert / --no-alert  Alert fluctuation.
  --min-rate FLOAT      Minimum rate percentage of alert.
  --max-rate FLOAT      Maximum rate percentage of alert.
  --rate-window FLOAT   Rate percentage window range.
  --times INTEGER       Watch n times.
  --help                Show this message and exit.
```

- `alert` **is still under development.**

- `rate-window` stands for error range percentage between `min_rate`/`max_rate` and the btc increase percentage.

## Example

```
$ python btc_tracker.py mxn --min-rate 0.01 --max-rate 0.01 --rate-window 0.001

        ,d8    88
      ,d888    88             ,d
    ,d8" 88    88             88
  ,d8"   88    88,dPPYba,   MM88MMM   ,adPPYba,
,d8"     88    88P'    "8a    88     a8"     ""
8888888888888  88       d8    88     8b
         88    88b,   ,a8"    88,    "8a,   ,aa
         88    8Y"Ybbd8"'     "Y888   `"Ybbd8"'


    http://luisesteban.mx/      © Powered by 4MLabs

		****** Tr4ck3r ******


[!] - Tracking from CoinDesk -
[-] INITIAL: $115,057.8052 MXN   ====   Sun 15-03-2020 04:07:50865120


[+] Sun 15-03-2020 10:08:00000000 UTC

[+] INITIAL RATE: $115,057.8052 MXN
[+] CURRENT RATE: $115,072.7436 MXN
[+] CURRENT PROFIT: $14.938399999999092 MXN
[+] GLOBAL PROFIT: $14.938399999999092 MXN
[+] CURRENT BALANCE  % 0.012983386893251021
[+] GLOBAL BALANCE  % 0.012983386893251021
·········································································π
```

## Author

**Luis Esteban Rodríguez** <*rodriguezjluis0@gmail.com*>
<br>
[Personal Website](luisesteban.mx/)
