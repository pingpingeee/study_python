file_names = ["file1.py", "file2.txt", "file3.pptx", "file4.doc"]

for i in range(len(file_names)):
    file1 = file_names[i].split(".")
    print(
        file_names[i] + " => " + "파일명 : " + file1[0] + ", " + "확장자 : " + file1[1]
    )
# 출력
# file1.py => 파일명 : file1, 확장자 : py
# file2.txt => 파일명 : file2, 확장자 : txt
# file3.pptx => 파일명 : file3, 확장자 : pptx
# file4.doc => 파일명 : file4, 확장자 : doc
