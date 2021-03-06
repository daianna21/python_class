#Clase 2:
import Bio
from Bio import SeqIO
#Ejercicio 3: Leer archivos Fastq: letter annotations es especifico de fastq

mala_calidad=[]
umbral=40
promedio=0
for record in SeqIO.parse("C:/Users/hp/Downloads/sample.fastq", "fastq"):
    promedio=sum( record.letter_annotations["phred_quality"])/len(record.letter_annotations["phred_quality"])
    if (promedio<umbral):
        temp=(promedio,record.id)
        mala_calidad.append(temp)
print ('{} secuencias con promedio menor a umbral:{}\n'.format(len(mala_calidad),umbral))



#GENBANK

for gb_record in SeqIO.parse("C:/Users/hp/Downloads/aichi.gb", "genbank"):
    print('ID', gb_record.id)
    print('Secuencia', str(gb_record.seq)[0:30],'...')
    print('Longitud', len(gb_record))
atributos = gb_record.__dict__
print(atributos.keys())

#GenBank annotations (acceder a metadata)
for annotation, value in gb_record.annotations.items():
  print(annotation, value)


#Ejercicio 4 y 5:
for gb_record in SeqIO.parse("C:/Users/hp/Downloads/virus.gb", "genbank"):
    print(gb_record.annotations['date'])
    print(gb_record.annotations['organism'])
    print(gb_record.features[0].qualifiers)
    print(gb_record.features[0].qualifiers['country'])

#Ejercicio 6:
for gb_record in SeqIO.parse("C:/Users/hp/Downloads/virus.gb", "genbank"):
    for feature in gb_record.features:
        if feature.type=='CDS' and feature.qualifiers['gene']==['L']:
            start = feature.location.nofuzzy_start
            end = feature.location.nofuzzy_end
            seq = gb_record.seq[start:end]
            #print(seq)
            #print(seq.transcribe())
            #print(seq.translate())
            

#Tarea:

def info_organism(path, genes):
    """
    This function gets a genbank file and returns a series of interest traits
    of the organisms
            Parameters:
                    path: absolute path to file
                    genes: list with the names of the genes, each one in capital
                           letters and within brackets 
            Returns:
                    Organism: name of the organism
                    Date: date whern it was reported
                    Country: country where it was reported
                    Gene name: single letter name of the gene
                    Protein names: genes products
                    DNA: the first 15 nucleotides of each gene
                    RNA: the transcrit of DNA
                    Protein: peptide from DNA
    """
    #Get the file and format
    for gb_record in SeqIO.parse(path, "genbank"):
        #Get metadata
        print('Organism: ',gb_record.annotations['organism'])
        print('Date: ',gb_record.annotations['date'])
        #Get country from source 
        print('County: ',gb_record.features[0].qualifiers['country'])
        print('Isolation source: ',gb_record.features[0].qualifiers['isolation_source'])

        #Get those features that are CDS
        for feature in gb_record.features:
            if feature.type=='CDS':
                #Check if the CDS correspond to one of the given genes
                for gene in genes:
                     if feature.qualifiers['gene']==gene:
                         #Get info from the feature
                         print ('Gene name: ',feature.qualifiers['gene'])
                         print ('Protein name: ',feature.qualifiers['product'])
                         start = feature.location.nofuzzy_start
                         end = start + 15
                         seq = gb_record.seq[start:end]
                         print('DNA: ',seq, '...')
                         print('RNA: ',seq.transcribe(),'...')
                         print('Protein: ',seq.translate(),'...')
                     
       
#Example
print(info_organism("C:/Users/hp/Downloads/virus.gb", [['L'],['G']]))
    


            













  
