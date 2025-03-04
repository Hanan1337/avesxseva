import requests
import json

url = "https://www.binance.com/bapi/futures/v2/private/future/leaderboard/getOtherPosition"

payload = {
  "encryptedUid": "86D933788100EB972D1F417848557B92",
  "tradeType": "PERPETUAL"
}

headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'Content-Type': "application/json",
  'fvideo-token': "WG4FpEMS4yehWVfWnO3I5YrXzjY/AIfaZv4f/fqOlHfOBYqJ3u0nAAasPnernm5LBn0YBYicjrgK9XjejDu/w+NBfd4e74k30foL+blKhLtMBn2Q0cWPWZS00xAjVh41ADTc+kX5LdK/cpiWTpl93O8t34FttNmfXuCZzbc+asVfe6Lo8V23R3iGMWd2/lTMU=6a",
  'sec-ch-ua-platform': "\"Android\"",
  'csrftoken': "4adae86afd683f51960dde44d733d4d0",
  'lang': "en",
  'sec-ch-ua': "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Brave\";v=\"134\"",
  'sec-ch-ua-mobile': "?1",
  'x-trace-id': "6243e2bd-f716-4374-8f77-17173615da50",
  'fvideo-id': "33dde122bc96a882a0a31240de4d8ac8478f0d49",
  'bnc-uuid': "7d3480e4-25ee-456a-9be1-9f6717d3b8f3",
  'x-ui-request-trace': "6243e2bd-f716-4374-8f77-17173615da50",
  'x-passthrough-token': "",
  'clienttype': "web",
  'device-info': "eyJzY3JlZW5fcmVzb2x1dGlvbiI6IjgzNSwzNzYiLCJhdmFpbGFibGVfc2NyZWVuX3Jlc29sdXRpb24iOiI4MzUsMzc2Iiwic3lzdGVtX3ZlcnNpb24iOiJBbmRyb2lkIDEwIiwiYnJhbmRfbW9kZWwiOiJtb2JpbGUgIEsgIiwic3lzdGVtX2xhbmciOiJlbi1VUyIsInRpbWV6b25lIjoiR01UKzA3OjAwIiwidGltZXpvbmVPZmZzZXQiOi00MjAsInVzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoTGludXg7IEFuZHJvaWQgMTA7IEspIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMzQuMC4wLjAgTW9iaWxlIFNhZmFyaS81MzcuMzYiLCJsaXN0X3BsdWdpbiI6IlRvVVNSUXYsQkVLTkdpd1kiLCJjYW52YXNfY29kZSI6IjE4NWM5NDY3Iiwid2ViZ2xfdmVuZG9yIjoiQVJNIiwid2ViZ2xfcmVuZGVyZXIiOiJNYWxpLUc3MjAtSW1tb3J0YWxpcyBNQzEyIiwiYXVkaW8iOiIxMjQuMDEyNjM4NDg4MzY5NyIsInBsYXRmb3JtIjoiTGludXggYXJtdjgxIiwid2ViX3RpbWV6b25lIjoiQXNpYS9KYWthcnRhIiwiZGV2aWNlX25hbWUiOiJDaHJvbWUgVjEzNC4wLjAuMCAoQW5kcm9pZCkiLCJmaW5nZXJwcmludCI6ImYzZDMzY2E4ZjI3N2RkZjg0Yjc3Yjk0MjU1MWU2Nzg5IiwiZGV2aWNlX2lkIjoiIiwicmVsYXRlZF9kZXZpY2VfaWRzIjoiIn0=",
  'sec-gpc': "1",
  'accept-language': "en-US,en;q=0.9",
  'origin': "https://www.binance.com",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "cors",
  'sec-fetch-dest': "empty",
  'referer': "https://www.binance.com/en/futures-activity/leaderboard/user/um?encryptedUid=86D933788100EB972D1F417848557B92",
  'priority': "u=1, i",
  'Cookie': "BNC_FV_KEY=33dde122bc96a882a0a31240de4d8ac8478f0d49; language=en; currentAccount=; logined=y; BNC-Location=ID; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2265165582%22%2C%22first_id%22%3A%221950f082aab622-0544324976c3ab8-b457453-313960-1950f082aac1267%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22internal%22%2C%22%24latest_utm_medium%22%3A%22homepage%22%2C%22%24latest_utm_campaign%22%3A%22trading_dashboard%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk1MGYwODJhYWI2MjItMDU0NDMyNDk3NmMzYWI4LWI0NTc0NTMtMzEzOTYwLTE5NTBmMDgyYWFjMTI2NyIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjY1MTY1NTgyIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2265165582%22%7D%2C%22%24device_id%22%3A%221950f082aab622-0544324976c3ab8-b457453-313960-1950f082aac1267%22%7D; futures-layout=pro; se_gd=QVbVQQhkaFbBVIP8ZExFgZZDADBUTBTW1BU9QUk9lFcUwCVNWV5W1; se_gsd=CjgmOztnIgAjCQkCNDUyMzUHUFNWBQIFUVVFU1xaV1FaHVNT1; cr00=C4A6BFA9980E07400B5E0CF7E07E76E8; d1og=web.65165582.2F4B1CE9CF950147F91FF203ADBDA1EE; r2o1=web.65165582.D9C2454CCD0A2E4704B2DD6964B6D967; f30l=web.65165582.E7B6AF8943EFB034AB2BC0E54FD3FD1F; __BNC_USER_DEVICE_ID__={\"983c8cafb075d8ac82093cad828ac768\":{\"date\":1740808837864,\"value\":\"\"}}; bnc-uuid=7d3480e4-25ee-456a-9be1-9f6717d3b8f3; BNC_FV_KEY_T=101-2eiOm2Jk2Ys6FMXylAKGkEa0LexpQmR76awUYxja0Uclco23IfqNwhhCk1u1vXrySRXSR4W%2FyHjtM7eRlUn5fg%3D%3D-AEei%2FHqrqhrRHg%2BGY83lew%3D%3D-dd; BNC_FV_KEY_EXPIRE=1741072552898; p20t=web.65165582.ADAEEB30485FBD8A42124A1B8664792D; lang=en; theme=dark"
}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.text)
