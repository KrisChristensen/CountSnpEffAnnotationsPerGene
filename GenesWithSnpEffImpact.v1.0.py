##########################################################
### Import Necessary Modules

import argparse                       #provides options at the command line
import sys                       #take command line arguments and uses it in the script
import gzip                       #allows gzipped files to be read
import re                       #allows regular expressions to be used

##########################################################
### Command-line Arguments
parser = argparse.ArgumentParser(description="A script to identify the number of genes with SnpEff impact categorizations")
parser.add_argument("-file", help = "The location of the vcf file, default=<stdin>, comma-separated for multiple files", nargs='+')
parser.add_argument("-out", help = "The annotation to look for, default = HIGH, option = MEDIUM, LOW, or MODIFIER", default="HIGH")
args = parser.parse_args()

#########################################################
### Global Variables
class Variables():
    genes = {}

#########################################################
### Opening files and functions
class OpenFile():
    def __init__ (self, f, typ):
        """Opens a file a gzipped or bgzip file accepted"""
        if re.search(".gz$", f):
            self.filename = gzip.open(f, 'rb')
        else:
            self.filename = open(f, 'r')
        sys.stderr.write("\n\tOpening file {}\n\n".format(f))
        if typ == "vcf":
            OpenVCF(self.filename)

class OpenVCF():
    def __init__ (self, vcf):
        """Reads the vcf file and finds the distribution of variants in all windows"""
        print("{}\t{}".format("geneID", "variant Count"))
        self.totalGeneCount = 0
        for self.line in vcf:
            try:
                self.line = self.line.decode('utf-8')
            except:
                pass        
            self.line = self.line.rstrip('\n')
            if not re.search("^#", self.line):  
                self.chrom, self.pos, self.id, self.ref, self.alt, self.qual, self.filter, self.info, self.format = self.line.split("\t")[0:9]        
                ################################
                ###Check for annotation      ###
                #print ("{}".format(self.info))
                self.annotations = self.info.split(";")[-1][4:].split(",")
                self.count = {}
                for self.index, self.annotation in enumerate(self.annotations):
                    self.nucl, self.type, self.impact, self.gene = self.annotation.split("|")[0:4]
                    #print("nucleotide: {}, type: {}, impact: {}".format(self.nucl, self.type, self.impact))
                    if self.impact == args.out:
                        self.count[self.gene] = 1
                for self.gene in self.count:
                    if self.gene in Variables.genes:
                        Variables.genes[self.gene] += 1
                    else:
                        self.totalGeneCount += 1
                        Variables.genes[self.gene] = 1
                ################################
        for self.finalGene in Variables.genes:
            print("{}\t{}".format(self.finalGene, Variables.genes[self.finalGene]))
        sys.stderr.write("\tNumber of genes identified with the snpEff category {}: {}\n\n".format(self.totalGeneCount, args.out))
        vcf.close()                


#########################################################
###Order of things to be called
if __name__ == '__main__':
    Variables()
    if len(args.file) > 0:
        for index, vcfFile in enumerate(args.file):
            open_file = OpenFile(vcfFile, "vcf")
