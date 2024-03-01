## ICARUS Plot Style Definitions
## 2024 - version 1.0, work in progress led by Bruce Howard, Jaesung Kim, Justin Mueller
##
## Thanks to the DUNE MPLSTYLE FILE for guidance in our mplstyle file
## Thanks to various other sources and documentation for help in using some of the functions

import matplotlib.pyplot as plt
import numpy as np
import os

envvar=str(os.getenv('PYTHONPATH'))
part=envvar.partition(':')
for i in part:
    if i.find('icarusplot')>=0:
        plt.style.use(i+'/icarus_style.mplstyle')

def ICARUSMCPreliminary(_axis):
    _yrange = _axis.get_ylim()
    _use_y = _yrange[1] + 0.025*(_yrange[1] - _yrange[0])
    _xrange = _axis.get_xlim()
    _use_x = _xrange[0] + 0.025*(_xrange[1] - _xrange[0])    
    _axis.text( x=_use_x, y=_use_y, s=r'$\bf{ICARUS}$ Simulation Preliminary', fontsize=14, color='blue' )

def ICARUSDataPreliminary(_axis):
    _yrange = _axis.get_ylim()
    _use_y = _yrange[1] + 0.025*(_yrange[1] - _yrange[0])
    _xrange = _axis.get_xlim()
    _use_x = _xrange[0] + 0.025*(_xrange[1] - _xrange[0])    
    _axis.text( x=_use_x, y=_use_y, s=r'$\bf{ICARUS}$ Data Preliminary', fontsize=14, color='#d67a11' )

def ICARUSMC(_axis):
    _yrange = _axis.get_ylim()
    _use_y = _yrange[1] + 0.025*(_yrange[1] - _yrange[0])
    _xrange = _axis.get_xlim()
    _use_x = _xrange[0] + 0.025*(_xrange[1] - _xrange[0])    
    _axis.text( x=_use_x, y=_use_y, s=r'$\bf{ICARUS}$ Simulation', fontsize=14, color='blue' )

def ICARUSData(_axis):
    _yrange = _axis.get_ylim()
    _use_y = _yrange[1] + 0.025*(_yrange[1] - _yrange[0])
    _xrange = _axis.get_xlim()
    _use_x = _xrange[0] + 0.025*(_xrange[1] - _xrange[0])
    _axis.text( x=_use_x, y=_use_y, s=r'$\bf{ICARUS}$ Data', fontsize=14, color='#d67a11' )

def POT(_axis,_pot):
    _yrange = _axis.get_ylim()
    _use_y = _yrange[1] + 0.02*(_yrange[1] - _yrange[0])
    _xrange = _axis.get_xlim()
    _use_x = _xrange[1] - 0.02*(_xrange[1] - _xrange[0])
    _use_pot = _pot/1.0e20
    _axis.text( x=_use_x, y=_use_y, s='{:0.2}'.format(_use_pot)+r'$\times 10^{20}$'+' POT',\
                fontsize=13, color='black', horizontalalignment='right' )

def RatioCanvas(_title='null'):
    fig, axs = plt.subplots(2, sharex=True, height_ratios=[0.7,0.3])
    fig.subplots_adjust(hspace=0)
    if _title!='null':
        axs[0].set_title(_title)
    axs[1].set_ylim(0.65,1.35)
    return fig, axs

def UnityLine(_axis):
    _xrange = _axis.get_xlim()
    _axis.plot(np.linspace(_xrange[0],_xrange[1],1001),np.ones(1001),'--',color='gray')
