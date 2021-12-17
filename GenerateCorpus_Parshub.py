
# %%
from os.path import isfile, join
from os import listdir
from os import walk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib.ticker as ticker
import json
import os
import re
import numpy as np
from datetime import datetime
import spacy


nlp = spacy.load("en_core_web_md")

#%%
#Parshub
#Structure:
# "Post": [
#   {
#    "name": "Weathering with precautions",
#    "url": "https://devpost.com/software/weathering-with-precautions",
#    "Likes": "0",
#    "Comments": "0",
#    "Description": "Inspiration - to help peoples to save them from weather damage\nWhat it does- it helps to know the right weather to us and get ready for the precautions\nHow we built it - By using knowledge of c , c++ and java\nChallenges we ran into- lots of challenges like time saving , errors\nAccomplishments that we're proud of\nWhat we learned-too much knowledge\nWhat's next for Weathering with precautions --many more to do this for make it better"
#   },

datapath = '/Users/joshcornau/Code/LeadUserAnalysis/data/_Input/Core/Parshub/parsehub_devpost.json'


with open(datapath, 'r') as f:
        jsonFile = json.loads(f.read())
res= pd.json_normalize(jsonFile,record_path=['Post'])
res.head()

#%%
res.shape
#%%

df3 = pd.DataFrame(columns=['autor', 'date', 'content', 'link', 'origin', 'suborigin','removed','score','comments','media','medialink','identifyer'
                            ])

Corpus=[]
for idx, row in res.iterrows():
    print(idx)
    Corpus.append({
        "autor": row.name,
         "date":'nan', 
         "content":row.Description,
         "link":row.url,
         "origin": 'Devpost',
         "suborigin": 'Devpost',
         "removed":"Nan",
         "score":row.Likes,
         "comments":row.Comments,
         "media":'nan',
         "medialink":'nan',
         "identifyer":idx+3000000
    })


#df = pd.read_csv('/Users/joshcornau/Code/LeadUserAnalysis/data/_Output/Core/Parsehub/Devpost.csv',dtype={"Unnamed: 0": int, "autor": "string","date": "float64","content": "string","link": "string","origin": "string","suborigin": "string","removed": "string","score": "string","comments": "string","media": "string","medialink": "string","identifyer": "int64"})
# df.head()
#dtype={"Unnamed: 0": int, "autor": "string","date": "float64","content": "string","link": "string","origin": "string","suborigin": "string","removed": "string","score": "string","comments": "string","media": "string","medialink": "string","identifyer": "int64"}
# df.to_csv('/Users/joshcornau/Code/LeadUserAnalysis/data/_Output/Core/Parsehub/test.csv',)


#%%
AnalyseFile= pd.DataFrame(data=Corpus)
AnalyseFile.to_csv('/Users/joshcornau/Code/LeadUserAnalysis/data/_Output/Core/Parsehub/Devpost.csv')
AnalyseFile.head()



#-––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

# "Category": [
#   {
#    "Category_Name": "Forestry Forum Pod Casts",
#    "Thread": [
#     {
#      "Threadname": "Podcast",
#      "Post": [
#       {
#        "Body": "I would listen to a podcast for sure. This Newbie needs a lot of help learning.",
#        "Author": "Kemp",
#        "Date": "« on: February 13, 2019, 04:34:47 AM »"
#       },
#       {
#        "Body": "Yeah, sounds like a great idea!",
#        "Author": "dltimbertech",
#        "Date": "« Reply #1 on: February 19, 2019, 01:46:23 PM »"
#       },
#       {
#        "Body": "Thats two",
#        "Author": "Kemp",
#        "Date": "« Reply #2 on: February 19, 2019, 03:16:24 PM »"
#       },
#       {
#        "Body": "I’m another for that route. Heck, I would be inclined to participate and talk but I don’t know if I would have anything pertinent to say, just a slightly different way of looking at life. But I’m still here (for now)!\nAfter all, who wants to hear from someone with a 25yr background in selling automotive and equipment parts? Automotive, I was top notch. Equipment, I would like to think I was a rookie at best!\nBut the customers like me because of attitude. That can’t be taught. Learned, yes. You just have to pay attention.\nTwo ears and one mouth. God gave us this as a reminder: listen twice as much as you talk! Easy to see, but hard to teach. Just be humble.\nI’m far, FAR from being a preacher, my life is to “colorful” for that. But my father-in-law is. He knows my life and doesn’t look down on me. I’ve asked for his ear and he’s willing to give it. And he’s asked for advice on a few things that I know about that are specialized and I give it to him. In fact, they are planning to come up from MS next weekend. Maybe they will come up close to Magic Man, but we’ll not count on the planets being in perfect alignment. But a man can dream!",
#        "Author": "Tacotodd",
#        "Date": "« Reply #3 on: January 11, 2021, 02:10:11 AM »"
#       },
#       {
#        "Body": "Hi there, can you guide me a little bit? I really want to listen to the podcast, but I can't find it.",
#        "Author": "stillc",
#        "Date": "« Reply #4 on: April 05, 2021, 12:01:36 AM »"
#       },
#       {
#        "Body": "I’m just wondering if @jeff is seeing this. I know he is, but no response as of yet.",
#        "Author": "Tacotodd",
#        "Date": "« Reply #5 on: April 05, 2021, 12:43:15 AM »"
#       },
#       {
#        "Body": "I'm strongly considering something a step up from a podcast, but too much on my plate at the moment to dive into it, but id strongly suggest following and getting subscribed to the Forestry Forum youtube channel",
#        "Author": "Jeff",
#        "Date": "« Reply #6 on: April 05, 2021, 11:42:02 AM »"
#       },
#       {
#        "Body": "10-4! Message received & understood!",
#        "Author": "Tacotodd",
#        "Date": "« Reply #7 on: April 05, 2021, 04:11:20 PM »"
#       }
#      ]
#     },

#Body, Author, Date, 



#%%
datapath = '/Users/joshcornau/Code/LeadUserAnalysis/data/_Input/Core/Parshub/parsehub_Forestry_hopefullywithurl.json'


with open(datapath, 'r') as f:
        jsonFile = json.loads(f.read())
res= pd.json_normalize(jsonFile,record_path=['Category'])
res.head()



#%%

print(len(jsonFile['Category']))
print(jsonFile['Category'][0]['Category_Name'])

# print(jsonFile['Category'][0]['Thread'][0]['Post'])
#%%
Corpus=[]
for idx, file in enumerate(jsonFile['Category']):
    suborigin = file['Category_Name']
    print(suborigin)
    try:
        for idx2, thread in enumerate(file['Thread']):
            # print(len(thread['Post']))
            for idx3, post in enumerate(thread['Post']):
                try:
                    autor = post['Author']
                except Exception as e:
                    autor='Nan'
                try:
                    content = post['Body'],
                except Exception as e:
                    content = 'Nan'
                try:
                    link = post['Link_url'],
                    date = post['Date'],
                except Exception as e:
                    link = 'Nan'
                    date = 'Nan'

                Corpus.append({
                    "autor": autor,
                    "date":date, 
                    "content":content,
                    "link":link,
                    "origin": 'Forestry',
                    "suborigin": suborigin,
                    "removed":"Nan",
                    "score":'Nan',
                    "comments":'Nan',
                    "media":'nan',
                    "medialink":'nan',
                    "identifyer":idx+4000000
                })
    except Exception as e:
        print('none')
print('done')



#%%
#Structure Github
# {
#  "Projecttitle": [
#   {
#    "name": "Tasmota",
#    "url": "https://github.com/arendst/Tasmota",
#    "Body": "Alternative firmware for ESP8266 and ESP32 based devices with easy configuration using webUI, OTA updates, automation using timers or rules, expandability and entirely local control over MQTT, HTTP, Serial or KNX. Written for PlatformIO with limited support for Arduino IDE.\nIf you like Tasmota, give it a star, or fork it and contribute!\nSee RELEASENOTES.md for release information.\nFirmware binaries can be downloaded from http://ota.tasmota.com/tasmota/release/ or http://ota.tasmota.com/tasmota32/release/ for ESP32 binaries.\nEasy initial installation of Tasmota can be performed using the Tasmota WebInstaller.\nDevelopment\nSee CHANGELOG.md for detailed change information.\nUnless your Tasmota powered device exhibits a problem or you need to make use of a feature that is not available in the Tasmota version currently installed on your device, leave your device alone - it works so don't make unnecessary changes! If the release version (i.e., the master branch) exhibits unexpected behaviour for your device and configuration, you should upgrade to the latest development version instead to see if your problem is resolved as some bugs in previous releases or development builds may already have been resolved.\nEvery commit made to the development branch, which is compiling successfuly, will post new binary files at http://ota.tasmota.com/tasmota/ (this web address can be used for OTA updates too). It is important to note that these binaries are based on the current development codebase. These commits are tested as much as is possible and are typically quite stable. However, it is infeasible to test on the hundreds of different types of devices with all the available configuration options permitted.\nNote that there is a chance, as with any upgrade, that the device may not function as expected. You must always account for the possibility that you may need to flash the device via the serial programming interface if the OTA upgrade fails. Even with the master release, you should always attempt to test the device or a similar prototype before upgrading a device which is in production or is hard to reach. And, as always, make a backup of the device configuration before beginning any firmware update.\nDisclaimer\n⚠️ DANGER OF ELECTROCUTION ⚠️\nIf your device connects to mains electricity (AC power) there is danger of electrocution if not installed properly. If you don't know how to install it, please call an electrician (Beware: certain countries prohibit installation without a licensed electrician present). Remember: SAFETY FIRST. It is not worth the risk to yourself, your family and your home if you don't know exactly what you are doing. Never tinker or try to flash a device using the serial programming interface while it is connected to MAINS ELECTRICITY (AC power).\nWe don't take any responsibility nor liability for using this software nor for the installation or any tips, advice, videos, etc. given by any member of this site or any related site.\nNote\nPlease do not ask to add new devices unless it requires additional code for new features. If the device is not listed as a module, try using Templates first. If it is not listed in the Tasmota Device Templates Repository create your own Template.\nQuick Install\nDownload one of the released binaries from http://ota.tasmota.com/tasmota/release/ or http://ota.tasmota.com/tasmota32/release/ and flash it to your hardware using our installation guide.\nImportant User Compilation Information\nIf you want to compile Tasmota yourself keep in mind the following:\nFor ESP8285 based devices only Flash Mode DOUT is supported. Do not use Flash Mode DIO / QIO / QOUT as it might seem to brick your device.\nFor ESP8285 based devices Tasmota uses a 1M linker script WITHOUT spiffs 1M (no SPIFFS) for optimal code space.\nTo make compile time changes to Tasmota use the user_config_override.h file. It assures keeping your custom settings when you download and compile a new version. You have to make a copy from the provided user_config_override_sample.h file and add your setting overrides.\nConfiguration Information\nPlease refer to the installation and configuration articles in our documentation.\nMigration Information\nSee wiki migration path for instructions how to migrate to a major version. Pay attention to the following version breaks due to dynamic settings updates:\nMigrate to Sonoff-Tasmota 3.9.x\nMigrate to Sonoff-Tasmota 4.x\nMigrate to Sonoff-Tasmota 5.14\nMigrate to Sonoff-Tasmota 6.7.1 (http://ota.tasmota.com/tasmota/release-6.7.1/)\nMigrate to Tasmota 7.2.0 (http://ota.tasmota.com/tasmota/release-7.2.0/)\n--- Major change in parameter storage layout ---\nMigrate to Tasmota 8.5.1 (http://ota.tasmota.com/tasmota/release-8.5.1/)\n--- Major change in internal GPIO function representation ---\nMigrate to Tasmota 9.1 (http://ota.tasmota.com/tasmota/release-9.1.0/)\nWhile fallback or downgrading is common practice it was never supported due to Settings additions or changes in newer releases. Starting with version v9.0.0.1 the internal GPIO function representation has changed in such a way that fallback is only possible to the latest GPIO configuration before installing v9.0.0.1.\nSupport Information\nFor a database of supported devices see Tasmota Device Templates Repository\nIf you're looking for support on Tasmota there are some options available:\nDocumentation\nDocumentation Site: For information on how to flash Tasmota, configure, use and expand it\nFAQ and Troubleshooting: For information on common problems and solutions.\nCommands Information: For information on all the commands supported by Tasmota.\nSupport's Community\nTasmota Discussions: For Tasmota usage questions, Feature Requests and Projects.\nTasmota Users Chat: For support, troubleshooting and general questions. You have better chances to get fast answers from members of the Tasmota Community.\nSearch in Issues: You might find an answer to your question by searching current or closed issues.\nSoftware Problem Report: For reporting problems of Tasmota Software.\nContribute\nYou can contribute to Tasmota by\nProviding Pull Requests (Features, Proof of Concepts, Language files or Fixes)\nTesting new released features and report issues\nDonating to acquire hardware for testing and implementing or out of gratitude\nContributing missing documentation for features and devices\nCredits\nPeople helping to keep the show on the road:\nDavid Lang providing initial issue resolution and code optimizations\nHeiko Krupp for his IRSend, HTU21, SI70xx and Wemo/Hue emulation drivers\nWiktor Schmidt for Travis CI implementation\nThom Dietrich for PlatformIO optimizations\nMarinus van den Broek for his EspEasy groundwork\nPete Ba for more user friendly energy monitor calibration\nLobradov providing compile optimization tips\nFlexiti for his initial timer implementation\nreloxx13 for his TasmoAdmin management tool\nJoachim Banzhaf for his TSL2561 library and driver\nAndre Thomas for providing many drivers\nGijs Noorlander for his MHZ19, SenseAir and updated PubSubClient drivers\nErik Montnemery for his HomeAssistant Discovery concept and many code tuning tips\nFederico Leoni for continued HomeAssistant Discovery support\nAidan Mountford for his HSB support\nDaniel Ztolnai for his Serial Bridge implementation\nGerhard Mutz for multiple sensor & display drivers, Sunrise/Sunset, and scripting\nNuno Ferreira for his HC-SR04 driver\nAdrian Scillato for his (security)fixes and implementing and maintaining KNX\nGennaro Tortone for implementing and maintaining Eastron drivers\nRaymond Mouthaan for managing Wemos Wiki information\nNorbert Richter for his decode-config.py tool\nJoel Stein, digiblur and Shantur Rathore for their Tuya research and driver\nFrogmore42 for providing many issue answers\nJason2866 for platformio support and providing many issue answers\nBlakadder for managing the new document site and providing template management\nStephan Hadinger for refactoring light driver, enhancing HueEmulation, LVGL, Zigbee and Berry support\ntmo for designing the official Tasmota logo\nStefan Bode for his Shutter and Deep sleep drivers\nJacek Ziółkowski for his TDM management tool and Tasmotizer flashing tool\nChristian Staars for NRF24L01 and HM-10 Bluetooth sensor support\nPaul Diem for UDP Group communication support\nJörg Schüler-Maroldt for his initial ESP32 port\nJavier Arigita for his thermostat driver\nMany more providing Tips, Wips, Pocs, PRs and Donations\nLicense\nThis program is licensed under GPL-3.0"
#   },

datapath = '/Users/joshcornau/Code/LeadUserAnalysis/data/_Input/Core/Parshub/parsehub_Github_Arduino.json'
datapath2 = '/Users/joshcornau/Code/LeadUserAnalysis/data/_Input/Core/Parshub/parsehub_Github_Robotics.json'
datapath3 = '/Users/joshcornau/Code/LeadUserAnalysis/data/_Input/Core/Parshub/parsehub_Github_IoT.json'


with open(datapath, 'r') as f:
        Arduino = json.loads(f.read())
        resArduino= pd.json_normalize(Arduino,record_path=['Projecttitle'])
        resArduino['suborigin']='arduino'

with open(datapath2, 'r') as f:
        Robotics = json.loads(f.read())
        resRobotics= pd.json_normalize(Robotics,record_path=['Projecttitle'])
        resRobotics['suborigin']='robotics'

with open(datapath3, 'r') as f:
        IoT = json.loads(f.read())
        resIot= pd.json_normalize(IoT,record_path=['Projecttitle'])
        resIot['suborigin']='Iot'
        
#%%
combined = pd.concat([resIot,resRobotics,resArduino])
#%%
combined.shape

#%%
df3 = pd.DataFrame(columns=['autor', 'date', 'content', 'link', 'origin', 'suborigin','removed','score','comments','media','medialink','identifyer'
                            ])

Corpus=[]
for idx, row in combined.iterrows():
    print(idx)
    Corpus.append({
        "autor": row.name,
         "date":'nan', 
         "content":row.Body,
         "link":row.url,
         "origin": 'Github',
         "suborigin": row.suborigin,
         "removed":"Nan",
         "score":'NaN',
         "comments":'NaN',
         "media":'Nan',
         "medialink":'Nan',
         "identifyer":idx+7000000
    })

#%%
print(len(Corpus))



#%%
AnalyseFile= pd.DataFrame(data=Corpus)
AnalyseFile.to_csv('/Users/joshcornau/Code/LeadUserAnalysis/data/_Input/Core/Parshub/Github.csv')
AnalyseFile.head()


#%%

print(len(Corpus))
#%%
res.shape
#%%

df3 = pd.DataFrame(columns=['autor', 'date', 'content', 'link', 'origin', 'suborigin','removed','score','comments','media','medialink','identifyer'
                            ])

Corpus=[]
for idx, row in res.iterrows():
    print(idx)
    Corpus.append({
        "autor": row.name,
         "date":'nan', 
         "content":row.Description,
         "link":row.url,
         "origin": 'Devpost',
         "suborigin": 'Devpost',
         "removed":"Nan",
         "score":row.Likes,
         "comments":row.Comments,
         "media":'nan',
         "medialink":'nan',
         "identifyer":idx+3000000
    })


Corpus.head()

#%%
AnalyseFile= pd.DataFrame(data=Corpus)
AnalyseFile.to_csv('/Users/joshcornau/Code/LeadUserAnalysis/data/_Output/Core/Parsehub/Devpost.csv')
AnalyseFile.head()



#%%
mypath = '/Users/joshcornau/Code/LeadUserAnalysis/data/_Input/Core/Twitter_Core/'
Paths = []
for (dirpath, dirnames, filenames) in walk(mypath):

    for file in filenames:
        if file.endswith('.json'):
            Paths.append(file)
    break

print(Paths)


#%%

List = []
for idx, File in enumerate(Paths):
    path = mypath+File
    res = pd.read_json(path, lines=True)
    List.append(res
    )

#%%
alltweets= pd.concat(List)
alltweets.shape
#%%

df3 = pd.DataFrame(columns=['autor', 'date', 'content', 'link', 'origin', 'suborigin','removed','score','comments','media','medialink','identifyer'
                            ])

Corpus=[]
for idx, row in alltweets.iterrows():
    print(idx)
    Corpus.append({
        "autor": row.user,
         "date":row.date, 
         "content":row.renderedContent,
         "link":row.url,
         "origin": 'Twitter',
         "suborigin": row.hashtags,
         "removed":"Nan",
         "score":row.likeCount,
         "comments":row.replyCount,
         "media":row.media,
         "medialink":row.media,
         "identifyer":row.id
    })
#%%
print(len(Corpus))
# df3.shape
#%%



new= pd.DataFrame(data=Corpus)
new.to_csv('/Users/joshcornau/Code/LeadUserAnalysis/data/_Input/Core/Parshub/Forestry.csv')
new.head()
#%%
new.shape
#%%

#%%
def countWords(Analyse):
    doc = nlp(Analyse)
    i=0
    for token in doc:
        if(token.pos_ !='PUNCT'):
            i+=1
    return(i)





#%%

df = pd.read_csv('/Users/joshcornau/Code/LeadUserAnalysis/data/_Output/Core/Parsehub/Devpost.csv')
df.head()
# %%
df.dtypes
# %%
 
