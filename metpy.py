# library for metpy
from datetime import datetime
from siphon.simplewebservice.wyoming import WyomingUpperAir
from metpy.units import units
import metpy.calc as mpcalc

# library for sharppy
# import qtpy
# import numpy
# import PySide2
# import requests
# import dateutil
# import sharppy
# from sharppy.sharptab import sharptab
# from sharppy.sharptab import params

df = WyomingUpperAir.request_data(datetime(2012, 4, 14, 12), 'OUN')

p = df['pressure'].values * units(df.units['pressure'])
t = df['temperature'].values * units(df.units['temperature'])
dt = df['dewpoint'].values * units(df.units['dewpoint'])

# Calculate full parcel profile
# https://unidata.github.io/MetPy/latest/examples/Advanced_Sounding.html?highlight=cape
prof = mpcalc.parcel_profile(p, t[0], dt[0]).to('degC')
mpcalc.cape_cin(p, t, dt, prof)
