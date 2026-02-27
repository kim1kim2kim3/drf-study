import requests


#endpoint = "http://127.0.0.1:8000/" # Django REST Framework API 엔드포인트
#endpoint = "http://localhost:8000/" # Django REST Framework API 엔드포인트


#get_response = requests.get(endpoint, json={"query":"Hello World"}) # HTTP GET 요청 보내기(쿼리 파라미터 포함) => Data 부분에 우리의 딕셔너리가 채워져 있음
#print(f"get_response.text() : {get_response.text}") # HTML 입력을 받아서 출력
#print(f"get_response.status_code : {get_response.status_code}") # 응답 상태 코드 출력




endpoint = "http://127.0.0.1:8000/api" # Django REST Framework API 엔드포인트
endpoint = "http://localhost:8000/api" # Django REST Framework API 엔드포인트


get_response = requests.get(endpoint, json={"query":"Hello World"}) # HTTP GET 요청 보내기(쿼리 파라미터 포함) => Data 부분에 우리의 딕셔너리가 채워져 있음

print(f"get_response.text() : {get_response.text}")
print(f"get_response.text() : {type(get_response.text)}")

print(f"get_response.json() : {get_response.json()}") # json 입력을 받아서 출력
print(f"get_response.json() : {type(get_response.json())}") # json 입력을 받아서 출력

print(f"get_response.status_code : {get_response.status_code}") # 응답 상태 코드 출력

