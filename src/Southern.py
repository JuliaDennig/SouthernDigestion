from Cbx import southern_in_cbx
from InLocus import southern_in_locus


southern_type = input("What kind of integration are you checking for with the southern blot? cbx/in locus\n")


if southern_type == "cbx" or southern_type == "Cbx":
    southern_in_cbx()

elif southern_type == "in locus" or southern_type == "In locus" or southern_type == "In Locus" or southern_type == "in Locus":
    southern_in_locus()

#Dateien:
#wt - C:\Users\julia\Desktop\PythonPro\Testfiles\UMAG_04391_Genom.ape
#del - C:\Users\julia\Desktop\PythonPro\Testfiles\del04391_GenR_Genom.ape

#wt - C:\Users\julia\Desktop\PythonPro\Testfiles\04391_Genom.ape
#del - C:\Users\julia\Desktop\PythonPro\Testfiles\04391_Genom+ GFP-Fusion.ape

#wt - C:\Users\julia\Downloads\Hdp1 Lokus.ape
#del - C:\Users\julia\Downloads\Hdp1 lokus pJU55.ape

#wt - C:\Users\julia\Desktop\PythonPro\Testfiles\cbx_locus.ape
#si - C:\Users\julia\Desktop\PythonPro\Testfiles\suc2_cbx-locus_single.ape
#mi - C:\Users\julia\Desktop\PythonPro\Testfiles\suc2_cbx-locus_multiple.ape