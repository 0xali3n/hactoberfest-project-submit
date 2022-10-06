"""
25/09/22 02:02:15 PM
THM-DL/thm.py : @riz4d
"""

import wget
import requests


url = 'https://tryhackme-certificates.s3-eu-west-1.amazonaws.com/'
certificate_no = input("Enter Certificate number : ")
cerdl = url+certificate_no+'.png'
req = requests.get(cerdl)
status=req.status_code
dl=''
if status==200:
    print("Congrats!! \n"+ certificate_no+" Is Issued By TryHackMe ")
    dl = str(input('Did You Wanna Download This Certificate?? (Y/N) :'))
else:
    print("Sorry \n" + certificate_no+" Is A Invalid Certificate")
    

if dl=='Y': 
    file_name = wget.download(cerdl)
    print('Certificate Is Successfully Downloaded: ', file_name)
elif dl=='y':
    file_name = wget.download(cerdl)
    print('Certificate Is Successfully Downloaded: ', file_name)
elif dl=='N':
    print('Okay,Thanks for using.')
elif dl=='n':
    print('Okay,Thanks for using.')
else:
    print("Invalid Option Choose Y/N")
    
