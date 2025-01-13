---
 GuiCommand:Container
|
{{GuiCommand/fr
   Name: FEM MeshNetgenFromShape
   Name/fr: FEM Mailler avec Netgen
   MenuLocation: Maillage , Mailler avec le mailleur Netgen
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_tutorial/fr
}}
{{GuiCommandFemInfo/fr
   Solvers: CalculiX, Mystran, Z88
}}
---

# FEM MeshNetgenFromShape/fr

## Description

Pour une analyse par éléments finis, la géométrie doit être discrétisée en [FEM Maillage](FEM_Mesh/fr.md). Cette commande utilise [Netgen](https://www.ngsolve.org/) (à installer sur le système) pour générer le maillage. Les maillages Netgen ne sont pas pris en charge par le solveur [Elmer](FEM_SolverElmer/fr.md).

En fonction de votre système d\'exploitation et de le paquetage d\'installation, Netgen peut être fourni avec FreeCAD ou pas. Pour plus d\'informations voir [FEM Installation des composants requis](FEM_Install/fr.md).



## Utilisation

1.  Sélectionnez la forme que vous voulez analyser. Pour un volume, il doit s\'agir d\'un solide ou d\'un compsolide (composé de solides). Un compsolid est nécessaire si votre pièce est faite de plusieurs matériaux. (Un compsolid peut être créé avec la commande [Part Fragments booléens](Part_BooleanFragments/fr.md)).
2.  Activez l\'outil par l\'un des moyens suivants :
    -   Appuyez sur le bouton **<img src="images/FEM_MeshNetgenFromShape.svg" width=16px> [Mailler avec le mailleur Netgen](FEM_MeshNetgenFromShape/fr.md)
**
    -   Sélectionnez le bouton **Maillage → <img src="images/FEM_MeshGmshFromShape.svg" width=16px> Mailler avec le mailleur Netgen** du menu.
3.  Vous pouvez également définir la taille max/min des éléments (le paramètre par défaut crée généralement des maillages trop grossiers) et l\'ordre des éléments (en utilisant la case à cocher *Second ordre*).
4.  Vous pouvez également changer la *Précision* pour l\'un des choix prédéfinis ou choisir *Défini par l\'utilisateur* et éditer manuellement les paramètres.
5.  Cliquez sur le bouton **Appliquer** pour générer le maillage. {{Version/fr|1.0}} : vous pouvez utiliser le bouton **Annuler** pour annuler le maillage si vous utilisez la nouvelle implémentation de Netgen.
6.  Cliquez sur le bouton **OK** pour générer le maillage et fermer la fenêtre de dialogue. Vous pouvez également cliquer sur le bouton **Annuler** pour annuler les modifications ou la création de l\'objet de maillage.



## Propriétés

-    **Max. Size**: taille maximale de l\'élément en mm.

-    **Min. Size**: taille minimale de l\'élément en mm. {{Version/fr|1.0}}

-    **Second order**: les éléments de second ordre contiennent plus de noeuds par élément. En général, il suffit d\'utiliser un maillage plus grossier pour obtenir la même précision de solution qu\'avec les éléments de premier ordre,

    -   true (valueur par défaut) ; éléments de second ordre,
    -   false ; éléments de premier ordre.

-    **Fineness**: offre des niveaux prédéfinis de densité de maillage.

-    **Growth Rate**: définit de combien les éléments adjacents peuvent différer en taille.

-    **Nb. Segs per Edge**: définit le nombre minimum de segments de maille par arête.

-    **Nb. Segs per Radius**: définit le nombre minimum de segments de maillage par rayon.

-    **Optimize**:

    -   true (valeur par défaut) : applique un algorithme d\'optimisation pour améliorer la qualité du maillage
    -   false





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MeshNetgenFromShape/fr
