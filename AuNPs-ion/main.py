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
# Molar fraction aqua and molar volume
x_h2o_data = [0.511, 0.6083, 0.6400, 0.6643, 0.6833, 0.7401, 0.7876]

x_acetone = [0.488, 0.3916, 0.3599, 0.3356, 0.3166, 0.2598, 0.2123]

molarv_data = [42.1113, 35.6641, 34.5910, 33.3499, 32.0369, 28.8607, 26.1838]

mygraph = Graphmaker()

# ==========================================================================

# Plot graph and linearRegression type Time vs Temperature


def Makegrap():

    # x_{H2O} vs Vm
    mygraph.GraphXY(
        r"Volumen molar en función de la fracción molar de $H_{2}O$",
        r"Fracción molar $X_{H_{2}O}$", r"Volumen molar ($\frac{mL}{mol}$)",
        "H2OvsFM.png",
        x_h2o_data,
        molarv_data,
        ".",
        r'$X_{H_{2}O}$' + ' vs ' + r'$\bar{V}_{m}$',
        "upper right",
        False,
        (),
        False,
        ()
    )

    """
    # Linealización
    LSOnlyGraph(
        x_h2o_data,
        molarv_data,
        r"$\bar{V}_{m}=f(H_{2}O)$",
        r"Fracción molar $X_{H_{2}O}$",
        r"Volumen molar ($\frac{mL}{mol}$)",
        "linealizacionOnly_H2OvsFM.png",
        6
    )
    # Linealización
    LinearSolveComp(
        x_h2o_data,
        molarv_data,
        r"$\bar{V}_{m}=f(H_{2}O)$",
        r"Fracción molar $X_{H_{2}O}$",
        r"Volumen molar ($\frac{mL}{mol}$)",
        "linealizacion_H2OvsFM.png",
        6
    )
    """


if __name__ == "__main__":
    Makegrap()
