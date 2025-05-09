def get_header(account_info_url: str):
    """
    Membuat header HTTP yang diperlukan untuk request ke API terbaru Binance.
    
    Parameters:
        account_info_url (str): URL referer untuk request.
    
    Returns:
        dict: Dictionary yang berisi header HTTP.
    """
    return {
  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'Content-Type': "application/json",
  'fvideo-token': "mbIVZwJQrUFix1quCdfXrv34eG1qIOWurxtdruzWmuTmHXkqD2CnHhw/GU3lIui0OsVweRoPGr0hvRcee5PQ/JYCx6R5L2x7XVH4Jw1Vpxo1nKjBJDuMY963bL9NyEtm7CP0kHAIloyVDfO9Kyv/9yb3nEaKaq/IJUkDakHCfXEDhnwl/zTSUtrvmx/aj5Iyg=5f",
  'sec-ch-ua-platform': "\"Android\"",
  'csrftoken': "8cfa4ba906019628bd92df50cc1043e7",
  'lang': "en",
  'sec-ch-ua': "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Brave\";v=\"134\"",
  'sec-ch-ua-mobile': "?1",
  'x-trace-id': "dc8df32e-ed80-478d-9eba-8e161870e0ed",
  'fvideo-id': "33dde122bc96a882a0a31240de4d8ac8478f0d49",
  'bnc-uuid': "48da46da-4ce8-4784-97dc-699584135210",
  'x-ui-request-trace': "dc8df32e-ed80-478d-9eba-8e161870e0ed",
  'x-passthrough-token': "",
  'clienttype': "web",
  'device-info': "eyJzY3JlZW5fcmVzb2x1dGlvbiI6IjgzNSwzNzYiLCJhdmFpbGFibGVfc2NyZWVuX3Jlc29sdXRpb24iOiI4MzUsMzc2Iiwic3lzdGVtX3ZlcnNpb24iOiJBbmRyb2lkIDEwIiwiYnJhbmRfbW9kZWwiOiJtb2JpbGUgIEsgIiwic3lzdGVtX2xhbmciOiJlbi1VUyIsInRpbWV6b25lIjoiR01UKzA3OjAwIiwidGltZXpvbmVPZmZzZXQiOi00MjAsInVzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoTGludXg7IEFuZHJvaWQgMTA7IEspIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMzQuMC4wLjAgTW9iaWxlIFNhZmFyaS81MzcuMzYiLCJsaXN0X3BsdWdpbiI6InhCQUlqUm4sdlhMTk9QbTYiLCJjYW52YXNfY29kZSI6ImE0ZmU3OTQxIiwid2ViZ2xfdmVuZG9yIjoiQVJNIiwid2ViZ2xfcmVuZGVyZXIiOiJNYWxpLUc3MjAtSW1tb3J0YWxpcyBNQzEyIiwiYXVkaW8iOiIxMjMuNjYzMDEwNDM4NzAwNDQiLCJwbGF0Zm9ybSI6IkxpbnV4IGFybXY4MSIsIndlYl90aW1lem9uZSI6IkFzaWEvSmFrYXJ0YSIsImRldmljZV9uYW1lIjoiQ2hyb21lIFYxMzQuMC4wLjAgKEFuZHJvaWQpIiwiZmluZ2VycHJpbnQiOiJiYzc5M2YzZjlhYjMyNDc5ZmNkNGRkZDhlYTAyMzllYyIsImRldmljZV9pZCI6IiIsInJlbGF0ZWRfZGV2aWNlX2lkcyI6IiJ9",
  'sec-gpc': "1",
  'accept-language': "en-US,en;q=0.9",
  'origin': "https://www.binance.com",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "cors",
  'sec-fetch-dest': "empty",
  'referer': "https://www.binance.com/en/futures-activity/leaderboard/user?encryptedUid=F63F56BA698CE9861024D1ADC2684136",
  'priority': "u=1, i",
  'Cookie': "BNC_FV_KEY=33dde122bc96a882a0a31240de4d8ac8478f0d49; se_gd=xgQVRQwRaBaChZSVWUFMgZZAxARUTBYV1IN9bUkZVhcUABlNWUMI1; se_gsd=ZDU2BShkJgMiFjACNDYyGgQ0VFIRAgcDUV5DUFxRUFhaI1NT1; language=en; userPreferredCurrency=USD_USD; currentAccount=; logined=y; BNC-Location=ID; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2265165582%22%2C%22first_id%22%3A%221950f082aab622-0544324976c3ab8-b457453-313960-1950f082aac1267%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22internal%22%2C%22%24latest_utm_medium%22%3A%22homepage%22%2C%22%24latest_utm_campaign%22%3A%22trading_dashboard%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk1MGYwODJhYWI2MjItMDU0NDMyNDk3NmMzYWI4LWI0NTc0NTMtMzEzOTYwLTE5NTBmMDgyYWFjMTI2NyIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjY1MTY1NTgyIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2265165582%22%7D%2C%22%24device_id%22%3A%221950f082aab622-0544324976c3ab8-b457453-313960-1950f082aac1267%22%7D; futures-layout=pro; bnc-uuid=48da46da-4ce8-4784-97dc-699584135210; BNC_FV_KEY_T=101-O2XZI%2FFBW9i8FcbmiGoski0AojTV0PeRsgOq%2BE2yVguNcGgVEKuaGaIRgIW9QOkm3%2BDsBWlRVoDvLNDLi5xMnQ%3D%3D-5WDgdVRD%2FyBrljEUcISQmw%3D%3D-ed; BNC_FV_KEY_EXPIRE=1740369699922; se_sd=gwJCQBlAEQaV1EXcZDhAgZZERVBoWEXUVRdZZU0RlFXVQGlNWVke1; s9r1=C313165DC9FD6867B043C1B3349A1C89; cr00=10F273C9F37EAF76D692DFFA4D63240A; d1og=web.65165582.7E9B1CE461286B21211F41D66D633C07; r2o1=web.65165582.465192638DACDB583E3FA6DD5583EE2C; f30l=web.65165582.636AC7E6DC698FF434368B80DC60428C; __BNC_USER_DEVICE_ID__={\"983c8cafb075d8ac82093cad828ac768\":{\"date\":1740361126287,\"value\":\"\"}}; p20t=web.65165582.A1A352051F918A20790EF28E883A7DF5; lang=en; theme=dark"
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
