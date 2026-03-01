import requests as rq
from bs4 import BeautifulSoup as BS
import sys
import subprocess

url = 'https://www.mercadolivre.com.br/p/MLB36772633?pdp_filters=item_id:MLB3692281025&matt_tool=38524122#origin=share&sid=share&wid=MLB3692281025&action=copy'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}
try:
    req = rq.get(url, headers=headers)
except Exception as e:
    mensagem = f'ocorreu um erro no monitor do produto: {e}'
    subprocess.run(["termux-notification", "--title", "Alerta de preço!", "--content", mensagem])
    sys.exit(1)    
    
soup = BS(req.text, 'html.parser')

soup2 = soup.find('span', class_= 'andes-money-amount__fraction')

if soup2 == None:
    mensagem = 'ERRO! Não foi possivel buscar a informação do produto monitorado'
    subprocess.run(["termux-notification", "--title", "Alerta de preço!", "--content", mensagem])
    sys.exit(1)
    
preco_normal =  2668
preco_brl = f'R$ {soup2.text}'
preco = int(soup2.text.replace('.', ''))

if preco < preco_normal:
    mensagem = f'preço diminuiu!: Notebook Asus por {preco_brl}'
    subprocess.run(["termux-notification", "--title", "Alerta de preço!", "--content", mensagem])
    subprocess.run(["termux-media-player", "play", "/storage/emulated/0/Notifications/alarm.mp3"])