import os
from pprint import pprint
import selenium
import  time
from os import system
from msedge.selenium_tools import Edge, EdgeOptions

options = EdgeOptions()
options.use_chromium = True
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)
path = 'drivers\\edge93.exe'
driver = Edge(path, options=options)

driver.get("https://utweb.trontv.com/gui/index.html?v=1.2.2.3593&localauth=localapi408633b1fcfe0a34:#/library")
_ = system('cls')
for t in reversed(range(0,10)):
    time.sleep(1)
    print("Waiting for "+str(t)+"sec\r",end="")
print("Finding Files Names.......")
torFilesName = []
for i in range(1,337):
    torFilesName.append(driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[{}]/div[2]/div[1]'.format(i)).text)
    print(str(i)+" filename found.\r",end="")
_ = system('cls')
# pprint(torFilesName)
print("Total name found: "+str(len(torFilesName)))

files = []
for dirname, dirnames, filenames in os.walk('H:\Courses\The_Complete_Mobile_Ethical_Hacking_Course\[Freeeducationweb.com] The Complete Mobile Ethical Hacking Course'):
    # print path to all subdirectories first.
    # for subdirname in dirnames:
    #     files.append(os.path.join(dirname, subdirname))

    # print path to all filenames.
    for filename in filenames:
        files.append(os.path.join(filename))
fileNames=[]
for file in files:
    file = file.replace(".mp4", "", 1)
    if ".srt" in file:
        file = file.replace(".srt","-en_US",1)
        fileNames.append(file)
    else:
        fileNames.append(file)
# pprint(fileNames)
print("Total Files Found: "+str(len(files)))

print("Compairing Both........")
for name in torFilesName:
    if name not in fileNames:
        print(name)