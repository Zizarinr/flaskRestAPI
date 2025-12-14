import requests

BASE = "http://127.0.0.1:5000/"
'''
data = [{"Umur": 23, "Nama": "Imaduddin", "Daerah": "Karawang"},
        {"Umur": 20, "Nama": "Kecipak", "Daerah": "Gowa"},
        {"Umur": 19, "Nama": "Aozora", "Daerah": "Cikampek"}]

for i in range(len(data)):
    response = requests.put(BASE + "Mahasiswa/" + str(i), json=data[i])
    print(response.json())

input()
'''
response = requests.patch(BASE + "Mahasiswa/0", {"Umur":99, "Daerah": "Rangkasbitung"})
print(response.json())
