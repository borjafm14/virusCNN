# virusCNN

Implementation of a distributed convolutional neural network for DNA clasification based on the article "Analysis of DNA Sequence Classification Using CNN and Hybrid Models" by Hemalatha Gunasekaran et al (https://www.hindawi.com/journals/cmmm/2021/1835056/) and Horovod framework (https://github.com/horovod/horovod)

Follow the instructions of dataLocation.txt inside data folder in order to download the dataset, that includes DNA sequences of five viruses, covid-19, sars, mers, dengue and ebola.

This project includes two CNNs, the traditional one to be executed in one process (just execute "python main.py") and one adaptation of this CNN to be executed in more than one process using Horovod (mainHorovod.py). The file load_and_preprocessing.py is in charge of loading the sequences and creating the dataset.

The training phase of the Horovod CNN will be done in parallel between several nodes, depending on the configuration made on the execution commands.

The project also includes the scripts to execute the CNN on up to three computational nodes. These scripts are made for SLURM workload manager (https://slurm.schedmd.com/documentation.html)

For example, "submit1x1" means one node and one process per node, therefore this script just executes main.py. The script "submit2x1" means two nodes, one process per node, therefore this will execute mainHorovod.py and will tell SLURM to reserve two nodes exclusively.



