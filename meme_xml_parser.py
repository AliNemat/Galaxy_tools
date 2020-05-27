import os
import xml.etree.ElementTree as ET
import argparse
import shutil
import time

parser = argparse.ArgumentParser()
parser.add_argument('--input_xml_file' , dest='input_xml_files', action='append', required=True, help='Galaxy name with absolute directory address of xml input file')
parser.add_argument('--input_file_name' , dest='input_files_name', action='append', required=True, help='Real name of xml input file')
parser.add_argument('--output_xml_path' , dest='output_xml_path', required=True, help='Desired path of writing xml output file with absolute directory address')
args = parser.parse_args()
#time.sleep(60)



txt_file_name = "subtype_meme_motif_info.txt"
fileM = open(txt_file_name,'w')
fileM.write ("subtype, meme_motif_found\n")


if (args.output_xml_path[-1] != '/'):
    args.output_xml_path = args.output_xml_path + '/'


for (input_xml_file, file_name) in zip (args.input_xml_files, args.input_files_name):
    
    tree = ET.parse(input_xml_file)
    root = tree.getroot()
    
    for item in root.findall("motifs"):
        result = len(list(item))
    
    if (result == 0):
        fileM.write (str(file_name) + ", " + str(result) + '\n')
    else:
        shutil.copy (input_xml_file, args.output_xml_path + file_name  + '.xml')
        fileM.write (str(file_name) + ", " + str(result) + ' \n')

#time.sleep(180)
