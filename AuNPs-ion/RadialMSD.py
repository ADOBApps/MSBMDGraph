#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
"""
Created on 29/01/2023
    Functions to graph solution differential heat data
@author: ADOB

require matplotlib, sympy, numpy, scipy
execute: pip install matplotlib sympy numpy scipy
"""

from win.graphmaker import Graphmaker
import csv

# ==========================================================================
# Vars
file_Au = open("Resources/MD/Full/Ion/2NPsys/RRMSD/radial_msd_WBFNP_sys_MD_topol_Au.csv", "r")
# /media/bloch/ACXEL_USB/Investigation/DEV/OpenMD/Metals/AuNPs/AuNPs-ion/Analysis/MSBMDGraph/Resources/MD/Full/Ion/2NPsys/RRMSD/radial_msd_WBFNP_sys_MD_topol_Au.csv

# convert csv to list of list
all_data_Au = list(csv.reader(file_Au, delimiter=";"))
file_Au.close()
time_Au = [float(row[0]) for row in all_data_Au]
corrVal_Au = [float(row[1]) for row in all_data_Au]

'''
file_Na = open("Resources/MD/Full/Ion/2NPsys/RRMSDRRMSD/radial_msd_WBNP_sys_MD_topol_Na.csv", "r")
# convert csv to list of list
all_data_Na = list(csv.reader(file_Na, delimiter=";"))
file_Na.close()
time_Na = [float(row[0]) for row in all_data_Na]
corrVal_Na = [float(row[1]) for row in all_data_Na]

file_Cl = open("Resources/MD/Full/Ion/2NPsys/RRMSDRRMSD/radial_msd_WBNP_sys_MD_topol_Cl.csv", "r")
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
        r"Radial Mean Squared Displacement",
        r"Time (fs)",
        r"Radial projection (corrVal)",
        "Resources/MD/Full/Ion/2NPsys/RRMSD/radialmsd_Au.0.pdf",
        time_Au,
        corrVal_Au,
        ".",
        r'Radial $MSD_{Au}(corrVal)$',
        4,  # "lower right"
        False,
        (),
        False,
        ()
    )
    mygraph.GraphXY(
        r"Radial Mean Squared Displacement",
        r"Time (fs)",
        r"Radial projection (corrVal)",
        "Resources/MD/Full/Ion/2NPsys/RRMSD/radialmsd_Au.0.png",
        time_Au,
        corrVal_Au,
        ".",
        r'Radial $MSD_{Au}(corrVal)$',
        4,  # "lower right"
        False,
        (),
        False,
        ()
    )

    # Sodium
    '''
    mygraph.GraphXY(
        r"Radial Mean Squared Displacement",
        r"Time (fs)",
        rResources/MD/Full/Ion/2NPsys/RRMSDRRMSD/radialmsd_Na.0.pdf",
        time_Na,
        corrVal_Na,
        ".",
        r'Radial $MSD_{Na}(corrVal)$',
        4,  # "lower right"
        False,
        (),
        False,
        ()
    )
    mygraph.GraphXY(
        r"Radial Mean Squared Displacement",
        r"Time (fs)",
        rResources/MD/Full/Ion/2NPsys/RRMSDRRMSD/radialmsd_Na.0.png",
        time_Na,
        corrVal_Na,
        ".",
        r'Radial $MSD_{Na}(corrVal)$',
        4,  # "lower right"
        False,
        (),
        False,
        ()
    )

    # Chloride
    mygraph.GraphXY(
        r"Radial Mean Squared Displacement",
        r"Time (fs)",
        rResources/MD/Full/Ion/2NPsys/RRMSDRRMSD/radialmsd_Cl.0.pdf",
        time_Cl,
        corrVal_Cl,
        ".",
        r'Radial $MSD_{Cl}(corrVal)$',
        4,  # "lower right"
        False,
        (),
        False,
        ()
    )
    mygraph.GraphXY(
        r"Radial Mean Squared Displacement",
        r"Time (fs)",
        rResources/MD/Full/Ion/2NPsys/RRMSDRRMSD/radialmsd_Cl.0.png",
        time_Cl,
        corrVal_Cl,
        ".",
        r'Radial $MSD_{Cl}(corrVal)$',
        4,  # "lower right"
        False,
        (),
        False,
        ()
    )
    '''


if __name__ == "__main__":
    Makegrap()
