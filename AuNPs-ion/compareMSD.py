#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
"""
Created on 08/07/2022
    Functions to graph solution differential heat data
@author: ADOB

require matplotlib, sympy, numpy, scipy
execute: pip install matplotlib sympy numpy scipy
"""

from win.graphmaker import Graphmaker
import csv

""""""

# ==========================================================================
# Vars

# Ion/1NPsys
# Resources/MD/Full/Ion/1NPsys/RMSD/rmsd_WBFDL_sys_MD_topol_Au.csv

# Nucleus/1NPsys
# Resources/MD/Full/Nucleus/1NPsys/RMSD/rmsd_WBFNP_sys_MD_topol_Au.csv


# Ion/2NPsys
# Resources/MD/Full/Ion/2NPsys/RMSD/rmsd_WBFNP_sys_MD_topol_Au.csv

# Nucleus/2NPsys
# Resources/MD/Full/Nucleus/2NPsys/RMSD/rmsd_WBFNP_sys_MD_topol_Au.csv

file_Au = open(
    "Resources/MD/Full/Nucleus/1NPsys/RMSD/rmsd_WBFNP_sys_MD_topol_Au.csv",
    "r"
)

# convert csv to list of list
all_data_Au = list(csv.reader(file_Au, delimiter=";"))
file_Au.close()

file_Au2 = open(
    "Resources/MD/Full/Ion/1NPsys/RMSD/rmsd_WBFDL_sys_MD_topol_Au.csv",
    "r"
)

# convert csv to list of list
all_data_Au2 = list(csv.reader(file_Au2, delimiter=";"))
file_Au2.close()

time = [float(row[0]) for row in all_data_Au]
corrVal_Nuc_Au = [float(colm[1]) for colm in all_data_Au]
corrVal_Ion_Au = [float(row2[1]) for row2 in all_data_Au2]

mygraph = Graphmaker()

# ==========================================================================

# Plot graph and linearRegression type Time vs Temperature


def Makegrap():

    # Gold
    mygraph.ComparisonXY2(
        r"MSD Comparison",
        r"Time (fs)",
        r"MSD $(10^{-20}m^{2})$",
        "Resources/MD/Full/Both/1NPsys/RMSD/rmsd_Au.0.pdf",
        time,
        corrVal_Nuc_Au,
        corrVal_Ion_Au,
        ".",
        ".",
        r'Nucleic Mono-AuNP',
        r'Ionic Mono-AuNP',
        4,  # "lower right"
        False,
        (),
        False,
        ()
    )
    mygraph.ComparisonXY2(
        r"MSD Comparison",
        r"Time (fs)",
        r"MSD $(10^{-20}m^{2})$",
        "Resources/MD/Full/Both/1NPsys/RMSD/rmsd_Au.0.png",
        time,
        corrVal_Nuc_Au,
        corrVal_Ion_Au,
        ".",
        ".",
        r'Nucleic Mono-AuNP',
        r'Ionic Mono-AuNP',
        4,  # "lower right"
        False,
        (),
        False,
        ()
    )


if __name__ == "__main__":
    Makegrap()
