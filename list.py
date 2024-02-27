from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup as bs4
import json

song_name = input("Enter a song for me put on for you: ")


driver = webdriver.Chrome()
driver.get("https://www.youtube.com")
element = driver.find_element(By.XPATH, "//input[@id='search']")
element.send_keys(song_name)
time.sleep(1)
element.send_keys(Keys.ENTER)
time.sleep(3)
lis = []
soup = bs4(driver.page_source, 'html.parser')
lis = []
a = [i for i in soup.find_all('a', attrs={'href':True, 'id':"video-title"})]
lis = [i['title'] for i in soup.find_all('a', attrs={'href':True, 'id':"video-title"})]
for i in lis:
	print(i)

video_info = []
for a in a:
	video_info.append({
			'title': a['title'],
			'link': a['href']
		}) 
video_info_json = json.dumps(video_info, indent=4)
video_infos = json.loads(video_info_json)
link = input("type out the name of one of the videos to play it(case sensitive): \n")
for k in video_infos:
	if(k['title'] == link):
		video = k['link']
ele = driver.find_element(By.XPATH, "//a[@href='{}']".format(video))
ele.click()
driver.maximize_window()
while True:
	pass
driver.close()