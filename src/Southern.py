from Cbx import southern_in_cbx
from InLocus import southern_in_locus


southern_type = input("What kind of integration are you checking for with the southern blot? cbx/in locus\n")


if southern_type == "cbx" or southern_type == "Cbx":
    southern_in_cbx()

elif southern_type == "in locus" or southern_type == "In locus" or southern_type == "In Locus" or southern_type == "in Locus":
    southern_in_locus()
