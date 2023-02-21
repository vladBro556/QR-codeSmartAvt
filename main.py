from bs4 import BeautifulSoup
import requests
from PIL import Image, ImageDraw, ImageFont
import warnings
txt = input('Введите номер Автобуса::::>')
x = input('Введите ссылку для генерации::::>')
datas={
    'd':x,
    's':'4'
}
reqq = requests.post('http://qrcoder.ru', params=datas)
#print(reqq.url)
req = requests.get(reqq.url)
src=req.text
with open('Forest.html', 'w',encoding='UTF-8') as fd:
        #print('Ссылка записана')
        fd.write(src)
warnings.filterwarnings('ignore')
with open('Forest.html',encoding='UTF-8') as file:
    src = file.read()
soup = BeautifulSoup(src,"lxml")
ss=soup.find(class_="inputCover")
for item in ss:
    sss=item.get("value")
#print(sss)

req = requests.get(sss, stream=True)
req.raise_for_status()
with open('qrcode.jpg', 'wb') as fd:
    for chunk in req.iter_content(chunk_size=50000):
        #print('QR-code загружен')
        fd.write(chunk)

img1 = Image.open('maket.jpg')
img0 = Image.open('qrcode.jpg')
img2 = img0.resize((325,325))
idraw=ImageDraw.Draw(img1)
line = ImageFont.truetype('arial.ttf', size = 30)
idraw.text((150,480),txt,font=line, fill=(0,0,0,255))
idraw.text((610,480),txt,font=line, fill=(0,0,0,255))
img1.paste(img2,(47,120))
img1.paste(img2,(507,120))
img1.save(txt+'.JPG')
xx=input("QRcode готов, нажмите Enter чтоб закрыть приложение")


