from os import path
from pytube import YouTube
import os.path
import time

os.system('cls' if os.name == 'nt' else 'clear')
print("\033[1;31;40mWelcome to Py4mp3 !!!")
time.sleep(1)
print("This program is coded and designed by Mehmet Akif VARDAR")
time.sleep(1)
print("https://mehmetakifvardar.com")
print("")
print("")

text = "DownloadList.txt"
lines = []
run = True
while run:
    if path.exists(text):
        print("\033[1;32;40mDownloadList.txt found, proceeding...")
        print("\033[1;33;40mReading links...")
        with open(text) as f:
            lines = f.readlines()
            count = -1
            for line in lines:
                count +=1
                yt = YouTube(lines[count])
                video = yt.streams.filter(only_audio=True).first()
                destination = "Downloads"
                if path.exists(destination):
                    print("\033[1;36;40m'Downloads' folder has been found! We will download your mp3 file here...")
                    out_file = video.download(output_path=destination)
                    base, ext = os.path.splitext(out_file)
                    new_file = base + '.mp3'
                    os.rename(out_file, new_file)
                    print("\033[1;31;40mYour mp3 file: \033[1;32;40m"+yt.title + " \033[1;31;40mhas been successfully downloaded.")
                else:
                    print("\033[1;30;40m'Downloads' folder can not be found. Please create it to proceed.")
                    break
    else:
        print("You should create DownloadList.txt and fill it with links before proceed!")
        break
    break