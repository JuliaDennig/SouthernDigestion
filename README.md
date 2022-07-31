# SouthernDigestion

## What to use for?
The program searches for one/two enzyme(s) used in Southern Blot to verify the transformation of an organism.
The program differentiates between an _in locus_ transformation and an _in cbx_ (_Ustilago maydis_ specific locus) transformation.


## How to use?
You need the `.ape`-files in which the features where the probe used in Southern Blot is marked.
The program is started by `python Southern.py`. First input differentiates between _in locus_ or
_cbx_ integration. 

If you chose _in locus_ integration the program first takes the location of the wildtype `.ape`-file, giving the annotated features and taking the features where the probe used in Southern Blot is binding. Next, it takes the location of the mutation `.ape`-file, giving the annotated features and taking the features where the probe used in Southern Blot is binding.

If you chose _cbx_ integration the program first takes the location of the wildtype `.ape`-file, giving the annotated features and taking the features where the probe used in Southern Blot is binding. Next, it takes the location of the single integration `.ape`-file, giving the annotated features and taking the features where the probe used in Southern Blot is binding. Next, it takes the location of the multiple integration `.ape`-file, giving the annotated features and taking the features where the probe used in Southern Blot is binding. After taking in the location of the used `.ape`-files, the program moves on to the results, first giving one single enzyme suitable for digesting the DNA prior to Southern Blot. If you already found a fitting enzyme for digestion, you can stop the program at this point by typing `n`. If you want the program to also search for combinations using two enzymes or the program couldn't find an enzyme for single use for digestion, it moves on to giving enzyme combinations suitable for digesting the DNA before Southern Blot.

## Which enzymes are the program checking for?
You can find the list of enzymes and their features in the file `Enyzmedatabase.py`. The list can also be adapted to your needs.

## What are the criteria for suitable enzymes?
All bands have to be between 8000 bp and 1000 bp. The difference between the two bands has to be at least 500 bp. If one of the compared bands is over the size of 3000 bp the difference of the bands has to be at least 1000 bp. If one of the compared bands is over the size of 6000 bp the difference of the bands has to be at least 2000 bp. In the case of _in locus_ integration at least one of the sequences digestions (wildtype or mutation) should result in more than one band.

## How do the single files of the program work together?

The file `OpenApe.py` takes the location of the `.ape`-files, opens them and saves the features, their locations and the sequence. 

The file `EnzymeBindingSites.py` takes the sequence from`OpenApe.py`, searches for cutting sites of enzymes listed in `Enzymedatabase.py` and in case of cutting saves the enzyme name and the cutting sites.

The file `OneEnzyme.py` creates a dictionary of all single enzymes and their resulting bands in Southern Blot. 

The file `TwoEnzymes.py` creates a dictionary of all enzyme combinations and their resulting bands in Southern Blot.

The file `Southern_current.py` runs `OpenApe.py`,`EnzymeBindingSites.py`, `OneEnzyme.py` and `TwoEnzymes`.

The file `BiologicalCheck.py` checks the dictionaries created in `OneEnzyme.py` and `TwoEnzyme.py` if the resulting bands are suitable for Southern Blot. The file `Cbx.py` collects in case of the input `cbx` the results and prints them. 

The file `InLocus.py` collects in case of the input `in locus` the results and prints them. The file `Southern.py` starts the program, differentiates between cbx and in locus integration and then either runs `Cbx.py` or `InLocus.py`.
