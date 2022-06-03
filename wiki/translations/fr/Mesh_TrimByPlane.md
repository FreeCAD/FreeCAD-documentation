---
- GuiCommand   */fr
   Name   *Mesh TrimByPlane
   Name/fr   *Mesh Ajuster par plan
   MenuLocation   *Maillages → Cutting → Ajuster le maillage avec un plan
   Workbenches   *[Mesh](Mesh_Workbench/fr.md)
   SeeAlso   *[Mesh Couper le maillage](Mesh_PolyCut/fr.md), [Mesh Découper](Mesh_PolyTrim/fr.md)
---

# Mesh TrimByPlane/fr

## Description

La commande **Mesh Ajuster par plan** permet de découper les faces et parties de faces d\'un côté d\'un plan à partir d\'un objet maillé.

## Utilisation

1.  Sélectionnez un seul objet maillé et un seul [Part Plan](Part_Plane/fr.md). Le plan (étendu) doit croiser l\'objet maillé.

2.  Il existe plusieurs façons d\'appeler la commande   *
    -   Appuyez sur le bouton **<img src="images/Mesh_TrimByPlane.svg" width=16px> [Ajuster le maillage avec un plan](Mesh_TrimByPlane/fr.md)
**
    -   Sélectionnez l\'option **Maillages → Cutting → <img src="images/Mesh_TrimByPlane.svg" width=16px> Ajuster le maillage avec un plan** dans le menu.

3.  La boîte de dialogue **Découper par un plan** s\'ouvre.

4.  
    **Sélectionner le côté que vous souhaitez garder**en appuyant sur l\'un des boutons   *

    -   
        {{button|En-dessous}}
        

    -   
        {{button|Au-dessus}}
        

    -   
        {{button|Scinder}}
        
           * supprime les faces et les parties de faces au-dessus du plan, et crée un nouvel objet maillé les contenant.





{{Mesh Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh TrimByPlane/fr
