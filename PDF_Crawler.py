import re
import PyPDF2

file_name = input("Enter PDF file name inside this folder with extension '.pdf': ")
object = PyPDF2.PdfFileReader(file_name)

NumPages = object.getNumPages()

txt1 = input("Enter text to find: ")
String = txt1

for i in range(0, NumPages):
    PageObj = object.getPage(i)
    print("this is page " + str(i)) 
    Text = PageObj.extractText() 
    # print(Text)
    ResSearch = re.search(String, Text)
    print(ResSearch)
