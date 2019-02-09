import urllib.request
import os


url = 'http://www.berkshirehathaway.com/'
#url = 'https://www.accenture.com/us-en'
#url = 'https://investor.apple.com/investor-relations/default.aspx'

folder_start =0
folder_end =0
folder_start = url.find("www.",folder_start)
folder_end = url.find(".com",folder_end)
resp = urllib.request.urlopen(url)
respData = resp.read()
htmll = str(respData)

from bs4 import BeautifulSoup
soup = BeautifulSoup(htmll, 'html.parser')


# print(htmll)

a_Tag = soup.find_all('a')


for a in a_Tag:
    print(a['href'])
#
# print()
#
# link_start = "href"
# indx = 0
# indx2 = 0
# link_end = "\">"
#
# #os.mkdir('c:/'+str(url[12:len(url)-5]))
# #os.mkdir('c:/')
# current_dir = str(os.getcwd())+"/"+str(url[folder_start+4:folder_end])
# os.mkdir(current_dir)
#
# while indx < len(htmll):
#     indx = htmll.find(link_start,indx)
#     if indx==-1:
#         break
#     indx2 = htmll.find(link_end,indx)
#     #print string from index+6 to indx2-1
#     temp1 = indx + 6
#     file_list = htmll[temp1:indx2]
#     if htmll[indx2-3:indx2]=="pdf":
#         file_name = url+file_list
#         new_path = os.path.join(current_dir,file_list)
#         urllib.request.urlretrieve(file_name, new_path)
#         #urllib.request.urlretrieve(file_name, file_list)
#         #print()
#         print("File downloaded ::"+file_list)
#     print(file_list)
#     #print("Found at:: ",str(indx)+" and "+str(indx2))
#     indx += 4
#
# print()
# print("HTML Page contains "+str(len(htmll))+" characters")
# print()
# print("Number of urls =  "+str(htmll.count(link_start)))
