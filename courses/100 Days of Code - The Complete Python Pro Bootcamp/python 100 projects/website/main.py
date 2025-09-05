import requests

DEEPL_API_KEY = "여기에_당신의_정확한_키"
url = "https://api-free.deepl.com/v2/translate"

params = {
    "auth_key": DEEPL_API_KEY,
    "text": "Hello, how are you?",
    "target_lang": "KO"
}

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

response = requests.post(url, data=params, headers=headers)
print("응답 상태 코드:", response.status_code)
print("응답 내용:", response.text)