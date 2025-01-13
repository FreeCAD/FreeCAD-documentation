---
 GuiCommand:
   Name: Part Fuse
   Name/fr: Part Union
   MenuLocation: Part , Opération booléenne , Union
   Workbenches: Part_Workbench/fr
   SeeAlso: Part_Boolean/fr, Part_Cut/fr, Part_Common/fr, 
---

# Part Fuse/fr

## Description

L\'outil **![](images/)_[Union](Part_Fuse/fr.md)** fusionne les objets Part sélectionnés en un seul. Cette opération est entièrement paramétrique et les composants peuvent être modifiés et le résultat recalculé.

**Remarque :** Cette commande est une forme automatisée de <img alt="" src=images/Part_Boolean.svg  style="width:24px;"> [Part Opération booléenne](Part_Boolean/fr.md).



## Utilisation

1.  Sélectionnez deux formes
2.  Plusieurs manières pour lancer cette commande :
    -   Appuyez sur le bouton **![](images/) Union** de la barre d**\'outils Part**
    -   Utilisez l\'entrée **Part → Opération booléenne → Union** depuis le menu Part



## Entrées prises en charge 

Les objets utilisés doivent être des formes [OpenCASCADE](OpenCASCADE/fr.md). Exemples : les trucs faits avec un des ateliers Part, PartDesign, Sketcher. Pas de maillages (sauf s\'ils ont été convertis en formes) - pour les maillages, il existe des outils booléens spécifiques dans l\'atelier MeshDesign.

-   Solide + Solide : le résultat est un solide qui occupe tout le volume couvert par les volumes d\'origine.

-   Coque (shell) + coque, coque + face, face + face : le résultat est une coque. Lorsque les faces se croisent, elles sont séparées. Les coques peuvent être non-manifold. Après la fusion, les faces peuvent être unies en [affinant](Part_RefineShape/fr.md) le résultat.

-   Fil (wire) + fil, arête + fil, arête + arête : le résultat est un fil. Les arêtes sont diviséss là où elles se croisent.

Les composés sont pris en charge ; cependant, il est supposé que les formes contenues dans un composé ne se touchent pas ou ne se croisent pas. Si c\'est le cas, la fusion échouera probablement ou produira un résultat incorrect.

## Options

Les éléments peuvent être ajoutés et retirés d\'une fusion, en les faisant glisser dans ou hors de l\'élément de fusion dans l\'arborescence avec la souris. Pour faire glisser des éléments hors d\'une fusion, vous devez les déposer sur le nœud du document (le nom du fichier) de votre modèle. Un recalcul manuel (appuyez sur la touche **F5** ou cliquez sur l\'icône <img alt="" src=images/Std_Refresh.svg  style="width:24px;"> [Recalculer](Std_Refresh/fr.md)) est nécessaire pour voir les résultats.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Fuse/fr
