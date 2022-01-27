# 编码转换工具，将路径下所有".c .h .cpp .hpp .bat"文件都转为 utf-8 格式
#i!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os 
import sys 
import codecs 
import chardet 
 
gErrArray = []
 
def convert(fileName, filePath,out_enc="utf-8"): 
	try: 
		content=codecs.open(filePath,'rb').read()
		source_encoding=chardet.detect(content)['encoding'] 
		print ("fileName:%s \tfileEncoding:%s" %(fileName, source_encoding))
 
		if source_encoding != None:
			if source_encoding == out_enc or source_encoding == "ascii": # ascii编码也不要转换
				print("  curFile don't need convert!")
				return
			content=content.decode(source_encoding).encode(out_enc) 
			codecs.open(filePath,'wb').write(content)
		else :
			gErrArray.append("can not recgonize file encoding %s" % filePath)
	except Exception as err: 
		gErrArray.append("Error in %s: %s"%(filePath, err))
  
def explore(dir): 
	for root,dirs,files in os.walk(dir): 
		for file in files:
			suffix = os.path.splitext(file)[1]
			if suffix == '.h' or suffix == '.c' or suffix == '.cpp' or suffix == '.hpp' or suffix == '.bat': 
				path=os.path.join(root,file)
				convert(file, path)
  
def main(): 		
	#explore(os.getcwd()) 
	filePath = input("please input dir: \n")
	explore(filePath)
	print('\r\n---------错误统计------------')
	for index,item in enumerate(gErrArray):
		print(item)
	print('\r\n        共%d个错误！'%(len(gErrArray)))
	print('\r\n-----------------------------')
if __name__=="__main__": 
  main()