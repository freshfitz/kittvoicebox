# kittvoicebox
Knight Rider Kitt voicebox in python

Kitt's voicebox uses an HTML5 voice recorder to convert a wav file to text, search that text for a matching keyword then play the appropaite KITT mp3 file

You have to install APACHE with modssl, the html5 voice recorder needs SSL to run.

I have my python dir at /home/pi/kitt the html recorder in /var/www/html it will upload the transcribe wav file to /home/pi/kitt 

To modify your own keywords edit the input.txt file, make sure there are spaces before and after : so a : a.mp3 not a:a.mp3

to run python3 kitt.py
