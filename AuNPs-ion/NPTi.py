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
file = open("Resources/NPTi/Nucleus/1NPsys/WBNP_sys_NPTi_topol.csv", "r")
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

# ==========================================================================

# Plot graph and linearRegression type Time vs Temperature


def Makegrap():

    # t vs Total energy
    mygraph.GraphXY(
        r"NPTi Total Energy",
        r"Time (fs)",
        r"Total Energy ($\frac{kcal}{mol}$)",
        "Resources/NPTi/Nucleus/1NPsys/total_Energy.pdf",
        time,
        t_energy,
        ".",
        r'$E_{total}(\frac{kcal}{mol})$',
        "upper right",
        False,
        (),
        False,
        ()
    )
    mygraph.GraphXY(
        r"NPTi Total Energy",
        r"Time (fs)",
        r"Total Energy ($\frac{kcal}{mol}$)",
        "Resources/NPTi/Nucleus/1NPsys/total_Energy.png",
        time,
        t_energy,
        ".",
        r'$E_{total}(\frac{kcal}{mol})$',
        "upper right",
        False,
        (),
        False,
        ()
    )

    # t vs Potential energy
    mygraph.GraphXY(
        r"NPTi Potential Energy",
        r"Time (fs)",
        r"Potential Energy ($\frac{kcal}{mol}$)",
        "Resources/NPTi/Nucleus/1NPsys/potential_Energy.pdf",
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
        r"NPTi Potential Energy",
        r"Time (fs)",
        r"Potential Energy ($\frac{kcal}{mol}$)",
        "Resources/NPTi/Nucleus/1NPsys/potential_Energy.png",
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

    # t vs Kinietc energy
    mygraph.GraphXY(
        r"NPTi Kinetic Energy",
        r"Time (fs)",
        r"Kinetic Energy ($\frac{kcal}{mol}$)",
        "Resources/NPTi/Nucleus/1NPsys/kinetic_Energy.pdf",
        time,
        k_energy,
        ".",
        r'$E_{kinetic}(\frac{kcal}{mol})$',
        "upper right",
        False,
        (),
        False,
        ()
    )
    mygraph.GraphXY(
        r"NPTi Kinetic Energy",
        r"Time (fs)",
        r"Kinetic Energy ($\frac{kcal}{mol}$)",
        "Resources/NPTi/Nucleus/1NPsys/kinetic_Energy.png",
        time,
        k_energy,
        ".",
        r'$E_{kinetic}(\frac{kcal}{mol})$',
        "upper right",
        False,
        (),
        False,
        ()
    )

    # t vs Temperature
    mygraph.GraphXY(
        r"NPTi Temperature",
        r"Time (fs)",
        r"Temperature ($K$)",
        "Resources/NPTi/Nucleus/1NPsys/temperature.pdf",
        time,
        temperature,
        ".",
        r'Temperature $(K)$',
        "upper right",
        False,
        (),
        False,
        ()
    )
    mygraph.GraphXY(
        r"NPTi Temperature",
        r"Time (fs)",
        r"Temperature ($K$)",
        "Resources/NPTi/Nucleus/1NPsys/temperature.png",
        time,
        temperature,
        ".",
        r'Temperature $(K)$',
        "upper right",
        False,
        (),
        False,
        ()
    )

    # t vs Pressure
    mygraph.GraphXY(
        r"NPTi Pressure",
        r"Time (fs)",
        r"Pressure ($atm$)",
        "Resources/NPTi/Nucleus/1NPsys/pressure.pdf",
        time,
        pressure,
        ".",
        r'Pressure $(atm)$',
        "upper right",
        False,
        (),
        False,
        ()
    )
    mygraph.GraphXY(
        r"NPTi Pressure",
        r"Time (fs)",
        r"Pressure ($atm$)",
        "Resources/NPTi/Nucleus/1NPsys/pressure.png",
        time,
        pressure,
        ".",
        r'Pressure $(atm)$',
        "upper right",
        False,
        (),
        False,
        ()
    )

    # t vs Volume
    mygraph.GraphXY(
        r"NPTi Volume",
        r"Time (fs)",
        r"Volume $(A^3)$",
        "Resources/NPTi/Nucleus/1NPsys/volume.pdf",
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
        r"NPTi Volume",
        r"Time (fs)",
        r"Volume ($atm$)",
        "Resources/NPTi/Nucleus/1NPsys/volume.png",
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

    # t vs Conserved Quantity
    mygraph.GraphXY(
        r"NPTi Conserved Quantity",
        r"Time (fs)",
        r"Conserved Quantity ($\frac{kcal}{mol}$)",
        "Resources/NPTi/Nucleus/1NPsys/CQuantity.pdf",
        time,
        conserved_quant,
        ".",
        r'Conserved Quantity $(\frac{kcal}{mol})$',
        "upper right",
        False,
        (),
        False,
        ()
    )
    mygraph.GraphXY(
        r"NPTi Conserved Quantity",
        r"Time (fs)",
        r"Conserved Quantity ($\frac{kcal}{mol}$)",
        "Resources/NPTi/Nucleus/1NPsys/CQuantity.png",
        time,
        conserved_quant,
        ".",
        r'Conserved Quantity $(\frac{kcal}{mol})$',
        "upper right",
        False,
        (),
        False,
        ()
    )


if __name__ == "__main__":
    Makegrap()
