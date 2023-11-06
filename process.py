import os
import glob
spoof=os.listdir("/home4/khanhnd/combined_data/spoofing_data")
speaker_lst_with_spoof=spoof
from random import sample 
vn_celeb_speaker_lst=os.listdir("/home4/khanhnd/combined_data/vietnam_celeb")
bonafide_audio_lst=[]
for i in speaker_lst_with_spoof:
    path="/home4/khanhnd/combined_data/spoofing_data/"+i+"/bonafide/*"
    bonafide_audio_lst=bonafide_audio_lst+glob.glob(path)
all_bonafide=bonafide_audio_lst+sample(glob.glob("/home4/khanhnd/combined_data/vietnam_celeb/*/*"),100000)
print(len(all_bonafide))
import random
spoof_audio_lst=[]
for i in speaker_lst_with_spoof:
    path="/home4/khanhnd/combined_data/spoofing_data/"+i+"/spoofed*/*"
    spoof_audio_lst=spoof_audio_lst+glob.glob(path)
print(len(spoof_audio_lst))
random.shuffle(spoof_audio_lst)
random.shuffle(all_bonafide)
with open("/home4/khanhnd/combined_data/train.txt", "w") as f:
    for i in spoof_audio_lst[0:int(len(spoof_audio_lst)*9/10)]:
        f.write(f"{i}\tspoof\n")
    for i in all_bonafide[0:int(len(all_bonafide)*9/10)]:
        f.write(f"{i}\tbonafide\n")
with open("/home4/khanhnd/combined_data/dev.txt", "w") as f:
    for i in spoof_audio_lst[int(len(spoof_audio_lst)*9/10):]:
        f.write(f"{i}\tspoof\n")
    for i in all_bonafide[int(len(all_bonafide)*9/10):]:
        f.write(f"{i}\tbonafide\n")