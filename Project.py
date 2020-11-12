from tkinter import *
from tkinter import filedialog as fd
from pathlib import Path
from tkinter import messagebox

result = ""

def transcribe(sequence):
    #Transcribes the sequence
    RNA_sequence = sequence.replace('T', 'U')
    return RNA_sequence

def translate(sequence):
    #Genetic code table for translation
    table = {"AAA":"K", "AAC":"N", "AAG":"K", "AAU":"N", 
            "ACA":"T", "ACC":"T", "ACG":"T", "ACU":"T", 
            "AGA":"R", "AGC":"S", "AGG":"R", "AGU":"S", 
            "AUA":"I", "AUC":"I", "AUG":"M", "AUU":"I", 

            "CAA":"Q", "CAC":"H", "CAG":"Q", "CAU":"H", 
            "CCA":"P", "CCC":"P", "CCG":"P", "CCU":"P", 
            "CGA":"R", "CGC":"R", "CGG":"R", "CGU":"R", 
            "CUA":"L", "CUC":"L", "CUG":"L", "CUU":"L", 

            "GAA":"E", "GAC":"D", "GAG":"E", "GAU":"D", 
            "GCA":"A", "GCC":"A", "GCG":"A", "GCU":"A", 
            "GGA":"G", "GGC":"G", "GGG":"G", "GGU":"G", 
            "GUA":"V", "GUC":"V", "GUG":"V", "GUU":"V", 

            "UAA":"_", "UAC":"Y", "UAG":"_", "UAU":"T", 
            "UCA":"S", "UCC":"S", "UCG":"S", "UCU":"S", 
            "UGA":"_", "UGC":"C", "UGG":"W", "UGU":"C", 
            "UUA":"L", "UUC":"P", "UUG":"L", "UUU":"P"
    }
    #Possible start codon sequnce iniation
    #start_codon = sequence.find('ATG')
    #sequence_start = sequence[int(start_codon):]

    #Checks for amount of codons possible, cuts down until its possible by modulo 3
    protein = ""
    if len(sequence) % 3 == 0:
        for i in range(0, len(sequence), 3):
            codon = sequence[i:i + 3]                
            protein += table[codon]

    elif (len(sequence) - 1) % 3 == 0:
        for i in range(0, len(sequence)-1, 3):
            codon = sequence[i:i + 3]                
            protein += table[codon]
    
    elif (len(sequence) - 2) % 3 == 0:
        for i in range(0, len(sequence)-2, 3):
            codon = sequence[i:i + 3]                
            protein += table[codon]
    return protein


def MSA(sequence1, sequence2):
    #Multiple sequence alignment, compare two given sequences and compares them to count for matches, mismatches and gaps
    matches = 0
    gaps = 0    
    mismatch = 0
    max_seq = ""
    min_seq = ""
    #Checks for the longer sequence as threshold for the alignment
    if (len(sequence1) >= len(sequence2)):
        max_seq = sequence1
        min_seq = sequence2
    else:
        max_seq = sequence2
        min_seq = sequence1
    counter = 0

    while(counter < len(max_seq) and counter < len(min_seq)):
        if(max_seq[counter] == "_" or min_seq[counter] == "_"):
            gaps += 1
        elif(max_seq[counter] ==  min_seq[counter]):
            matches += 1
        elif(max_seq[counter] != min_seq[counter]):
            mismatch += 1
        counter += 1
       
    #Counts for the rest of the ssequence as gaps  
    while(counter < len(max_seq)):
        gaps += 1 
        counter += 1   

    percentageMatch = matches/len(max_seq)*100
    return ("Matches: ", matches, "Mismatches: ", mismatch, "Gaps: ", gaps, "Percentage for matches: ", "{:.0f}".format(percentageMatch), "%")
    
def read_sequence(file):
    #Read sequnce, and "cleans" file for unecessary chars
    with open(file, "r") as f: 
        seq = f.read() 
    seq = seq.replace("\n", "")  
    seq = seq.replace("\r", "")   
    seq = seq.upper()
    return seq
    
def main(file1, file2):
    #Runs through the whole program, backend.
    global result
    sequence1 = read_sequence(file1)
    sequence2 = read_sequence(file2)

    td_seq1 = transcribe(sequence1)
    td_seq2 = transcribe(sequence2)

    protein_seq1 = translate(td_seq1)
    #print("Proteinseq1", protein_seq1)
    protein_seq2 = translate(td_seq2)
    #print("Proteinseq2", protein_seq2)

    result = MSA(protein_seq1, protein_seq2)
    return result
  

#GUI, root window/frame
root = Tk()


#Iniating global varibales 
file1 = StringVar()
file1.set("File1")
file2 = StringVar()
file2.set("File2")
filename1 = ""
filename2 = ""

#Sets sizes and layout
root.geometry('400x400')
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

#Button eventhandler for button1 
def buttonClick1():
    global filename1
    seqeunce1 = fd.askopenfilename()
    path = Path(seqeunce1)
    file1.set(path.name)
    filename1 = path.name

#Button event handler for button2 
def buttonClick2():
    #Gets file and filename for sequence 
    global filename2
    seqeunce1 = fd.askopenfilename()
    path = Path(seqeunce1)
    file2.set(path.name)
    filename2 = path.name

def runMSAmain():
    #Runs the program
    #print(filename1)
    #print(filename2)
    msaresult = main(filename1, filename2)
    messagebox.showinfo("MSAResult", msaresult)


#Iniation of frontend variables
chooseFileButton1 = Button(topFrame, command=buttonClick1, text = "Choose file")
chooseFileButton1.pack()
labelFile1 = Label(topFrame, textvariable=file1)
labelFile1.pack()

chooseFileButton2 = Button(topFrame, command=buttonClick2,text = "Choose file")
chooseFileButton2.pack()
labelFile2 = Label(topFrame, textvariable=file2)
labelFile2.pack()

runMSA = Button(topFrame, command = runMSAmain, text = "Run MSA")
runMSA.pack()

#Runs the program until its quit
root.mainloop()
