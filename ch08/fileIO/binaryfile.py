# 바이너리 파일 - 텍스트가 아닌 파일(음성,영상,이미지)

with open("data.bin",'wb') as f:
    data = "비가 내리다"
    f.write(data.encode())

with open("data.bin",'rb') as f:
    data = f.read()
    print(data.decode())
