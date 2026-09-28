print ('--------DNA SEQUENCE ANALYZER--------')


Input_dna = input("Enter a DNA sequence:- ").replace(" ", "")

if Input_dna == "":
    print ("DNA sequence cannot be empty.")
    exit()
Input_dna= Input_dna.upper()

if all (base in "ATGC" for base in Input_dna):

    print(" Valid DNA sequence :] ")

    print(" Your entered value: ", Input_dna)

    print (" Total Sequence length :", len(Input_dna))

    print ("No of A count:", Input_dna.count("A"))

    print ("No of T count:", Input_dna.count("T"))

    print ("No of G count:", Input_dna.count("G"))

    print("No of C count:", Input_dna.count("C"))

    gc_content = (Input_dna.count("G") + Input_dna.count("C")) /len(Input_dna) *100

    at_content =(Input_dna.count("A") + Input_dna.count("T")) / len(Input_dna)* 100

    print ("GC Content:", round(gc_content, 2), "%")

    print ("AT Content:", round(at_content, 2), "%")
    complements = ""

    for base in Input_dna:
        if base =="A":
            complements +="T"
        elif base =="T":
            complements  +="A"
        elif base =="G":
            complements +="C"
        elif base =="C":
            complements+="G"

    print  ("Complement:",  complements)
    reverse_complement = complements[::-1]

    print("Reverse Complement:" , reverse_complement)
    rna = Input_dna.replace("T", "U")

    print("RNA sequence:", rna)
    
    codons = []

for i in range (0, len(Input_dna) - 2, 3):
    codon = Input_dna[i:i+3]
    codons.append(codon)


 
    print ("Codons:", codons)
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]

    if start_codon in codons:
        print ("Start codon found: ATG")
        
    else:
        print ("No start codon found")

    found_stop =False

    for codon in codons:
        if codon in stop_codons:
            print  ("Stop codon found:", codon)
            found_stop = True

    if not found_stop:
            
            print("Not stopping codon found")


    codon_table = {
        "ATG": "Methionine",
        "TTT": "Phenylalanine",
        "TTC": "Phenylalanine",
        "TTA": "Leucine",
        "TTG":"Leucine",
        "TAA": "Stop",
        "TAG": "Stop",
        "TGA": "Stop"
    }
    

print ("Amino acids:")

for codon in codons:
    if codon in codon_table:
        print( codon, "->", codon_table[codon])
    else:
        print(codon, "-> Unknown")
stop_codons = ["TAA","TAG", "TGA"]

found_stop =  False
if gc_content > 50:
    print ("DNA is GC rich")
elif gc_content < 50:
    print("DNA is AT rich")
else:
    print("DNA has total equal no of GC and AT content")



gc_at_ratio =  gc_content /  at_content
print ("GC /AT ratio:",round(gc_at_ratio, 2))