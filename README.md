# Host-Taxon-Predictor
Authors: Anna Mashkovksaya, Olga Makarikova, Kirill Tsyganov
# Installation and Usage
The following command may be used for installation of the virus-classifier software:
```
pip install git+https://github.com/wojciech-galan/viruses_classifier.git –user
```
To install the additional libraries the following command is required:
```
conda install qt
```
To obtain the results of classification for several number of viral genomes, we used the following command:
```
viruses_classifier raw_or_FASTA-formatted_sequence_file --nucleic_acid rna --classifier [qda/lr/svc/knn]
```


