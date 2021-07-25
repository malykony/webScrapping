#Dockerfile
#from docker hub get python in version 3.8
FROM python:3.8

#take our code and create image into the same directory (the dot .)
#ADD main.py .
ADD main.py .

#import dependencies - requests and bs4 (random is already in python 3.8)
RUN pip install requests beautifulsoup4

#and specify what to run
CMD [ "python", "./main.py" ]

#now we have to create image
#in cmd run>
#docker build -t image-name .
#the -t is for "suit to terminal"
#if we want to use user input we have to add -i which stands for "interactive mode"
#docker build -t -i image-name .