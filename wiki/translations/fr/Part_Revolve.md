---
- GuiCommand:/fr
   Name:Part_Revolve
   Name/fr:Part Révolution
   MenuLocation:Pièce → Révolution...
   Workbenches:[Part](Part_Workbench/fr.md)
---


</div>

## Description

Fait pivoter l\'objet sélectionné autour d\'un axe donné. Les types de forme suivants sont autorisés et mènent aux formes de sortie énumérées ([Voir Remarques pour les exceptions](#Remarques.md)):

  Objet en entrée,   Objet résultant
  ------------------ ----------------------------
  Sommet             Arête
  Arête              Face
  Filaire            Enveloppe
  Face               Solide
  Enveloppe          Solide Composé (Compsolid)

Les solides, ou les compositions avec des solides, ne sont pas autorisés comme formes d\'entrée. Les compositions normales ne sont actuellement pas autorisées. Les versions futures vérifieront le type de forme réel des objets composés.

![](images/Dialog-revolve.png )

L\'argument Angle spécifie l\'angle selon lequel l\'objet doit être tourné. Les coordonnées déplacent l\'origine de l\'axe de rotation, par rapport à l\'axe d\'origine du système de coordonnées.

Si vous sélectionnez un axe défini par l\'utilisateur, les nombres définissent la direction de l\'axe de rotation par rapport au système de coordonnées d\'origine: Si la coordonnée Z est 0 et les coordonnées Y et X ne sont pas nulles, alors l\'axe se trouvera dans le Plan X-Y. Son angle est tel que sa tangente est le rapport entre les coordonnées X et Y.

### Remarques

-   Si votre version de FreeCAD a une case à cocher pour Solide dans le dialogue de Révolution, vous pouvez faire des Solides à partir de filaires fermés et d\'Arêtes.
-   Si la révolution est effectuée à l\'aide d\'un axe qui coupe la face à pivoter et que vous souhaitez créer un solide, le résultat peut être invalide. Cela peut se produire pour diverses raisons, auto-intersection, direction, etc.


<div class="mw-translate-fuzzy">





</div>


  
