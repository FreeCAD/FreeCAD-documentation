---
 GuiCommand:
   Name: Mesh EvaluateFacet
   Name/fr: Mesh Infos sur la face
   MenuLocation: Maillages , Analyser , Infos sur la face
   Workbenches: Mesh_Workbench/fr
---

# Mesh EvaluateFacet/fr

## Description

La commande **Infos sur la face** affiche des informations sur les faces des objets maillés.

Mesh: Ellipsoid Facet 3631: Points: <1817, 1818, 1866>, Neighbours: <3534, 3632, 3630>
Triangle: <[1.964574, 0.047063, 0.748046], [1.937166, 0.062461, 0.992797], [1.964574, -0.047063, 0.748046]>



*Exemple des informations affichées dans la Vue rapport*



## Utilisation

1.  Il est conseillé d\'activer la [Vue rapport](Report_view/fr.md). La commande y affichera des informations détaillées.
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Mesh_EvaluateFacet.svg" width=16px> [Infos sur la face](Mesh_EvaluateFacet/fr.md)
**
    -   Sélectionnez l\'option {{MenuCommand |Maillages → Analyser → <img src="images/Mesh_EvaluateFacet.svg" width=16px> Infos sur la face}} du menu.
3.  Le curseur se transforme en icône pipette.
4.  Sélectionnez une face d\'un objet maillé.
5.  Son index sera affiché dans la [vue 3D](3D_view/fr.md).
6.  Des informations supplémentaires sont affichées dans la Vue rapport :
    -   Le nom interne de l\'objet maillage.
    -   L\'index du visage sélectionné.
    -   Les indices des trois points de la face.
    -   Les indices des faces qui partagent une arête avec la face sélectionnée.
    -   Les coordonnées des points de la face.
7.  Vous pouvez sélectionner plus de faces.
8.  Sélectionnez l\'option **Quitter le mode information** du menu contextuel de la vue 3D pour terminer la commande.





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh EvaluateFacet/fr
