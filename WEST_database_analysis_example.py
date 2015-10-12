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

# Within the IPython interpreter, '%reset' 
# is the Matlab equivalent of 'clear all'
# but beware : it also clear all the imported packages!

# Within the IPython interpreter, '%pylab'
# will import all the content of the NumPy and Matplotlib packages

# Within the IPython interpreter, '%matplotlib inline'
# will indicates to matplotlib to plot the figure
# directly inside the interpreter


shot = 47979
ip_signame = 'SIPMES' 


ip, ip_t, ip_infos = tsbase(shot, ip_signame)
Plh, Plh_t, je_sais_pas, lh_infos = tsbase(shot, 'GPHYB')
# ip_infos is a list of strings which contains:
# [[], 40, '30/06/2011', '12:32:13', 'mcs', 'MA', '', 'SIPMES', 'B']

figure(1)
ax=subplot(211)
plot(ip_t, ip, lw=2)
grid()
ylabel('Ip [MA]')
title('A nice figure')
# the second subplot shares first subplot x-axis
subplot(212, sharex=ax) 
plot(Plh_t, Plh[:,0], lw=2, color='k')
ylabel('$P_{LH}$ [MW]', fontsize=12)
grid()
xlim(-5, 160)
xlabel('t [s]', fontsize=14)
