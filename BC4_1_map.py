# -*- coding:utf-8 -*-

#!/usr/bin/python
import os
import argparse
import re

parser=argparse.ArgumentParser(description='')
parser.add_argument('-i', type =argparse.FileType('r'),help='')
parser.add_argument('-i1', type =argparse.FileType('r'),help='')
parser.add_argument('-o', type =argparse.FileType('w'),help='')
#parser.add_argument('-r', type = float ,help='rate of heterozygous')

args=parser.parse_args()
debug=True

#eg:python3 BC4_1_map.py -i snp_idea_samples_genotype.txt -i1 DHbin_131.position.txt
# using about 30 minutes



import matplotlib.pyplot as plt
#import matplotlib as mpl
import numpy as np

fig = plt.figure(figsize=(10,10),dpi=300)
ax = fig.add_subplot(111)
ax.set_xlim(-1,18)
ax.set_ylim(-1000000,47000000)
#ax.set_xticks([])
#ax.set_yticks([])

chr_length = np.array([29528419,31442979,38154160,20746285,28493056,29167992,28701632,22981702,44994586,20662122])
#print(chr_length)

map_length = np.array([106.843,98.248,111.755,71.577,108.504,98.831,90.359,71.876,115.21,72.105])

plt.plot([0,0],[1,45000000], color='black',linestyle="-",linewidth = 1.5)
plt.plot([16.5,16.5],[1,115*(np.sum(chr_length)/np.sum(map_length))], color='black',linestyle="-",linewidth = 1.5)


start_x = 1
for i in range(10):
    #square = plt.Rectangle(xy=(start_x, 1), width=0.2, height=chr_length[i], alpha=1, angle=0.0,color = '#48D8FF' )
    square1 = plt.Rectangle(xy=(start_x+1, 1), width=0.2, height=(map_length[i]+1)*(np.sum(chr_length)/np.sum(map_length)), alpha=1, angle=0.0,color = '#FFE990' )
    start_x += 1.5  
    ax.add_patch(square1) 

chr_list = ['A01','A02','A03','A04','A05','A06','A07','A08','A09','A10']
#infile = open('C:\\Users\\1\\Desktop\\A03_genotype.txt','r')


chr_pos= []
y = []
start_x = np.arange(1,15,1.5)

for line in args.i:
    list1= line.strip().split('\t')
    if list1[0] == '#CHROM' or list1[0][0] == 'S':
        continue
    else:
        x = start_x[chr_list.index(list1[0])]
        y = int(list1[1])
        if list1[4] == list1[5]:
            color = '#48D8FF'
        elif list1[4] == list1[6]:
            color = 'red'
        else:
            color = '#003EC4'
        
        plt.plot([x,x+0.2],[y,y], color=color,linestyle="-",linewidth = 0.02)

args.i.close()

genetic = []
chr_pos= []
ystart = []
yend = []
for line in args.i1:
    list1= line.strip().split('\t')
    genetic.append(list1[1])
    chr_pos.append(list1[2])
    ystart.append(list1[3])
    yend.append(list1[4])

start_x = np.arange(1,15,1.5)
#print(start_x)
############lines of marker on chr
for i in range(len(chr_list)):
    for t in range(len(genetic)):
        if chr_list[i] == chr_pos[t]:
            plt.plot([start_x[i],start_x[i]+0.2],[(int(ystart[t])+int(yend[t]))/2,(int(ystart[t])+int(yend[t]))/2], color='black',linestyle="-",linewidth = 0.6)

############lines of marker on map            
for i in range(len(chr_list)):
    for t in range(len(genetic)):
        if chr_list[i] == chr_pos[t]:
            plt.plot([start_x[i]+1,start_x[i]+1.2],[float(genetic[t])*(np.sum(chr_length)/np.sum(map_length)),float(genetic[t])*(np.sum(chr_length)/np.sum(map_length))], color='blue',linestyle="-",linewidth = 0.6)

############ linked lines between chr and map            
for i in range(len(chr_list)):
    for t in range(len(genetic)):
        if chr_list[i] == chr_pos[t]:
            plt.plot([start_x[i]+0.2,start_x[i]+1],[(int(ystart[t])+int(yend[t]))/2,float(genetic[t])*(np.sum(chr_length)/np.sum(map_length))], color='black',linestyle="-",linewidth = 0.3)


##########add centromere position#####

centromere_s = [17017026,18917150,33225753,6789134,14052900,14464955,5186592,5944273,18738630,5421047]
centromere_e = [18025305,19940795,35218826,7016840,15396098,15702129,6999698,7027252,24037572,8162618]


for i in range(10):
    plt.plot([start_x[i]+0.09,start_x[i]+0.09],[centromere_s[i],centromere_e[i]], color='black',linestyle="-", linewidth = 6)

plt.plot([4.09,4.09],[12000000,12200000], color='#00FF00',linestyle="-",linewidth = 6)

ax.text(0,46000000,'45Mb',family = 'Times New Roman',  fontsize = 12, horizontalalignment= 'center',weight = 'black')

ax.text(16.5,118*(np.sum(chr_length)/np.sum(map_length)), '115cM',family = 'Times New Roman',  fontsize = 12, horizontalalignment= 'center',weight = 'black')


start_x = np.arange(1.6,16,1.5)
for i in range(10):
    ax.text(start_x[i], -1500000,chr_list[i],family = 'Times New Roman',  fontsize = 12, horizontalalignment= 'center',weight = 'black' )

plt.axis('off')

plt.savefig('BC4_1_map.png')

args.i1.close()
