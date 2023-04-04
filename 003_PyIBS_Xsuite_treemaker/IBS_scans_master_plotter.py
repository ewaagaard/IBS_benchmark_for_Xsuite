"""
Master plotter for all parametric IBS scans for SPS ion injection
by Elias Waagaard 
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import yaml

import matplotlib as mpl
mpl.rcParams['axes.labelsize'] = 16
mpl.rcParams['xtick.labelsize'] = 14
mpl.rcParams['ytick.labelsize'] = 14
mpl.rcParams['ytick.labelsize'] = 14
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.markersize'] = 8

# Specify the AFS directory path, where all config files are located 
afs_path = '/afs/cern.ch/work/e/elwaagaa/public/IBS/IBS_benchmark_for_Xsuite/003_PyIBS_Xsuite_treemaker'

# Do the main walk over the Degrees Of Freedom 
DOFs = ['bunch_intensity', 'bunch_length', 'emittanceX', 'emittanceY', 'IBS_step', \
       'number_of_particles', 'RF_voltage']
main_data = dict.fromkeys(DOFs, [])  # master dictionaries 
    
# Read all the parquet iles in each subdirectory  
for scan in DOFs:
    for root, dirs, files in os.walk(f"/eos/user/e/elwaagaa/PhD/Projects/IBS/IBSresults_SPS_injection_ions_{scan}"):
        for directory in dirs:
            # Load simulation parameters from correct job folder
            with open(f"{afs_path}/SPS_injection_ions_{scan}/{directory}/config.yaml", "r") as f:
                config = yaml.safe_load(f)
            
            # Make new dictionary with all the info:
            data = {
                'xsuite_line': config['xsuite_line'],
                'energy': config['energy'],
                'nemitt_x': config["emit_x"]*1e-6,
                'nemitt_y': config["emit_y"]*1e-6,
                'RF_Voltage': config["V0max"],
                'Harmonic_Num': config["h"],
                'bunch_intensity': float(config["bunch_intensity"]),
                'sigma_z': config['sigma_z'],
                'n_part': int(config['n_part']),
                'n_turns': int(config['n_turns']),
                'IBS_step': int(config['IBS_step']),
                'Scan': scan
                }    
                
            # Activate the different modes and store the data 
            modes = []
            if config['mode_kinetic']: 
                modes.append('kinetic')
                data['kinetic_data'] = pd.read_parquet(f"IBSresults_SPS_injection_ions_{scan}/{directory}/xsuite_kinetic.parquet")
            if config['mode_analytical']: 
                modes.append('analytical')
                data['analytical_data'] = pd.read_parquet(f"IBSresults_SPS_injection_ions_{scan}/{directory}/xsuite_analytical.parquet")
            if config['mode_simple']: 
                modes.append('simple')
                data['simple_data'] = pd.read_parquet(f"IBSresults_SPS_injection_ions_{scan}/{directory}/xsuite_simple.parquet")
            data['modes'] = modes

            # Append to main_data
            main_data[scan].append(data)