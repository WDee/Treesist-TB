# Treesist-TB
A modified decision tree approach to improve the prediction and mutation discovery for drug resistance in Mycobacterium tuberculosis

# Installation 
The modified decision tree requires adjusting the default sklearn decision tree. the following steps are needed. 1. Copy the five files from the directory "new_splitter". 2. Create an activate a new virtual environment following the code steps as per below 

`conda create --name py3 python=3.6 ipykernel jupyter anaconda scipy graphviz pydotplus python-graphviz cython gxx_linux-64

`conda activate py3

`ipython kernel install --name py3 --user

`conda install gxx_linux-64

`export PATH=$PATH:/#enteryourpath#/anaconda2/envs/py3/bin'

It migth be needed to find and subsequently rename the quad_tree files, e.g. approximately as per below (after locating and going to the right directory):

'mv _quad_tree.pxd quad_tree.pxd

In case there is an error in installation, it might be needed to copy over the numpy headers (e.g. approximately as per below, adjust path where needed): 

'cp -r ~/anaconda2/envs/py3/lib/python3.6/site-packages/numpy/core/include/numpy/* ~/anaconda2/envs/py3/include/python3.6m/numpy/

Subsequently, resource the bash (source ~/.bashrc) and run the main file. The installation of the new splitter is done by the following lines, that one should uncomment if needed: 

'!python setup.py build_ext –inplace
'%load_ext autoreload
'%autoreload 2
'from new_splitter import NewBestSplitter

# Notes
The jupyter notebook demonstrates the algorithm on dummy (random) data. Any actual genomic files should be provided in the same format (e.g. same column headers) 
