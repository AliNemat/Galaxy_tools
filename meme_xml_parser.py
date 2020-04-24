import os
import xml.etree.ElementTree as ET
import argparse
import shutil
import time

parser = argparse.ArgumentParser()
parser.add_argument('--input_bed_file' , dest='input_bed_file', required=True, help='name of bed input file with absolute directory address ')
parser.add_argument('--input_xml_file' , dest='input_xml_file', required=True, help='name of xml input file with absolute directory address ')
parser.add_argument('--output_bed_path' , dest='output_bed_path', required=True, help='desired path of writing bed output file with absolute directory address')
parser.add_argument('--output_xml_path' , dest='output_xml_path', required=True, help='desired path of writing xml output file with absolute directory address')
args = parser.parse_args()
time.sleep(60)


tree = ET.parse(args.input_xml_file)
root = tree.getroot()

for item in root.findall("motifs"):
    result = len(list(item))

bed_filename_tmp = ( ((args.input_bed_file).split('/'))[-1])
bed_filename     = bed_filename_tmp.split('.')[0]
xml_filename_tmp = ( ((args.input_xml_file).split('/'))[-1])
xml_filename     = xml_filename_tmp.split('.')[0]
if (args.output_bed_path[-1] != '/'):
    args.output_bed_path = args.output_bed_path + '/'

if (args.output_xml_path[-1] != '/'):
    args.output_xml_path = args.output_xml_path + '/'

if (result == 0):
    shutil.copy (args.input_bed_file, args.output_bed_path + bed_filename + '.bed')
    shutil.copy (args.input_xml_file, args.output_xml_path + xml_filename + '.xml')
else:
    shutil.copy (args.input_bed_file, args.output_bed_path + bed_filename  + '.bed')
    shutil.copy (args.input_xml_file, args.output_xml_path + xml_filename  + '.xml')

#time.sleep(180)
