# -*- coding: utf-8 -*-
"""
Written by Daniel M. Aukes and CONTRIBUTORS
Email: danaukes<at>asu.edu.
Please see LICENSE for full license.
"""

import sys

import qt.QtCore as qc
import qt.QtGui as qg

#must import sympy before pyqtgraph
import sympy
#must import pyqtgraph before creating app
import pyqtgraph

app = qg.QApplication([sys.argv[0]])
import popupcad
plugins = []

#try:
import popupcad_manufacturing_plugins
plugins.append(popupcad_manufacturing_plugins)
#except ImportError:
#    print('Manufacturing Plugin Not Found')

try:
    import popupcad_microrobotics
    plugins.append(popupcad_microrobotics)
except ImportError:
    print('Microrobotics Plugin Not Found')

try:
    import popupcad_gazebo
    plugins.append(popupcad_gazebo)
except ImportError:
    print('Gazebo Plugin Not Found')

program = popupcad.filetypes.program.Program(app, plugins, *sys.argv)
sys.exit(app.exec_())