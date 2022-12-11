import requests
import subprocess
from bs4 import BeautifulSoup

forge_version = input('Enter the version of forge that you want: ')


def get_url():
    download_page = requests.get(f'https://files.minecraftforge.net/net/minecraftforge/forge/index_{forge_version}.html').content

    with open('index.html', 'wb') as f:
        f.write(download_page)

    with open('index.html') as f:
        soup = BeautifulSoup(f, 'html.parser')
        match = soup.find('div', class_='link link-boosted')
        redirect_url = match.a['href']
        url = redirect_url[48:]
        return url


def download(url):
    req = requests.get(url).content
    with open(f'forge_{forge_version}.jar', 'wb') as f:
        f.write(req)

    user_input = input('Enter would you like to open the file now? y/n: ')

    if user_input == 'y' or 'Y':
        subprocess.run(['java', '-jar', f'forge_{forge_version}.jar'])
    else:
        print('finished!')


def main():
    url = get_url()
    download(url)


if __name__ == '__main__':
    main()
