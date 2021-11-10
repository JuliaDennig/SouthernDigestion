from Cbx import southernInCbx
from InLocus import southernInLocus


southerntype = input("What kind of integration are you checking for with the southern blot? cbx/in locus\n")


if southerntype == "cbx" or southerntype == "Cbx":
    southernInCbx()

elif southerntype == "in locus" or southerntype == "In locus" or southerntype == "In Locus" or southerntype == "in Locus":
    southernInLocus()

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