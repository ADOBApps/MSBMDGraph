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
file = open("Resources/NVT/Full/Ion/1NPsys/WBFDL_sys_NVT_topol.csv", "r")
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
        r"NVT Total Energy",
        r"Time (fs)",
        r"Total Energy ($\frac{kcal}{mol}$)",
        "Resources/NVT/NVT_total_Energy.pdf",
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
        r"NVT Total Energy",
        r"Time (fs)",
        r"Total Energy ($\frac{kcal}{mol}$)",
        "Resources/NVT/NVT_total_Energy.png",
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
        r"NVT Potential Energy",
        r"Time (fs)",
        r"Potential Energy ($\frac{kcal}{mol}$)",
        "Resources/NVT/NVT_potential_Energy.pdf",
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
        r"NVT Potential Energy",
        r"Time (fs)",
        r"Potential Energy ($\frac{kcal}{mol}$)",
        "Resources/NVT/NVT_potential_Energy.png",
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
        r"NVT Kinetic Energy",
        r"Time (fs)",
        r"Kinetic Energy ($\frac{kcal}{mol}$)",
        "Resources/NVT/NVT_kinetic_Energy.pdf",
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
        r"NVT Kinetic Energy",
        r"Time (fs)",
        r"Kinetic Energy ($\frac{kcal}{mol}$)",
        "Resources/NVT/NVT_kinetic_Energy.png",
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
        r"NVT Temperature",
        r"Time (fs)",
        r"Temperature ($K$)",
        "Resources/NVT/NVT_temperature.pdf",
        time,
        temperature,
        ".",
        r'$Temperature(K)$',
        "upper right",
        False,
        (),
        False,
        ()
    )
    mygraph.GraphXY(
        r"NVT Temperature",
        r"Time (fs)",
        r"Temperature ($K$)",
        "Resources/NVT/NVT_temperature.png",
        time,
        temperature,
        ".",
        r'$Temperature(K)$',
        "upper right",
        False,
        (),
        False,
        ()
    )

    # t vs Pressure
    mygraph.GraphXY(
        r"NVT Pressure",
        r"Time (fs)",
        r"Pressure ($atm$)",
        "Resources/NVT/NVT_pressure.pdf",
        time,
        pressure,
        ".",
        r'$Pressure(atm)$',
        "upper right",
        False,
        (),
        False,
        ()
    )
    mygraph.GraphXY(
        r"NVT Pressure",
        r"Time (fs)",
        r"Pressure ($atm$)",
        "Resources/NVT/NVT_pressure.png",
        time,
        pressure,
        ".",
        r'$Pressure(atm)$',
        "upper right",
        False,
        (),
        False,
        ()
    )

    # t vs Volume
    mygraph.GraphXY(
        r"NVT Volume",
        r"Time (fs)",
        r"Volume ($atm$)",
        "Resources/NVT/NVT_volume.pdf",
        time,
        volume,
        ".",
        r'$Volume(A^3)$',
        "upper right",
        False,
        (),
        False,
        ()
    )
    mygraph.GraphXY(
        r"NVT Volume",
        r"Time (fs)",
        r"Volume ($atm$)",
        "Resources/NVT/NVT_volume.png",
        time,
        volume,
        ".",
        r'$Volume(A^3)$',
        "upper right",
        False,
        (),
        False,
        ()
    )

    # t vs Conserved Quantity
    mygraph.GraphXY(
        r"NVT Conserved Quantity",
        r"Time (fs)",
        r"Conserved Quantity ($\frac{kcal}{mol}$)",
        "Resources/NVT/NVT_CQuantity.pdf",
        time,
        conserved_quant,
        ".",
        r'$Conserved Quantity(\frac{kcal}{mol})$',
        "upper right",
        False,
        (),
        False,
        ()
    )
    mygraph.GraphXY(
        r"NVT Conserved Quantity",
        r"Time (fs)",
        r"Conserved Quantity ($\frac{kcal}{mol}$)",
        "Resources/NVT/NVT_CQuantity.png",
        time,
        conserved_quant,
        ".",
        r'$Conserved Quantity(\frac{kcal}{mol})$',
        "upper right",
        False,
        (),
        False,
        ()
    )


if __name__ == "__main__":
    Makegrap()
