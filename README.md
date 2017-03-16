# crawl
* 검색 결과 수집 스크립트.

## 설치
```python
$ python setup.py install
```

## 사용 예시
```
# sample.txt에 있는 질의들의 web1 검색 결과를 sample.serp.txt 파일에 저장.
# 'web1'은 아래에서 설명할 설정 파일에서 section name이다.
# 총 10개의 쓰레드로 검색 결과 동시에 수집.
crawl --query sample.txt --outfile sample.serp.txt --workers 10 web1
```

## 준비사항
### putils
* https://github.daumkakao.com/SRCHMDL/putils

### crawl.cfg 설정 파일
* config 파일명은 옵션으로도 전달 가능.
* section별로 base_url은 반드시 존재해야 한다.
* base_url에 함께 넘어갈 옵션들도 적어준다.
* 예를 들어 아래와 같이 기술된 파일이라면, 실제로 호출되는 URL은 다음과 같다.

```
# cfg 파일 기술 예시

[section name]
base_url = http://10.41.105.121:8887/front/web/tab.py
p = 1
search_timeout = 60
gateway_timeout = 60


# 실제 호출되는 URL
http://10.41.105.121:8887/front/web/tab.py?p=1&search_timeout=60&gateway_timeout=60
```

## 중요 옵션
### --element
* 문서에서 추출하려는 필드값들을 연달아 적어준다.
* 예를 들어 url, title, content 섹션을 가져와야 한다면, 다음과 같이 기술한다.
```
# url은 default.
crawl --element title --element content ...
```

### --scores
* 프론트 필드 중에 'scores'에는 각 calculator들의 score를 리스트로 저장한다.
* 이 필드값을 가져와야 하는 경우, --scores를 사용한다.

### --workers
* 검색 결과를 동시에 수집할 worker의 개수.
* 질의 셋을 5개로 나누어 동시에 수집하려면 다음과 같이 수집한다.
```
crawl --workers 5 ...
```

## 결과 파일
* [qid] [query] [qtc] [rank] [url] 가 기본 필드이고 (qid는 해당 정보가 있는 경우에만)
* 이후에 --element 로 기술한 필드들이 순서대로 추가된다.
```
# 검색 실행 예시
echo "kakao" | crawl --log_level DEBUG --element cafename --element caferank cafe

# 결과
kakao	1	1	http://cafe.daum.net/ok211/680V/1035602	뉴빵카페 　	195
kakao	1	2	http://cafe.daum.net/stop5go/t16/9657	대리운전 대리기사 (달빛기사카페)	133
...
```
