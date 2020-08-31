import requests
import json
import csv
r_NY = requests.get("https://api.weather.yandex.ru/v2/forecast?lat=40.730610&lon=֊73.935242&limit=5", headers={'X-Yandex-API-Key':'f6d5e33d-cc2f-477a-a9c4-da317118dd64'})
cont = r_NY.content

dic = json.loads(cont)
x = dic['forecasts']
choosen = []
print(x[0])
for i in range(len(x)):
    new_dic = {
        'date': x[i]['date'],
        'sunrise': x[i]['sunrise'],
        'sunset': x[i]['sunset'],
        'night_temp_avg': x[i]['parts']['night']['temp_avg'],
        'day_temp_avg': x[i]['parts']['day']['temp_avg'],
        }
    choosen.append(new_dic)
print(choosen)

with open('/home/rafael/Desktop/Python_projects/forecast_exam/file.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(choosen)