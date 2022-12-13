import requests
import time
import os
import threading
from concurrent.futures import ThreadPoolExecutor

def fetcher(params):
    session = params[0]
    url = params[1]
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        return response.text

def main():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"] * 3

    executor = ThreadPoolExecutor(max_workers=10)

    # session = requests.Session()
    # session.get(url)
    # session.close()

    with requests.Session() as session:
        # result = [fetcher(session, url) for url in urls]
        # print(result)
        params = [(session, url) for url in urls]
        results = list(executor.map(fetcher, params))
        print(results)

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)