import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from .house import House


def search() -> House:
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    driver = webdriver.Chrome("driver/chromedriver", options=options)
    driver.implicitly_wait(1)

    try:
        READ_WAIT_SECONDS = 1
        url = "https://new.land.naver.com/complexes/1464?ms=37.3999576,126.9559953,17&a=APT:ABYG:JGC:JGB&b=A1&e=RETAIL&h=66&i=132&l=300"
        driver.get(url)

        # 시세/실거래가
        driver.find_element(by=By.CSS_SELECTOR, value="#summaryInfo > div.complex_summary_info > div.complex_detail_link > button:nth-child(2)").click()
        time.sleep(READ_WAIT_SECONDS)

        # 평으로 전환
        driver.find_element(by=By.CSS_SELECTOR, value="#ct > div.map_wrap > div.detail_panel > div > div.detail_contents_inner > div.detail_fixed > div > button").click()
        time.sleep(READ_WAIT_SECONDS)

        # 평
        area_path = "#tab5 > span"
        area = driver.find_element(by=By.CSS_SELECTOR, value=area_path).text
        driver.find_element(by=By.CSS_SELECTOR, value=area_path).click()
        time.sleep(READ_WAIT_SECONDS)

        # 매매가
        sales_price = driver.find_element(by=By.CSS_SELECTOR, value="#tabpanel1 > div.detail_price_area > div.detail_asking_price > div > div:nth-child(2) > strong").text

        # 전세가
        driver.find_element(by=By.CSS_SELECTOR, value="#marketPriceTab2").click()
        time.sleep(READ_WAIT_SECONDS)
        jeonse_price = driver.find_element(by=By.CSS_SELECTOR, value="#tabpanel1 > div.detail_price_area > div.detail_asking_price > div.detail_price_table > div:nth-child(2) > strong").text

        # 단지정보
        driver.find_element(by=By.CSS_SELECTOR, value="#summaryInfo > div.complex_summary_info > div.complex_detail_link > button:nth-child(1)").click()
        time.sleep(READ_WAIT_SECONDS)
        address = driver.find_element(by=By.CSS_SELECTOR,
                                      value="#detailContents1 > div.detail_box--complex > table > tbody > tr:nth-child(8) > td > p:nth-child(1)").text

        # 세대수
        households_count = driver.find_element(by=By.CSS_SELECTOR,
                                               value="#detailContents1 > div.detail_box--complex > table > tbody > tr:nth-child(1) > td:nth-child(2)").text

        # 사용승인일
        approval_date = driver.find_element(by=By.CSS_SELECTOR,
                                            value="#detailContents1 > div.detail_box--complex > table > tbody > tr:nth-child(2) > td:nth-child(2)").text

        # 용적률
        floor_area_ratio = driver.find_element(by=By.CSS_SELECTOR,
                                               value="#detailContents1 > div.detail_box--complex > table > tbody > tr:nth-child(3) > td:nth-child(2)").text

        # 제목
        title = driver.find_element(by=By.CSS_SELECTOR, value="#complexTitle").text

        return House(address, title, area, sales_price, jeonse_price, households_count, approval_date, floor_area_ratio)

    finally:
        driver.quit()
