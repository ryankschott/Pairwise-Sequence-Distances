import sys
import os
from subprocess import call
import csv

folder = sys.argv[1]
output = sys.argv[2]

for filename in os.listdir(folder):
    if (filename.endswith(".fas") and not filename.endswith(".best.fas")):
        filename = filename[:-4]
        call(["prank", "-d="+folder+"\\"+filename+".fas", "-o="+folder+"\\"+filename+"_prank", "-codon"])
        call(["usearch", "-calc_distmx", folder+"\\"+filename+"_prank.best.fas", "--tabbedout", folder+"\\"+filename+"_distance.txt"])

file_list = []
[file_list.append(i) for i in os.listdir(folder) if i.endswith(".txt")]
output_f = open(output+".csv", "w")
writer = csv.writer(output_f)
output_f.write("Gene" + "," + "output" + '\n')

for text_file in sorted(file_list, key=lambda x: x.split('_')[-2]):
    fd = open(folder+"/"+text_file)
    distance = fd.read().split()
    gene = text_file.split('_')[-2]
    if gene.islower():
        gene = gene.title()
    #writer.writerow((gene.strip(), distance[-1].strip('\n')))
    output_f.write(gene.strip() + ',' + distance[-1].strip() + '\n')

output_f.close()
