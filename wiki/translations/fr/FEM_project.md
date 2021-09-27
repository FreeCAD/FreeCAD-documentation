# FEM project/fr
**
Ce plan de développement est probablement obsolète. Pour plus d'informations, voir [Plan de développement](Development_roadmap/fr.md).<br>
Si vous n'êtes pas impliqué dans le développement discuté ici :<br>
!!! S'IL VOUS PLAÎT, NE MODIFIEZ PAS ET NE TRADUISEZ PAS !!!
**


{{TOCright}}

Ceci, est le plan du projet d\'intégration de **FreeCAD FEM**, dans le cadre de [la feuille de route de développement](Development_roadmap.md).

## Unités

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

## Pense bête 

### Mailleur Potentiel 

<img alt="" src=images/Netgen.jpg  style="width:600px;">

Voir [Mesh](FEM_Mesh/fr.md)

### Solveur potentiel 

Voir [Solveur](FEM_Solver/fr.md)


{{FEM Tools navi

}}  

_

---
[documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > FEM project/fr
