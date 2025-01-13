---
 GuiCommand:
   Name: Sketcher External
   Name/fr: Sketcher Géométrie externe
   MenuLocation: Esquisse , Outils d'esquisse , Créer une géométrie externe
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **G** **X**
   SeeAlso: Sketcher_ToggleConstruction/fr
---

# Sketcher External/fr

## Description


{{VersionMinus/fr|1.0}}

: L\'outil <img alt="" src=images/Sketcher_External.svg  style="width:24px;"> [Sketcher Géométrie externe](Sketcher_External/fr.md) projette sur le plan de l\'esquisse des arêtes et/ou des sommets appartenant à des objets situés en dehors de l\'esquisse. La géométrie projetée est appelée \"géométrie externe\". Elle reste paramétriquement liée à ses objets sources. Les arêtes de la géométrie externe sont marquées par une [couleur](Sketcher_Preferences/fr#Apparence.md) dédiée (magenta par défaut) et ({{Version/fr|1.0}}) un type de ligne. Comme la géométrie de construction, la géométrie externe n\'est pas visible à l\'extérieur de l\'esquisse. Elle est destinée à aider à définir les contraintes et autres géométries à l\'intérieur de l\'esquisse elle-même.


{{VersionPlus/fr|1.1}}

: voir <img alt="" src=images/Sketcher_Projection.svg  style="width:24px;"> [Sketcher Projection](Sketcher_Projection/fr.md)

![](images/Sketcher_ExternalEsempio1.png ) 
*Les deux lignes magenta sont des géométries externes liées aux arêtes d'une [protrusion](PartDesign_Pad/fr.md) préexistante. Elles sont utilisées pour contraindre les cercles.*



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).

1.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **[<img src=images/Sketcher_External.svg style="width:16px"> [Créer une géométrie externe](Sketcher_External/fr.md)**.
    -   Sélectionnez l\'option **Esquisse → Outils d'esquisse → <img src="images/Sketcher_External.svg" width=16px> Créer une géométrie externe** du menu.
    -   Cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **<img src="images/Sketcher_External.svg" width=16px> Créer une géométrie externe** du menu contextuel.
    -   Utilisez le raccourci clavier : **G** puis **X**.
2.  Le curseur se transforme en croix avec l\'icône de l\'outil.
3.  Sélectionnez une arête externe ou un sommet. Voir [Remarques](##Remarques.md).
4.  La géométrie externe est créée.
5.  Cet outil fonctionne toujours en mode continu : vous pouvez continuer à sélectionner des arêtes externes et/ou des sommets.
6.  Pour terminer, cliquez avec le bouton droit de la souris ou appuyez sur **Échap**, ou démarrez un autre outil de création de géométrie ou de contrainte.



## Remarques

-   Seuls les arêtes et les sommets des objets situés dans le même système de coordonnées peuvent être sélectionnés. L\'esquisse et l\'objet doivent se trouver dans le même [corps](PartDesign_Body/fr.md), ou le même [Part](Std_Part/fr.md), ou les deux dans le système de coordonnées global. Utilisez un [lien](PartDesign_SubShapeBinder/fr.md) pour amener une copie de l\'objet dans le système de coordonnées en cours si nécessaire.
-   Les dépendances circulaires ne sont pas autorisées. Vous ne pouvez pas créer de lien vers un objet qui dépend de l\'esquisse elle-même.
-   Les liens vers des éléments d\'autres esquisses sont possibles et encouragés, car ils sont plus fiables que les liens vers une géométrie générée (solide). Ces derniers peuvent souffrir du [problème de dénomination topologique](Topological_naming_problem/fr.md). Voir [Conseils pour les modèles stables](Feature_editing/fr#Conseils_pour_la_création_de_modèles_robustes.md).





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher External/fr
