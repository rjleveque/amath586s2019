
import os,sys,glob,re

from convert_notebooks import make_html

run_notebooks = True   # if False, only fix existing html files

if 1:
    # all notebooks in this directory:
    notebook_files = glob.glob('*.ipynb')
    notebooks = [os.path.splitext(f)[0] for f in notebook_files]

    # filter out those not mentioned in the Index, if desired:
    index_file = open('Index.ipynb').read()
    notebooks = [f for f in notebooks if f+'.ipynb' in index_file]

if 0:
    # test or remake one notebook:
    notebooks = ['Index', 'Advection']

if 'Debugging_hints' in notebooks:
    # this one intentionally fails, need to make html by hand
    notebooks.remove('Debugging_hints')
    
make_html(notebooks, run_notebooks=run_notebooks)
