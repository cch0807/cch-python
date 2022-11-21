"""
Concurrency, CPU Bound vs I/O Bound - I/O Bound(1) - Synchronous
Keyword - I/O Bound, aiohttp
"""
import asyncio
import multiprocessing
import aiohttp
import time


session = None


def set_global_session():
    global session
    if not session:
        session = aiohttp.Session()


# 실행함수1 (다운로드)
async def request_site(session, url):

    # with session.get(url) as response:
    #     name = multiprocessing.current_process().name
    #     print(
    #         f"[{name} -> Read Contents : {len(response.content)}, Status Code : {response.status_code} from {url}"
    #     )
    async 


# 실행함수2 (요청)
async def request_all_sites(urls):
    # 멀티프로세싱 실행
    # 반드시 processes 개수 조절 후 session 객체 및 실행 시간 확인
    # with multiprocessing.Pool(initializer=set_global_session, processes=4) as pool:
    #     pool.map(request_site, urls)
    async with aiohttp.ClientSession() as session:
        # 작업 목록
        tasks = []
        for url in urls:
            # 태스크 목록 생성
            task = asyncio.ensure_future(request_site(session, url))
            tasks.append(task)

        # 태스크 확인
        # print(*tasks)
        # print(tasks)
        await asyncio.gather(*tasks, return_exception=True)


def main():
    # 테스트 URLS
    urls = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
        "https://realpython.com",
    ] * 3  # 요청

    # 실행 시간 측정
    start_time = time.time()

    # 실행
    asyncio.run(request_all_sites(urls))
    # asyncio.get_event_loop().run_until_complete(request_all_sites(urls))

    # 실행 시간 종료
    duration = time.time() - start_time

    print()

    # 결과 출력
    print(f"Downloaded {len(urls)} sites in {duration} seconds")


if __name__ == "__main__":
    main()
