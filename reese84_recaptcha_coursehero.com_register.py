from math import fabs
import requests
import json
import uuid

# captcha api config on https://www.clearcaptcha.com 
clearcaptcha_reese84_api="http://api.clearcaptcha.com/captcha/incapsula_reese84_sub";
clearcaptcha_recaptcha_api="http://api.clearcaptcha.com/captcha/recaptcha_enterprise_v2v3";
token = 'd7897e0ac82d47909af94a4a9b30test'
jsurl = "https://www.coursehero.com/Ifainesse-What-mine-Alasterd-the-How-I-haile-Lad"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

session = requests.Session()

headers={
        "Content-Type":"text/plain; charset=utf-8",
        "Host": "www.coursehero.com",
        "User-Agent": user_agent,
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.coursehero.com/register/",
        "Origin": "https://www.coursehero.com",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Connection": "keep-alive",
    }

response = session.get("https://www.coursehero.com/register/",headers=headers,verify=False)


post_data = {
    "token": token,
    "jsurl": jsurl,
    "user_agent": user_agent,
}

response = requests.post(clearcaptcha_reese84_api, data=post_data)
if response.status_code == 200:
    response_data = response.json()
    print(response_data)
else:
    print({
        "error": "api error",
        "status_code": response.status_code,
        "response": response.text
    })
    

post_data=response_data.get("data", {}).get("post_data", {})


post_url="https://www.coursehero.com/Ifainesse-What-mine-Alasterd-the-How-I-haile-Lad?d=www.coursehero.com"

response = session.post(post_url, data=post_data,verify=False)
response_data = response.json()
reese84=response_data.get("token", {})

post_data =  {
    "token": token,
    "sitekey": "6LeIuD4bAAAAAPcFHlgJrN8t44BjPiFWmns2-Dt3",
    "referer":"https://www.coursehero.com",
    "recaptcha_anchor_size":"normal",
    "page_title":"Sign Up - Course Hero",
}
response = requests.post(clearcaptcha_recaptcha_api, data=post_data)
response_data = response.json()
recaptcha_token=response_data.get("data", {}).get("recaptcha_token", {})


register_url="https://www.coursehero.com/api/v1/users/"
post_data =  {
    "email": "test@gmail.com",
    "password": "test123456",
    "userType":"student",
    "schoolName":"Hashtnagar Institute of Education, Charsadda",
    "schoolIdString":"123658",
    "captchaToken":recaptcha_token,
}

cookies = {"reese84": reese84}
session.cookies.update(cookies);
headers["Content-Type"]="application/x-www-form-urlencoded"
headers["X-NewRelic-ID"]="Ug8CUVVbGwIDUlVUBgkGVg=="
response = session.post(register_url, data=post_data,headers=headers,verify=False)
if response.status_code == 200:
    response_data = response.json()
else:
    response_data={
        "error": "api error",
        "status_code": response.status_code,
        "response": response.text
    }
    
print(response_data)
