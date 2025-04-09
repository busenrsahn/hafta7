import requests
from bs4 import BeautifulSoup
import os

def content(url):
    masaustu_yolu = r"C:\Users\BUSENUR\Desktop\icerik.txt"

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    tarih_tag = soup.find('time')
    tarih = tarih_tag.get_text(strip=True) if tarih_tag else 'Tarih Bulunamadı.'

    title_tag = soup.find("h1")
    baslik = title_tag.get_text(strip=True) if title_tag else "Başlık Bulunamadı"

    paragraphs = soup.find_all("p")
    icerik = "\n".join([p.get_text().strip() for p in paragraphs]) if paragraphs else "İçerik Bulunamadı."

    data = '{};{};{}'.format(tarih, baslik, icerik)

    with open(masaustu_yolu, "a", encoding="utf-8") as file:
        file.write(f"URL: {url}\n")
        file.write(f"Tarih: {tarih}\n")
        file.write(f"Başlık: {baslik}\n")
        file.write(f"İçerik: {icerik}\n")
        file.write("-" * 50 + "\n")
        file.write(f"Data: {data}\n")
        file.write("-" * 50 + "\n")
content("https://www.milligazete.com.tr/haber/24244937/serdar-haydanli-kimdir")
