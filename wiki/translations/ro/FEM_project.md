# FEM project/ro
Acesta este planul proiectului pentru integrarea MEF FreeCAD ca parte a foii de parcurs [Development roadmap](Development_roadmap.md).

## Unități de măsură 

  Length   Time   Mass             Force            Pressure           Velocity   Density      Energy    Gravity
  -------- ------ ---------------- ---------------- ------------------ ---------- ------------ --------- ---------
  m        s      kg               kg m/s2          N/m2               m/s        kg/m3        kgm2/s2   9.81
  m        s      kg               N                Pa                 m/s        m kg/l       J         9.81
  m        s      g                mN               mPa                m/s        micro kg/l   mJ        9.81
  m        s      Mg (ton)         kN               kPa                m/s        kg/l         kJ        9.81
  m        ms     kg               MN               MPa                km/s       m kg/l       MJ        9.81e-6
  m        ms     g                kN               kPa                km/s       micro kg/l   kJ        9.81e-6
  m        ms     Mg (ton)         GN               GPa                km/s       kg/l         GJ        9.81e-6
  mm       s      kg               mN               kPa                mm/s       M kg/l       micro J   9.81e+3
  mm       s      g                micro N          Pa                 mm/s       g/mm3        nJ        9.81e+3
  mm       s      Mg (ton)         N                MPa                mm/s       Mg/mm3       mJ        9.81e+3
  mm       ms     kg               kN               GPa                m/s        M            kg/l J    9.81e-3
  mm       ms     g                N                MPa                m/s        k kg/l       mJ        9.81e-3
  mm       ms     Mg (ton)         MN               TPa                m/s        G kg/l       kJ        9.81e-3
  cm       ms     g                daN              10\^5 Pa (bar)     dam/s      kg/l         dJ        9.81e-4
  cm       ms     kg               10\^4 N (kdaN)   10\^8 Pa (kbar)    dam/s      k kg/l       hJ        9.81e-4
  cm       ms     Mg (ton) 10\^7   N(MdaN)          10\^11 Pa (Mbar)   dam/s      M kg/l       10\^5 J   9.81e-4

  : **Units**

## Brainstorming


<div class="mw-translate-fuzzy">

### Potențialul ochiurilor de Plasă 

<img alt="" src=images/Netgen.jpg  style="width:300px;">


</div>


<div class="mw-translate-fuzzy">

Câteva administratori de ochiuri de plasă:

-   [Netgen](http://www.hpfem.jku.at/netgen/) administrator de plase foarte bun, cu bibliotecă suport LGPL
-   [Salome](http://www.salome-platform.org/) pachet complicat, e așa greu pentru a obține codul de care avem nevoie!?
-   [PythonOCC](http://www.pythonocc.org/) Biblioteca Python, care oferă și o interfață (în prezent) aproximativ ca Code-Aster, ar fi o modalitate rapidă și ușoară de a obține o primă soluție de lucru.


</div>


<div class="mw-translate-fuzzy">

### Rezolvitori Potențial 

unii solver sunt

-   [Calculix](http://www.calculix.de/) software open source, program tridimensional, structurat pe metoda elementuluir finit (MEF)
-   [Code-Aster](http://www.code-aster.org) un solver scris preponderent în Python
-   [PythonOCC](http://www.pythonocc.org/) arhitectură python, care oferă, de asemenea, o interfață (în prezent) aproximativ ca Code\_Aster, care ar fi, de asemenea, o cale simplă și rapidă către o primă soluție de lucru


</div>


{{FEM Tools navi

}}  

[Category:Roadmap](Category:Roadmap.md)

---
[documentation index](../README.md) > [Roadmap](Category:Roadmap.md) > FEM project/ro
