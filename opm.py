from lxml import html
import requests, os
from downloader import download
from tqdm import tqdm

def extract():
    url = 'https://ww3.readopm.com/chapter/one-punch-man-chapter-136/'
    page = requests.get(url)
    tree = html.fromstring(page.content)

    manga = tree.xpath('//*[@id="content"]/div[1]/div/div[1]/div/div/select/option/@value')[0]
    
    page = requests.get(manga)
    tree = html.fromstring(page.content)

    pics = tree.xpath('//div[@class="img_container mb-2"]/img/@src')
    manga = tree.xpath('//h1[@class="mb-3"]/text()')[0].replace("/", " ")

    try:    
        os.mkdir(manga)
    except FileExistsError:
        pass

    print(manga)
    path = os.getcwd()
    os.chdir(manga)
    
    for url in tqdm(pics, ascii=True):
        download(url.strip('\r'))

    os.chdir(path)
