import json
import random
import itertools
from web3 import Web3
from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet

colour_cyan = '\033[36m'
colour_reset = '\033[0;0;39m'
colour_red = '\033[31m'
colour_green='\033[0;32m'
colour_Lightred     = "\033[91m"


d = open('file.json') #mnemonic ["", ""]
j = json.load(d)
p = itertools.permutations(j, 12)

apix = open('web3eth.json')  # api keys from infura
apiy = json.load(apix)
apixx = open('web3bsc.json') # api keys from binance smart chain
apiyy = json.load(apixx)


total= 0
no= 0
for val in (p):
    total+=1
    y = (' '.join(val))
    x = str(y)
    mapi = random.sample(apiy, k=1)
    api = str(' '. join(mapi))
    mapib = random.sample(apiyy, k=1)
    apibsc = str(' '. join(mapib))
    
    
    
    try:
        bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency = EthereumMainnet, account = 0, change = False, address = 0)
        mne = str(x)
        bip44_hdwallet.from_mnemonic(mnemonic = mne)
        pw = (bip44_hdwallet.private_key())
        ethadd = str(bip44_hdwallet.address())
        
        
        
        web3 = Web3(Web3.HTTPProvider(api))
        balance = web3.eth.getTransactionCount(ethadd)
        web3 = Web3(Web3.HTTPProvider(apibsc))
        saldo = web3.eth.getTransactionCount(ethadd)
        
        
        
        
        print (colour_green + '\n>>>>>>>>>>>>>>>>>>>>>>>>>>' +  colour_green + '\n|' + colour_reset + 'Transaction Nonce eth: ' + str(balance) +   colour_green + '\n|' + colour_reset + 'Transaction Nonce bsc: ' + str(saldo) + colour_green + '\n>>>>>>>>>>>>>>>>>>>>>>>>>>')
        
        print(colour_reset + '------------------------------------------------------' + colour_cyan + "\nTotal Mnemonic Checked : " + colour_cyan + str (total) + colour_cyan +  "    Scan Number : " +  str(no) + colour_reset + '\n------------------------------------------------------')
        
        print(colour_cyan + "Addres: " + colour_cyan + ethadd + colour_cyan +'\nPharse' + ': ' + x + colour_reset + '\n------------------------------------------------------')
        
        
        if int(balance) > 0:
            f=open(u"ethyesss.txt","a")
            f.write('\n Eth Address: ' + ethadd)
            f.write('\nPrivateKey (hex): ' + key)
            f.write('\n---------------------------')
            f.close()
        if int(saldo) > 0:
            f=open(u"bscyesss.txt","a")
            f.write('\n Bsc Address: ' + bscadd)
            f.write('\nPrivateKey (hex): ' + key)
            f.write('\n---------------------------')
            f.close()

        
        
        
        
        
        no = no + 1

    except:
        
        stop = ("= ")
        if stop == '':
            break
        



