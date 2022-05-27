import numpy
import math


class ReferenceEllipsoid:

    def __init__(self, semi_major_axis, inverse_flattening):
        self.semi_major_axis = semi_major_axis
        self.inverse_flattening = inverse_flattening


GRS80_ELLIPSOID = ReferenceEllipsoid(6378137.0, 298.257222101)
INT24_ELLIPSOID = ReferenceEllipsoid(6378388.0, 297.000000000)


class TransverseMercatorProjection:

    def __init__(self, reference_ellipsoid, central_meridian, false_easting, scaling_factor):
        self.reference_ellipsoid = reference_ellipsoid
        self.central_meridian = central_meridian
        self.false_easting = false_easting
        self.scaling_factor = scaling_factor

    def project(self, latitude, longitude):
        return _convert_geodetic_to_projected(latitude, longitude,
            self.reference_ellipsoid.semi_major_axis,
            1./self.reference_ellipsoid.inverse_flattening,
            self.central_meridian, self.false_easting, self.scaling_factor)

    def inverse_project(self, x, y):
        return _convert_projected_to_geodetic(x, y,
            self.reference_ellipsoid.semi_major_axis,
            1./self.reference_ellipsoid.inverse_flattening,
            self.central_meridian, self.false_easting, self.scaling_factor)


TM35_PROJECTION = TransverseMercatorProjection(GRS80_ELLIPSOID, 27.0, 0.500e6, 0.9996)
KKJ0_PROJECTION = TransverseMercatorProjection(INT24_ELLIPSOID, 18.0, 0.500e6, 1.0000)
KKJ1_PROJECTION = TransverseMercatorProjection(INT24_ELLIPSOID, 21.0, 1.500e6, 1.0000)
KKJ2_PROJECTION = TransverseMercatorProjection(INT24_ELLIPSOID, 24.0, 2.500e6, 1.0000)
KKJ3_PROJECTION = TransverseMercatorProjection(INT24_ELLIPSOID, 27.0, 3.500e6, 1.0000)
KKJ4_PROJECTION = TransverseMercatorProjection(INT24_ELLIPSOID, 30.0, 4.500e6, 1.0000)
KKJ5_PROJECTION = TransverseMercatorProjection(INT24_ELLIPSOID, 33.0, 5.500e6, 1.0000)
GK19_PROJECTION = TransverseMercatorProjection(GRS80_ELLIPSOID, 19.0, 19.50e6, 1.0000)
GK20_PROJECTION = TransverseMercatorProjection(GRS80_ELLIPSOID, 20.0, 20.50e6, 1.0000)
GK21_PROJECTION = TransverseMercatorProjection(GRS80_ELLIPSOID, 21.0, 21.50e6, 1.0000)
GK22_PROJECTION = TransverseMercatorProjection(GRS80_ELLIPSOID, 22.0, 22.50e6, 1.0000)
GK23_PROJECTION = TransverseMercatorProjection(GRS80_ELLIPSOID, 23.0, 23.50e6, 1.0000)
GK24_PROJECTION = TransverseMercatorProjection(GRS80_ELLIPSOID, 24.0, 24.50e6, 1.0000)
GK25_PROJECTION = TransverseMercatorProjection(GRS80_ELLIPSOID, 25.0, 25.50e6, 1.0000)
GK26_PROJECTION = TransverseMercatorProjection(GRS80_ELLIPSOID, 26.0, 26.50e6, 1.0000)
GK27_PROJECTION = TransverseMercatorProjection(GRS80_ELLIPSOID, 27.0, 27.50e6, 1.0000)
GK28_PROJECTION = TransverseMercatorProjection(GRS80_ELLIPSOID, 28.0, 28.50e6, 1.0000)
GK29_PROJECTION = TransverseMercatorProjection(GRS80_ELLIPSOID, 29.0, 29.50e6, 1.0000)
GK30_PROJECTION = TransverseMercatorProjection(GRS80_ELLIPSOID, 30.0, 30.50e6, 1.0000)
GK31_PROJECTION = TransverseMercatorProjection(GRS80_ELLIPSOID, 31.0, 31.50e6, 1.0000)


_NUMERICAL_TOLERANCE = 1.0e-9
_MAXIMUM_ITERATIONS = 100


def _convert_projected_to_geodetic(E, N, a, f, lam0, E0, k0):

    n = f / (2.0 - f);
    A1 = a / (1.0 + n) * (1.0 + n * n / 4.0 + n * n * n * n / 64.0)
    e = math.sqrt(2.0 * f - f**2)

    ksi = N / (A1 * k0)
    eta = (E - E0) / (A1 * k0)

    h1 = (n / 2.0) - (2.0 * n**2 / 3.0) + (37.0 * n**3 / 96.0) - (n**4 / 360.0)
    h2 = (n**2 / 48.0) + (n**3 / 15.0) - (437.0 * n**4 / 1440.0)
    h3 = (17.0 * n**3 / 480.0) - (37.0 * n**4 / 840.0)
    h4 = 4397.0 * n**4 / 161280.0

    ksi1p = h1 * math.sin(2.0 * ksi) * math.cosh(2.0 * eta)
    ksi2p = h2 * math.sin(4.0 * ksi) * math.cosh(4.0 * eta)
    ksi3p = h3 * math.sin(6.0 * ksi) * math.cosh(6.0 * eta)
    ksi4p = h4 * math.sin(8.0 * ksi) * math.cosh(8.0 * eta)

    eta1p = h1 * math.cos(2.0 * ksi) * math.sinh(2.0 * eta)
    eta2p = h2 * math.cos(4.0 * ksi) * math.sinh(4.0 * eta)
    eta3p = h3 * math.cos(6.0 * ksi) * math.sinh(6.0 * eta)
    eta4p = h4 * math.cos(8.0 * ksi) * math.sinh(8.0 * eta)

    ksip = ksi - (ksi1p + ksi2p + ksi3p + ksi4p)
    etap = eta - (eta1p + eta2p + eta3p + eta4p)

    beta = math.asin(_sech(etap) * math.sin(ksip))
    l = math.asin(math.tanh(etap) / math.cos(beta))

    Q = _asinh(math.tan(beta))
    Qp = Q + e * _atanh(e * math.tanh(Q))

    for i in range(_MAXIMUM_ITERATIONS):
        delta = Qp
        Qp = Q + e * _atanh(e * math.tanh(Qp))
        delta = abs(Qp - delta)
        if delta < _NUMERICAL_TOLERANCE:
            break

    if i == _MAXIMUM_ITERATIONS:
        raise RuntimeException(f"No convergence after {_MAXIMUM_ITERATIONS} iterations.")

    return (math.degrees(math.atan(math.sinh(Qp))), lam0 + math.degrees(l))


def _convert_geodetic_to_projected(latitude, longitude, a, f, lam0, E0, k0):

    phi, lam = math.radians(latitude), math.radians(longitude)

    n = f / (2.0 - f);
    A1 = a / (1.0 + n) * (1.0 + n * n / 4.0 + n * n * n * n / 64.0)
    e = math.sqrt(2.0 * f - f**2)

    h1p = (n / 2.0) - (2.0 * n**2 / 3.0) + (5.0 * n**3 / 16.0) + (41.0 * n**4 / 180.0)
    h2p = (13.0 * n**2 / 48.0) - (3.0 * n**3 / 5.0) + (557.0 * n**4 / 1440.0)
    h3p = (61.0 * n**3 / 240.0) - (103.0 * n**4 / 140.0)
    h4p = 49561.0 * n**4 / 161280.0

    Qp = _asinh(math.tan(phi))
    Qpp = _atanh(e * math.sin(phi))
    Q = Qp - e * Qpp

    l = lam - math.radians(lam0)
    beta = math.atan(math.sinh(Q))
    etap = _atanh(math.cos(beta) * math.sin(l))
    ksip = math.asin(math.sin(beta) / _sech(etap))

    ksi1 = h1p * math.sin(2.0 * ksip) * math.cosh(2.0 * etap)
    ksi2 = h2p * math.sin(4.0 * ksip) * math.cosh(4.0 * etap)
    ksi3 = h3p * math.sin(6.0 * ksip) * math.cosh(6.0 * etap)
    ksi4 = h4p * math.sin(8.0 * ksip) * math.cosh(8.0 * etap)

    eta1 = h1p * math.cos(2.0 * ksip) * math.sinh(2.0 * etap)
    eta2 = h2p * math.cos(4.0 * ksip) * math.sinh(4.0 * etap)
    eta3 = h3p * math.cos(6.0 * ksip) * math.sinh(6.0 * etap)
    eta4 = h4p * math.cos(8.0 * ksip) * math.sinh(8.0 * etap)

    ksi = ksip + ksi1 + ksi2 + ksi3 + ksi4
    eta = etap + eta1 + eta2 + eta3 + eta4

    return (A1 * eta * k0 + E0, A1 * ksi * k0)


_convert_geodetic_to_projected = numpy.vectorize(_convert_geodetic_to_projected)
_convert_projected_to_geodetic = numpy.vectorize(_convert_projected_to_geodetic)


def _sech(x):
    return 2.0 / (math.exp(x) + math.exp(-x))


def _asinh(x):
    return math.log(x + math.sqrt(x**2 + 1.0))


def _atanh(x):
    return math.log((1.0 + x) / (1.0 - x)) / 2.0
