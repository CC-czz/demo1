# ---------------------------------------------------------------------- 
# This model file was automatically created by SARAH version4.15.3
# SARAH References: arXiv:0806.0538, arXiv:0909.2863, arXiv:1002.0840   
# (c) Florian Staub, Mark Goodsell, Werner Porod and Martin Gabelmann 2023 
# ---------------------------------------------------------------------- 
# File created at 11:53 on 26.8.2025  
# ---------------------------------------------------------------------- 


from __future__ import division
from object_library import all_particles,Particle
import parameters as Param


d1 = Particle(pdg_code =1,
    name = 'd1' ,
    antiname = 'd1bar' ,
    spin = 2 ,
    color = 3 ,
    mass = Param.Md1 ,
    width = Param.ZERO ,
    line = 'swavy' ,
    charge = -1/3 ,
    texname = '{d}_1' ,
    antitexname = '{\\bar{d}}_1' )

d1bar = d1.anti()


d2 = Particle(pdg_code =3,
    name = 'd2' ,
    antiname = 'd2bar' ,
    spin = 2 ,
    color = 3 ,
    mass = Param.Md2 ,
    width = Param.ZERO ,
    line = 'swavy' ,
    charge = -1/3 ,
    texname = '{d}_2' ,
    antitexname = '{\\bar{d}}_2' )

d2bar = d2.anti()


d3 = Particle(pdg_code =5,
    name = 'd3' ,
    antiname = 'd3bar' ,
    spin = 2 ,
    color = 3 ,
    mass = Param.Md3 ,
    width = Param.ZERO ,
    line = 'swavy' ,
    charge = -1/3 ,
    texname = '{d}_3' ,
    antitexname = '{\\bar{d}}_3' )

d3bar = d3.anti()


u1 = Particle(pdg_code =2,
    name = 'u1' ,
    antiname = 'u1bar' ,
    spin = 2 ,
    color = 3 ,
    mass = Param.Mu1 ,
    width = Param.ZERO ,
    line = 'swavy' ,
    charge = 2/3 ,
    texname = '{u}_1' ,
    antitexname = '{\\bar{u}}_1' )

u1bar = u1.anti()


u2 = Particle(pdg_code =4,
    name = 'u2' ,
    antiname = 'u2bar' ,
    spin = 2 ,
    color = 3 ,
    mass = Param.Mu2 ,
    width = Param.ZERO ,
    line = 'swavy' ,
    charge = 2/3 ,
    texname = '{u}_2' ,
    antitexname = '{\\bar{u}}_2' )

u2bar = u2.anti()


u3 = Particle(pdg_code =6,
    name = 'u3' ,
    antiname = 'u3bar' ,
    spin = 2 ,
    color = 3 ,
    mass = Param.Mu3 ,
    width = Param.Wu3 ,
    line = 'swavy' ,
    charge = 2/3 ,
    texname = '{u}_3' ,
    antitexname = '{\\bar{u}}_3' )

u3bar = u3.anti()


e1 = Particle(pdg_code =11,
    name = 'e1' ,
    antiname = 'e1bar' ,
    spin = 2 ,
    color = 1 ,
    mass = Param.Me1 ,
    width = Param.ZERO ,
    line = 'swavy' ,
    charge = -1 ,
    texname = '{e}_1' ,
    antitexname = '{\\bar{e}}_1' )

e1bar = e1.anti()


e2 = Particle(pdg_code =13,
    name = 'e2' ,
    antiname = 'e2bar' ,
    spin = 2 ,
    color = 1 ,
    mass = Param.Me2 ,
    width = Param.ZERO ,
    line = 'swavy' ,
    charge = -1 ,
    texname = '{e}_2' ,
    antitexname = '{\\bar{e}}_2' )

e2bar = e2.anti()


e3 = Particle(pdg_code =15,
    name = 'e3' ,
    antiname = 'e3bar' ,
    spin = 2 ,
    color = 1 ,
    mass = Param.Me3 ,
    width = Param.ZERO ,
    line = 'swavy' ,
    charge = -1 ,
    texname = '{e}_3' ,
    antitexname = '{\\bar{e}}_3' )

e3bar = e3.anti()


nu1 = Particle(pdg_code =12,
    name = 'nu1' ,
    antiname = 'nu1' ,
    spin = 2 ,
    color = 1 ,
    mass = Param.ZERO ,
    width = Param.ZERO ,
    line = 'swavy' ,
    charge = 0 ,
    texname = '{\\nu}_1' ,
    antitexname = '{\\nu}_1' )

nu2 = Particle(pdg_code =14,
    name = 'nu2' ,
    antiname = 'nu2' ,
    spin = 2 ,
    color = 1 ,
    mass = Param.ZERO ,
    width = Param.ZERO ,
    line = 'swavy' ,
    charge = 0 ,
    texname = '{\\nu}_2' ,
    antitexname = '{\\nu}_2' )

nu3 = Particle(pdg_code =16,
    name = 'nu3' ,
    antiname = 'nu3' ,
    spin = 2 ,
    color = 1 ,
    mass = Param.ZERO ,
    width = Param.ZERO ,
    line = 'swavy' ,
    charge = 0 ,
    texname = '{\\nu}_3' ,
    antitexname = '{\\nu}_3' )

nu4 = Particle(pdg_code =112,
    name = 'nu4' ,
    antiname = 'nu4' ,
    spin = 2 ,
    color = 1 ,
    mass = Param.Mnu4 ,
    width = Param.Wnu4 ,
    line = 'swavy' ,
    charge = 0 ,
    texname = '{\\nu}_4' ,
    antitexname = '{\\nu}_4' )

nu5 = Particle(pdg_code =114,
    name = 'nu5' ,
    antiname = 'nu5' ,
    spin = 2 ,
    color = 1 ,
    mass = Param.Mnu5 ,
    width = Param.Wnu5 ,
    line = 'swavy' ,
    charge = 0 ,
    texname = '{\\nu}_5' ,
    antitexname = '{\\nu}_5' )

h1 = Particle(pdg_code =25,
    name = 'h1' ,
    antiname = 'h1' ,
    spin = 1 ,
    color = 1 ,
    mass = Param.Mh1 ,
    width = Param.Wh1 ,
    line = 'dashed' ,
    charge = 0 ,
    texname = '{h}_1' ,
    antitexname = '{h}_1' )

h2 = Particle(pdg_code =35,
    name = 'h2' ,
    antiname = 'h2' ,
    spin = 1 ,
    color = 1 ,
    mass = Param.Mh2 ,
    width = Param.Wh2 ,
    line = 'dashed' ,
    charge = 0 ,
    texname = '{h}_2' ,
    antitexname = '{h}_2' )

h3 = Particle(pdg_code =36,
    name = 'h3' ,
    antiname = 'h3' ,
    spin = 1 ,
    color = 1 ,
    mass = Param.Mh3 ,
    width = Param.Wh3 ,
    line = 'dashed' ,
    charge = 0 ,
    texname = '{h}_3' ,
    antitexname = '{h}_3' )

h4 = Particle(pdg_code =55,
    name = 'h4' ,
    antiname = 'h4' ,
    spin = 1 ,
    color = 1 ,
    mass = Param.Mh4 ,
    width = Param.Wh4 ,
    line = 'dashed' ,
    charge = 0 ,
    texname = '{h}_4' ,
    antitexname = '{h}_4' )

Ah1 = Particle(pdg_code =45,
    name = 'Ah1' ,
    antiname = 'Ah1' ,
    spin = 1 ,
    color = 1 ,
    mass = Param.MAh1 ,
    width = Param.WAh1 ,
    line = 'dashed' ,
    charge = 0 ,
    texname = '{A_h}_1' ,
    antitexname = '{A_h}_1' )

Ah2 = Particle(pdg_code =46,
    name = 'Ah2' ,
    antiname = 'Ah2' ,
    spin = 1 ,
    color = 1 ,
    mass = Param.MAh2 ,
    width = Param.WAh2 ,
    line = 'dashed' ,
    charge = 0 ,
    texname = '{A_h}_2' ,
    antitexname = '{A_h}_2' )

Ah3 = Particle(pdg_code =56,
    name = 'Ah3' ,
    antiname = 'Ah3' ,
    spin = 1 ,
    color = 1 ,
    mass = Param.MAh3 ,
    width = Param.ZERO,
    goldstone = True ,
    line = 'dashed' ,
    charge = 0 ,
    texname = '{A_h}_3' ,
    antitexname = '{A_h}_3' )

Ah4 = Particle(pdg_code =66,
    name = 'Ah4' ,
    antiname = 'Ah4' ,
    spin = 1 ,
    color = 1 ,
    mass = Param.MAh4 ,
    width = Param.ZERO,
    goldstone = True ,
    line = 'dashed' ,
    charge = 0 ,
    texname = '{A_h}_4' ,
    antitexname = '{A_h}_4' )

Hpm1 = Particle(pdg_code =37,
    name = 'Hpm1' ,
    antiname = 'Hpm1c' ,
    spin = 1 ,
    color = 1 ,
    mass = Param.MHpm1 ,
    width = Param.WHpm1 ,
    line = 'dashed' ,
    charge = 1 ,
    texname = '{H^+}_1' ,
    antitexname = '{{H^+}^*}_1' )

Hpm1c = Hpm1.anti()


Hpm2 = Particle(pdg_code =47,
    name = 'Hpm2' ,
    antiname = 'Hpm2c' ,
    spin = 1 ,
    color = 1 ,
    mass = Param.MHpm2 ,
    width = Param.WHpm2 ,
    line = 'dashed' ,
    charge = 1 ,
    texname = '{H^+}_2' ,
    antitexname = '{{H^+}^*}_2' )

Hpm2c = Hpm2.anti()


Hpm3 = Particle(pdg_code =57,
    name = 'Hpm3' ,
    antiname = 'Hpm3c' ,
    spin = 1 ,
    color = 1 ,
    mass = Param.MHpm3 ,
    width = Param.ZERO,
    goldstone = True ,
    line = 'dashed' ,
    charge = 1 ,
    texname = '{H^+}_3' ,
    antitexname = '{{H^+}^*}_3' )

Hpm3c = Hpm3.anti()


g = Particle(pdg_code =21,
    name = 'g' ,
    antiname = 'g' ,
    spin = 3 ,
    color = 8 ,
    mass = Param.ZERO ,
    width = Param.ZERO ,
    line = 'wavy' ,
    charge = 0 ,
    texname = 'g' ,
    antitexname = 'g' )

A = Particle(pdg_code =22,
    name = 'A' ,
    antiname = 'A' ,
    spin = 3 ,
    color = 1 ,
    mass = Param.ZERO ,
    width = Param.ZERO ,
    line = 'wavy' ,
    charge = 0 ,
    texname = '\\gamma' ,
    antitexname = '\\gamma' )

Z = Particle(pdg_code =23,
    name = 'Z' ,
    antiname = 'Z' ,
    spin = 3 ,
    color = 1 ,
    mass = Param.MZ ,
    width = Param.WZ ,
    line = 'wavy' ,
    charge = 0 ,
    texname = 'Z' ,
    antitexname = 'Z' )

Zp = Particle(pdg_code =31,
    name = 'Zp' ,
    antiname = 'Zp' ,
    spin = 3 ,
    color = 1 ,
    mass = Param.MZp ,
    width = Param.WZp ,
    line = 'wavy' ,
    charge = 0 ,
    texname = '{Z^{\\prime}}' ,
    antitexname = '{Z^{\\prime}}' )

Wm = Particle(pdg_code =-24,
    name = 'Wm' ,
    antiname = 'Wmc' ,
    spin = 3 ,
    color = 1 ,
    mass = Param.MWm ,
    width = Param.WWm ,
    line = 'wavy' ,
    charge = -1 ,
    texname = 'W^-' ,
    antitexname = 'W^+' )

Wmc = Wm.anti()


gG = Particle(pdg_code =999900,
    name = 'gG' ,
    antiname = 'gGc' ,
    spin = -1 ,
    color = 8 ,
    mass = Param.ZERO ,
    width = Param.ZERO ,
    propagating = False,
    line = 'dotted' ,
    charge = 0 ,
    texname = '\\eta^G' ,
    antitexname = '\\bar{\\eta^G}' )

gGc = gG.anti()


gA = Particle(pdg_code =999901,
    name = 'gA' ,
    antiname = 'gAc' ,
    spin = -1 ,
    color = 1 ,
    mass = Param.ZERO ,
    width = Param.ZERO ,
    propagating = False,
    line = 'dotted' ,
    charge = 0 ,
    texname = '\\eta^{\\gamma}' ,
    antitexname = '\\bar{\\eta^{\\gamma}}' )

gAc = gA.anti()


gZ = Particle(pdg_code =999902,
    name = 'gZ' ,
    antiname = 'gZc' ,
    spin = -1 ,
    color = 1 ,
    mass = Param.MgZ ,
    width = Param.WZ ,
    propagating = False,
    line = 'dotted' ,
    charge = 0 ,
    texname = '\\eta^Z' ,
    antitexname = '\\bar{\\eta^Z}' )

gZc = gZ.anti()


gZp = Particle(pdg_code =999903,
    name = 'gZp' ,
    antiname = 'gZpc' ,
    spin = -1 ,
    color = 1 ,
    mass = Param.ZERO ,
    width = Param.WZp ,
    propagating = False,
    line = 'dotted' ,
    charge = 0 ,
    texname = '\\eta^{Z^{\\prime}}' ,
    antitexname = '\\bar{\\eta^{Z^{\\prime}}}' )

gZpc = gZp.anti()


gWm = Particle(pdg_code =999904,
    name = 'gWm' ,
    antiname = 'gWmc' ,
    spin = -1 ,
    color = 1 ,
    mass = Param.MgWm ,
    width = Param.WWm ,
    propagating = False,
    line = 'dotted' ,
    charge = -1 ,
    texname = '\\eta^-' ,
    antitexname = '\\bar{\\eta^-}' )

gWmc = gWm.anti()


gWpC = Particle(pdg_code =999905,
    name = 'gWpC' ,
    antiname = 'gWpCc' ,
    spin = -1 ,
    color = 1 ,
    mass = Param.MgWpC ,
    width = Param.WWm ,
    propagating = False,
    line = 'dotted' ,
    charge = 1 ,
    texname = '\\eta^+' ,
    antitexname = '\\bar{\\eta^+}' )

gWpCc = gWpC.anti()


