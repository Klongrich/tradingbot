from main import poloniex;
from coindata import coindata;
from time import sleep;
import urllib
import urllib2
import json
import time
import hmac, hashlib

btc = 'BTC_XRP'
usd = 'USDT_XRP'

polo = poloniex("API KEY", "SECRECT KEY");

while True:
    btc_data = coindata('USDT_BTC', polo);
    ltc_btc = coindata(btc, polo);
    ltc_usd = coindata(usd, polo);
   ## x = polo.returnBalances();
    sleep(1);
  ## print ('Current posistion: ' + x['USDT_BTC']);
    print('BTC_USD ASK: ' + btc_data.ask());
    print('ETH_BTC BID: ' + ltc_btc.bid());
    print('ETH_USD ASK: ' + ltc_usd.ask());
    diff = (float(ltc_btc.bid()) * float(btc_data.ask()) / float(ltc_usd.ask()));
    print ((diff - 1) * 100);
    print


