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
p_energy = [-76265.566, 2420459.3, 2343601.2, 95905.836, -59963.035, -73768.306, -76357.421, -76858.85, -76836.452, -76704.511, -76577.03, -76478.697, -76408.491, -76360.304, -76327.864, -76306.375, -76292.249, -76282.987, -76276.906, -76272.941, -76270.376, -76268.69, -76267.598, -76266.887, -76266.425, -76266.124, -76265.929, -76265.802, -76265.72, -76265.666, -76265.631, -76265.609, -76265.594, -76265.584, -76265.578, -76265.574, -76265.571, -76265.57, -76265.569, -76265.568, -76265.567, -76265.567, -76265.567, -76265.567, -76265.567, -76265.567, -76265.567, -76265.567, -76265.567, -76265.567, -76265.567, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566, -76265.566]
mygraph = Graphmaker()

# ==========================================================================

# Plot graph and linearRegression type Time vs Temperature


def Makegrap():

    # t vs Potential energy
    mygraph.GraphXY(
        r"Energy Minimization",
        r"Time (fs)",
        r"Potential Energy ($\frac{kcal}{mol}$)",
        "Resources/EM/Nuc2NPsysEM_potential_Energy.pdf",
        time,
        p_energy,
        ".",
        r'$E_{potential}(\frac{kcal}{mol})$',
        "upper right",
        False,
        (),
        False,
        ()
    )
    mygraph.GraphXY(
        r"Energy Minimization",
        r"Time (fs)",
        r"Potential Energy ($\frac{kcal}{mol}$)",
        "Resources/EM/Nuc2NPsysEM_potential_Energy.png",
        time,
        p_energy,
        ".",
        r'$E_{potential}(\frac{kcal}{mol})$',
        "upper right",
        False,
        (),
        False,
        ()
    )


if __name__ == "__main__":
    Makegrap()
