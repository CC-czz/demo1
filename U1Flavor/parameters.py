# ----------------------------------------------------------------------
# This model file was automatically created by SARAH version4.15.3
# SARAH References: arXiv:0806.0538, arXiv:0909.2863, arXiv:1002.0840
# (c) Florian Staub, Mark Goodsell, Werner Porod and Martin Gabelmann 2023
# ----------------------------------------------------------------------
# File created at 11:53 on 26.8.2025
# ----------------------------------------------------------------------

from object_library import all_parameters,Parameter

from function_library import complexconjugate,re,im,csc,sec,acsc,asec
ZERO = Parameter(name='ZERO',
    nature='internal',
    type='real',
    value='0.0',
    texname='0')

Md1 = Parameter(name = 'Md1',
    nature = 'external',
    type = 'real',
    value = 0.0035,
    texname = 'M_{{d}_1}',
    lhablock = 'MASS',
    lhacode = [1])

Md2 = Parameter(name = 'Md2',
    nature = 'external',
    type = 'real',
    value = 0.104,
    texname = 'M_{{d}_2}',
    lhablock = 'MASS',
    lhacode = [3])

Md3 = Parameter(name = 'Md3',
    nature = 'external',
    type = 'real',
    value = 4.2,
    texname = 'M_{{d}_3}',
    lhablock = 'MASS',
    lhacode = [5])

Mu1 = Parameter(name = 'Mu1',
    nature = 'external',
    type = 'real',
    value = 0.0015,
    texname = 'M_{{u}_1}',
    lhablock = 'MASS',
    lhacode = [2])

Mu2 = Parameter(name = 'Mu2',
    nature = 'external',
    type = 'real',
    value = 1.27,
    texname = 'M_{{u}_2}',
    lhablock = 'MASS',
    lhacode = [4])

Mu3 = Parameter(name = 'Mu3',
    nature = 'external',
    type = 'real',
    value = 171.2,
    texname = 'M_{{u}_3}',
    lhablock = 'MASS',
    lhacode = [6])

Wu3 = Parameter(name = 'Wu3',
    nature = 'external',
    type = 'real',
    value = 1.51,
    texname = '\\Gamma_{{u}_3}',
    lhablock = 'DECAY',
    lhacode = [6])

Me1 = Parameter(name = 'Me1',
    nature = 'external',
    type = 'real',
    value = 0.000511,
    texname = 'M_{{e}_1}',
    lhablock = 'MASS',
    lhacode = [11])

Me2 = Parameter(name = 'Me2',
    nature = 'external',
    type = 'real',
    value = 0.105,
    texname = 'M_{{e}_2}',
    lhablock = 'MASS',
    lhacode = [13])

Me3 = Parameter(name = 'Me3',
    nature = 'external',
    type = 'real',
    value = 1.776,
    texname = 'M_{{e}_3}',
    lhablock = 'MASS',
    lhacode = [15])

Mnu4 = Parameter(name = 'Mnu4',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{\\nu}_4}',
    lhablock = 'MASS',
    lhacode = [112])

Wnu4 = Parameter(name = 'Wnu4',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{\\nu}_4}',
    lhablock = 'DECAY',
    lhacode = [112])

Mnu5 = Parameter(name = 'Mnu5',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{\\nu}_5}',
    lhablock = 'MASS',
    lhacode = [114])

Wnu5 = Parameter(name = 'Wnu5',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{\\nu}_5}',
    lhablock = 'DECAY',
    lhacode = [114])

Mh1 = Parameter(name = 'Mh1',
    nature = 'external',
    type = 'real',
    value = 125.2,
    texname = 'M_{{h}_1}',
    lhablock = 'MASS',
    lhacode = [25])

Wh1 = Parameter(name = 'Wh1',
    nature = 'external',
    type = 'real',
    value = 0.0037,
    texname = '\\Gamma_{{h}_1}',
    lhablock = 'DECAY',
    lhacode = [25])

Mh2 = Parameter(name = 'Mh2',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{h}_2}',
    lhablock = 'MASS',
    lhacode = [35])

Wh2 = Parameter(name = 'Wh2',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{h}_2}',
    lhablock = 'DECAY',
    lhacode = [35])

Mh3 = Parameter(name = 'Mh3',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{h}_3}',
    lhablock = 'MASS',
    lhacode = [36])

Wh3 = Parameter(name = 'Wh3',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{h}_3}',
    lhablock = 'DECAY',
    lhacode = [36])

Mh4 = Parameter(name = 'Mh4',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{h}_4}',
    lhablock = 'MASS',
    lhacode = [55])

Wh4 = Parameter(name = 'Wh4',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{h}_4}',
    lhablock = 'DECAY',
    lhacode = [55])

MAh1 = Parameter(name = 'MAh1',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{A_h}_1}',
    lhablock = 'MASS',
    lhacode = [45])

WAh1 = Parameter(name = 'WAh1',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{A_h}_1}',
    lhablock = 'DECAY',
    lhacode = [45])

MAh2 = Parameter(name = 'MAh2',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{A_h}_2}',
    lhablock = 'MASS',
    lhacode = [46])

WAh2 = Parameter(name = 'WAh2',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{A_h}_2}',
    lhablock = 'DECAY',
    lhacode = [46])

MHpm1 = Parameter(name = 'MHpm1',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{H^+}_1}',
    lhablock = 'MASS',
    lhacode = [37])

WHpm1 = Parameter(name = 'WHpm1',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{H^+}_1}',
    lhablock = 'DECAY',
    lhacode = [37])

MHpm2 = Parameter(name = 'MHpm2',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{H^+}_2}',
    lhablock = 'MASS',
    lhacode = [47])

WHpm2 = Parameter(name = 'WHpm2',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{H^+}_2}',
    lhablock = 'DECAY',
    lhacode = [47])

MZ = Parameter(name = 'MZ',
    nature = 'external',
    type = 'real',
    value = 91.1876,
    texname = 'M_{Z}',
    lhablock = 'MASS',
    lhacode = [23])

WZ = Parameter(name = 'WZ',
    nature = 'external',
    type = 'real',
    value = 2.4952,
    texname = '\\Gamma_{Z}',
    lhablock = 'DECAY',
    lhacode = [23])

MZp = Parameter(name = 'MZp',
    nature = 'external',
    type = 'real',
    value = 100.,
    texname = 'M_{{Z^{\\prime}}}',
    lhablock = 'MASS',
    lhacode = [31])

WZp = Parameter(name = 'WZp',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\Gamma_{{Z^{\\prime}}}',
    lhablock = 'DECAY',
    lhacode = [31])

WWm = Parameter(name = 'WWm',
    nature = 'external',
    type = 'real',
    value = 2.141,
    texname = '\\Gamma_{W^-}',
    lhablock = 'DECAY',
    lhacode = [24])

g1p = Parameter(name='g1p',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'g_{F}',
    lhablock = 'GAUGE',
    lhacode = [2] )

gYF = Parameter(name='gYF',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{gYF}',
    lhablock = 'GAUGE',
    lhacode = [3] )

rYu21 = Parameter(name='rYu21',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{u21}',
    lhablock = 'YU',
    lhacode = [3] )

iYu21 = Parameter(name='iYu21',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{u21}',
    lhablock = 'IMYU',
    lhacode = [3] )

rYu31 = Parameter(name='rYu31',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{u31}',
    lhablock = 'YU',
    lhacode = [5] )

iYu31 = Parameter(name='iYu31',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{u31}',
    lhablock = 'IMYU',
    lhacode = [5] )

rYu12 = Parameter(name='rYu12',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{u12}',
    lhablock = 'YU',
    lhacode = [2] )

iYu12 = Parameter(name='iYu12',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{u12}',
    lhablock = 'IMYU',
    lhacode = [2] )

rYu32 = Parameter(name='rYu32',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{u32}',
    lhablock = 'YU',
    lhacode = [7] )

iYu32 = Parameter(name='iYu32',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{u32}',
    lhablock = 'IMYU',
    lhacode = [7] )

rYu13 = Parameter(name='rYu13',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{u13}',
    lhablock = 'YU',
    lhacode = [4] )

iYu13 = Parameter(name='iYu13',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{u13}',
    lhablock = 'IMYU',
    lhacode = [4] )

rYu23 = Parameter(name='rYu23',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{u23}',
    lhablock = 'YU',
    lhacode = [6] )

iYu23 = Parameter(name='iYu23',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{u23}',
    lhablock = 'IMYU',
    lhacode = [6] )

rYu33 = Parameter(name='rYu33',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{u33}',
    lhablock = 'YU',
    lhacode = [1] )

iYu33 = Parameter(name='iYu33',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{u33}',
    lhablock = 'IMYU',
    lhacode = [1] )

rYvD21 = Parameter(name='rYvD21',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y^D_{\\nu21}',
    lhablock = 'YVD',
    lhacode = [2] )

iYvD21 = Parameter(name='iYvD21',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y^D_{\\nu21}',
    lhablock = 'IMYVD',
    lhacode = [2] )

rYvD31 = Parameter(name='rYvD31',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y^D_{\\nu31}',
    lhablock = 'YVD',
    lhacode = [3] )

iYvD31 = Parameter(name='iYvD31',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y^D_{\\nu31}',
    lhablock = 'IMYVD',
    lhacode = [3] )

rYvM11 = Parameter(name='rYvM11',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y^M_{\\nu11}',
    lhablock = 'YVM',
    lhacode = [1] )

iYvM11 = Parameter(name='iYvM11',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y^M_{\\nu11}',
    lhablock = 'IMYVM',
    lhacode = [1] )

rYvD12 = Parameter(name='rYvD12',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y^D_{\\nu12}',
    lhablock = 'YVD',
    lhacode = [1] )

iYvD12 = Parameter(name='iYvD12',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y^D_{\\nu12}',
    lhablock = 'IMYVD',
    lhacode = [1] )

rYvD32 = Parameter(name='rYvD32',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y^D_{\\nu32}',
    lhablock = 'YVD',
    lhacode = [4] )

iYvD32 = Parameter(name='iYvD32',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y^D_{\\nu32}',
    lhablock = 'IMYVD',
    lhacode = [4] )

rYvM22 = Parameter(name='rYvM22',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y^M_{\\nu22}',
    lhablock = 'YVM',
    lhacode = [2] )

iYvM22 = Parameter(name='iYvM22',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y^M_{\\nu22}',
    lhablock = 'IMYVM',
    lhacode = [2] )

rYd31 = Parameter(name='rYd31',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{d31}',
    lhablock = 'YD',
    lhacode = [5] )

iYd31 = Parameter(name='iYd31',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{d31}',
    lhablock = 'IMYD',
    lhacode = [5] )

rYd13 = Parameter(name='rYd13',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{d13}',
    lhablock = 'YD',
    lhacode = [4] )

iYd13 = Parameter(name='iYd13',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{d13}',
    lhablock = 'IMYD',
    lhacode = [4] )

rYe31 = Parameter(name='rYe31',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{e31}',
    lhablock = 'YE',
    lhacode = [5] )

iYe31 = Parameter(name='iYe31',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{e31}',
    lhablock = 'IMYE',
    lhacode = [5] )

rYe13 = Parameter(name='rYe13',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{e13}',
    lhablock = 'YE',
    lhacode = [4] )

iYe13 = Parameter(name='iYe13',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{e13}',
    lhablock = 'IMYE',
    lhacode = [4] )

rKappa = Parameter(name='rKappa',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\kappa',
    lhablock = 'BL',
    lhacode = [11] )

iKappa = Parameter(name='iKappa',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\kappa',
    lhablock = 'IMBL',
    lhacode = [11] )

rYd32 = Parameter(name='rYd32',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{d32}',
    lhablock = 'YD',
    lhacode = [7] )

iYd32 = Parameter(name='iYd32',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{d32}',
    lhablock = 'IMYD',
    lhacode = [7] )

rYd23 = Parameter(name='rYd23',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{d23}',
    lhablock = 'YD',
    lhacode = [6] )

iYd23 = Parameter(name='iYd23',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{d23}',
    lhablock = 'IMYD',
    lhacode = [6] )

rYe32 = Parameter(name='rYe32',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{e32}',
    lhablock = 'YE',
    lhacode = [7] )

iYe32 = Parameter(name='iYe32',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{e32}',
    lhablock = 'IMYE',
    lhacode = [7] )

rYe23 = Parameter(name='rYe23',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{e23}',
    lhablock = 'YE',
    lhacode = [6] )

iYe23 = Parameter(name='iYe23',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{e23}',
    lhablock = 'IMYE',
    lhacode = [6] )

rYd21 = Parameter(name='rYd21',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{d21}',
    lhablock = 'YD',
    lhacode = [3] )

iYd21 = Parameter(name='iYd21',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{d21}',
    lhablock = 'IMYD',
    lhacode = [3] )

rYd12 = Parameter(name='rYd12',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{d12}',
    lhablock = 'YD',
    lhacode = [2] )

iYd12 = Parameter(name='iYd12',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{d12}',
    lhablock = 'IMYD',
    lhacode = [2] )

rYd33 = Parameter(name='rYd33',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{d33}',
    lhablock = 'YD',
    lhacode = [1] )

iYd33 = Parameter(name='iYd33',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{d33}',
    lhablock = 'IMYD',
    lhacode = [1] )

rYe21 = Parameter(name='rYe21',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{e21}',
    lhablock = 'YE',
    lhacode = [3] )

iYe21 = Parameter(name='iYe21',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{e21}',
    lhablock = 'IMYE',
    lhacode = [3] )

rYe12 = Parameter(name='rYe12',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{e12}',
    lhablock = 'YE',
    lhacode = [2] )

iYe12 = Parameter(name='iYe12',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{e12}',
    lhablock = 'IMYE',
    lhacode = [2] )

rYe33 = Parameter(name='rYe33',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{e33}',
    lhablock = 'YE',
    lhacode = [1] )

iYe33 = Parameter(name='iYe33',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'Y_{e33}',
    lhablock = 'IMYE',
    lhacode = [1] )

rL10 = Parameter(name='rL10',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\lambda_{10}',
    lhablock = 'BL',
    lhacode = [10] )

iL10 = Parameter(name='iL10',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\lambda_{10}',
    lhablock = 'IMBL',
    lhacode = [10] )

rLchi = Parameter(name='rLchi',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\lambda_{\\chi}',
    lhablock = 'BL',
    lhacode = [12] )

iLchi = Parameter(name='iLchi',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\lambda_{\\chi}',
    lhablock = 'IMBL',
    lhacode = [12] )

rL7 = Parameter(name='rL7',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\lambda_7',
    lhablock = 'BL',
    lhacode = [7] )

iL7 = Parameter(name='iL7',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\lambda_7',
    lhablock = 'IMBL',
    lhacode = [7] )

rL1 = Parameter(name='rL1',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\lambda_1',
    lhablock = 'BL',
    lhacode = [1] )

iL1 = Parameter(name='iL1',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\lambda_1',
    lhablock = 'IMBL',
    lhacode = [1] )

rL4p = Parameter(name='rL4p',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\lambda^{\\prime}_4',
    lhablock = 'BL',
    lhacode = [4] )

iL4p = Parameter(name='iL4p',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\lambda^{\\prime}_4',
    lhablock = 'IMBL',
    lhacode = [4] )

rL5p = Parameter(name='rL5p',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\lambda^{\\prime}_5',
    lhablock = 'BL',
    lhacode = [5] )

iL5p = Parameter(name='iL5p',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\lambda^{\\prime}_5',
    lhablock = 'IMBL',
    lhacode = [5] )

rL4pp = Parameter(name='rL4pp',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\lambda^{\\prime \\prime}_4',
    lhablock = 'BL',
    lhacode = [41] )

iL4pp = Parameter(name='iL4pp',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\lambda^{\\prime \\prime}_4',
    lhablock = 'IMBL',
    lhacode = [41] )

rL5pp = Parameter(name='rL5pp',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\lambda^{\\prime \\prime}_5',
    lhablock = 'BL',
    lhacode = [51] )

iL5pp = Parameter(name='iL5pp',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\lambda^{\\prime \\prime}_5',
    lhablock = 'IMBL',
    lhacode = [51] )

rL8 = Parameter(name='rL8',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\lambda_8',
    lhablock = 'BL',
    lhacode = [8] )

iL8 = Parameter(name='iL8',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\lambda_8',
    lhablock = 'IMBL',
    lhacode = [8] )

rL2 = Parameter(name='rL2',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\lambda_2',
    lhablock = 'BL',
    lhacode = [2] )

iL2 = Parameter(name='iL2',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\lambda_2',
    lhablock = 'IMBL',
    lhacode = [2] )

rL6p = Parameter(name='rL6p',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\lambda^{\\prime}_6',
    lhablock = 'BL',
    lhacode = [6] )

iL6p = Parameter(name='iL6p',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\lambda^{\\prime}_6',
    lhablock = 'IMBL',
    lhacode = [6] )

rL6pp = Parameter(name='rL6pp',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\lambda^{\\prime \\prime}_6',
    lhablock = 'BL',
    lhacode = [61] )

iL6pp = Parameter(name='iL6pp',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\lambda^{\\prime \\prime}_6',
    lhablock = 'IMBL',
    lhacode = [61] )

rL9 = Parameter(name='rL9',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\lambda_9',
    lhablock = 'BL',
    lhacode = [9] )

iL9 = Parameter(name='iL9',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\lambda_9',
    lhablock = 'IMBL',
    lhacode = [9] )

rL3 = Parameter(name='rL3',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\lambda_3',
    lhablock = 'BL',
    lhacode = [3] )

iL3 = Parameter(name='iL3',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\lambda_3',
    lhablock = 'IMBL',
    lhacode = [3] )

vphi1 = Parameter(name='vphi1',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'v_{\\phi_1}',
    lhablock = 'VP',
    lhacode = [1] )

vphi2 = Parameter(name='vphi2',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'v_{\\phi_2}',
    lhablock = 'VP',
    lhacode = [2] )

vphi3 = Parameter(name='vphi3',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'v_{\\phi_3}',
    lhablock = 'VP',
    lhacode = [3] )

vchi = Parameter(name='vchi',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = 'v_\\chi',
    lhablock = 'VP',
    lhacode = [4] )

ZH11 = Parameter(name='ZH11',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZH11}',
    lhablock = 'SCALARMIX',
    lhacode = [1, 1] )

ZH12 = Parameter(name='ZH12',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZH12}',
    lhablock = 'SCALARMIX',
    lhacode = [1, 2] )

ZH13 = Parameter(name='ZH13',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZH13}',
    lhablock = 'SCALARMIX',
    lhacode = [1, 3] )

ZH14 = Parameter(name='ZH14',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZH14}',
    lhablock = 'SCALARMIX',
    lhacode = [1, 4] )

ZH21 = Parameter(name='ZH21',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZH21}',
    lhablock = 'SCALARMIX',
    lhacode = [2, 1] )

ZH22 = Parameter(name='ZH22',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZH22}',
    lhablock = 'SCALARMIX',
    lhacode = [2, 2] )

ZH23 = Parameter(name='ZH23',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZH23}',
    lhablock = 'SCALARMIX',
    lhacode = [2, 3] )

ZH24 = Parameter(name='ZH24',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZH24}',
    lhablock = 'SCALARMIX',
    lhacode = [2, 4] )

ZH31 = Parameter(name='ZH31',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZH31}',
    lhablock = 'SCALARMIX',
    lhacode = [3, 1] )

ZH32 = Parameter(name='ZH32',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZH32}',
    lhablock = 'SCALARMIX',
    lhacode = [3, 2] )

ZH33 = Parameter(name='ZH33',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZH33}',
    lhablock = 'SCALARMIX',
    lhacode = [3, 3] )

ZH34 = Parameter(name='ZH34',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZH34}',
    lhablock = 'SCALARMIX',
    lhacode = [3, 4] )

ZH41 = Parameter(name='ZH41',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZH41}',
    lhablock = 'SCALARMIX',
    lhacode = [4, 1] )

ZH42 = Parameter(name='ZH42',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZH42}',
    lhablock = 'SCALARMIX',
    lhacode = [4, 2] )

ZH43 = Parameter(name='ZH43',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZH43}',
    lhablock = 'SCALARMIX',
    lhacode = [4, 3] )

ZH44 = Parameter(name='ZH44',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZH44}',
    lhablock = 'SCALARMIX',
    lhacode = [4, 4] )

ZA11 = Parameter(name='ZA11',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZA11}',
    lhablock = 'PSEUDOSCALARMIX',
    lhacode = [1, 1] )

ZA12 = Parameter(name='ZA12',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZA12}',
    lhablock = 'PSEUDOSCALARMIX',
    lhacode = [1, 2] )

ZA13 = Parameter(name='ZA13',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZA13}',
    lhablock = 'PSEUDOSCALARMIX',
    lhacode = [1, 3] )

ZA14 = Parameter(name='ZA14',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZA14}',
    lhablock = 'PSEUDOSCALARMIX',
    lhacode = [1, 4] )

ZA21 = Parameter(name='ZA21',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZA21}',
    lhablock = 'PSEUDOSCALARMIX',
    lhacode = [2, 1] )

ZA22 = Parameter(name='ZA22',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZA22}',
    lhablock = 'PSEUDOSCALARMIX',
    lhacode = [2, 2] )

ZA23 = Parameter(name='ZA23',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZA23}',
    lhablock = 'PSEUDOSCALARMIX',
    lhacode = [2, 3] )

ZA24 = Parameter(name='ZA24',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZA24}',
    lhablock = 'PSEUDOSCALARMIX',
    lhacode = [2, 4] )

ZA31 = Parameter(name='ZA31',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZA31}',
    lhablock = 'PSEUDOSCALARMIX',
    lhacode = [3, 1] )

ZA32 = Parameter(name='ZA32',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZA32}',
    lhablock = 'PSEUDOSCALARMIX',
    lhacode = [3, 2] )

ZA33 = Parameter(name='ZA33',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZA33}',
    lhablock = 'PSEUDOSCALARMIX',
    lhacode = [3, 3] )

ZA34 = Parameter(name='ZA34',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZA34}',
    lhablock = 'PSEUDOSCALARMIX',
    lhacode = [3, 4] )

ZA41 = Parameter(name='ZA41',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZA41}',
    lhablock = 'PSEUDOSCALARMIX',
    lhacode = [4, 1] )

ZA42 = Parameter(name='ZA42',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZA42}',
    lhablock = 'PSEUDOSCALARMIX',
    lhacode = [4, 2] )

ZA43 = Parameter(name='ZA43',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZA43}',
    lhablock = 'PSEUDOSCALARMIX',
    lhacode = [4, 3] )

ZA44 = Parameter(name='ZA44',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZA44}',
    lhablock = 'PSEUDOSCALARMIX',
    lhacode = [4, 4] )

ZP11 = Parameter(name='ZP11',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZP11}',
    lhablock = 'CHARGEMIX',
    lhacode = [1, 1] )

ZP12 = Parameter(name='ZP12',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZP12}',
    lhablock = 'CHARGEMIX',
    lhacode = [1, 2] )

ZP13 = Parameter(name='ZP13',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZP13}',
    lhablock = 'CHARGEMIX',
    lhacode = [1, 3] )

ZP21 = Parameter(name='ZP21',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZP21}',
    lhablock = 'CHARGEMIX',
    lhacode = [2, 1] )

ZP22 = Parameter(name='ZP22',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZP22}',
    lhablock = 'CHARGEMIX',
    lhacode = [2, 2] )

ZP23 = Parameter(name='ZP23',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZP23}',
    lhablock = 'CHARGEMIX',
    lhacode = [2, 3] )

ZP31 = Parameter(name='ZP31',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZP31}',
    lhablock = 'CHARGEMIX',
    lhacode = [3, 1] )

ZP32 = Parameter(name='ZP32',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZP32}',
    lhablock = 'CHARGEMIX',
    lhacode = [3, 2] )

ZP33 = Parameter(name='ZP33',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZP33}',
    lhablock = 'CHARGEMIX',
    lhacode = [3, 3] )

rZDL11 = Parameter(name='rZDL11',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDL11}',
    lhablock = 'UDLMIX',
    lhacode = [1, 1] )

iZDL11 = Parameter(name='iZDL11',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDL11}',
    lhablock = 'IMUDLMIX',
    lhacode = [1, 1] )

rZDL12 = Parameter(name='rZDL12',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDL12}',
    lhablock = 'UDLMIX',
    lhacode = [1, 2] )

iZDL12 = Parameter(name='iZDL12',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDL12}',
    lhablock = 'IMUDLMIX',
    lhacode = [1, 2] )

rZDL13 = Parameter(name='rZDL13',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDL13}',
    lhablock = 'UDLMIX',
    lhacode = [1, 3] )

iZDL13 = Parameter(name='iZDL13',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDL13}',
    lhablock = 'IMUDLMIX',
    lhacode = [1, 3] )

rZDL21 = Parameter(name='rZDL21',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDL21}',
    lhablock = 'UDLMIX',
    lhacode = [2, 1] )

iZDL21 = Parameter(name='iZDL21',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDL21}',
    lhablock = 'IMUDLMIX',
    lhacode = [2, 1] )

rZDL22 = Parameter(name='rZDL22',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDL22}',
    lhablock = 'UDLMIX',
    lhacode = [2, 2] )

iZDL22 = Parameter(name='iZDL22',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDL22}',
    lhablock = 'IMUDLMIX',
    lhacode = [2, 2] )

rZDL23 = Parameter(name='rZDL23',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDL23}',
    lhablock = 'UDLMIX',
    lhacode = [2, 3] )

iZDL23 = Parameter(name='iZDL23',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDL23}',
    lhablock = 'IMUDLMIX',
    lhacode = [2, 3] )

rZDL31 = Parameter(name='rZDL31',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDL31}',
    lhablock = 'UDLMIX',
    lhacode = [3, 1] )

iZDL31 = Parameter(name='iZDL31',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDL31}',
    lhablock = 'IMUDLMIX',
    lhacode = [3, 1] )

rZDL32 = Parameter(name='rZDL32',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDL32}',
    lhablock = 'UDLMIX',
    lhacode = [3, 2] )

iZDL32 = Parameter(name='iZDL32',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDL32}',
    lhablock = 'IMUDLMIX',
    lhacode = [3, 2] )

rZDL33 = Parameter(name='rZDL33',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDL33}',
    lhablock = 'UDLMIX',
    lhacode = [3, 3] )

iZDL33 = Parameter(name='iZDL33',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDL33}',
    lhablock = 'IMUDLMIX',
    lhacode = [3, 3] )

rZDR11 = Parameter(name='rZDR11',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDR11}',
    lhablock = 'UDRMIX',
    lhacode = [1, 1] )

iZDR11 = Parameter(name='iZDR11',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDR11}',
    lhablock = 'IMUDRMIX',
    lhacode = [1, 1] )

rZDR12 = Parameter(name='rZDR12',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDR12}',
    lhablock = 'UDRMIX',
    lhacode = [1, 2] )

iZDR12 = Parameter(name='iZDR12',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDR12}',
    lhablock = 'IMUDRMIX',
    lhacode = [1, 2] )

rZDR13 = Parameter(name='rZDR13',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDR13}',
    lhablock = 'UDRMIX',
    lhacode = [1, 3] )

iZDR13 = Parameter(name='iZDR13',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDR13}',
    lhablock = 'IMUDRMIX',
    lhacode = [1, 3] )

rZDR21 = Parameter(name='rZDR21',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDR21}',
    lhablock = 'UDRMIX',
    lhacode = [2, 1] )

iZDR21 = Parameter(name='iZDR21',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDR21}',
    lhablock = 'IMUDRMIX',
    lhacode = [2, 1] )

rZDR22 = Parameter(name='rZDR22',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDR22}',
    lhablock = 'UDRMIX',
    lhacode = [2, 2] )

iZDR22 = Parameter(name='iZDR22',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDR22}',
    lhablock = 'IMUDRMIX',
    lhacode = [2, 2] )

rZDR23 = Parameter(name='rZDR23',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDR23}',
    lhablock = 'UDRMIX',
    lhacode = [2, 3] )

iZDR23 = Parameter(name='iZDR23',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDR23}',
    lhablock = 'IMUDRMIX',
    lhacode = [2, 3] )

rZDR31 = Parameter(name='rZDR31',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDR31}',
    lhablock = 'UDRMIX',
    lhacode = [3, 1] )

iZDR31 = Parameter(name='iZDR31',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDR31}',
    lhablock = 'IMUDRMIX',
    lhacode = [3, 1] )

rZDR32 = Parameter(name='rZDR32',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDR32}',
    lhablock = 'UDRMIX',
    lhacode = [3, 2] )

iZDR32 = Parameter(name='iZDR32',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDR32}',
    lhablock = 'IMUDRMIX',
    lhacode = [3, 2] )

rZDR33 = Parameter(name='rZDR33',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDR33}',
    lhablock = 'UDRMIX',
    lhacode = [3, 3] )

iZDR33 = Parameter(name='iZDR33',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZDR33}',
    lhablock = 'IMUDRMIX',
    lhacode = [3, 3] )

rZUL11 = Parameter(name='rZUL11',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUL11}',
    lhablock = 'UULMIX',
    lhacode = [1, 1] )

iZUL11 = Parameter(name='iZUL11',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUL11}',
    lhablock = 'IMUULMIX',
    lhacode = [1, 1] )

rZUL12 = Parameter(name='rZUL12',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUL12}',
    lhablock = 'UULMIX',
    lhacode = [1, 2] )

iZUL12 = Parameter(name='iZUL12',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUL12}',
    lhablock = 'IMUULMIX',
    lhacode = [1, 2] )

rZUL13 = Parameter(name='rZUL13',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUL13}',
    lhablock = 'UULMIX',
    lhacode = [1, 3] )

iZUL13 = Parameter(name='iZUL13',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUL13}',
    lhablock = 'IMUULMIX',
    lhacode = [1, 3] )

rZUL21 = Parameter(name='rZUL21',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUL21}',
    lhablock = 'UULMIX',
    lhacode = [2, 1] )

iZUL21 = Parameter(name='iZUL21',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUL21}',
    lhablock = 'IMUULMIX',
    lhacode = [2, 1] )

rZUL22 = Parameter(name='rZUL22',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUL22}',
    lhablock = 'UULMIX',
    lhacode = [2, 2] )

iZUL22 = Parameter(name='iZUL22',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUL22}',
    lhablock = 'IMUULMIX',
    lhacode = [2, 2] )

rZUL23 = Parameter(name='rZUL23',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUL23}',
    lhablock = 'UULMIX',
    lhacode = [2, 3] )

iZUL23 = Parameter(name='iZUL23',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUL23}',
    lhablock = 'IMUULMIX',
    lhacode = [2, 3] )

rZUL31 = Parameter(name='rZUL31',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUL31}',
    lhablock = 'UULMIX',
    lhacode = [3, 1] )

iZUL31 = Parameter(name='iZUL31',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUL31}',
    lhablock = 'IMUULMIX',
    lhacode = [3, 1] )

rZUL32 = Parameter(name='rZUL32',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUL32}',
    lhablock = 'UULMIX',
    lhacode = [3, 2] )

iZUL32 = Parameter(name='iZUL32',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUL32}',
    lhablock = 'IMUULMIX',
    lhacode = [3, 2] )

rZUL33 = Parameter(name='rZUL33',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUL33}',
    lhablock = 'UULMIX',
    lhacode = [3, 3] )

iZUL33 = Parameter(name='iZUL33',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUL33}',
    lhablock = 'IMUULMIX',
    lhacode = [3, 3] )

rZUR11 = Parameter(name='rZUR11',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUR11}',
    lhablock = 'UURMIX',
    lhacode = [1, 1] )

iZUR11 = Parameter(name='iZUR11',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUR11}',
    lhablock = 'IMUURMIX',
    lhacode = [1, 1] )

rZUR12 = Parameter(name='rZUR12',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUR12}',
    lhablock = 'UURMIX',
    lhacode = [1, 2] )

iZUR12 = Parameter(name='iZUR12',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUR12}',
    lhablock = 'IMUURMIX',
    lhacode = [1, 2] )

rZUR13 = Parameter(name='rZUR13',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUR13}',
    lhablock = 'UURMIX',
    lhacode = [1, 3] )

iZUR13 = Parameter(name='iZUR13',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUR13}',
    lhablock = 'IMUURMIX',
    lhacode = [1, 3] )

rZUR21 = Parameter(name='rZUR21',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUR21}',
    lhablock = 'UURMIX',
    lhacode = [2, 1] )

iZUR21 = Parameter(name='iZUR21',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUR21}',
    lhablock = 'IMUURMIX',
    lhacode = [2, 1] )

rZUR22 = Parameter(name='rZUR22',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUR22}',
    lhablock = 'UURMIX',
    lhacode = [2, 2] )

iZUR22 = Parameter(name='iZUR22',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUR22}',
    lhablock = 'IMUURMIX',
    lhacode = [2, 2] )

rZUR23 = Parameter(name='rZUR23',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUR23}',
    lhablock = 'UURMIX',
    lhacode = [2, 3] )

iZUR23 = Parameter(name='iZUR23',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUR23}',
    lhablock = 'IMUURMIX',
    lhacode = [2, 3] )

rZUR31 = Parameter(name='rZUR31',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUR31}',
    lhablock = 'UURMIX',
    lhacode = [3, 1] )

iZUR31 = Parameter(name='iZUR31',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUR31}',
    lhablock = 'IMUURMIX',
    lhacode = [3, 1] )

rZUR32 = Parameter(name='rZUR32',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUR32}',
    lhablock = 'UURMIX',
    lhacode = [3, 2] )

iZUR32 = Parameter(name='iZUR32',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUR32}',
    lhablock = 'IMUURMIX',
    lhacode = [3, 2] )

rZUR33 = Parameter(name='rZUR33',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUR33}',
    lhablock = 'UURMIX',
    lhacode = [3, 3] )

iZUR33 = Parameter(name='iZUR33',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZUR33}',
    lhablock = 'IMUURMIX',
    lhacode = [3, 3] )

rZEL11 = Parameter(name='rZEL11',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZEL11}',
    lhablock = 'UELMIX',
    lhacode = [1, 1] )

iZEL11 = Parameter(name='iZEL11',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZEL11}',
    lhablock = 'IMUELMIX',
    lhacode = [1, 1] )

rZEL12 = Parameter(name='rZEL12',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZEL12}',
    lhablock = 'UELMIX',
    lhacode = [1, 2] )

iZEL12 = Parameter(name='iZEL12',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZEL12}',
    lhablock = 'IMUELMIX',
    lhacode = [1, 2] )

rZEL13 = Parameter(name='rZEL13',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZEL13}',
    lhablock = 'UELMIX',
    lhacode = [1, 3] )

iZEL13 = Parameter(name='iZEL13',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZEL13}',
    lhablock = 'IMUELMIX',
    lhacode = [1, 3] )

rZEL21 = Parameter(name='rZEL21',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZEL21}',
    lhablock = 'UELMIX',
    lhacode = [2, 1] )

iZEL21 = Parameter(name='iZEL21',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZEL21}',
    lhablock = 'IMUELMIX',
    lhacode = [2, 1] )

rZEL22 = Parameter(name='rZEL22',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZEL22}',
    lhablock = 'UELMIX',
    lhacode = [2, 2] )

iZEL22 = Parameter(name='iZEL22',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZEL22}',
    lhablock = 'IMUELMIX',
    lhacode = [2, 2] )

rZEL23 = Parameter(name='rZEL23',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZEL23}',
    lhablock = 'UELMIX',
    lhacode = [2, 3] )

iZEL23 = Parameter(name='iZEL23',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZEL23}',
    lhablock = 'IMUELMIX',
    lhacode = [2, 3] )

rZEL31 = Parameter(name='rZEL31',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZEL31}',
    lhablock = 'UELMIX',
    lhacode = [3, 1] )

iZEL31 = Parameter(name='iZEL31',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZEL31}',
    lhablock = 'IMUELMIX',
    lhacode = [3, 1] )

rZEL32 = Parameter(name='rZEL32',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZEL32}',
    lhablock = 'UELMIX',
    lhacode = [3, 2] )

iZEL32 = Parameter(name='iZEL32',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZEL32}',
    lhablock = 'IMUELMIX',
    lhacode = [3, 2] )

rZEL33 = Parameter(name='rZEL33',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZEL33}',
    lhablock = 'UELMIX',
    lhacode = [3, 3] )

iZEL33 = Parameter(name='iZEL33',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZEL33}',
    lhablock = 'IMUELMIX',
    lhacode = [3, 3] )

rZER11 = Parameter(name='rZER11',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZER11}',
    lhablock = 'UERMIX',
    lhacode = [1, 1] )

iZER11 = Parameter(name='iZER11',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZER11}',
    lhablock = 'IMUERMIX',
    lhacode = [1, 1] )

rZER12 = Parameter(name='rZER12',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZER12}',
    lhablock = 'UERMIX',
    lhacode = [1, 2] )

iZER12 = Parameter(name='iZER12',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZER12}',
    lhablock = 'IMUERMIX',
    lhacode = [1, 2] )

rZER13 = Parameter(name='rZER13',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZER13}',
    lhablock = 'UERMIX',
    lhacode = [1, 3] )

iZER13 = Parameter(name='iZER13',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZER13}',
    lhablock = 'IMUERMIX',
    lhacode = [1, 3] )

rZER21 = Parameter(name='rZER21',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZER21}',
    lhablock = 'UERMIX',
    lhacode = [2, 1] )

iZER21 = Parameter(name='iZER21',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZER21}',
    lhablock = 'IMUERMIX',
    lhacode = [2, 1] )

rZER22 = Parameter(name='rZER22',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZER22}',
    lhablock = 'UERMIX',
    lhacode = [2, 2] )

iZER22 = Parameter(name='iZER22',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZER22}',
    lhablock = 'IMUERMIX',
    lhacode = [2, 2] )

rZER23 = Parameter(name='rZER23',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZER23}',
    lhablock = 'UERMIX',
    lhacode = [2, 3] )

iZER23 = Parameter(name='iZER23',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZER23}',
    lhablock = 'IMUERMIX',
    lhacode = [2, 3] )

rZER31 = Parameter(name='rZER31',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZER31}',
    lhablock = 'UERMIX',
    lhacode = [3, 1] )

iZER31 = Parameter(name='iZER31',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZER31}',
    lhablock = 'IMUERMIX',
    lhacode = [3, 1] )

rZER32 = Parameter(name='rZER32',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZER32}',
    lhablock = 'UERMIX',
    lhacode = [3, 2] )

iZER32 = Parameter(name='iZER32',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZER32}',
    lhablock = 'IMUERMIX',
    lhacode = [3, 2] )

rZER33 = Parameter(name='rZER33',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZER33}',
    lhablock = 'UERMIX',
    lhacode = [3, 3] )

iZER33 = Parameter(name='iZER33',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{ZER33}',
    lhablock = 'IMUERMIX',
    lhacode = [3, 3] )

rUV11 = Parameter(name='rUV11',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV11}',
    lhablock = 'UVMIX',
    lhacode = [1, 1] )

iUV11 = Parameter(name='iUV11',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV11}',
    lhablock = 'IMUVMIX',
    lhacode = [1, 1] )

rUV12 = Parameter(name='rUV12',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV12}',
    lhablock = 'UVMIX',
    lhacode = [1, 2] )

iUV12 = Parameter(name='iUV12',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV12}',
    lhablock = 'IMUVMIX',
    lhacode = [1, 2] )

rUV13 = Parameter(name='rUV13',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV13}',
    lhablock = 'UVMIX',
    lhacode = [1, 3] )

iUV13 = Parameter(name='iUV13',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV13}',
    lhablock = 'IMUVMIX',
    lhacode = [1, 3] )

rUV14 = Parameter(name='rUV14',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV14}',
    lhablock = 'UVMIX',
    lhacode = [1, 4] )

iUV14 = Parameter(name='iUV14',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV14}',
    lhablock = 'IMUVMIX',
    lhacode = [1, 4] )

rUV15 = Parameter(name='rUV15',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV15}',
    lhablock = 'UVMIX',
    lhacode = [1, 5] )

iUV15 = Parameter(name='iUV15',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV15}',
    lhablock = 'IMUVMIX',
    lhacode = [1, 5] )

rUV21 = Parameter(name='rUV21',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV21}',
    lhablock = 'UVMIX',
    lhacode = [2, 1] )

iUV21 = Parameter(name='iUV21',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV21}',
    lhablock = 'IMUVMIX',
    lhacode = [2, 1] )

rUV22 = Parameter(name='rUV22',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV22}',
    lhablock = 'UVMIX',
    lhacode = [2, 2] )

iUV22 = Parameter(name='iUV22',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV22}',
    lhablock = 'IMUVMIX',
    lhacode = [2, 2] )

rUV23 = Parameter(name='rUV23',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV23}',
    lhablock = 'UVMIX',
    lhacode = [2, 3] )

iUV23 = Parameter(name='iUV23',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV23}',
    lhablock = 'IMUVMIX',
    lhacode = [2, 3] )

rUV24 = Parameter(name='rUV24',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV24}',
    lhablock = 'UVMIX',
    lhacode = [2, 4] )

iUV24 = Parameter(name='iUV24',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV24}',
    lhablock = 'IMUVMIX',
    lhacode = [2, 4] )

rUV25 = Parameter(name='rUV25',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV25}',
    lhablock = 'UVMIX',
    lhacode = [2, 5] )

iUV25 = Parameter(name='iUV25',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV25}',
    lhablock = 'IMUVMIX',
    lhacode = [2, 5] )

rUV31 = Parameter(name='rUV31',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV31}',
    lhablock = 'UVMIX',
    lhacode = [3, 1] )

iUV31 = Parameter(name='iUV31',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV31}',
    lhablock = 'IMUVMIX',
    lhacode = [3, 1] )

rUV32 = Parameter(name='rUV32',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV32}',
    lhablock = 'UVMIX',
    lhacode = [3, 2] )

iUV32 = Parameter(name='iUV32',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV32}',
    lhablock = 'IMUVMIX',
    lhacode = [3, 2] )

rUV33 = Parameter(name='rUV33',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV33}',
    lhablock = 'UVMIX',
    lhacode = [3, 3] )

iUV33 = Parameter(name='iUV33',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV33}',
    lhablock = 'IMUVMIX',
    lhacode = [3, 3] )

rUV34 = Parameter(name='rUV34',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV34}',
    lhablock = 'UVMIX',
    lhacode = [3, 4] )

iUV34 = Parameter(name='iUV34',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV34}',
    lhablock = 'IMUVMIX',
    lhacode = [3, 4] )

rUV35 = Parameter(name='rUV35',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV35}',
    lhablock = 'UVMIX',
    lhacode = [3, 5] )

iUV35 = Parameter(name='iUV35',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV35}',
    lhablock = 'IMUVMIX',
    lhacode = [3, 5] )

rUV41 = Parameter(name='rUV41',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV41}',
    lhablock = 'UVMIX',
    lhacode = [4, 1] )

iUV41 = Parameter(name='iUV41',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV41}',
    lhablock = 'IMUVMIX',
    lhacode = [4, 1] )

rUV42 = Parameter(name='rUV42',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV42}',
    lhablock = 'UVMIX',
    lhacode = [4, 2] )

iUV42 = Parameter(name='iUV42',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV42}',
    lhablock = 'IMUVMIX',
    lhacode = [4, 2] )

rUV43 = Parameter(name='rUV43',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV43}',
    lhablock = 'UVMIX',
    lhacode = [4, 3] )

iUV43 = Parameter(name='iUV43',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV43}',
    lhablock = 'IMUVMIX',
    lhacode = [4, 3] )

rUV44 = Parameter(name='rUV44',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV44}',
    lhablock = 'UVMIX',
    lhacode = [4, 4] )

iUV44 = Parameter(name='iUV44',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV44}',
    lhablock = 'IMUVMIX',
    lhacode = [4, 4] )

rUV45 = Parameter(name='rUV45',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV45}',
    lhablock = 'UVMIX',
    lhacode = [4, 5] )

iUV45 = Parameter(name='iUV45',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV45}',
    lhablock = 'IMUVMIX',
    lhacode = [4, 5] )

rUV51 = Parameter(name='rUV51',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV51}',
    lhablock = 'UVMIX',
    lhacode = [5, 1] )

iUV51 = Parameter(name='iUV51',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV51}',
    lhablock = 'IMUVMIX',
    lhacode = [5, 1] )

rUV52 = Parameter(name='rUV52',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV52}',
    lhablock = 'UVMIX',
    lhacode = [5, 2] )

iUV52 = Parameter(name='iUV52',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV52}',
    lhablock = 'IMUVMIX',
    lhacode = [5, 2] )

rUV53 = Parameter(name='rUV53',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV53}',
    lhablock = 'UVMIX',
    lhacode = [5, 3] )

iUV53 = Parameter(name='iUV53',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV53}',
    lhablock = 'IMUVMIX',
    lhacode = [5, 3] )

rUV54 = Parameter(name='rUV54',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV54}',
    lhablock = 'UVMIX',
    lhacode = [5, 4] )

iUV54 = Parameter(name='iUV54',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV54}',
    lhablock = 'IMUVMIX',
    lhacode = [5, 4] )

rUV55 = Parameter(name='rUV55',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV55}',
    lhablock = 'UVMIX',
    lhacode = [5, 5] )

iUV55 = Parameter(name='iUV55',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{UV55}',
    lhablock = 'IMUVMIX',
    lhacode = [5, 5] )

aEWM1 = Parameter(name='aEWM1',
    nature = 'external',
    type = 'real',
    value = 137.035999679,
    texname = '\\text{aEWM1}',
    lhablock = 'SMINPUTS',
    lhacode = [1] )

aS = Parameter(name='aS',
    nature = 'external',
    type = 'real',
    value = 0.119,
    texname = '\\text{aS}',
    lhablock = 'SMINPUTS',
    lhacode = [3] )

Gf = Parameter(name='Gf',
    nature = 'external',
    type = 'real',
    value = 0.0000116639,
    texname = 'G_f',
    lhablock = 'SMINPUTS',
    lhacode = [2] )

Yu21 = Parameter(name='Yu21',
    nature = 'internal',
    type = 'complex',
    value = 'rYu21 + complex(0,1)*iYu21',
    texname = 'Y_{u21}' )

Yu31 = Parameter(name='Yu31',
    nature = 'internal',
    type = 'complex',
    value = 'rYu31 + complex(0,1)*iYu31',
    texname = 'Y_{u31}' )

Yu12 = Parameter(name='Yu12',
    nature = 'internal',
    type = 'complex',
    value = 'rYu12 + complex(0,1)*iYu12',
    texname = 'Y_{u12}' )

Yu32 = Parameter(name='Yu32',
    nature = 'internal',
    type = 'complex',
    value = 'rYu32 + complex(0,1)*iYu32',
    texname = 'Y_{u32}' )

Yu13 = Parameter(name='Yu13',
    nature = 'internal',
    type = 'complex',
    value = 'rYu13 + complex(0,1)*iYu13',
    texname = 'Y_{u13}' )

Yu23 = Parameter(name='Yu23',
    nature = 'internal',
    type = 'complex',
    value = 'rYu23 + complex(0,1)*iYu23',
    texname = 'Y_{u23}' )

Yu33 = Parameter(name='Yu33',
    nature = 'internal',
    type = 'complex',
    value = 'rYu33 + complex(0,1)*iYu33',
    texname = 'Y_{u33}' )

YvD21 = Parameter(name='YvD21',
    nature = 'internal',
    type = 'complex',
    value = 'rYvD21 + complex(0,1)*iYvD21',
    texname = 'Y^D_{\\nu21}' )

YvD31 = Parameter(name='YvD31',
    nature = 'internal',
    type = 'complex',
    value = 'rYvD31 + complex(0,1)*iYvD31',
    texname = 'Y^D_{\\nu31}' )

YvM11 = Parameter(name='YvM11',
    nature = 'internal',
    type = 'complex',
    value = 'rYvM11 + complex(0,1)*iYvM11',
    texname = 'Y^M_{\\nu11}' )

YvD12 = Parameter(name='YvD12',
    nature = 'internal',
    type = 'complex',
    value = 'rYvD12 + complex(0,1)*iYvD12',
    texname = 'Y^D_{\\nu12}' )

YvD32 = Parameter(name='YvD32',
    nature = 'internal',
    type = 'complex',
    value = 'rYvD32 + complex(0,1)*iYvD32',
    texname = 'Y^D_{\\nu32}' )

YvM22 = Parameter(name='YvM22',
    nature = 'internal',
    type = 'complex',
    value = 'rYvM22 + complex(0,1)*iYvM22',
    texname = 'Y^M_{\\nu22}' )

Yd31 = Parameter(name='Yd31',
    nature = 'internal',
    type = 'complex',
    value = 'rYd31 + complex(0,1)*iYd31',
    texname = 'Y_{d31}' )

Yd13 = Parameter(name='Yd13',
    nature = 'internal',
    type = 'complex',
    value = 'rYd13 + complex(0,1)*iYd13',
    texname = 'Y_{d13}' )

Ye31 = Parameter(name='Ye31',
    nature = 'internal',
    type = 'complex',
    value = 'rYe31 + complex(0,1)*iYe31',
    texname = 'Y_{e31}' )

Ye13 = Parameter(name='Ye13',
    nature = 'internal',
    type = 'complex',
    value = 'rYe13 + complex(0,1)*iYe13',
    texname = 'Y_{e13}' )

Kappa = Parameter(name='Kappa',
    nature = 'internal',
    type = 'complex',
    value = 'rKappa + complex(0,1)*iKappa',
    texname = '\\kappa' )

Yd32 = Parameter(name='Yd32',
    nature = 'internal',
    type = 'complex',
    value = 'rYd32 + complex(0,1)*iYd32',
    texname = 'Y_{d32}' )

Yd23 = Parameter(name='Yd23',
    nature = 'internal',
    type = 'complex',
    value = 'rYd23 + complex(0,1)*iYd23',
    texname = 'Y_{d23}' )

Ye32 = Parameter(name='Ye32',
    nature = 'internal',
    type = 'complex',
    value = 'rYe32 + complex(0,1)*iYe32',
    texname = 'Y_{e32}' )

Ye23 = Parameter(name='Ye23',
    nature = 'internal',
    type = 'complex',
    value = 'rYe23 + complex(0,1)*iYe23',
    texname = 'Y_{e23}' )

Yd21 = Parameter(name='Yd21',
    nature = 'internal',
    type = 'complex',
    value = 'rYd21 + complex(0,1)*iYd21',
    texname = 'Y_{d21}' )

Yd12 = Parameter(name='Yd12',
    nature = 'internal',
    type = 'complex',
    value = 'rYd12 + complex(0,1)*iYd12',
    texname = 'Y_{d12}' )

Yd33 = Parameter(name='Yd33',
    nature = 'internal',
    type = 'complex',
    value = 'rYd33 + complex(0,1)*iYd33',
    texname = 'Y_{d33}' )

Ye21 = Parameter(name='Ye21',
    nature = 'internal',
    type = 'complex',
    value = 'rYe21 + complex(0,1)*iYe21',
    texname = 'Y_{e21}' )

Ye12 = Parameter(name='Ye12',
    nature = 'internal',
    type = 'complex',
    value = 'rYe12 + complex(0,1)*iYe12',
    texname = 'Y_{e12}' )

Ye33 = Parameter(name='Ye33',
    nature = 'internal',
    type = 'complex',
    value = 'rYe33 + complex(0,1)*iYe33',
    texname = 'Y_{e33}' )

L10 = Parameter(name='L10',
    nature = 'internal',
    type = 'complex',
    value = 'rL10 + complex(0,1)*iL10',
    texname = '\\lambda_{10}' )

Lchi = Parameter(name='Lchi',
    nature = 'internal',
    type = 'complex',
    value = 'rLchi + complex(0,1)*iLchi',
    texname = '\\lambda_{\\chi}' )

L7 = Parameter(name='L7',
    nature = 'internal',
    type = 'complex',
    value = 'rL7 + complex(0,1)*iL7',
    texname = '\\lambda_7' )

L1 = Parameter(name='L1',
    nature = 'internal',
    type = 'complex',
    value = 'rL1 + complex(0,1)*iL1',
    texname = '\\lambda_1' )

L4p = Parameter(name='L4p',
    nature = 'internal',
    type = 'complex',
    value = 'rL4p + complex(0,1)*iL4p',
    texname = '\\lambda^{\\prime}_4' )

L5p = Parameter(name='L5p',
    nature = 'internal',
    type = 'complex',
    value = 'rL5p + complex(0,1)*iL5p',
    texname = '\\lambda^{\\prime}_5' )

L4pp = Parameter(name='L4pp',
    nature = 'internal',
    type = 'complex',
    value = 'rL4pp + complex(0,1)*iL4pp',
    texname = '\\lambda^{\\prime \\prime}_4' )

L5pp = Parameter(name='L5pp',
    nature = 'internal',
    type = 'complex',
    value = 'rL5pp + complex(0,1)*iL5pp',
    texname = '\\lambda^{\\prime \\prime}_5' )

L8 = Parameter(name='L8',
    nature = 'internal',
    type = 'complex',
    value = 'rL8 + complex(0,1)*iL8',
    texname = '\\lambda_8' )

L2 = Parameter(name='L2',
    nature = 'internal',
    type = 'complex',
    value = 'rL2 + complex(0,1)*iL2',
    texname = '\\lambda_2' )

L6p = Parameter(name='L6p',
    nature = 'internal',
    type = 'complex',
    value = 'rL6p + complex(0,1)*iL6p',
    texname = '\\lambda^{\\prime}_6' )

L6pp = Parameter(name='L6pp',
    nature = 'internal',
    type = 'complex',
    value = 'rL6pp + complex(0,1)*iL6pp',
    texname = '\\lambda^{\\prime \\prime}_6' )

L9 = Parameter(name='L9',
    nature = 'internal',
    type = 'complex',
    value = 'rL9 + complex(0,1)*iL9',
    texname = '\\lambda_9' )

L3 = Parameter(name='L3',
    nature = 'internal',
    type = 'complex',
    value = 'rL3 + complex(0,1)*iL3',
    texname = '\\lambda_3' )

ZDL11 = Parameter(name='ZDL11',
    nature = 'internal',
    type = 'complex',
    value = 'rZDL11 + complex(0,1)*iZDL11',
    texname = '\\text{ZDL11}' )

ZDL12 = Parameter(name='ZDL12',
    nature = 'internal',
    type = 'complex',
    value = 'rZDL12 + complex(0,1)*iZDL12',
    texname = '\\text{ZDL12}' )

ZDL13 = Parameter(name='ZDL13',
    nature = 'internal',
    type = 'complex',
    value = 'rZDL13 + complex(0,1)*iZDL13',
    texname = '\\text{ZDL13}' )

ZDL21 = Parameter(name='ZDL21',
    nature = 'internal',
    type = 'complex',
    value = 'rZDL21 + complex(0,1)*iZDL21',
    texname = '\\text{ZDL21}' )

ZDL22 = Parameter(name='ZDL22',
    nature = 'internal',
    type = 'complex',
    value = 'rZDL22 + complex(0,1)*iZDL22',
    texname = '\\text{ZDL22}' )

ZDL23 = Parameter(name='ZDL23',
    nature = 'internal',
    type = 'complex',
    value = 'rZDL23 + complex(0,1)*iZDL23',
    texname = '\\text{ZDL23}' )

ZDL31 = Parameter(name='ZDL31',
    nature = 'internal',
    type = 'complex',
    value = 'rZDL31 + complex(0,1)*iZDL31',
    texname = '\\text{ZDL31}' )

ZDL32 = Parameter(name='ZDL32',
    nature = 'internal',
    type = 'complex',
    value = 'rZDL32 + complex(0,1)*iZDL32',
    texname = '\\text{ZDL32}' )

ZDL33 = Parameter(name='ZDL33',
    nature = 'internal',
    type = 'complex',
    value = 'rZDL33 + complex(0,1)*iZDL33',
    texname = '\\text{ZDL33}' )

ZDR11 = Parameter(name='ZDR11',
    nature = 'internal',
    type = 'complex',
    value = 'rZDR11 + complex(0,1)*iZDR11',
    texname = '\\text{ZDR11}' )

ZDR12 = Parameter(name='ZDR12',
    nature = 'internal',
    type = 'complex',
    value = 'rZDR12 + complex(0,1)*iZDR12',
    texname = '\\text{ZDR12}' )

ZDR13 = Parameter(name='ZDR13',
    nature = 'internal',
    type = 'complex',
    value = 'rZDR13 + complex(0,1)*iZDR13',
    texname = '\\text{ZDR13}' )

ZDR21 = Parameter(name='ZDR21',
    nature = 'internal',
    type = 'complex',
    value = 'rZDR21 + complex(0,1)*iZDR21',
    texname = '\\text{ZDR21}' )

ZDR22 = Parameter(name='ZDR22',
    nature = 'internal',
    type = 'complex',
    value = 'rZDR22 + complex(0,1)*iZDR22',
    texname = '\\text{ZDR22}' )

ZDR23 = Parameter(name='ZDR23',
    nature = 'internal',
    type = 'complex',
    value = 'rZDR23 + complex(0,1)*iZDR23',
    texname = '\\text{ZDR23}' )

ZDR31 = Parameter(name='ZDR31',
    nature = 'internal',
    type = 'complex',
    value = 'rZDR31 + complex(0,1)*iZDR31',
    texname = '\\text{ZDR31}' )

ZDR32 = Parameter(name='ZDR32',
    nature = 'internal',
    type = 'complex',
    value = 'rZDR32 + complex(0,1)*iZDR32',
    texname = '\\text{ZDR32}' )

ZDR33 = Parameter(name='ZDR33',
    nature = 'internal',
    type = 'complex',
    value = 'rZDR33 + complex(0,1)*iZDR33',
    texname = '\\text{ZDR33}' )

ZUL11 = Parameter(name='ZUL11',
    nature = 'internal',
    type = 'complex',
    value = 'rZUL11 + complex(0,1)*iZUL11',
    texname = '\\text{ZUL11}' )

ZUL12 = Parameter(name='ZUL12',
    nature = 'internal',
    type = 'complex',
    value = 'rZUL12 + complex(0,1)*iZUL12',
    texname = '\\text{ZUL12}' )

ZUL13 = Parameter(name='ZUL13',
    nature = 'internal',
    type = 'complex',
    value = 'rZUL13 + complex(0,1)*iZUL13',
    texname = '\\text{ZUL13}' )

ZUL21 = Parameter(name='ZUL21',
    nature = 'internal',
    type = 'complex',
    value = 'rZUL21 + complex(0,1)*iZUL21',
    texname = '\\text{ZUL21}' )

ZUL22 = Parameter(name='ZUL22',
    nature = 'internal',
    type = 'complex',
    value = 'rZUL22 + complex(0,1)*iZUL22',
    texname = '\\text{ZUL22}' )

ZUL23 = Parameter(name='ZUL23',
    nature = 'internal',
    type = 'complex',
    value = 'rZUL23 + complex(0,1)*iZUL23',
    texname = '\\text{ZUL23}' )

ZUL31 = Parameter(name='ZUL31',
    nature = 'internal',
    type = 'complex',
    value = 'rZUL31 + complex(0,1)*iZUL31',
    texname = '\\text{ZUL31}' )

ZUL32 = Parameter(name='ZUL32',
    nature = 'internal',
    type = 'complex',
    value = 'rZUL32 + complex(0,1)*iZUL32',
    texname = '\\text{ZUL32}' )

ZUL33 = Parameter(name='ZUL33',
    nature = 'internal',
    type = 'complex',
    value = 'rZUL33 + complex(0,1)*iZUL33',
    texname = '\\text{ZUL33}' )

ZUR11 = Parameter(name='ZUR11',
    nature = 'internal',
    type = 'complex',
    value = 'rZUR11 + complex(0,1)*iZUR11',
    texname = '\\text{ZUR11}' )

ZUR12 = Parameter(name='ZUR12',
    nature = 'internal',
    type = 'complex',
    value = 'rZUR12 + complex(0,1)*iZUR12',
    texname = '\\text{ZUR12}' )

ZUR13 = Parameter(name='ZUR13',
    nature = 'internal',
    type = 'complex',
    value = 'rZUR13 + complex(0,1)*iZUR13',
    texname = '\\text{ZUR13}' )

ZUR21 = Parameter(name='ZUR21',
    nature = 'internal',
    type = 'complex',
    value = 'rZUR21 + complex(0,1)*iZUR21',
    texname = '\\text{ZUR21}' )

ZUR22 = Parameter(name='ZUR22',
    nature = 'internal',
    type = 'complex',
    value = 'rZUR22 + complex(0,1)*iZUR22',
    texname = '\\text{ZUR22}' )

ZUR23 = Parameter(name='ZUR23',
    nature = 'internal',
    type = 'complex',
    value = 'rZUR23 + complex(0,1)*iZUR23',
    texname = '\\text{ZUR23}' )

ZUR31 = Parameter(name='ZUR31',
    nature = 'internal',
    type = 'complex',
    value = 'rZUR31 + complex(0,1)*iZUR31',
    texname = '\\text{ZUR31}' )

ZUR32 = Parameter(name='ZUR32',
    nature = 'internal',
    type = 'complex',
    value = 'rZUR32 + complex(0,1)*iZUR32',
    texname = '\\text{ZUR32}' )

ZUR33 = Parameter(name='ZUR33',
    nature = 'internal',
    type = 'complex',
    value = 'rZUR33 + complex(0,1)*iZUR33',
    texname = '\\text{ZUR33}' )

ZEL11 = Parameter(name='ZEL11',
    nature = 'internal',
    type = 'complex',
    value = 'rZEL11 + complex(0,1)*iZEL11',
    texname = '\\text{ZEL11}' )

ZEL12 = Parameter(name='ZEL12',
    nature = 'internal',
    type = 'complex',
    value = 'rZEL12 + complex(0,1)*iZEL12',
    texname = '\\text{ZEL12}' )

ZEL13 = Parameter(name='ZEL13',
    nature = 'internal',
    type = 'complex',
    value = 'rZEL13 + complex(0,1)*iZEL13',
    texname = '\\text{ZEL13}' )

ZEL21 = Parameter(name='ZEL21',
    nature = 'internal',
    type = 'complex',
    value = 'rZEL21 + complex(0,1)*iZEL21',
    texname = '\\text{ZEL21}' )

ZEL22 = Parameter(name='ZEL22',
    nature = 'internal',
    type = 'complex',
    value = 'rZEL22 + complex(0,1)*iZEL22',
    texname = '\\text{ZEL22}' )

ZEL23 = Parameter(name='ZEL23',
    nature = 'internal',
    type = 'complex',
    value = 'rZEL23 + complex(0,1)*iZEL23',
    texname = '\\text{ZEL23}' )

ZEL31 = Parameter(name='ZEL31',
    nature = 'internal',
    type = 'complex',
    value = 'rZEL31 + complex(0,1)*iZEL31',
    texname = '\\text{ZEL31}' )

ZEL32 = Parameter(name='ZEL32',
    nature = 'internal',
    type = 'complex',
    value = 'rZEL32 + complex(0,1)*iZEL32',
    texname = '\\text{ZEL32}' )

ZEL33 = Parameter(name='ZEL33',
    nature = 'internal',
    type = 'complex',
    value = 'rZEL33 + complex(0,1)*iZEL33',
    texname = '\\text{ZEL33}' )

ZER11 = Parameter(name='ZER11',
    nature = 'internal',
    type = 'complex',
    value = 'rZER11 + complex(0,1)*iZER11',
    texname = '\\text{ZER11}' )

ZER12 = Parameter(name='ZER12',
    nature = 'internal',
    type = 'complex',
    value = 'rZER12 + complex(0,1)*iZER12',
    texname = '\\text{ZER12}' )

ZER13 = Parameter(name='ZER13',
    nature = 'internal',
    type = 'complex',
    value = 'rZER13 + complex(0,1)*iZER13',
    texname = '\\text{ZER13}' )

ZER21 = Parameter(name='ZER21',
    nature = 'internal',
    type = 'complex',
    value = 'rZER21 + complex(0,1)*iZER21',
    texname = '\\text{ZER21}' )

ZER22 = Parameter(name='ZER22',
    nature = 'internal',
    type = 'complex',
    value = 'rZER22 + complex(0,1)*iZER22',
    texname = '\\text{ZER22}' )

ZER23 = Parameter(name='ZER23',
    nature = 'internal',
    type = 'complex',
    value = 'rZER23 + complex(0,1)*iZER23',
    texname = '\\text{ZER23}' )

ZER31 = Parameter(name='ZER31',
    nature = 'internal',
    type = 'complex',
    value = 'rZER31 + complex(0,1)*iZER31',
    texname = '\\text{ZER31}' )

ZER32 = Parameter(name='ZER32',
    nature = 'internal',
    type = 'complex',
    value = 'rZER32 + complex(0,1)*iZER32',
    texname = '\\text{ZER32}' )

ZER33 = Parameter(name='ZER33',
    nature = 'internal',
    type = 'complex',
    value = 'rZER33 + complex(0,1)*iZER33',
    texname = '\\text{ZER33}' )

UV11 = Parameter(name='UV11',
    nature = 'internal',
    type = 'complex',
    value = 'rUV11 + complex(0,1)*iUV11',
    texname = '\\text{UV11}' )

UV12 = Parameter(name='UV12',
    nature = 'internal',
    type = 'complex',
    value = 'rUV12 + complex(0,1)*iUV12',
    texname = '\\text{UV12}' )

UV13 = Parameter(name='UV13',
    nature = 'internal',
    type = 'complex',
    value = 'rUV13 + complex(0,1)*iUV13',
    texname = '\\text{UV13}' )

UV14 = Parameter(name='UV14',
    nature = 'internal',
    type = 'complex',
    value = 'rUV14 + complex(0,1)*iUV14',
    texname = '\\text{UV14}' )

UV15 = Parameter(name='UV15',
    nature = 'internal',
    type = 'complex',
    value = 'rUV15 + complex(0,1)*iUV15',
    texname = '\\text{UV15}' )

UV21 = Parameter(name='UV21',
    nature = 'internal',
    type = 'complex',
    value = 'rUV21 + complex(0,1)*iUV21',
    texname = '\\text{UV21}' )

UV22 = Parameter(name='UV22',
    nature = 'internal',
    type = 'complex',
    value = 'rUV22 + complex(0,1)*iUV22',
    texname = '\\text{UV22}' )

UV23 = Parameter(name='UV23',
    nature = 'internal',
    type = 'complex',
    value = 'rUV23 + complex(0,1)*iUV23',
    texname = '\\text{UV23}' )

UV24 = Parameter(name='UV24',
    nature = 'internal',
    type = 'complex',
    value = 'rUV24 + complex(0,1)*iUV24',
    texname = '\\text{UV24}' )

UV25 = Parameter(name='UV25',
    nature = 'internal',
    type = 'complex',
    value = 'rUV25 + complex(0,1)*iUV25',
    texname = '\\text{UV25}' )

UV31 = Parameter(name='UV31',
    nature = 'internal',
    type = 'complex',
    value = 'rUV31 + complex(0,1)*iUV31',
    texname = '\\text{UV31}' )

UV32 = Parameter(name='UV32',
    nature = 'internal',
    type = 'complex',
    value = 'rUV32 + complex(0,1)*iUV32',
    texname = '\\text{UV32}' )

UV33 = Parameter(name='UV33',
    nature = 'internal',
    type = 'complex',
    value = 'rUV33 + complex(0,1)*iUV33',
    texname = '\\text{UV33}' )

UV34 = Parameter(name='UV34',
    nature = 'internal',
    type = 'complex',
    value = 'rUV34 + complex(0,1)*iUV34',
    texname = '\\text{UV34}' )

UV35 = Parameter(name='UV35',
    nature = 'internal',
    type = 'complex',
    value = 'rUV35 + complex(0,1)*iUV35',
    texname = '\\text{UV35}' )

UV41 = Parameter(name='UV41',
    nature = 'internal',
    type = 'complex',
    value = 'rUV41 + complex(0,1)*iUV41',
    texname = '\\text{UV41}' )

UV42 = Parameter(name='UV42',
    nature = 'internal',
    type = 'complex',
    value = 'rUV42 + complex(0,1)*iUV42',
    texname = '\\text{UV42}' )

UV43 = Parameter(name='UV43',
    nature = 'internal',
    type = 'complex',
    value = 'rUV43 + complex(0,1)*iUV43',
    texname = '\\text{UV43}' )

UV44 = Parameter(name='UV44',
    nature = 'internal',
    type = 'complex',
    value = 'rUV44 + complex(0,1)*iUV44',
    texname = '\\text{UV44}' )

UV45 = Parameter(name='UV45',
    nature = 'internal',
    type = 'complex',
    value = 'rUV45 + complex(0,1)*iUV45',
    texname = '\\text{UV45}' )

UV51 = Parameter(name='UV51',
    nature = 'internal',
    type = 'complex',
    value = 'rUV51 + complex(0,1)*iUV51',
    texname = '\\text{UV51}' )

UV52 = Parameter(name='UV52',
    nature = 'internal',
    type = 'complex',
    value = 'rUV52 + complex(0,1)*iUV52',
    texname = '\\text{UV52}' )

UV53 = Parameter(name='UV53',
    nature = 'internal',
    type = 'complex',
    value = 'rUV53 + complex(0,1)*iUV53',
    texname = '\\text{UV53}' )

UV54 = Parameter(name='UV54',
    nature = 'internal',
    type = 'complex',
    value = 'rUV54 + complex(0,1)*iUV54',
    texname = '\\text{UV54}' )

UV55 = Parameter(name='UV55',
    nature = 'internal',
    type = 'complex',
    value = 'rUV55 + complex(0,1)*iUV55',
    texname = '\\text{UV55}' )

G = Parameter(name='G',
    nature = 'internal',
    type = 'real',
    value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
    texname = 'g_3')

gFY = Parameter(name='gFY',
    nature = 'internal',
    type = 'real',
    value = '0',
    texname = '\\text{gFY}')

el = Parameter(name='el',
    nature = 'internal',
    type = 'real',
    value = '2*cmath.sqrt(1/aEWM1)*cmath.sqrt(cmath.pi)',
    texname = '\\text{el}')

TWp = Parameter(name='TWp',
    nature = 'internal',
    type = 'real',
    value = '0',
    texname = '\\text{TWp}')

MWm = Parameter(name='MWm',
    nature = 'internal',
    type = 'real',
    value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (MZ**2*cmath.pi)/(cmath.sqrt(2)*aEWM1*Gf)))',
    texname = '\\text{MWm}')

TW = Parameter(name='TW',
    nature = 'internal',
    type = 'real',
    value = 'cmath.asin(cmath.sqrt(1 - MWm**2/MZ**2))',
    texname = '\\text{TW}')

g1 = Parameter(name='g1',
    nature = 'internal',
    type = 'real',
    value = 'el*1./cmath.cos(TW)',
    texname = 'g_1')

g2 = Parameter(name='g2',
    nature = 'internal',
    type = 'real',
    value = 'el*1./cmath.sin(TW)',
    texname = 'g_2')

RXiWm = Parameter(name='RXiWm',
    nature = 'internal',
    type = 'real',
    value = '1.',
    texname = '\\xi_{W^-}')

MHpm3 = Parameter(name = 'MHpm3',
    nature = 'internal',
    type = 'real',
    value = 'MWm*RXiWm',
    texname = 'M_{{H^+}_3}')

MgWm = Parameter(name = 'MgWm',
    nature = 'internal',
    type = 'real',
    value = 'MWm*RXiWm',
    texname = 'M_{\\eta^-}')

MgWpC = Parameter(name = 'MgWpC',
    nature = 'internal',
    type = 'real',
    value = 'MWm*RXiWm',
    texname = 'M_{\\eta^+}')

RXiZ = Parameter(name='RXiZ',
    nature = 'internal',
    type = 'real',
    value = '1.',
    texname = '\\xi_{Z}')

MAh3 = Parameter(name = 'MAh3',
    nature = 'internal',
    type = 'real',
    value = 'MZ*RXiZ',
    texname = 'M_{{A_h}_3}')

MgZ = Parameter(name = 'MgZ',
    nature = 'internal',
    type = 'real',
    value = 'MZ*RXiZ',
    texname = 'M_{\\eta^Z}')

RXiZp = Parameter(name='RXiZp',
    nature = 'internal',
    type = 'real',
    value = '1.',
    texname = '\\xi_{{Z^{\\prime}}}')

MAh4 = Parameter(name = 'MAh4',
    nature = 'internal',
    type = 'real',
    value = 'MZp*RXiZp',
    texname = 'M_{{A_h}_4}')

HPP1 = Parameter(name='HPP1',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{HPP1}',
    lhablock = 'EFFHIGGSCOUPLINGS',
    lhacode = [25,22,22] )

HGG1 = Parameter(name='HGG1',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{HGG1}',
    lhablock = 'EFFHIGGSCOUPLINGS',
    lhacode = [25,21,21] )

HPP2 = Parameter(name='HPP2',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{HPP2}',
    lhablock = 'EFFHIGGSCOUPLINGS',
    lhacode = [35,22,22] )

HGG2 = Parameter(name='HGG2',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{HGG2}',
    lhablock = 'EFFHIGGSCOUPLINGS',
    lhacode = [35,21,21] )

HPP3 = Parameter(name='HPP3',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{HPP3}',
    lhablock = 'EFFHIGGSCOUPLINGS',
    lhacode = [36,22,22] )

HGG3 = Parameter(name='HGG3',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{HGG3}',
    lhablock = 'EFFHIGGSCOUPLINGS',
    lhacode = [36,21,21] )

HPP4 = Parameter(name='HPP4',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{HPP4}',
    lhablock = 'EFFHIGGSCOUPLINGS',
    lhacode = [55,22,22] )

HGG4 = Parameter(name='HGG4',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{HGG4}',
    lhablock = 'EFFHIGGSCOUPLINGS',
    lhacode = [55,21,21] )

APP1 = Parameter(name='APP1',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{APP1}',
    lhablock = 'EFFHIGGSCOUPLINGS',
    lhacode = [45,22,22] )

AGG1 = Parameter(name='AGG1',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{AGG1}',
    lhablock = 'EFFHIGGSCOUPLINGS',
    lhacode = [45,21,21] )

APP2 = Parameter(name='APP2',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{APP2}',
    lhablock = 'EFFHIGGSCOUPLINGS',
    lhacode = [46,22,22] )

AGG2 = Parameter(name='AGG2',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{AGG2}',
    lhablock = 'EFFHIGGSCOUPLINGS',
    lhacode = [46,21,21] )

APP3 = Parameter(name='APP3',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{APP3}',
    lhablock = 'EFFHIGGSCOUPLINGS',
    lhacode = [56,22,22] )

AGG3 = Parameter(name='AGG3',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{AGG3}',
    lhablock = 'EFFHIGGSCOUPLINGS',
    lhacode = [56,21,21] )

APP4 = Parameter(name='APP4',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{APP4}',
    lhablock = 'EFFHIGGSCOUPLINGS',
    lhacode = [66,22,22] )

AGG4 = Parameter(name='AGG4',
    nature = 'external',
    type = 'real',
    value = 0.,
    texname = '\\text{AGG4}',
    lhablock = 'EFFHIGGSCOUPLINGS',
    lhacode = [66,21,21] )

