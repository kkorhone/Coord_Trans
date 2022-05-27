import eureffin
import tm

# Transforms the location of the Havis Amanda statue given in GK25FIN coordinates to KKJ2 coordinates.

# Path: GK25FIN (E, N) => EUREF-FIN (lat, lon) => TM35FIN (E, N) => KKJ3 (x, y) => KKJ (lat, lon) => KKJ2 (x, y)

E = 25_497_301.91 # GK25FIN easting
N =  6_672_745.28 # GK25FIN northing

lat, lon = tm.GK25_PROJECTION.inverse_project(E, N) # EUREF-FIN lat and lon

E, N = tm.TM35_PROJECTION.project(lat, lon) # TM35FIN easting and northing

x, y = eureffin.transform_TM35_to_KKJ3(E, N) # KKJ3 easting and northing

lat, lon = tm.KKJ3_PROJECTION.inverse_project(x, y) # KKJ lat and lon

x0, y0 = 2_552_996.1783, 6_673_264.6043 # KKJ2 easting and norting from https://kartta.paikkatietoikkuna.fi/

x, y = tm.KKJ2_PROJECTION.project(lat, lon) # KKJ2 easting and northing using the Python code

print("Havis Amanda")
print(f"Source GK25FIN:   E = {E:14.6f} m, N = {N:14.6f} m")
print(f"Source EUREF-FIN: \u03d5 = {lat:15.7f}\xb0, \u03bb = {lon:15.7f}\xb0")
print(f"Expected KKJ2:    x = {x0:14.6f} m, y = {y0:14.6f} m")
print(f"Resulting KKJ2:   x = {x:14.6f} m, y = {y:14.6f} m")
print(f"Difference:       x = {x-x0:14.6f} m, y = {y-y0:14.6f} m")
