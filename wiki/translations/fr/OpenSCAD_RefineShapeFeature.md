---
- GuiCommand:
   Name: OpenSCAD RefineShapeFeature
   Name/fr: OpenSCAD Affiner la forme
   MenuLocation: OpenSCAD - Affiner la forme
   Workbenches: [OpenSCAD](OpenSCAD_Workbench/fr.md)
   SeeAlso: [Part Affiner la forme](Part_RefineShape.md)
---

# OpenSCAD RefineShapeFeature/fr

## Description

Nettoie les arêtes résiduelles. Après une opération booléenne, certaines arêtes définissant les formes précédentes restent visibles, cet outil crée une copie de la totalité de l\'objet nettoyé.

![](images/PartRefineShape_it.png )

## Utilisation

1.  Sélectionnez la forme à nettoyer.
2.  Cliquez sur le menu **OpenSCAD → Affiner la forme**.

-   Un objet-parent est créé et entièrement nettoyé, l\'objet original est rendu caché.

## Limitations

-   L\'algorithme de raffinement ne fonctionne que sur les coques. Par conséquent, il itère sur les coques de la forme originale, puis pour chaque coque, il crée une nouvelle coque avec des faces jointes autant que possible. Cela signifie que si votre forme originale est seulement une face, une polyligne, une arête ou un sommet, alors l\'algorithme ne fait rien.
-   À l\'opposé de l\'outil <img alt="" src=images/Part_RefineShape.svg  style="width:24px;"> [Part Affiner la forme](Part_RefineShape/fr.md) de l\'<img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [atelier Part](Part_Workbench/fr.md), cette fonctionnalité se met à jour lorsque les formes sous-jacentes sont modifiées.

## Remarques

-   La fonction ne modifie pas la forme originale mais retourne une nouvelle forme.
-   La fonction est normalement utilisée comme dernière étape dans l\'historique de modélisation.
-   La fonction peut être utile pour obtenir des filets difficiles à travailler
-   La fonction est destinée à empêcher les imprimantes 3D d\'imprimer des arêtes indésirables.





{{OpenSCAD_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [OpenSCAD](OpenSCAD_Workbench.md) > OpenSCAD RefineShapeFeature/fr
