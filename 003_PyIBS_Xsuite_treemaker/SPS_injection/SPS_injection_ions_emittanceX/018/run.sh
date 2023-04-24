#!/bin/bash
source /afs/cern.ch/work/e/elwaagaa/public/IBS/IBS_benchmark_for_Xsuite/003_PyIBS_Xsuite_treemaker/miniconda/bin/activate
cp -rf /afs/cern.ch/work/e/elwaagaa/public/IBS/IBS_benchmark_for_Xsuite/003_PyIBS_Xsuite_treemaker/SPS_injection_ions_emittanceX/018/* .
ls
pwd
python run_analysis.py > output_ht.txt 2> error_ht.txt
python plot_analysis.py > output_ht_plot.txt 2> error_ht_plot.txt
cp -rf *output* *parquet* *txt* /afs/cern.ch/work/e/elwaagaa/public/IBS/IBS_benchmark_for_Xsuite/003_PyIBS_Xsuite_treemaker/SPS_injection_ions_emittanceX/018
