# -*- coding: utf-8 -*-

import contextlib
import os
import sys

import arcpy

class Toolbox(object):
    def __init__(self):
        self.label = u'species distribution model'
        self.alias = u'sdm'
        self.tools = [SDM]

class SDM(object):
    def __init__(self):
        self.label = u'Run Species Distribution Model'
        self.canRunInBackground = False

    def getParameterInfo(self):
        # Test_String
        file_param = arcpy.Parameter()
        file_param.name = u'Output Plot'
        file_param.displayName = u'Output Plot'
        file_param.parameterType = 'Required'
        file_param.direction = 'Output'
        file_param.datatype = u'File'

        return [file_param]

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        validator = getattr(self, 'ToolValidator', None)
        if validator:
            return validator(parameters).updateParameters()

    def updateMessages(self, parameters):
        validator = getattr(self, 'ToolValidator', None)
        if validator:
            return validator(parameters).updateMessages()

    def execute(self, parameters, messages):
        arcpy.AddMessage("executing species distribution model")
        out=parameters[0].valueAsText
        import classifier
        classifier.main(out_filename=out)
        os.startfile(out)
