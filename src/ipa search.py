#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from pprint import pprint
import json

searchLIST = []
searchDICT = {
        "voice": 0,
        "place": {
            "labial": {
                "bilabial": 0,
                "labiodental": 0,
                "linguolabial": 0
            },
            "coronal": {
                "dental": 0,
                "alveolar": 0,
                "post-alveolar": 0,
                "retroflex": 0
            },
            "dorsal": {
                "palatal": 0,
                "velar": 0,
                "uvular": 0
            },
            "laryngeal": {
                "pharyngeal": 0,
                "epiglottal": 0,
                "glottal": 0
            }
        },
        "manner": {
            "nasal": 0,
            "plosive": 0,
            "affricate": {
                "sibilant": 0,
                "non-sibilant": 0,
                "lateral": 0
            },
            "fricative": {
                "sibilant": 0,
                "non-sibilant": 0,
                "lateral": 0
            },
            "approximant": {
                "lateral": 0,
                "approximant":0
            },
            "tap": {
                "lateral": 0,
                "tap":0
            },
            "flap": {
                "lateral": 0,
                "flap":0
            },
            "trill": 0
        }
    }

for i in searchDICT["place"]:
    print(searchDICT["place"][i].items())
print(searchDICT["place"].keys())
print(searchDICT["place"].items())
print(dict(list(searchDICT["place"].values())[0]))
inputSTR = input("search： ")
inputLIST = inputSTR.lower().split()
print(inputLIST)

with open("pulmonic.json", "r", encoding="utf-8") as jFILE:
    pulmonicDICT = json.load(jFILE)

def inputArrange(inputLIST):
    for i in inputLIST:
        if i == "voiced" or i == "voiceless":
            searchLIST.insert(0, i)
        elif i in searchDICT["place"].keys():
            searchLIST.insert(1, i)
        elif i in searchDICT["manner"].keys():
            searchLIST.insert(-1, i)
        else:
            if j in searchDICT["place"][]    
    return searchLIST       
#except:
    #print(searchLIST, "something might be wrong with your input ! ")
            
print(searchLIST)

