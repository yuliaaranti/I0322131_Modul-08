import math

def LPkubus(r):
    return 6(r**2)

def Vkubus(r):
    return r**3

def LPbalok(p,l,t):
    return (2*p*l) + (2*p*t) + (2*l*t)

def Vbalok(p,l,t):
    return p*l*t

def LP_limas_persegi(s, t_sisi, tinggi):
    return 4(0.5*t_sisi*s) + (s**2)

def Vlimas_persegi(s, tinggi):
    return (1/3)*(s**2)*tinggi