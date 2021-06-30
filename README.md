
# HackerTracker

Description: A desktop application that functions as a journaling alternative for you to better understand how certain lifestyle choices and other triggers affect your wellbeing with four easy steps: select categories, choose best option for each category, note trends, and make lifestyle changes.

Intended to track habits of the user and promote a healthier lifestyle. It includes vizualizations of progress in order to 
motivate the user. 


Package Name: hacker-tracker-reeyagup
Link to repo: https://github.com/FastAndFerbious/HackerTracker.git
Executable command: python3 homeScreen.py


git clone https://github.com/FastAndFerbious/HackerTracker.git


everything below this line should be ran upon using the application for the first time
---------------------------------------------------------------------------------------

pip3 install hacker-tracker-reeyagup

python3 -m spacy download en_core_web_sm

python3 src/hacker_tracker_application/homescreen.py


--------------------------------------------------------------------------------------
after ran once, the only line needed to run the program is:

python3 homeScreen.py


Packages used: 
    tkinter,
    tkcalendar,
    nltk,
    spacy,
    wordnet,
    spacytextblob,
    pandas,
    matplotlip
