#!/bin/bash
source /afs/cern.ch/work/e/elwaagaa/public/IBS/IBS_benchmark_for_Xsuite/003_PyIBS_Xsuite_treemaker/miniconda/bin/activate
cp -rf /afs/cern.ch/work/e/elwaagaa/public/IBS/IBS_benchmark_for_Xsuite/003_PyIBS_Xsuite_treemaker/SPS_injection_ions/001/* .
ls
pwd
python run_analysis.py > output_ht.txt 2> error_ht.txt
cp -rf *output* *log* *parquet* *txt* /afs/cern.ch/work/e/elwaagaa/public/IBS/IBS_benchmark_for_Xsuite/003_PyIBS_Xsuite_treemaker/SPS_injection_ions/001
