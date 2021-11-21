from Cbx import southern_in_cbx
from InLocus import southern_in_locus


southern_type = input("What kind of integration are you checking for with the southern blot? cbx/in locus\n")
southern_type = southern_type.upper()

if southern_type == "CBX":
    southern_in_cbx()

elif southern_type == "IN LOCUS":
    southern_in_locus()
