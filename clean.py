#Author: Xinnan SHEN
#Student ID: 1051380
#File Name: crawl.py
#Usage: Change the crawled data into JSON format
import os
import codecs
def merge_dict(d1,d2):
	return {**d1,**d2}
def build_json():
	current_path=os.path.abspath(os.curdir)
	file_folder=os.path.join(current_path,"pages")
	if not os.path.exists(file_folder):
		print("error:path not found")
		return
	fout=codecs.open(os.path.join(current_path,"externaldata.json"),"w","utf-8")
	i=1168
	dict_res={}
	for file in sorted(os.listdir(file_folder)):
		full_path=os.path.join(file_folder,file)
		fin=codecs.open(full_path,"r","utf-8")
		text=fin.read()
		if len(text.replace(' ','').replace('\n','').replace('\r',''))==0:
			print(file+" empty file")
			continue
		fin.close()
		dict_temp={"text":text,"label":0}
		dict_res["train-"+str(i)]=dict_temp
		print(str(i)+" completed.")
		i=i+1
	file_folder=os.path.join(current_path,"othertopics")
	if not os.path.exists(file_folder):
		print("error:path not found")
		return
	for file in sorted(os.listdir(file_folder)):
		full_path=os.path.join(file_folder,file)
		fin=codecs.open(full_path,"r","utf-8")
		text=fin.read()
		if len(text.replace(' ','').replace('\n','').replace('\r',''))==0:
			print(file+" empty file")
			continue
		fin.close()
		dict_temp={"text":text,"label":0}
		dict_res["train-"+str(i)]=dict_temp
		print(str(i)+" completed.")
		i=i+1
	fout.write(str(dict_res))
	fout.close()
	return
def combine_json():
	current_path=os.path.abspath(os.curdir)
	fold=codecs.open(os.path.join(current_path,"train.json"),"r","utf-8")
	s=fold.read()
	fold.close()
	dold=eval(s)
	fnew=codecs.open(os.path.join(current_path,"externaldata.json"),"r","utf-8")
	s=fnew.read()
	fnew.close()
	dnew=eval(s)
	dcombine=merge_dict(dold,dnew)
	s=str(dcombine)
	fcombine=codecs.open(os.path.join(current_path,"newtrain.json"),"w","utf-8")
	fcombine.write(s)
	fcombine.close()
	print("combination completed.")
	return
def main():
	build_json()
	combine_json()
	return
if __name__ == '__main__':
	main()
