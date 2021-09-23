---
- GuiCommand:/fr
   Name:PartDesign MoveTip
   Name/fr:PartDesign Désigner comme fonction résultante
   MenuLocation:Menu contextuel → Désigner comme fonction résultante
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   Version:0.17
   SeeAlso:[PartDesign Déplacer vers un autre corps](PartDesign_MoveFeature/fr.md), [PartDesign Déplacer après un autre objet](PartDesign_MoveFeatureInTree/fr.md)
---

# PartDesign MoveTip/fr

## Description

<img alt="" src=images/PartDesign_MoveTip.svg  style="width:24px;"> [Désigner comme fonction résultante](PartDesign_MoveTip/fr.md), comme elle est appelée dans le menu contextuel, redéfinit la fonction résultante qui est la caractéristique exposée à l\'extérieur du corps. Par défaut, la fonction résultante est la dernière fonctionnalité ajoutée au corps mais parfois, il peut être utile de définir temporairement une fonction en amont dans l\'arborescence comme fonction résultante. Cela peut être fait pour ajouter une esquisse, une géométrie de référence ou une fonction qui, rétrospectivement, aurait dû être créée plus tôt dans l\'historique du corps.

La fonction résultante se distingue visuellement dans l\'arborescence Modèle par une petite flèche blanche dans un cercle vert surimposée sur l\'icône de la fonction. Par exemple, la fonctionnalité suivante est la fonction résultante:

![](images/PartDesign_Body_tree-04.png )

## Utilisation

1.  Dans l\'arborescence du modèle, cliquer avec le bouton droit sur la fonction à définir comme fonction résultante.
2.  Sélectionner dans la liste du menu contextuel <img alt="" src=images/PartDesign_MoveTip.svg  style="width:24px;"> **Désigner comme fonction résultante**.
3.  La nouvelle fonction résultante est visible et tous les éléments se trouvant sous elle sont masqués. Les éléments nouvellement créés à partir de ce point seront placés sous la fonction résultante, et au-dessus des autres éléments existants.

**Remarque** : il est important de ne pas oublier de redéfinir la fonction résultante sur la dernière fonction au bas de l\'arborescence du corps.





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign MoveTip/fr
