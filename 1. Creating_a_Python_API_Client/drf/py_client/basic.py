import requests

endpoint = "https://httpbin.org/status/200"
endpoint = "https://httpbin.org/anything"  # JSON 응답(REST API)
# endpoint = "https://httpbin.org/" # HTML 문서 응답(보통의 웹사이트)



get_response = requests.get(endpoint) # HTTP GET 요청 보내기
print(f"get_response : {get_response}") # 응답 객체 출력
print(f"get_response.text : {get_response.text}") # 응답 본문 출력

# HTTP 요청 -> HTML
# REST API HTTP 요청 -> JSON
# JavaSCripts 객체 표기법 ~ Python 딕셔너리 유사

#print(f"get_response.json() : {get_response.json()}") # 응답 본문을 JSON으로 파싱하여 출력(Null을 None으로 변환)





#get_response = requests.get(endpoint, json={"query":"Hello World"}) # HTTP GET 요청 보내기(쿼리 파라미터 포함) => Data 부분에 우리의 딕셔너리가 채워져 있음
#print(f"get_response.json() : {get_response.json()}") # 응답 본문을 JSON으로 파싱하여 출력(Null을 None으로 변환)


# 데이터를 전송하는 또 다른 방법
#get_response = requests.get(endpoint, data={"query":"Hello World"}) # HTTP GET 요청 보내기(데이터 포함) => Form 부분에 우리의 딕셔너리가 채워져 있음(폼 데이터로 간주)
#print(f"get_response.json() : {get_response.json()}") 
#print(f"get_response.status_code : {get_response.status_code}") # 응답 상태 코드 출력