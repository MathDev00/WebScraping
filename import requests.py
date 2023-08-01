import requests
from bs4 import BeautifulSoup

def get_all_comments(url):
    all_comments = []
    page = 1

    while True:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        params = {'pageNumber': page}
        response = requests.get(url, headers=headers, params=params)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontrar o elemento que contém os comentários
        comments = soup.find_all('span', {'data-hook': 'review-body'})
        
        if not comments:
            break

        for comment in comments:
            all_comments.append(comment.text.strip())

        page += 1

    return all_comments

url = 'https://www.amazon.com.br/Se-quiser-mudar-mundo-político/product-reviews/6555351748/ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews&pageNumber=1'
all_comments = get_all_comments(url)

for i, comment in enumerate(all_comments, start=1):
    print(f"Comentário {i}: {comment}\n")
