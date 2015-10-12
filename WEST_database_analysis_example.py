# -*- coding: utf-8 -*-
"""
This Python script is a typical example of a
what someone who want to analysis TS/WEST database
would do.

This is the basic example on which the internal 
IRFM Python crash course is based on.  

This example is supposed to be run within the pylab mode, 
with all the pywed lib imported.

@author: Julien Hillairet
"""
from pywed import *
from numpy import *
from matplotlib.pylab import *

#ip, t, infos = tsbase(47799, 'SIPMES')

ip = rand(1000)
t = arange(1000)

plot(t, ip)