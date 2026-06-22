# 서울도서관 새로 들어온 도서정보
# https://data.seoul.go.kr/dataList/OA-15484/S/1/datasetView.do

import requests
import xml.etree.ElementTree as ET
import json

def fetch_seoul_library_data():
    API_KEY = "6a776b74577567633130347170457359"  # 발급받은 인증키
    BASE_URL = "http://openapi.seoul.go.kr:8088/{}/xml/SeoulLibNewArrivalInfo/{{}}/{{}}".format(API_KEY)

    start_index = 1
    batch_size = 1000
    books = []

    while True:
        end_index = start_index + batch_size - 1
        url = BASE_URL.format(start_index, end_index)
        response = requests.get(url)

        if response.status_code != 200:
            print("Error: Unable to fetch data, status code:", response.status_code)
            break

        try:
            root = ET.fromstring(response.text)

            result_code = root.find("RESULT/CODE")
            if result_code is not None and result_code.text != "INFO-000":
                print("API Error:", root.find("RESULT/MESSAGE").text)
                break

            rows = root.findall("row")
            if not rows:
                break  # 더 이상 데이터가 없으면 종료

            for item in rows:
                book = {
                    "TITLE": item.findtext("TITLE", "N/A"),
                    "AUTHOR": item.findtext("AUTHOR", "N/A"),
                    "PUBLISHER": item.findtext("PUBLISHER", "N/A"),
                    "PUBLISHER_YEAR": item.findtext("PUBLISHER_YEAR", "N/A"),
                    "TYPE": item.findtext("TYPE", "N/A"),
                    "LOCA": item.findtext("LOCA", "N/A"),
                    "INDT": item.findtext("INDT", "N/A"),
                }
                books.append(book)

            start_index += batch_size  # 다음 1000개 조회
        except ET.ParseError as e:
            print("XML Parse Error:", e)
            break

    print(f'데이터 개수 : {len(books)}')
    return books

def save_to_json(data, filename="seoul_library_books.json"):
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    data = fetch_seoul_library_data()
    if data:
        save_to_json(data)
        # for book in data:
        #     print(book)
