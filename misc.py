def get_header(account_info_url: str):
    """
    Membuat header HTTP yang diperlukan untuk request ke API terbaru Binance.
    
    Parameters:
        account_info_url (str): URL referer untuk request.
    
    Returns:
        dict: Dictionary yang berisi header HTTP.
    """
    return {
        'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Mobile Safari/537.36",
        'Accept-Encoding': "gzip, deflate, br, zstd",
        'Content-Type': "application/json",
        'fvideo-token': "H8spWgcAEvM7iYK6dvNqwEPHFTXMxw2WuM6bKzKqQhSn9VbfzWprbxd0EQtH5WFmq80ej0cpzXv5e2frUDpfzw+4i0fK6QWqw14vU9lqJ6GCAk/PQOvxxv6T1isaW5/sdLHc6KdC5hYIB9QANmdJAqSRQwROMe4v06FKdhQFDecgwG6jJtmBgIpSWoyDEZQDE=20",
        'sec-ch-ua-platform': "\"Android\"",
        'csrftoken': "e513b42464564957d1bed37536a02e88",
        'lang': "en",
        'sec-ch-ua': "\"Not(A:Brand\";v=\"99\", \"Brave\";v=\"133\", \"Chromium\";v=\"133\"",
        'sec-ch-ua-mobile': "?1",
        'x-trace-id': "e52bf2c9-f1db-4fb1-859c-f4c350c597c9",
        'fvideo-id': "33dde122bc96a882a0a31240de4d8ac8478f0d49",
        'bnc-uuid': "19b2840d-bf7d-43ee-a867-f6959a52f095",
        'x-ui-request-trace': "e52bf2c9-f1db-4fb1-859c-f4c350c597c9",
        'x-passthrough-token': "",
        'clienttype': "web",
        'device-info': "eyJzY3JlZW5fcmVzb2x1dGlvbiI6IjgzNSwzNzYiLCJhdmFpbGFibGVfc2NyZWVuX3Jlc29sdXRpb24iOiI4MzUsMzc2Iiwic3lzdGVtX3ZlcnNpb24iOiJBbmRyb2lkIDEwIiwiYnJhbmRfbW9kZWwiOiJtb2JpbGUgIEsgIiwic3lzdGVtX2xhbmciOiJlbi1VUyIsInRpbWV6b25lIjoiR01UKzA3OjAwIiwidGltZXpvbmVPZmZzZXQiOi00MjAsInVzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoTGludXg7IEFuZHJvaWQgMTA7IEspIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMzMuMC4wLjAgTW9iaWxlIFNhZmFyaS81MzcuMzYiLCJsaXN0X3BsdWdpbiI6ImpaTU9IREIsdDltYjA1RksiLCJjYW52YXNfY29kZSI6IjYwM2NhNDI3Iiwid2ViZ2xfdmVuZG9yIjoiQVJNIiwid2ViZ2xfcmVuZGVyZXIiOiJNYWxpLUc3MjAtSW1tb3J0YWxpcyBNQzEyIiwiYXVkaW8iOiIxMjMuNTU3MDQ0NjE0MjMwMTEiLCJwbGF0Zm9ybSI6IkxpbnV4IGFybXY4MSIsIndlYl90aW1lem9uZSI6IkFzaWEvSmFrYXJ0YSIsImRldmljZV9uYW1lIjoiQ2hyb21lIFYxMzMuMC4wLjAgKEFuZHJvaWQpIiwiZmluZ2VycHJpbnQiOiI5MTdkNTk2MDJhOTdkNDQ1YmI1OTcwODMwNzFiYmIxYSIsImRldmljZV9pZCI6IiIsInJlbGF0ZWRfZGV2aWNlX2lkcyI6IiJ9",
        'sec-gpc': "1",
        'accept-language': "en-US,en;q=0.7",
        'origin': "https://www.binance.com",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': account_info_url,
        'priority': "u=1, i",
        'Cookie': "bnc-uuid=19b2840d-bf7d-43ee-a867-f6959a52f095; BNC_FV_KEY=33dde122bc96a882a0a31240de4d8ac8478f0d49; aws-waf-token=bc7f8837-b1a8-4f2f-b28c-b66c49051194:BgoAYagC2RADAAAA:lLHiu9CUAkKx59JXMnAfq6UJt7Wo4E/SC8vH3CfFdk8IRIBV2SA9vXLN2XcU+UOwqgd3ZEB8nlGvyxoGLrljKpgeVDL87OhVi070UehfjsgGCVHCey265YHY3toppvsTBY+u4yMzTSS87TazI6M9eIQe7kJc6AsNRlEprrQiqoZteZzaJTEThJ2xDlTZIOgNT395bEgw5Qndog==; se_gd=xgQVRQwRaBaChZSVWUFMgZZAxARUTBYV1IN9bUkZVhcUABlNWUMI1; se_gsd=ZDU2BShkJgMiFjACNDYyGgQ0VFIRAgcDUV5DUFxRUFhaI1NT1; language=en; userPreferredCurrency=USD_USD; BNC_FV_KEY_T=101-rfBfEQs4VuQDMCkRVR88LK%2BKu4jSy7338Hvl1XKG%2Fk6Ixz1YfLHAyC427w9b5TzNyhwyYq0kL73CqMYVREMl9g%3D%3D-aDmQC%2F8GfzkPCf4jGbZ6xQ%3D%3D-9f; BNC_FV_KEY_EXPIRE=1739946777589; cr00=ED98096C0D3487A16A5482D7B9259E07; d1og=web.65165582.F2E8BB80F99FAA3FC56D74FA52C9E2A3; r2o1=web.65165582.0450FFD2215D1341479455AE75863578; f30l=web.65165582.4B668C0AC2286281DDD8BA38E07A81EB; currentAccount=; logined=y; BNC-Location=ID; __BNC_USER_DEVICE_ID__={\"983c8cafb075d8ac82093cad828ac768\":{\"date\":1739925457381,\"value\":\"\"}}; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22chatgpt.com%22%2C%22%24latest_utm_medium%22%3A%22GlobalSocial%22%2C%22%24latest_utm_campaign%22%3A%22GlobalSocial%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiIiwgIiRpZGVudGl0eV9sb2dpbl9pZCI6IiJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%22%22%7D; futures-layout=pro; p20t=web.65165582.11A4B424E146C79C675950822EA62449; lang=en; theme=dark"
    }

def get_json(uid: str):
    """
    Membuat payload JSON yang diperlukan untuk request ke API terbaru Binance.
    
    Parameters:
        uid (str): User ID (UID) dari akun Binance yang ingin dilacak.
    
    Returns:
        dict: Dictionary yang berisi payload JSON.
    """
    return {
        'encryptedUid': uid,
        'tradeType': 'PERPETUAL'
    }
