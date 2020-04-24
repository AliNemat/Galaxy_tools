import csv 
import argparse
import time


class Bed_File_Row:
    def __init__ (self):
        self.id_chr = None 
        self.first_bp = None 
        self.last_bp = None 
        self.subtype = None  
        self.score = None 
        self.strand_dir = None  


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', dest='event_file', required=True, help='Name of the .event file which is output of Chexmix')
    args = parser.parse_args()

    print (" Conversion started ..." )
    parsed_event_file = Parse_Event_File(args.event_file)
    print (" event file parsed" )
    bed_file          = Extract_Bed_File_Info(parsed_event_file)
    print ("bed file data extracted" )
    bed_files         = Split_Bed_File(bed_file)
    print ("bed file splitted" )
    Write_Bed_Files(bed_files)
    print ("bed/gff file written in the output file" )
    #Write_Gff_Files(bed_files)
def Parse_Event_File(file_name):
    with open(file_name) as data:                                                                                          
        data_reader = csv.reader(data, delimiter='\t')
        raw_data = list (data_reader)
    return raw_data


def Extract_Bed_File_Info (event_file):
    bed_file = [] 
    for event in event_file:
        tmp_string  = str(event[0])
        if (tmp_string[0:3] == 'chr'):
            bed_file_row = Bed_File_Row()
            bed_file_row.id_chr     =     (str(event[0])).split(':')[0]
            bed_file_row.first_bp   = int((str(event[0])).split(':')[1])-1 
            bed_file_row.last_bp    = int((str(event[0])).split(':')[1]) 
            bed_file_row.score      = float(   event[3])
            bed_file_row.strand_dir =     (str(event[5])).split(':')[-1]
            bed_file_row.subtype    = int((str(event[7])).split('type')[-1])
            bed_file.append (bed_file_row)
    return (bed_file)


def Split_Bed_File (bed_file):
    max_subtypes = -1
    for bed_file_row in bed_file:
        if (bed_file_row.subtype > max_subtypes):
            max_subtypes = bed_file_row.subtype
    
    bed_files = [[] for i in range (max_subtypes + 1)] 
    for bed_file_row in bed_file: 
        bed_files[bed_file_row.subtype].append (bed_file_row)
    return (bed_files)


def Write_Bed_Files(bed_files):
    file_name = 'subtype' + '0' + '.bed'
    fileM = open(file_name,'w')
    for i in range (len(bed_files)):
        if (len (bed_files[i]) > 0 ):
            #file_name = 'subtype' + str(i) + '.bed'
            #fileM = open(file_name,'w')
            #fileM.write ('Chrom, Start, End, Name, Score, Strand \n')
            for bed_file_row in bed_files[i]: 
                fileM.write(bed_file_row.id_chr + '\t')
                fileM.write(str(bed_file_row.first_bp)+ '\t')  
                fileM.write(str(bed_file_row.last_bp)+ '\t')  
                fileM.write('Subtype' + str (bed_file_row.subtype)+ '\t')  
                fileM.write(str(bed_file_row.score)+ '\t')  
                #fileM.write(bed_file_row.strand_dir)  
                fileM.write('\n')

def Write_Gff_Files(bed_files):
    file_name = 'subtype' + '0' + '.bed'
    fileM = open(file_name,'w')
    for i in range (len(bed_files)):
        if (len (bed_files[i]) > 0 ):
            #file_name = 'subtype' + str(i) + '.bed'
            #fileM = open(file_name,'w')
            #fileM.write ('Chrom, Start, End, Name, Score, Strand \n')
            for bed_file_row in bed_files[i]: 
                fileM.write(bed_file_row.id_chr + '\t')
                fileM.write("eventToGff" + '\t')   # for gff
                fileM.write('Subtype' + str (bed_file_row.subtype)+ '\t')  
                fileM.write(str(bed_file_row.first_bp)+ '\t')  
                fileM.write(str(bed_file_row.last_bp)+ '\t')  
                fileM.write(str(bed_file_row.score)+ '\t')  # for gff
                fileM.write(bed_file_row.strand_dir+ '\t' )  
                fileM.write('.'+ '\t')  
                fileM.write('Subtype' + str (bed_file_row.subtype)+ ';')  
                fileM.write('\n')



if __name__ == "__main__":
    main()
