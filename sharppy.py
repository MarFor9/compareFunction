import qtpy
import numpy
import PySide2
import requests
import dateutil
import sharppy

from datetime import datetime
from siphon.simplewebservice.wyoming import WyomingUpperAir
from metpy.units import units
import metpy.calc as mpcalc

df = WyomingUpperAir.request_data(datetime(2012, 4, 14, 12), 'OUN')

p = df['pressure'].values * units(df.units['pressure'])
t = df['temperature'].values * units(df.units['temperature'])
dt = df['dewpoint'].values * units(df.units['dewpoint'])
h = df['height'].values * units.meters
wd = df['direction'].values * units.degrees
sp = df['speed'].values * units.kts
u, v = mpcalc.wind_components(sp, wd)
print(u,v)

# params - computation of different parameters, indices, etc. from the Profile object
# https://sharppy.github.io/SHARPpy/scripting.html
import sharppy
import sharppy.sharptab.profile as profile
import sharppy.sharptab.params as params

h.sort()
prof = profile.create_profile(pres = p, hght = h, tmpc = t, dwpc = dt, wdir = wd, wspd = sp)
parcel = params.Parcel(pres = p, tmpc = t, dwpc = dt)
cape = params.cape(prof)