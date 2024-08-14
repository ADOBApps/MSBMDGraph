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
time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 102]
r2 = []
rparallel = []
rperpendicular = []
mygraph = Graphmaker()

# ==========================================================================

# Plot graph and linearRegression type Time vs Temperature


def Makegrap():

    # t vs Potential energy
    mygraph.GraphX1Y3(
        r"Directional Mean Squared Displacement",
        r"Time (fs)",
        r"radius (nm)",
        "Resources/MD/DRMSD/Nuc1NPsys_drmsd_Au.pdf",
        time,
        r2,
        rparallel,
        rperpendicular,
        ".",
        "v",
        "*",
        r'$r^2(nm^2)$',
        r'$r_{parallel}(nm)$',
        r'$r_{perpendicular}(nm)$',
        "upper right",
        False,
        (),
        False,
        ()
    )

    # t vs Potential energy
    mygraph.GraphX1Y3(
        r"Directional Mean Squared Displacement",
        r"Time (fs)",
        r"radius (nm)",
        "Resources/MD/DRMSD/Nuc1NPsys_drmsd_Au.png",
        time,
        r2,
        rparallel,
        rperpendicular,
        ".",
        "v",
        "*",
        r'$r^2(nm^2)$',
        r'$r_{parallel}(nm)$',
        r'$r_{perpendicular}(nm)$',
        "upper right",
        False,
        (),
        False,
        ()
    )


if __name__ == "__main__":
    Makegrap()
