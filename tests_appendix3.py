import numpy as np
import tm

# -----------------------------------------------------------------------------
# Point G4
# -----------------------------------------------------------------------------

lat = 60.3851068722
lon = 19.8481367944

print("TM35FIN coordinates of point G4")

E0 =   106_256.35961
N0 = 6_715_706.37708

E, N = tm.TM35_PROJECTION.project(lat, lon)

print(f"Result:     N = {N:13.5f} m, E = {E:12.5f} m")
print(f"Expected:   N = {N0:13.5f} m, E = {E0:12.5f} m")
print(f"Difference: N = {abs(N-N0):13.5f} m, E = {abs(E-E0):12.5f} m")

print("EUREF-FIN coordinates of point G4")

E =   106_256.35958
N = 6_715_706.37705

lat0 = np.degrees(1.053918934984532)
lon0 = np.degrees(0.346415337004409)

lat, lon = tm.TM35_PROJECTION.inverse_project(E, N)

print(f"Result:     lat = {lat:16.13f}\xb0, lon = {lon:16.13f}\xb0")
print(f"Expected:   lat = {lat0:16.13f}\xb0, lon = {lon0:16.13f}\xb0")
print(f"Difference: lat = {abs(lat-lat0):16.13f}\xb0, lon = {abs(lon-lon0):16.13f}\xb0")

# -----------------------------------------------------------------------------
# Point G42
# -----------------------------------------------------------------------------

lat = 60.5210735277
lon = 26.9071565278

# -----------------------------------------------------------------------------
# GK19FIN coordinates of point G42
# -----------------------------------------------------------------------------

print("GK19FIN coordinates of point G42")

E0 = 19_933_549.030
N0 =  6_738_233.823

E, N = tm.GK19_PROJECTION.project(lat, lon)

print(f"Result:     N = {N:13.5f} m, E = {E:14.5f} m")
print(f"Expected:   N = {N0:13.5f} m, E = {E0:14.5f} m")
print(f"Difference: N = {abs(N-N0):13.5f} m, E = {abs(E-E0):14.5f} m")

# -----------------------------------------------------------------------------
# GK20FIN coordinates of point G42
# -----------------------------------------------------------------------------

print("GK20FIN coordinates of point G42")

E0 = 20_878_867.261
N0 =  6_732_045.175

E, N = tm.GK20_PROJECTION.project(lat, lon)

print(f"Result:     N = {N:13.5f} m, E = {E:14.5f} m")
print(f"Expected:   N = {N0:13.5f} m, E = {E0:14.5f} m")
print(f"Difference: N = {abs(N-N0):13.5f} m, E = {abs(E-E0):14.5f} m")

# -----------------------------------------------------------------------------
# GK21FIN coordinates of point G42
# -----------------------------------------------------------------------------

print("GK21FIN coordinates of point G42")

E0 = 21_824_125.258
N0 =  6_726_693.699

E, N = tm.GK21_PROJECTION.project(lat, lon)

print(f"Result:     N = {N:13.5f} m, E = {E:14.5f} m")
print(f"Expected:   N = {N0:13.5f} m, E = {E0:14.5f} m")
print(f"Difference: N = {abs(N-N0):13.5f} m, E = {abs(E-E0):14.5f} m")

# -----------------------------------------------------------------------------
# GK22FIN coordinates of point G42
# -----------------------------------------------------------------------------

print("GK22FIN coordinates of point G42")

E0 = 22_769_331.899
N0 =  6_722_178.673

E, N = tm.GK22_PROJECTION.project(lat, lon)

print(f"Result:     N = {N:13.5f} m, E = {E:14.5f} m")
print(f"Expected:   N = {N0:13.5f} m, E = {E0:14.5f} m")
print(f"Difference: N = {abs(N-N0):13.5f} m, E = {abs(E-E0):14.5f} m")

# -----------------------------------------------------------------------------
# GK23FIN coordinates of point G42
# -----------------------------------------------------------------------------

print("GK23FIN coordinates of point G42")

E0 = 23_714_495.986
N0 =  6_718_499.484

E, N = tm.GK23_PROJECTION.project(lat, lon)

print(f"Result:     N = {N:13.5f} m, E = {E:14.5f} m")
print(f"Expected:   N = {N0:13.5f} m, E = {E0:14.5f} m")
print(f"Difference: N = {abs(N-N0):13.5f} m, E = {abs(E-E0):14.5f} m")

# -----------------------------------------------------------------------------
# GK24FIN coordinates of point G42
# -----------------------------------------------------------------------------

print("GK24FIN coordinates of point G42")

E0 = 24_659_626.265
N0 =  6_715_655.628

E, N = tm.GK24_PROJECTION.project(lat, lon)

print(f"Result:     N = {N:13.5f} m, E = {E:14.5f} m")
print(f"Expected:   N = {N0:13.5f} m, E = {E0:14.5f} m")
print(f"Difference: N = {abs(N-N0):13.5f} m, E = {abs(E-E0):14.5f} m")

# -----------------------------------------------------------------------------
# GK25FIN coordinates of point G42
# -----------------------------------------------------------------------------

print("GK25FIN coordinates of point G42")

E0 = 25_604_731.429
N0 =  6_713_646.713

E, N = tm.GK25_PROJECTION.project(lat, lon)

print(f"Result:     N = {N:13.5f} m, E = {E:14.5f} m")
print(f"Expected:   N = {N0:13.5f} m, E = {E0:14.5f} m")
print(f"Difference: N = {abs(N-N0):13.5f} m, E = {abs(E-E0):14.5f} m")

# -----------------------------------------------------------------------------
# GK26FIN coordinates of point G42
# -----------------------------------------------------------------------------

print("GK26FIN coordinates of point G42")

E0 = 26_549_820.136
N0 =  6_712_472.461

E, N = tm.GK26_PROJECTION.project(lat, lon)

print(f"Result:     N = {N:13.5f} m, E = {E:14.5f} m")
print(f"Expected:   N = {N0:13.5f} m, E = {E0:14.5f} m")
print(f"Difference: N = {abs(N-N0):13.5f} m, E = {abs(E-E0):14.5f} m")

# -----------------------------------------------------------------------------
# GK27FIN coordinates of point G42
# -----------------------------------------------------------------------------

print("GK27FIN coordinates of point G42")

E0 = 27_494_901.020
N0 =  6_712_132.709

E, N = tm.GK27_PROJECTION.project(lat, lon)

print(f"Result:     N = {N:13.5f} m, E = {E:14.5f} m")
print(f"Expected:   N = {N0:13.5f} m, E = {E0:14.5f} m")
print(f"Difference: N = {abs(N-N0):13.5f} m, E = {abs(E-E0):14.5f} m")

# -----------------------------------------------------------------------------
# GK28FIN coordinates of point G42
# -----------------------------------------------------------------------------

print("GK28FIN coordinates of point G42")

E0 = 28_439_982.705
N0 =  6_712_627.410

E, N = tm.GK28_PROJECTION.project(lat, lon)

print(f"Result:     N = {N:13.5f} m, E = {E:14.5f} m")
print(f"Expected:   N = {N0:13.5f} m, E = {E0:14.5f} m")
print(f"Difference: N = {abs(N-N0):13.5f} m, E = {abs(E-E0):14.5f} m")

# -----------------------------------------------------------------------------
# GK29FIN coordinates of point G42
# -----------------------------------------------------------------------------

print("GK29FIN coordinates of point G42")

E0 = 29_385_073.814
N0 =  6_713_956.632

E, N = tm.GK29_PROJECTION.project(lat, lon)

print(f"Result:     N = {N:13.5f} m, E = {E:14.5f} m")
print(f"Expected:   N = {N0:13.5f} m, E = {E0:14.5f} m")
print(f"Difference: N = {abs(N-N0):13.5f} m, E = {abs(E-E0):14.5f} m")

# -----------------------------------------------------------------------------
# GK30FIN coordinates of point G42
# -----------------------------------------------------------------------------

print("GK30FIN coordinates of point G42")

E0 = 30_330_182.986
N0 =  6_716_120.560

E, N = tm.GK30_PROJECTION.project(lat, lon)

print(f"Result:     N = {N:13.5f} m, E = {E:14.5f} m")
print(f"Expected:   N = {N0:13.5f} m, E = {E0:14.5f} m")
print(f"Difference: N = {abs(N-N0):13.5f} m, E = {abs(E-E0):14.5f} m")

# -----------------------------------------------------------------------------
# GK31FIN coordinates of point G42
# -----------------------------------------------------------------------------

print("GK31FIN coordinates of point G42")

E0 = 31_275_318.884
N0 =  6_719_119.494

E, N = tm.GK31_PROJECTION.project(lat, lon)

print(f"Result:     N = {N:13.5f} m, E = {E:14.5f} m")
print(f"Expected:   N = {N0:13.5f} m, E = {E0:14.5f} m")
print(f"Difference: N = {abs(N-N0):13.5f} m, E = {abs(E-E0):14.5f} m")
