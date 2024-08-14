# _*_ coding: utf-8 _*_
"""
@author: Acxel David Orozco Baldomero (ADOB)
@date: 12/11/2022
@description: Adaptation for multiple X-data
@version: 12.11
@require: matplotlib, numpy
@execute: 'pip install matplotlib numpy'

"""

import matplotlib.pyplot as plt
# import numpy as np


class Graphmaker:

    # Initial function
    def __init__(self):
        print("Calling constructor")
        class_name = self.__class__.__name__
        print(class_name, "Ready")

        '''set params characteristics at
        all plots and subplots for
        implements latext'''
        params = {
            'text.latex.preamble': [
                r'\usepackage{siunitx}',
                r'\usepackage{amsmath}'
            ]
        }
        plt.rcParams.update(params)

    # Destroyer function
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")

    # Graph 3 plots, same X-data
    def GraphX1Y3(
        self,
        curve_name: str,
        _xlabel: str,
        _ylabel: str,
        graph_name: str,
        _Xdata: list,
        _Y1data: list,
        _Y2data: list,
        _Y3data: list,
        _marker1: str,
        _marker2: str,
        _marker3: str,
        _latex1: str,
        _latex2: str,
        _latex3: str,
        _itLoc: int,
        _set_figlims: bool,
        _lims: tuple,
        _set_scale: bool,
        _scale: tuple
    ):
        # Inner vars
        _loc = ""

        # Create figure and axes
        fig = plt.figure()
        fig.clf()
        ax = fig.add_subplot(1, 1, 1)

        # _lims = ([x_left, x_right], [y_left, y_right])
        if (_set_figlims):
            ax.set_xlim(_lims[0])
            ax.set_ylim(_lims[1])

        if(_set_scale):
            ax.set_xscale(_scale[0])
            ax.set_yscale(_scale[1])
        else:
            ax.set_xscale("linear")
            ax.set_yscale("linear")
        '''
        _______________________________________________________
        |  'linear'  |   'log'     |  'symlog'   |   'logit'  |
        |------------|-------------|-------------|------------|
        '''

        # Set title
        ax.set_title(curve_name)
        '''
        Define marker plot
        ______________________________________________________________________
        |  'point'   |   'pixel'   |  'hline'   |   'circle'  |'triangle_down'|
        |    "."     |     ","     |    "_"     |     "o"     |      "v"      |
        |------------|-------------|------------------------------------------|
        |'triangleUP'|'3angle_left'|'3angleRIGT'|  'tri_down' |    'tri_up'   |
        |    "^"     |     "<"     |     ">"    |     '1'     |      '2'      |
        |------------|-------------|------------------------------------------|
        | 'tri_left' | 'tri_right' |  'octagon' |   'square'  |   'pentagon'  |
        |    "3"     |     "4"     |    "8"     |     "s"     |      "p"      |
        |------------|-------------|------------------------------------------|
        |'plus(flld)'|    'star'   | 'hexagon1' |  'hexagon2' |    'plus'     |
        |    "P"     |     "*"     |    "h"     |     "H"     |      "+"      |
        |------------|-------------|------------------------------------------|
        |    'x'     |  'x (flld)' |  'diamond' |'thinDiamond'|    'vline'    |
        |    "x"     |     "X"     |    "D"     |    "d"      |      "|"      |
        |------------|-------------|------------------------------------------|
        '''

        # Create the plot
        ax.set_xlabel(_xlabel)
        ax.set_ylabel(_ylabel)
        ax.plot(_Xdata, _Y1data, marker=_marker1, linestyle='-', label=_latex1)
        ax.plot(_Xdata, _Y2data, marker=_marker2, linestyle='-', label=_latex2)
        ax.plot(_Xdata, _Y3data, marker=_marker3, linestyle='-', label=_latex3)

        # Show the major and minor grid lines
        ax.grid(visible=True, which='major', color='#666666', linestyle='-')
        ax.minorticks_on()
        ax.grid(
            visible=True,
            which='minor',
            color='#999999',
            linestyle='-',
            alpha=0.2
        )
        '''
        Define legend location
        ____________________________
        |     1      |     2       |
        |'upper left'|'upper right'|
        -------------|--------------
        |      3     |     4       |
        |'lower left'|'lower right'|
        ----------------------------
        '''
        if(_itLoc == 1):
            _loc = 'upper left'
        elif(_itLoc == 2):
            _loc = 'upper right'
        elif(_itLoc == 3):
            _loc = 'lower left'
        elif(_itLoc == 4):
            _loc = 'lower right'
        else:
            _loc = "lower right"
        # Legend
        ax.legend(prop={'size': 10}, loc=_loc)

        # Save figure
        fig.savefig(graph_name)

        # Show plot
        plt.show()

    # Graph 3 plots, same X-data
    def GraphX1Y2(
        self,
        curve_name: str,
        _xlabel: str,
        _ylabel: str,
        graph_name: str,
        _Xdata: list,
        _Y1data: list,
        _Y2data: list,
        _marker1: str,
        _marker2: str,
        _latex1: str,
        _latex2: str,
        _itLoc: int,
        _set_figlims: bool,
        _lims: tuple,
        _set_scale: bool,
        _scale: tuple
    ):
        # Inner vars
        _loc = ""

        # Create figure and axes
        fig = plt.figure()
        fig.clf()
        ax = fig.add_subplot(1, 1, 1)

        # _lims = ([x_left, x_right], [y_left, y_right])
        if (_set_figlims):
            ax.set_xlim(_lims[0])
            ax.set_ylim(_lims[1])

        if(_set_scale):
            ax.set_xscale(_scale[0])
            ax.set_yscale(_scale[1])
        else:
            ax.set_xscale("linear")
            ax.set_yscale("linear")
        '''
        _______________________________________________________
        |  'linear'  |   'log'     |  'symlog'   |   'logit'  |
        |------------|-------------|-------------|------------|
        '''

        # Set title
        ax.set_title(curve_name)
        '''
        Define marker plot
        ______________________________________________________________________
        |  'point'   |   'pixel'   |  'hline'   |   'circle'  |'triangle_down'|
        |    "."     |     ","     |    "_"     |     "o"     |      "v"      |
        |------------|-------------|------------------------------------------|
        |'triangleUP'|'3angle_left'|'3angleRIGT'|  'tri_down' |    'tri_up'   |
        |    "^"     |     "<"     |     ">"    |     '1'     |      '2'      |
        |------------|-------------|------------------------------------------|
        | 'tri_left' | 'tri_right' |  'octagon' |   'square'  |   'pentagon'  |
        |    "3"     |     "4"     |    "8"     |     "s"     |      "p"      |
        |------------|-------------|------------------------------------------|
        |'plus(flld)'|    'star'   | 'hexagon1' |  'hexagon2' |    'plus'     |
        |    "P"     |     "*"     |    "h"     |     "H"     |      "+"      |
        |------------|-------------|------------------------------------------|
        |    'x'     |  'x (flld)' |  'diamond' |'thinDiamond'|    'vline'    |
        |    "x"     |     "X"     |    "D"     |    "d"      |      "|"      |
        |------------|-------------|------------------------------------------|
        '''

        # Create the plot
        ax.set_xlabel(_xlabel)
        ax.set_ylabel(_ylabel)
        ax.plot(_Xdata, _Y1data, marker=_marker1, linestyle='-', label=_latex1)
        ax.plot(_Xdata, _Y2data, marker=_marker2, linestyle='-', label=_latex2)

        # Show the major and minor grid lines
        ax.grid(visible=True, which='major', color='#666666', linestyle='-')
        ax.minorticks_on()
        ax.grid(
            visible=True,
            which='minor',
            color='#999999',
            linestyle='-',
            alpha=0.2
        )
        '''
        Define legend location
        ____________________________
        |     1      |     2       |
        |'upper left'|'upper right'|
        -------------|--------------
        |      3     |     4       |
        |'lower left'|'lower right'|
        ----------------------------
        '''
        if(_itLoc == 1):
            _loc = 'upper left'
        elif(_itLoc == 2):
            _loc = 'upper right'
        elif(_itLoc == 3):
            _loc = 'lower left'
        elif(_itLoc == 4):
            _loc = 'lower right'
        else:
            _loc = "lower right"
        # Legend
        ax.legend(prop={'size': 10}, loc=_loc)

        # Save figure
        fig.savefig(graph_name)

        # Show plot
        plt.show()

    # Graph one plot

    def GraphXY(
        self,
        curve_name: str,
        _xlabel: str,
        _ylabel: str,
        graph_name: str,
        _Xdata: list,
        _Y1data: list,
        _marker1: str,
        _latex1: str,
        _itLoc: int,
        _set_figlims: bool,
        _lims: tuple,
        _set_scale: bool,
        _scale: tuple
    ):

        # Inner vars
        _loc = ""

        # marker1 = 4

        # Create figure and axes
        fig = plt.figure()
        fig.clf()
        ax = fig.add_subplot(1, 1, 1)
        # _lims = ([x_left, x_right], [y_left, y_right])
        if (_set_figlims):
            ax.set_xlim(_lims[0])
            ax.set_ylim(_lims[1])

        if(_set_scale):
            ax.set_xscale(_scale[0])
            ax.set_yscale(_scale[1])
        else:
            ax.set_xscale("linear")
            ax.set_yscale("linear")

        '''
        _______________________________________________________
        |  'linear'  |   'log'     |  'symlog'   |   'logit'  |
        |------------|-------------|-------------|------------|
        '''

        # Set title
        ax.set_title(curve_name)

        # Create the plot
        ax.set_xlabel(_xlabel)
        ax.set_ylabel(_ylabel)
        '''
        Define marker plot
        ______________________________________________________________________
        |  'point'   |   'pixel'   |  'hline'   |   'circle'  |'triangle_down'|
        |    "."     |     ","     |    "_"     |     "o"     |      "v"      |
        |------------|-------------|------------------------------------------|
        |'triangleUP'|'3angle_left'|'3angleRIGT'|  'tri_down' |    'tri_up'   |
        |    "^"     |     "<"     |     ">"    |     '1'     |      '2'      |
        |------------|-------------|------------------------------------------|
        | 'tri_left' | 'tri_right' |  'octagon' |   'square'  |   'pentagon'  |
        |    "3"     |     "4"     |    "8"     |     "s"     |      "p"      |
        |------------|-------------|------------------------------------------|
        |'plus(flld)'|    'star'   | 'hexagon1' |  'hexagon2' |    'plus'     |
        |    "P"     |     "*"     |    "h"     |     "H"     |      "+"      |
        |------------|-------------|------------------------------------------|
        |    'x'     |  'x (flld)' |  'diamond' |'thinDiamond'|    'vline'    |
        |    "x"     |     "X"     |    "D"     |    "d"      |      "|"      |
        |------------|-------------|------------------------------------------|
        '''
        ax.plot(_Xdata, _Y1data, marker=_marker1, linestyle='-', label=_latex1)

        # Show the major and minor grid lines
        ax.grid(visible=True, which='major', color='#666666', linestyle='-')
        ax.minorticks_on()
        ax.grid(
            visible=True,
            which='minor',
            color='#999999',
            linestyle='-',
            alpha=0.2
        )
        '''
        Define legend location
        ____________________________
        |     1      |     2       |
        |'upper left'|'upper right'|
        -------------|--------------
        |      3     |     4       |
        |'lower left'|'lower right'|
        ----------------------------
        '''
        if(_itLoc == 1):
            _loc = 'upper left'
        elif(_itLoc == 2):
            _loc = 'upper right'
        elif(_itLoc == 3):
            _loc = 'lower left'
        elif(_itLoc == 4):
            _loc = 'lower right'
        else:
            _loc = "lower right"
        # Legend
        ax.legend(prop={'size': 10}, loc=_loc)

        # Save figure
        fig.savefig(graph_name)

        # Show plot
        plt.show()

    # Graph 3 plots whit diferente X-data
    def GraphX3Y3(
        self,
        curve_name: str,
        _xlabel: str,
        _ylabel: str,
        graph_name: str,
        _X1data: list,
        _X2data: list,
        _X3data: list,
        _Y1data: list,
        _Y2data: list,
        _Y3data: list,
        _marker1: str,
        _marker2: str,
        _marker3: str,
        _latex1: str,
        _latex2: str,
        _latex3: str,
        _itLoc: int,
        _set_figlims: bool,
        _lims: tuple,
        _set_scale: bool,
        _scale: tuple
    ):
        # Inner vars
        _loc = ""

        # Create figure and axes
        fig = plt.figure()
        fig.clf()
        ax = fig.add_subplot(1, 1, 1)

        # _lims = ([x_left, x_right], [y_left, y_right])
        if (_set_figlims):
            ax.set_xlim(_lims[0])
            ax.set_ylim(_lims[1])

        if(_set_scale):
            ax.set_xscale(_scale[0])
            ax.set_yscale(_scale[1])
        else:
            ax.set_xscale("linear")
            ax.set_yscale("linear")
        '''
        _______________________________________________________
        |  'linear'  |   'log'     |  'symlog'   |   'logit'  |
        |------------|-------------|-------------|------------|
        '''

        # Set title
        ax.set_title(curve_name)

        '''
        Define marker plot
        ______________________________________________________________________
        |  'point'   |   'pixel'   |  'hline'   |   'circle'  |'triangle_down'|
        |    "."     |     ","     |    "_"     |     "o"     |      "v"      |
        |------------|-------------|------------------------------------------|
        |'triangleUP'|'3angle_left'|'3angleRIGT'|  'tri_down' |    'tri_up'   |
        |    "^"     |     "<"     |     ">"    |     '1'     |      '2'      |
        |------------|-------------|------------------------------------------|
        | 'tri_left' | 'tri_right' |  'octagon' |   'square'  |   'pentagon'  |
        |    "3"     |     "4"     |    "8"     |     "s"     |      "p"      |
        |------------|-------------|------------------------------------------|
        |'plus(flld)'|    'star'   | 'hexagon1' |  'hexagon2' |    'plus'     |
        |    "P"     |     "*"     |    "h"     |     "H"     |      "+"      |
        |------------|-------------|------------------------------------------|
        |    'x'     |  'x (flld)' |  'diamond' |'thinDiamond'|    'vline'    |
        |    "x"     |     "X"     |    "D"     |    "d"      |      "|"      |
        |------------|-------------|------------------------------------------|
        '''

        # Create the plot
        ax.set_xlabel(_xlabel)
        ax.set_ylabel(_ylabel)
        ax.plot(
            _X1data,
            _Y1data,
            marker=_marker1,
            linestyle='-',
            label=_latex1
        )
        ax.plot(
            _X2data,
            _Y2data,
            marker=_marker2,
            linestyle='-',
            label=_latex2
        )
        ax.plot(
            _X3data,
            _Y3data,
            marker=_marker3,
            linestyle='-',
            label=_latex3
        )

        # Show the major and minor grid lines
        ax.grid(visible=True, which='major', color='#666666', linestyle='-')
        ax.minorticks_on()
        ax.grid(
            visible=True,
            which='minor',
            color='#999999',
            linestyle='-',
            alpha=0.2
        )
        '''
        Define legend location
        ____________________________
        |     1      |     2       |
        |'upper left'|'upper right'|
        -------------|--------------
        |      3     |     4       |
        |'lower left'|'lower right'|
        ----------------------------
        '''
        if(_itLoc == 1):
            _loc = 'upper left'
        elif(_itLoc == 2):
            _loc = 'upper right'
        elif(_itLoc == 3):
            _loc = 'lower left'
        elif(_itLoc == 4):
            _loc = 'lower right'
        else:
            _loc = "lower right"
        # Legend
        ax.legend(prop={'size': 10}, loc=_loc)

        # Save figure
        fig.savefig(graph_name)

        # Show plot
        plt.show()
