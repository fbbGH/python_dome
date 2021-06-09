# 淘宝爬商品信息详情
# 2021-6-8
# 引入依赖包
from selenium import webdriver
# 导入键盘事件
from selenium.webdriver.common.keys import Keys
# 导入鼠标事件
from selenium.webdriver import ActionChains
import time
from time import sleep
import json


# 1.打开chrome+打开淘宝

driver = webdriver.Chrome()
driver.get("https://uland.taobao.com/sem/tbsearch")
# driver.maximize_window()
time.sleep(0.5)

# # 3.定位搜索框+输入商品名称
driver.find_element_by_xpath('//*[@id="J_search_key"]').send_keys('李宁')
driver.find_element_by_xpath('//*[@id="J_searchForm"]/input').click()
time.sleep(1)

# 鼠标滑动
# driver.execute_script('document.documentElement.scrollTop=10000')



# 获取商品
list = driver.find_elements_by_class_name('pc-items-item')

# 储存一页商品数据
all_list = {}

# 从第一个商品开始
i=1
while i<= len(list):
    # 间隔2秒打开一个商品
    xpa = '//*[@id="mx_5"]/ul/li[{}]/a'.format(i)
    driver.find_element_by_xpath(xpa).click()
    # 获取当前所有页面句柄
    handles = driver.window_handles
    driver.switch_to.window(handles[-1])

    # 测试窗口
    driver.execute_script('document.documentElement.scrollTop=10000')

    # 定位商品详情
    rList = driver.find_elements_by_xpath('//*[@id="J_AttrUL"]//li')
    lis=[]
    j=1
    for r in rList:
        contentList = r.text.split('\n')
        lis.insert(j, contentList)
        j=j+1
    print(lis)
    all_list[i] = lis
    time.sleep(4)
    driver.close()
    # 切换到最开始打开的窗口
    time.sleep(1)
    driver.switch_to.window(handles[0])
    # print(xpa,'正在打开下个窗口')
    i=i+1

# 生成json
with open("1.json","w",encoding='utf-8') as f:
    json.dump(all_list,f,ensure_ascii=False,sort_keys=True, indent=4);
    print(u'加载入文件完成...');

driver.quit()