---
 GuiCommand:
   Name: Sketcher CreatePointFillet
   Name/fr: Sketcher Congé avec contraintes
   MenuLocation: Esquisse , Géometries d'esquisse , Congé d'esquisse préservant les contraintes
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **G** **F** **P**
   Version: 0.19
   SeeAlso: Sketcher_CreateFillet/fr
---

# Sketcher CreatePointFillet/fr

## Description

L\'outil <img alt="" src=images/Sketcher_CreatePointFillet.svg  style="width:24px;"> [Sketcher Congé avec contrainte](Sketcher_CreatePointFillet/fr.md) crée un congé entre deux arêtes non parallèles. Si deux arêtes droites reliées par une [contrainte de coïncidence](Sketcher_ConstrainCoincident/fr.md) sont supprimées, le point commun correspondant est préservé par l\'ajout d\'un [objet Point](Sketcher_CreatePoint/fr.md) ayant une [contrainte de point sur objet](Sketcher_ConstrainPointOnObject.md) avec les deux arêtes. Les contraintes liées au point commun sont transférées au nouvel objet Point. À part cela, cet outil est identique à l\'outil [Sketcher Congé](Sketcher_CreateFillet/fr.md). Voir cet outil pour plus d\'informations.



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).

1.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_CreatePointFillet.svg" width=16px> [Congé d'esquisse préservant les contraintes](Sketcher_CreatePointFillet/fr.md)**.
    -   Sélectionnez la commande **Esquisse → Géometries d'esquisse → <img src="images/Sketcher_CreatePointFillet.svg" width=16px> Congé d'esquisse préservant les contraintes** du menu.
    -   Cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **<img src="images/Sketcher_CreatePointFillet.svg" width=16px> Congé d'esquisse préservant les contraintes** du menu contextuel.
    -   Utilisez le raccourci clavier : **G** puis **F**, puis **P**.
2.  Pour plus d\'informations, voir [Sketcher Congé](Sketcher_CreateFillet/fr#Utilisation.md).



## Remarques

Voir [Sketcher Congé](Sketcher_CreateFillet/fr#Remarques.md).





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreatePointFillet/fr
