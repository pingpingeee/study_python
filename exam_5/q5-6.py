file_names = ["file1.py", "file2.txt", "file3.pptx", "file4.doc"]

for i in range(len(file_names)):
    file1 = file_names[i].split(".")
    print(file_names[i] + " => " + "파일명 : " + file1[0]+ "," +"확장자 : " + file1[1])