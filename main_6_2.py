import time
import traceback
from selenium.webdriver import Chrome
import pandas as pd
driver = Chrome('./chromedriver')
# driver = Firefox(executable_path = './geckodriver')
# 打開網址
# url = 'https://www.google.com.tw/maps/search/%E5%93%A5%E5%A4%A7%E8%85%B8%E9%BA%B5%E7%B7%9A/@24.9891249,121.491407,14z/data=!3m1!4b1'
url = 'https://www.google.com.tw/maps'
driver.get(url)
# find -> find_element
# find_all -> find_elements
time.sleep(5) # 等待1秒
keyword = '大腸麵線'

print('輸入框輸入欲搜尋關鍵字')
mylocation = driver.find_elements_by_id('widget-mylocation')
print(len(mylocation))
while len(mylocation) == 0:
    print('mylocation')
    mylocation = driver.find_elements_by_id('widget-mylocation')
mylocation[0].click()
time.sleep(4)
input = driver.find_element_by_class_name('tactile-searchbox-input')
input.send_keys(keyword)

print('點擊搜尋')
driver.find_element_by_id('searchbox-searchbutton').click()
time.sleep(7)
bfinal = False
page = 1
list_dem = []
list_demstar = []
list_add = []
list_ben = []
list_star = []
list_date = []
list_pim = []
n = 0
while not bfinal:
    try:
        sessions = driver.find_elements_by_class_name('section-result')
        count_thispage = len(sessions)
        print('sessions數，一開始:', count_thispage)
        count_store = 0
        while len(sessions) == 0:
            sessions = driver.find_elements_by_class_name('section-result')
            print('重新取session:', len(sessions))

        for i in range(count_thispage):
            # selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: element is not attached to the page document
            # 要重新select 店家嗎
            sessions = driver.find_elements_by_class_name('section-result')
            print('每次都重新抓一次sessions:',len(sessions))
            if sessions[i].get_attribute('aria-label') != '':
                ad = sessions[i].find_elements_by_class_name('ad-badge')[0] # 會有多個廣告tag，只看第一個
                if 'display' not in ad.get_attribute('style') :
                    print('跳過這個廣告店家:',sessions[i].get_attribute('aria-label'))
                    continue # 廣告，跳過
                if i == 2 :
                    print('已搜尋'+ str(i) + '個店家了，不想找了休息')
                    break
                sessions[i].click()
                name = sessions[i].get_attribute('aria-label')
                print('=== 點擊第'+ str(i) + '個店家:', name, '===')
                time.sleep(2)
                demstar = driver.find_elements_by_class_name('section-star-display')
                for star in demstar:
                	star_0 = star.text
                	print(star.text)
                time.sleep(2)
                address = driver.find_elements_by_class_name('section-info-action-button')
                for l in address:
                	add_0 = l.get_attribute('aria-label')[0]              
                	print("地址:", l.get_attribute('aria-label'))
                time.sleep(2)
                reviews = driver.find_elements_by_class_name('widget-pane-link')
                count = 0
                while len(reviews) == 0:
                    count += 1
                    reviews = driver.find_elements_by_class_name('widget-pane-link')
                print('重試次數:', count)
                print('搜尋"所有評論tag"，數量:', len(reviews))
                time.sleep(3)
                for j in reviews:
                    if '評論' in j.get_attribute('aria-label'):
                        j.click()
                        print('已點擊所有評論:', j.get_attribute('aria-label'))
                        time.sleep(2)

                        sort = driver.find_elements_by_class_name('section-layout-flex-horizontal')
                        print('點擊選擇排序框框:', len(sort))
                        while len(sort) == 0:
                            sort = driver.find_elements_by_class_name('section-layout-flex-horizontal')
                        sort[-1].click() # 第0個是"撰寫評論"
                        time.sleep(2)
                        menuitem = driver.find_elements_by_class_name('action-menu-entry')
                        for item in menuitem:
                            if item.text == '最新':
                                item.click()
                                print('點擊選擇依時間最新來排序')
                                break

                        print('開始找section-loading')
                        loading = driver.find_elements_by_class_name('section-loading')
                        loading_count = 0
                        while len(loading) != 0:
                            loading_count += 1
                            loading = driver.find_elements_by_class_name('section-loading')
                            # print('第', str(loading_count) + '次loading')

                            lstdate = driver.find_elements_by_class_name('section-review-publish-date')
                            if len(lstdate) > 0 and '年' in lstdate[-1].text:
                                print('目前最後一個評論已超過一年，不需再往下滑了')
                                break
                            if len(loading) == 0:
                                print('沒有section-loading了，停止往下滑')
                                break
                            loading[-1].click()
                            time.sleep(2)
                        each_review = driver.find_elements_by_class_name('section-review-review-content')
                        count_each_review = 0
                        while len(each_review) == 0:
                            count_each_review += 1
                            each_review = driver.find_elements_by_class_name('section-review-review-content')
                        print('取得評論重試次數:', count_each_review)
                        print('開始顯示一年內各個評論數量:', len(each_review))
                        print('=========================================')
                        review_star = driver.find_elements_by_class_name('section-review-stars')
                        publish_date = driver.find_elements_by_class_name('section-review-publish-date')
                        for k in range(len(each_review)):
                            if '年' in publish_date[k].text:
                                print('超過一年的評論不使用，擷取評論結束')
                                break

                            word = each_review[k].text.split('(原始評論)')
                            if each_review[k].text != "":
                                print('評論日期:', publish_date[k].text)
                                print('星星數:', review_star[k].get_attribute("aria-label"))
                                if len(word) > 1:                                	
                                    print('第' + str(k+1) + '筆:', '(由 Google 提供翻譯):', word[0].replace('(由 Google 提供翻譯)', '').replace('\n', ''))
                                    # print('(原始評論):', word[-1].replace('\n', ''))
                                else:                                	
                                    print('第' + str(k+1) + '筆:', each_review[k].text)
                                list_dem.append(name)
                                list_add.append(add_0)
                                list_demstar.append(star_0)
                                list_ben.append(str(k+1))
                                list_star.append(review_star[k].get_attribute("aria-label"))
                                list_date.append(publish_date[k].text)
                                list_pim.append(each_review[k].text)
                               	
                                print('=========================================')
                                n = n + 1
                        break

                # break
                back = driver.find_elements_by_class_name('ozj7Vb3wnYq__action-button-clickable')
                back[0].click()
                print('已點擊返回店家資訊', len(back))
                time.sleep((2))

                backlist = driver.find_elements_by_class_name('section-back-to-list-button')
                backlist[0].click()
                print('已點擊返回搜尋列表', len(backlist))
                time.sleep((2))
            count_store += 1
        print('目前這頁爬完了，換下一頁')
        time.sleep(2)
        print('目前在第', page, '頁，已點過的店家數:', count_store)
        nextpage = driver.find_element_by_id('n7lv7yjyC35__section-pagination-button-next')

        print('已點擊下一頁')
        count_store = 0
        if nextpage.get_attribute('disabled') != 'true':
            if page == 2:
                break
            nextpage.click()
            page += 1
            time.sleep((2))
        else:
            bfinal = True
            print('最後一頁了')
    except:
        traceback.print_exc()
print('結束了~~~~~~~~~~~~~~~~')
dis = {
	"店家" : list_dem,
	"店家星星數" : list_demstar,
	"地址" : list_add,
	"評論編號" : list_ben,
	"星星數" : list_star,
	"評論日期": list_date,
	"評論": list_pim 
}
df = pd.DataFrame(dis)
print(df)
df.to_csv("serch.csv", encoding="utf-8", index=False)
time.sleep(5)
# driver.close()

