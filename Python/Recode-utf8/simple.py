import chardet
# 检测字符串编码
with open(txtfilename, 'rb') as f:
    txt = f.read(1000)
    c = chardet.detect(txt)
    print(c)
# 转换字符编码到utf-8
encoding = c['encoding']
if encoding != 'utf-8':
    with open(txtfilename, 'r', encoding=encoding) as f:
        text = f.read()
    with open(txtfilename, 'w', encoding='utf-8') as f:
        f.write(text)