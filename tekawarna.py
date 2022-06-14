
from random import randint

print('==================================================')
print('               CUBA TEKA WARNA SAYA')
print('==================================================')
print('Anda boleh memilih dari senarai warna di bawah :')

print('     MERAH, BIRU, HITAM, HIJAU, KUNING, UNGU')
print('==================================================')

warna = ['merah', 'biru', 'hitam', 'hijau', 'ungu','kuning']
generator = randint(0,len(warna)-1)
guess = input('Teka warna saya : ')

while True:
    """anda perlu meneka sehingga dapat warna yang betul"""
    if guess != warna[generator]:
        print('Salah, cuba teka lagi.')
        guess = input('Teka warna saya :')
    elif guess == warna[generator]:
        break

print('YEAAHHHH.....warna saya ialah: ' + warna[generator])
print('********************** TAHNIAH **********************')