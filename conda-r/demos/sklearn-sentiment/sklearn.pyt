# -*- coding: utf-8 -*-

import contextlib
import os
import sys

import arcpy

class Toolbox(object):
    def __init__(self):
        self.label = u'sklearn'
        self.alias = u'sklearn'
        self.tools = [ClassifyTweets]

class ClassifyTweets(object):
    def __init__(self):
        self.label = u'Classify Tweets'
        self.canRunInBackground = False

    def getParameterInfo(self):
        # Input_CSV
        param_1 = arcpy.Parameter()
        param_1.name = u'Input_CSV'
        param_1.displayName = u'Input CSV'
        param_1.parameterType = 'Required'
        param_1.direction = 'Input'
        param_1.datatype = u'File'

        # Test_String
        param_2 = arcpy.Parameter()
        param_2.name = u'Test_String'
        param_2.displayName = u'Test String'
        param_2.parameterType = 'Required'
        param_2.direction = 'Input'
        param_2.datatype = u'String'
        param_2.value = u'I love my iPhone!'

        return [param_1, param_2]

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
        # Scikit learn model based Lukas Biewald's Scikit Learn class
        # https://github.com/lukas/scikit-class
        
        import arcpy
        import pandas as pd
        from sklearn.feature_extraction.text import CountVectorizer
        from sklearn.naive_bayes import MultinomialNB
        
        input_csv = parameters[0].valueAsText
        test_string = parameters[1].valueAsText
        
        df = pd.read_csv(input_csv)
        target = df['is_there_an_emotion_directed_at_a_brand_or_product']
        text = df['tweet_text']
        
        fixed_text = text[pd.notnull(text)]
        fixed_target = target[pd.notnull(text)]
        
        count_vect = CountVectorizer()
        count_vect.fit(fixed_text)
        
        counts = count_vect.transform(fixed_text)
        
        # NB has a bunch of parameters -- somewhat scary for those who haven't
        # used it before. That said, Scikit-Learn mostly has sane defaults,
        # and usually it's not necessary to modify them. Can also try to
        # change a new algorithm, but usually it's not the best way to spend
        # your time.
        nb = MultinomialNB()
        nb.fit(counts, fixed_target)
        
        messages.AddMessage(nb.predict(count_vect.transform([test_string][0])))
