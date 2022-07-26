
from bs4 import BeautifulSoup

import requests

def ekstraksi_data():

    """

tanggal: 21 juli 2021
waktu: 16:57:48 WIB
magnetudo: 4.3
kedalaman: 10 km
lokasi: 2.09 LS - 120.51 BT
pusat gempa: Pusat gempa berada di darat 62 Km Timur Laut Luwu Utara
dirasakan: Dirasakan (Skala MMI): II - III Malili
    :return:
    """

    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None


    if content.status_code == 200:

        soup = BeautifulSoup(content.text, 'html.parser')

        result = soup.find('span', {'class': "waktu"})
        result = result.text.split (', ')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitudo = None
        kedalaman = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None

        for res in result:
            print(i, res)

            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text

            i = i + 1




        hasil = dict()
        hasil['tanggal'] = tanggal  # '21 juli 2021'
        hasil['waktu'] = waktu  # '16:57:48 WIB'
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'ls': ls ,'bt': bt}
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan
        print(hasil)
        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print('tidak bisa menemukan data gempa terkini')
        return
    print('Gempa Terakhir berdasarkan BMKG')
    print(f"tanggal {result['tanggal']}")
    print(f"waktu {result['waktu']}")
    print(f"magnitudo {result['magnitudo']}")
    print(f"kedalaman {result['kedalaman']}")
    print(f"koordinat: LS={result['koordinat']['ls']}, BT={result['koordinat']['bt']}")
    print(f"lokasi {result['lokasi']}")
    print(f"dirasakan {result['dirasakan']}")
    print(result)

if __name__ == '__main__':
    result = ekstraksi_data()
    tampilkan_data(result)

