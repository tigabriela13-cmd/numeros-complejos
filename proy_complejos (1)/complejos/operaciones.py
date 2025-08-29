import math

def suma(z1, z2):
    return (z1[0] + z2[0], z1[1] + z2[1])

def resta(z1, z2):
    return (z1[0] - z2[0], z1[1] - z2[1])

def producto(z1, z2):
    real = z1[0]*z2[0] - z1[1]*z2[1]
    imag = z1[0]*z2[1] + z1[1]*z2[0]
    return (real, imag)

def division(z1, z2):
    denom = z2[0]**2 + z2[1]**2
    if denom == 0:
        raise ZeroDivisionError("División por cero en números complejos.")
    real = (z1[0]*z2[0] - z1[1]*z2[1]) / denom
    imag = (z1[1]*z2[0] + z1[0]*z2[1]) / denom
    return (real, imag)


def modulo(z):
    return math.sqrt(z[0]**2 + z[1]**2)

def conjugado(z):
    return (z[0], -z[1])

def cartesiano_a_polar(z):
    r = modulo(z)
    theta = math.atan2(z[1], z[0])
    return (r, theta)

def polar_a_cartesiano(p):
    a = p[0] * math.cos(p[1])
    b = p[0] * math.sin(p[1])
    return (a, b)

def fase(z):
    return math.atan2(z[1], z[0])
