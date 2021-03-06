# FEM project/cs
**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**


{{TOCright}}

Toto je projekt postupu pro FEM integraci FreeCADu jako části [Směru vývoje](Development_roadmap.md).

## Units

  Length   Time   Mass             Force            Pressure           Velocity   Density      Energy    Gravity
          
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

### Potential meshers 

<img alt="" src=images/Netgen.jpg  style="width:600px;">

See [FEM Mesh](FEM_Mesh.md)

### Potential solvers 

See [FEM Solver](FEM_Solver.md)


{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > [FEM](Category_FEM.md) > FEM project/cs
