#!/usr/bin/env python
import re
import os
import sys
import subprocess
import re
import speech_recognition as sr
from os import path
import time
import RPi.GPIO as GPIO

def start():

 print ("Starting")

 AUDIO_FILE = "transcribe.wav"
 #time_to_wait = 9999
 time_counter = 0
 while not os.path.exists(AUDIO_FILE):
    time.sleep(1)
    time_counter += 1
    #if time_counter > time_to_wait:break

# Convert transcibe.wav to text
 r = sr.Recognizer()
 with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file

#Search for a keyword match in the text
 def string_found(string1, string2):
    return re.search(r"\b" + re.escape(string1) + r"\b", string2)

 def find_words(text, words):
    return [word for word in words if string_found(word, text)]

#If blank audio is uploaded play do not understand 
 try:
  keyword = r.recognize_google(audio)
  print ("Keyword:" + keyword)
 except:
  omxprocess = subprocess.Popen(['omxplayer', '--no-keys', '-olocal', 'understand.mp3'],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
  os.remove(AUDIO_FILE)

#Match keyword to flat file input.txt and get audio MP3
 keyword = str(r.recognize_google(audio))
 sentences = (keyword)
 search_keywords=[ 'theme', 'son', 'serial','bonnie','cereal','morning','candy','who','scan']
 print ("Phrase:" + sentences)

 found = find_words(sentences, search_keywords)
 name = re.sub('\W+','', str(found))
 print (name)

 with open('input.txt') as fd:

#Do stuff based on the audio match
    for line in fd:
        match = re.search(rf'.*{name}.* : (\S+)', line)
        print (match)
    
        if (name == "candy"):
            omxprocess = subprocess.Popen(['omxplayer', '--no-keys', '-olocal', 'fx-scanner.mp3'],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
            os.remove(AUDIO_FILE)
            time.sleep(1)
            print ("GOing to chaser")
            chaser()
        
        elif (name == "skinny"):
            omxprocess = subprocess.Popen(['omxplayer', '--no-keys', '-olocal', 'fx-scanner.mp3'],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
            os.remove(AUDIO_FILE)
            time.sleep(1)
            print ("GOing to chaser")
            chaser()

        elif (name == "scan"):
            omxprocess = subprocess.Popen(['omxplayer', '--no-keys', '-olocal', 'fx-scanner.mp3'],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
            os.remove(AUDIO_FILE)
            time.sleep(1)
            print ("GOing to chaser")
            chaser()


        elif match:
            music = match.group(1)
            print('{}'.format(music))
            omxprocess = subprocess.Popen(['omxplayer', '--no-keys', '-olocal', music],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
            os.remove(AUDIO_FILE)
            start()
            
#run chaser LED's if needed           
def chaser():
 
 # Use BCM GPIO references
 # instead of physical pin numbers
 GPIO.setmode(GPIO.BCM)
  
 # Define GPIO signals to use
 # that are connected to 10 LEDs
 # Pins 7,11,15,21,23,16,18,22,24,26
 # GPIO4,GPIO17,GPIO22,GPIO9,GPIO11
 # GPIO23,GPIO24,GPIO25,GPIO8,GPIO7
 RpiGPIO = [4,17,22,9,11,23,24,25,8,7]
  
 # Set all pins as output
 for pinref in RpiGPIO:
 # print("Setup pins")
  GPIO.setup(pinref,GPIO.OUT)
  
 # Define some settings
 StepCounter = 0
 StepDir = 1
 WaitTime = 0.2
  
 # Define some sequences
  
 # One LED
 StepCount1 = 10
 Seq1 = []
 Seq1 = list(range(0,StepCount1))
 Seq1[0] =[1,0,0,0,0,0,0,0,0,0]
 Seq1[1] =[0,1,0,0,0,0,0,0,0,0]
 Seq1[2] =[0,0,1,0,0,0,0,0,0,0]
 Seq1[3] =[0,0,0,1,0,0,0,0,0,0]
 Seq1[4] =[0,0,0,0,1,0,0,0,0,0]
 Seq1[5] =[0,0,0,0,0,1,0,0,0,0]
 Seq1[6] =[0,0,0,0,0,0,1,0,0,0]
 Seq1[7] =[0,0,0,0,0,0,0,1,0,0]
 Seq1[8] =[0,0,0,0,0,0,0,0,1,0]
 Seq1[9] =[0,0,0,0,0,0,0,0,0,1]
  
 # Double LEDs
 StepCount2 = 11
 Seq2 = []
 Seq2 = list(range(0,StepCount2))
 Seq2[0] =[1,0,0,0,0,0,0,0,0,0]
 Seq2[1] =[1,1,0,0,0,0,0,0,0,0]
 Seq2[2] =[0,1,1,0,0,0,0,0,0,0]
 Seq2[3] =[0,0,1,1,0,0,0,0,0,0]
 Seq2[4] =[0,0,0,1,1,0,0,0,0,0]
 Seq2[5] =[0,0,0,0,1,1,0,0,0,0]
 Seq2[6] =[0,0,0,0,0,1,1,0,0,0]
 Seq2[7] =[0,0,0,0,0,0,1,1,0,0]
 Seq2[8] =[0,0,0,0,0,0,0,1,1,0]
 Seq2[9] =[0,0,0,0,0,0,0,0,1,1]
 Seq2[10]=[0,0,0,0,0,0,0,0,0,1]
  
 # Two LEDs from opposite ends
 StepCount3 = 9
 Seq3 = []
 Seq3 = list(range(0,StepCount3))
 Seq3[0] =[1,0,0,0,0,0,0,0,0,1]
 Seq3[1] =[0,1,0,0,0,0,0,0,1,0]
 Seq3[2] =[0,0,1,0,0,0,0,1,0,0]
 Seq3[3] =[0,0,0,1,0,0,1,0,0,0]
 Seq3[4] =[0,0,0,0,1,1,0,0,0,0]
 Seq3[5] =[0,0,0,1,0,0,1,0,0,0]
 Seq3[6] =[0,0,1,0,0,0,0,1,0,0]
 Seq3[7] =[0,1,0,0,0,0,0,0,1,0]
 Seq3[8] =[1,0,0,0,0,0,0,0,0,1]
 count = 1
 
  
 # Choose a sequence to use
 Seq = Seq3
 StepCount = StepCount3
 i=0
 
 # Start main loop
 while True:
 # print("-- Step : "+ str(StepCounter) +" --")
  for pinref in range(0, 10):
    xpin=RpiGPIO[pinref]#
    # Check if LED should be on or off
    if Seq[StepCounter][pinref]!=0:
    #  print(" Enable " + str(xpin))
      GPIO.output(xpin, True)
      i += 1
    else:
    #  print(" Disable " + str(xpin))
      GPIO.output(xpin, False)
  
  StepCounter += StepDir
  
  # If we reach the end of the sequence reverse
  # the direction and step the other way
  if (StepCounter==StepCount) or (StepCounter<0):
    
    StepDir = StepDir * -1
    StepCounter = StepCounter + StepDir + StepDir
    print(i)
  
  if (i > 51):
         print ("i = 8")
         GPIO.cleanup() 
         start()

    
  # Wait before moving on
  time.sleep(0.2)
  

start()
