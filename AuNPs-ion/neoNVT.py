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
"""
from mycontrollers.graph.ctrl.math.linearmath import LSOnlyGraph
from mycontrollers.graph.ctrl.math.linearmath import LinearSolveComp
from mycontrollers.graph.ctrl.math.linearmath import LinearSolve
"""

# ==========================================================================
# Vars
file = open("Resources/NVT/Full/Ion/2NPsys/WBFDL_sys_NVT_topol.csv", "r")
# convert csv to list of list
all_data = list(csv.reader(file, delimiter=";"))
file.close()

time = [float(row[0]) for row in all_data]
t_energy = [float(row[1]) for row in all_data]
p_energy = [float(row[2]) for row in all_data]
k_energy = [float(row[3]) for row in all_data]
temperature = [float(row[4]) for row in all_data]
pressure = [float(row[5]) for row in all_data]
volume = [float(row[6]) for row in all_data]
conserved_quant = [float(row[7]) for row in all_data]
restraint = [float(row[8]) for row in all_data]

mygraph = Graphmaker()

# 
# ==========================================================================

# Plot graph and linearRegression type Time vs Temperature


def Makegrap():

    # t vs Temperature
    mygraph.GraphXY(
        r"NVT Temperature",
        r"Time (fs)",
        r"Temperature ($K$)",
        "Resources/NVT/Full/Ion/2NPsys/temperature.0.pdf",
        time,
        temperature,
        ".",
        r'Temperature $(K)$',
        2,  # "upper right"
        False,
        (),
        False,
        ()
    )
    mygraph.GraphXY(
        r"NVT Temperature",
        r"Time (fs)",
        r"Temperature ($K$)",
        "Resources/NVT/Full/Ion/2NPsys/temperature.0.png",
        time,
        temperature,
        ".",
        r'Temperature $(K)$',
        2,  # "upper right"
        False,
        (),
        False,
        ()
    )

    # t vs Volume
    mygraph.GraphXY(
        r"NVT Volume",
        r"Time (fs)",
        r"Volume ($A^3$)",
        "Resources/NVT/Full/Ion/2NPsys/volume.0.pdf",
        time,
        volume,
        ".",
        r'Volume $(A^3)$',
        2,  # "upper right"
        False,
        (),
        False,
        ()
    )
    mygraph.GraphXY(
        r"NVT Volume",
        r"Time (fs)",
        r"Volume ($A^3$)",
        "Resources/NVT/Full/Ion/2NPsys/volume.0.png",
        time,
        volume,
        ".",
        r'Volume $(A^3)$',
        2,  # "upper right"
        False,
        (),
        False,
        ()
    )

    # t vs Conserved Quantity
    mygraph.GraphXY(
        r"NVT  Restraint Potential",
        r"Time (fs)",
        r"Restraint Potential ($\frac{kcal}{mol}$)",
        "Resources/NVT/Full/Ion/2NPsys/restraint.0.pdf",
        time,
        restraint,
        ".",
        r'Restraint Potential $(\frac{kcal}{mol})$',
        4,  # "uper right"
        False,
        (),
        False,
        ()
    )
    mygraph.GraphXY(
        r"NVT  Restraint Potential",
        r"Time (fs)",
        r"Restraint Potential ($\frac{kcal}{mol}$)",
        "Resources/NVT/Full/Ion/2NPsys/restraint.0.png",
        time,
        restraint,
        ".",
        r'Restraint Potential $(\frac{kcal}{mol})$',
        4,  # "uper right"
        False,
        (),
        False,
        ()
    )


if __name__ == "__main__":
    Makegrap()
