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
file = open("Resources/NPTi/Full/Ion/2NPsys/WBFDL_sys_NPTi_topol.csv", "r")
# convert csv to list of list
all_data = list(csv.reader(file, delimiter=";"))
file.close()

time = [float(row[0]) for row in all_data]
temperature = [float(row[4]) for row in all_data]
pressure = [float(row[5]) for row in all_data]
restraint = [float(row[8]) for row in all_data]

mygraph = Graphmaker()

# ==========================================================================

# Plot graph and linearRegression type Time vs Temperature


def Makegrap():

    # t vs Temperature
    mygraph.GraphXY(
        r"NPTi Temperature",
        r"Time (fs)",
        r'Temperature $(K)$',
        "Resources/NPTi/Full/Ion/2NPsys/temperature.0.pdf",
        time,
        temperature,
        ".",
        r'Temperature $(K)$',
        2,
        False,
        (),
        False,
        ()
    )
    mygraph.GraphXY(
        r"NPTi Temperature",
        r"Time (fs)",
        r'Temperature $(K)$',
        "Resources/NPTi/Full/Ion/2NPsys/temperature.0.png",
        time,
        temperature,
        ".",
        r'Temperature $(K)$',
        2,
        False,
        (),
        False,
        ()
    )

    # t vs pressure
    mygraph.GraphXY(
        r"NPTi pressure",
        r"Time (fs)",
        r"Pressure ($atm$)",
        "Resources/NPTi/Full/Ion/2NPsys/pressure.0.pdf",
        time,
        pressure,
        ".",
        r'Pressure $(atm)$',
        2,  # "upper right"
        False,
        (),
        False,
        ()
    )
    mygraph.GraphXY(
        r"NPTi pressure",
        r"Time (fs)",
        r"Pressure ($atm$)",
        "Resources/NPTi/Full/Ion/2NPsys/pressure.0.png",
        time,
        pressure,
        ".",
        r'Pressure $(atm)$',
        2,  # "upper right"
        False,
        (),
        False,
        ()
    )

    # t vs Conserved Quantity
    mygraph.GraphXY(
        r"NPTi  Restraint Potential",
        r"Time (fs)",
        r"Restraint Potential ($\frac{kcal}{mol}$)",
        "Resources/NPTi/Full/Ion/2NPsys/restraint.0.pdf",
        time,
        restraint,
        ".",
        r'Restraint Potential $(\frac{kcal}{mol})$',
        2,  # "upper right"
        False,
        (),
        False,
        ()
    )
    mygraph.GraphXY(
        r"NPTi  Restraint Potential",
        r"Time (fs)",
        r"Restraint Potential ($\frac{kcal}{mol}$)",
        "Resources/NPTi/Full/Ion/2NPsys/restraint.0.png",
        time,
        restraint,
        ".",
        r'Restraint Potential $(\frac{kcal}{mol})$',
        2,  # "upper right"
        False,
        (),
        False,
        ()
    )


if __name__ == "__main__":
    Makegrap()
