from collections import deque

###### 전체 프로세스
# 1. tor 브라우저 열기
# 2. root_url deque에 삽입
# 3. deque.popleft() ->  html안에서 file list 저장 및 root_url + & 형태의 url이 있다면 큐에 담기
# 4. deque가 빌 때까지 3번 행위를 반복
# 5. 전체 파일 리스트 txt로 저장
#######



def html(root_url):

    #현재 url로 html 읽어오기 소켓 통신 매번 요청할떄마다 연결해야하는지 유지만 가능한지 검토
    print("html 추출")
    url_pattern = []
    file_list =[]
    #만약 읽어온 html에서 herf = " " 구조안에 root_url+ & 형태의 url이 있다고 하면 url 패턴에 넣는다
    #또한 파일 리스트를 필터링해서 file_list에 추가

    return url_pattern,file_list

def open_tor(): #tor 웹 열기
    return None

def save_txt(total_file): #전체 폴더 리스트를 txt 파일 내리기, file format은 excel 등 다른 형태일 수 도 있음
    return None

##### 로직 시작################
open_tor()

root_url = 'test'
total_file =[]

q = deque()

q.append(root_url)

while q:

    url = q.popleft()

    url_list, file_list = html(url) #현재 url를 통해서 html 뽑고 하위 폴더 리스트로 받기
    total_file.append(file_list) #전체 파일 리스트에 추가

    if len(url_list) > 0: #하위폴더가 하나라도 있으면 큐에 넣기
        for i in url_list: #하위 폴더 url 큐에 추가
            q.append(i)

#전체 파일 리스트 탐색을 끝내면 txt file로 저장
save_txt(total_file)

print("darkweb file list scraping complete")
