# -*- coding: utf-8 -*-
"""
Written by Daniel M. Aukes and CONTRIBUTORS
Email: danaukes<at>asu.edu.
Please see LICENSE for full license.
"""
import sys

import qt.QtCore as qc
import qt.QtGui as qg
import popupcad
import logging
import traceback
import popupcad.guis.icons

class Program(object):

    def __init__(self, app,plugins, *args, **kwargs):

        args = list(args)

        self.app = app
        self.app.setWindowIcon(popupcad.guis.icons.get_icons()['printapede'])
        self.editor = popupcad.guis.editor.Editor()

        if len(args) > 1 and not '--' in args[-1]:
            self.editor.open_filename(filename=args[-1])
        self.editor.show()
        self.editor.move_center()

        self.logger = logging.Logger('popupCAD',level=logging.DEBUG)
        handler = logging.FileHandler(filename=popupcad.error_log_filename,mode='w')
        self.logger.addHandler(handler)  

        self.excepthook_internal = sys.excepthook
        sys.excepthook = self.excepthook          

        for plugin in plugins:
            plugin.initialize(self)

    def excepthook(self,exctype,value,tb):
        if exctype is not SystemExit:
            message = '''{}: {}'''.format(str(exctype),str(value))
            print(message)
    
            tbmessage = traceback.format_tb(tb)
            tbmessage = '  '.join(tbmessage)
    
#            logger = logging.getLogger('popupCAD')
            self.logger.error(message)
            self.logger.debug('\n'+tbmessage)
            
            self.editor.error_log.appendText(message+'\n'+tbmessage)
            self.excepthook_internal(exctype,value,tb)
            mb = qg.QMessageBox()
            mb.setText(message)
            mb.exec_()
        
        
