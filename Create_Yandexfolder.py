import requests


URL_P = 'https://cloud-api.yandex.net/'
token_P = "AQAAAABWYgW9AADLW2AiMJzYuUx1kosHKuWu600"
headers_P = {'accept': 'application/json', 'authorization': f'OAuth {token_P}'}


url_k = "https://cloud-api.yandex.net/v1/disk/resources/"
params = {
    'path': 'New'
}

def folder_create():
    requests.put(url=url_k, params=params, headers=headers_P).json()
    res = requests.get(url=URL_P + "v1/disk/resources/", headers=headers_P,
                  params={'path': 'New/', 'url': url_k})
    return res

folder_create()