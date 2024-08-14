#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
"""
Created on 08/07/2022
    Functions to graph Mean squared Displacement (MSD)
@author: ADOB
Last Modification: 22:23 10-06-2024

require matplotlib, sympy, numpy, scipy
execute: pip install matplotlib sympy numpy scipy
"""

from win.graphmaker import Graphmaker
import csv

""""""


# ==========================================================================
# Vars
file_Au = open(
    "Resources/MD/Full/Ion/2NPsys/RMSD/rmsd_WBFNP_sys_MD_topol_Au.csv",
    "r"
)

# Ion/1NPsys
# Resources/MD/Full/Ion/1NPsys/RMSD/rmsd_WBFDL_sys_MD_topol_Au.csv

# Nucleus/1NPsys
# Resources/MD/Full/Nucleus/1NPsys/RMSD/rmsd_WBFNP_sys_MD_topol_Au.csv

# Ion/2NPsys
# Resources/MD/Full/Ion/2NPsys/RMSD/rmsd_WBFNP_sys_MD_topol_Au.csv

# Nucleus/2NPsys
# Resources/MD/Full/Nucleus/2NPsys/RMSD/rmsd_WBFNP_sys_MD_topol_Au.csv

# convert csv to list of list
all_data_Au = list(csv.reader(file_Au, delimiter=";"))
file_Au.close()
time_Au = [float(row[0]) for row in all_data_Au]
corrVal_Au = [float(row[1]) for row in all_data_Au]

'''
file_Na = open(
    "Resources/MD/Nucleus/2NPsys/rmsd_WBNP_sys_MD_topol_Na.csv",
    "r"
)
# convert csv to list of list
all_data_Na = list(csv.reader(file_Na, delimiter=";"))
file_Na.close()
time_Na = [float(row[0]) for row in all_data_Na]
corrVal_Na = [float(row[1]) for row in all_data_Na]

file_Cl = open(
    "Resources/MD/Nucleus/2NPsys/rmsd_WBNP_sys_MD_topol_Cl.csv",
    "r"
)
# convert csv to list of list
all_data_Cl = list(csv.reader(file_Cl, delimiter=";"))
file_Cl.close()
time_Cl = [float(row[0]) for row in all_data_Cl]
corrVal_Cl = [float(row[1]) for row in all_data_Cl]
'''

mygraph = Graphmaker()

# ==========================================================================

# Plot graph and linearRegression type Time vs Temperature


def Makegrap():

    # Gold
    mygraph.GraphXY(
        r"Mean Squared Displacement",
        r"Time (fs)",
        r"MSD $(10^{-20}m^{2})$",
        "Resources/MD/Full/Ion/2NPsys/RMSD/rmsd_Au.0.pdf",
        time_Au,
        corrVal_Au,
        ".",
        r'$MSD_{Au}$',
        4,  # "lower right"
        False,
        (),
        False,
        ()
    )
    mygraph.GraphXY(
        r"Mean Squared Displacement",
        r"Time (fs)",
        r"MSD $(10^{-20}m^{2})$",
        "Resources/MD/Full/Ion/2NPsys/RMSD/rmsd_Au.0.png",
        time_Au,
        corrVal_Au,
        ".",
        r'$MSD_{Au}$',
        4,  # "lower right"
        False,
        (),
        False,
        ()
    )

    # Sodium
    '''
    mygraph.GraphXY(
        r"Mean Squared Displacement",
        r"Time (fs)",
        r"corrVal",
        "Resources/MD/Nucleus/2NPsys/rmsd_Na.0.pdf",
        time_Na,
        corrVal_Na,
        ".",
        r'$MSD_{Na}$ (corrVal)',
        4,  # "lower right"
        False,
        (),
        False,
        ()
    )
    mygraph.GraphXY(
        r"Mean Squared Displacement",
        r"Time (fs)",
        r"corrVal",
        "Resources/MD/Nucleus/2NPsys/rmsd_Na.0.png",
        time_Na,
        corrVal_Na,
        ".",
        r'$MSD_{Na}$ (corrVal)',
        4,  # "lower right"
        False,
        (),
        False,
        ()
    )

    # Chloride
    mygraph.GraphXY(
        r"Mean Squared Displacement",
        r"Time (fs)",
        r"corrVal",
        "Resources/MD/Nucleus/2NPsys/rmsd_Cl.0.pdf",
        time_Cl,
        corrVal_Cl,
        ".",
        r'$MSD_{Cl}$ (corrVal)',
        4,  # "lower right"
        False,
        (),
        False,
        ()
    )
    mygraph.GraphXY(
        r"Mean Squared Displacement",
        r"Time (fs)",
        r"corrVal",
        "Resources/MD/Nucleus/2NPsys/rmsd_Cl.0.png",
        time_Cl,
        corrVal_Cl,
        ".",
        r'$MSD_{Cl}$ (corrVal)',
        4,  # "lower right"
        False,
        (),
        False,
        ()
    )
    '''


if __name__ == "__main__":
    Makegrap()
