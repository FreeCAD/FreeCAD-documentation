---
- GuiCommand:
   Name:Part_Revolve
   Name/fr:Part Révolution
   MenuLocation:Part → Révolution...
   Workbenches:[Part](Part_Workbench/fr.md)
---

# Part Revolve/fr

## Description

Fait pivoter l\'objet sélectionné autour d\'un axe donné. Les formes initiales suivantes sont autorisées et amènent aux formes de sortie énumérées :

  Objet initial   Objet résultant
   
  Sommet          Arête
  Arête           Face
  Polyligne       Enveloppe
  Face            Solide
  Coque           Solide composé (Compsolid)

Une [esquisse](Sketcher_Workbench/fr.md) peut également être utilisée. Les solides ou les solides composés ne sont pas autorisés comme formes de départ. Les composés normaux ne sont actuellement pas autorisés non plus.

![](images/Dialog-revolve.png )

L\'argument Angle précise de combien l\'objet doit être tourné. Les coordonnées déplacent l\'origine de l\'axe de rotation, par rapport à l\'origine du système de coordonnées.

Si vous sélectionnez un axe défini par l\'utilisateur, les nombres définissent la direction de l\'axe de rotation par rapport au système de coordonnées d\'origine: Si la coordonnée Z est 0 et les coordonnées Y et X ne sont pas nulles, alors l\'axe se trouvera dans le Plan X-Y. Son angle est tel que sa tangente est le rapport entre les coordonnées X et Y.



## Remarques

-   Les objets [App Link](App_Link/fr.md) liés aux types d\'objets appropriés peuvent également être utilisés comme formes et pour spécifier l\'axe. {{Version/fr|0.20}}
-   Si l\'objet à faire pivoter coupe l\'axe de rotation, l\'opération échouera dans la plupart des cas.



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Revolve/fr
