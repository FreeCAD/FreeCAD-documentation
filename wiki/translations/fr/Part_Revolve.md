---
- GuiCommand:/fr
   Name:Part_Revolve
   Name/fr:Part Révolution
   MenuLocation:Pièce → Révolution...
   Workbenches:[Part](Part_Workbench/fr.md)
---

# Part Revolve/fr

## Description

Fait pivoter l\'objet sélectionné autour d\'un axe donné. Les types de forme suivants sont autorisés et mènent aux formes de sortie énumérées :

  Objet en entrée,   Objet résultant
   
  Sommet             Arête
  Arête              Face
  Filaire            Enveloppe
  Face               Solide
  Enveloppe          Solide Composé (Compsolid)

Une [esquisse](Sketcher_Workbench/fr.md) peut également être utilisée. Les solides ou les solides composés ne sont pas autorisés comme formes de départ. Les composés normaux ne sont actuellement pas autorisés non plus.

![](images/Dialog-revolve.png )

L\'argument Angle spécifie l\'angle selon lequel l\'objet doit être tourné. Les coordonnées déplacent l\'origine de l\'axe de rotation, par rapport à l\'axe d\'origine du système de coordonnées.

Si vous sélectionnez un axe défini par l\'utilisateur, les nombres définissent la direction de l\'axe de rotation par rapport au système de coordonnées d\'origine: Si la coordonnée Z est 0 et les coordonnées Y et X ne sont pas nulles, alors l\'axe se trouvera dans le Plan X-Y. Son angle est tel que sa tangente est le rapport entre les coordonnées X et Y.

## Remarques

-   Si l\'objet à faire pivoter coupe l\'axe de rotation, l\'opération échouera dans la plupart des cas.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Revolve/fr
