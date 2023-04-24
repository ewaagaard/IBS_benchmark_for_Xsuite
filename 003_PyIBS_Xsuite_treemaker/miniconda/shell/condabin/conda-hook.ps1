$Env:CONDA_EXE = "/afs/cern.ch/work/e/elwaagaa/public/IBS/IBS_benchmark_for_Xsuite/003_PyIBS_Xsuite_treemaker/miniconda/bin/conda"
$Env:_CE_M = ""
$Env:_CE_CONDA = ""
$Env:_CONDA_ROOT = "/afs/cern.ch/work/e/elwaagaa/public/IBS/IBS_benchmark_for_Xsuite/003_PyIBS_Xsuite_treemaker/miniconda"
$Env:_CONDA_EXE = "/afs/cern.ch/work/e/elwaagaa/public/IBS/IBS_benchmark_for_Xsuite/003_PyIBS_Xsuite_treemaker/miniconda/bin/conda"
$CondaModuleArgs = @{ChangePs1 = $True}
Import-Module "$Env:_CONDA_ROOT\shell\condabin\Conda.psm1" -ArgumentList $CondaModuleArgs

Remove-Variable CondaModuleArgs