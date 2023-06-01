#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from pprint import pprint
import json

ipaLIST = [
    "m̥", "m", "ɱ", "n̼", "n̥", "n", "ɳ̊", "ɳ", "ɲ̊", "ɲ", "ŋ̊", "ŋ",
    "ɴ", "p", "b", "p̪", "b̪", "t̼", "d̼", "t", "d", "ʈ", "ɖ", "c",
    "ɟ", "k", "ɡ", "q", "ɢ", "ʡ", "ʔ", "s", "z", "ʃ", "ʒ", "ʂ", "ʐ",
    "ɕ", "ʑ", "ɸ", "β", "f", "v", "θ̼", "ð̼", "θ", "ð", "θ̠", "ð̠", "ɹ̠̊˔",
    "ɹ̠˔", "ɻ̊˔", "ɻ˔", "ç", "ʝ", "x", "ɣ", "χ", "ʁ", "ħ", "ʕ", "h", "ɦ",
    "ʋ", "ɹ", "ɻ", "j", "ɰ", "ʔ̞", "ⱱ̟", "ⱱ", "ɾ̼", "ɾ̥", "ɾ", "ɽ̊", "ɽ",'ɢ̆', 'ʡ̆', 'ʙ̥', 'ʙ', 'r̥', 'r', 'ɽ̊r̥', 'ɽr'
    "ʀ̥", "ʀ", "ʜ", "ʢ", "ɬ", "ɮ", "ꞎ", "𝼅", "𝼆", "ʎ̝", "𝼄", "ʟ̝", "l",
    "ɭ", "ʎ", "ʟ", "ʟ̠", "ɺ̥", "ɺ", "𝼈̥", "𝼈", "ʎ̆", "ʟ̆"
]

pulmonic = {
    "voiced/voiceless":0,
    "place":{
        "labial":{
            "bilabial":0,
            "labio-dental":0,
            "linguo-labial":0
        },
        "coronal":{
            "dental":0,
            "alveolar":0,
            "post-alveolar":0,
            "retroflex":0
        },
        "dorsal":{
            "palatal":0,
            "velar":0,
            "uvular":0
        },
        "laryngeal":{
            "pharyngeal":0,
            "epiglottal":0,
            "glottal":0
        }
    },
        
    "manner":{
        "nasal":0,
        "plosive":0,
        "affricate":{
            "sibilant":0,
            "non-sibilant":0,
            "lateral":0
            },
        "fricative":{
            "sibilant":0,
            "non-sibilant":0,
            "lateral":0
            },
        "approximant":{
            "lateral":0
        },
        "tap":{
            "lateral":0
        },
        "flap":{
            "lateral":0
        },
        "trill":0           
    }

}

ipaDICT = {}

for i in ipaLIST:
    ipaDICT[i] = pulmonic
    
pprint(len(ipaDICT))
print(len(ipaLIST))

with open("./clean_pulmonic.json", "w", encoding='UTF-8') as jFILE:
    json.dump(ipaDICT, jFILE, ensure_ascii=False, indent=4)
    


