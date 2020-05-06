#Author: Xinnan SHEN
#Student ID: 1051380
#File Name: crawl.py
#Usage: Crawling data from the web
import requests
import re
import codecs
import time
import os
def main():
	current_path=os.path.abspath(os.curdir)
	#create a folder to store files
	file_folder=os.path.join(current_path,"pages")
	if not os.path.exists(file_folder):
		os.makedirs(file_folder)
	i=2967
	while i>500:
		url="https://climate.nasa.gov/news/"
		time.sleep(1)
		url=url+str(i)
		headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
		response=requests.get(url=url,headers=headers)#download contents from online pages
		print(response.url)
		response.encoding='utf-8'
		html=response.text
		#page does not exist,continue for the next page
		if html.find("Page not found")!=-1:
			print(str(i)+":error")
			i=i-1
			continue
		content_=re.findall(r"<section class='content_page(.*?)</section>",html,re.DOTALL)
		#find the contents in the page
		if len(content_)==0:
			print(str(i)+":error")
			i=i-1
			continue
		content=content_[0]
		del_strs=re.findall(r"<div class='author'>(.*?)</div>",content,re.DOTALL)
		for s in del_strs:
			content=re.sub(s,'',content)
		paras=re.findall(r"<p>(.*?)</p>",content,re.DOTALL)
		content_string=""
		for p in paras:
			if p.find("<")!=-1 and p.find("<a")==-1 and p.find("</a")==-1:
				continue
			else:
				content_string=content_string+p
		#delete some special characters in the content
		del_strs=re.findall(r"&(.*?);",content_string,re.DOTALL)
		for s in del_strs:
			content_string=re.sub(s,'',content_string)
		content_string=re.sub("&;",'',content_string)
		pattern=re.compile(r"<[^>]+>")
		content_string=pattern.sub('',content_string)
		while content_string!="" and content_string[-1]!='.':
			content_string=content_string[0:len(content_string)-1]
		#get the address of file
		addr=os.path.join(file_folder,str(i)+".txt")
		#save contents into file
		f=codecs.open(addr,"w","utf-8")
		f.write(content_string)
		f.close()
		print(str(i)+":success")
		i=i-1
	j=1
	file_folder=os.path.join(current_path,"othertopics")
	if not os.path.exists(file_folder):
		os.makedirs(file_folder)
	url="https://www.voanews.com"
	for suburl in ["/science-health","/arts-culture","/economy-business"]:
		for urlpage in range(0,30):
			real_url=url+suburl+"?date=&to=&page="+str(urlpage)
			headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
			response=requests.get(url=real_url,headers=headers)
			response.encoding='utf-8'
			html=response.text
			content_list=re.findall(r'<a class="teaser__title-link" href="(.*?)" title=(.*?)>',html,re.DOTALL)
			for i in content_list:
				content_url=url+str(i[0])
				response_content=requests.get(url=content_url,headers=headers)
				response_content.encoding='utf-8'
				content_html=response_content.text
				content=re.findall(r'<div class="article__body">(.*?)</div>',content_html,re.DOTALL)
				if len(content)==0:
					print(str(j)+":error")
					j=j+1
					continue
				content_string=content[0]
				del_strs=re.findall(r"&(.*?);",content_string,re.DOTALL)
				for s in del_strs:
					content_string=re.sub(s,'',content_string)
				content_string=re.sub("&;",'',content_string)
				pattern=re.compile(r"<[^>]+>")
				content_string=pattern.sub('',content_string)
				addr=os.path.join(file_folder,str(j)+".txt")
				f=codecs.open(addr,"w","utf-8")
				f.write(content_string)
				f.close()
				print(str(j)+":success")
				j=j+1
	return
if __name__ == '__main__':
	main()
