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

"""
from mycontrollers.graph.ctrl.math.linearmath import LSOnlyGraph
from mycontrollers.graph.ctrl.math.linearmath import LinearSolveComp
from mycontrollers.graph.ctrl.math.linearmath import LinearSolve
"""

# ==========================================================================
# Vars
time = []
temperature = []
pressure = []
volume = []
restraint = []
mygraph = Graphmaker()

# ==========================================================================

# Plot graph and linearRegression type Time vs Temperature


def Makegrap():

    # t vs Temperature
    mygraph.GraphXY(
        r"MD Temperature",
        r"Time (fs)",
        r'Temperature $(K)$',
        "Resources/MD/MD_Ion_1NPsys_temperature.0.pdf",
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
        r"MD Temperature",
        r"Time (fs)",
        r'Temperature $(K)$',
        "Resources/MD/MD_Ion_1NPsys_temperature.0.png",
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
        r"MD pressure",
        r"Time (fs)",
        r"Pressure ($atm$)",
        "Resources/MD/MD_Ion_1NPsys_pressure.0.pdf",
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
        r"MD pressure",
        r"Time (fs)",
        r"Pressure ($atm$)",
        "Resources/MD/MD_Ion_1NPsys_pressure.0.png",
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

    # t vs Volume
    mygraph.GraphXY(
        r"MD Volume",
        r"Time (fs)",
        r"Volume ($A^3$)",
        "Resources/MD/MD_Nuc_2NPsys_volume.0.pdf",
        time,
        volume,
        ".",
        r'Volume $(A^3)$',
        "upper right",
        False,
        (),
        False,
        ()
    )
    mygraph.GraphXY(
        r"MD Volume",
        r"Time (fs)",
        r"Volume ($A^3$)",
        "Resources/MD/MD_Nuc_2NPsys_volume.0.png",
        time,
        volume,
        ".",
        r'Volume $(A^3)$',
        "upper right",
        False,
        (),
        False,
        ()
    )


if __name__ == "__main__":
    Makegrap()
