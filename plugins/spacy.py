#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Ivan Vladimir Meza Ruiz 2018
# GPL 3.0

import random

def execute(*args):
    nombre=args[0]
    msg=args[1]
    #### Código de spacy
    return 'say "{0} {1}"'.format(msg,nombre)

