---
- GuiCommand:/fr
   Name:Part Fuse
   Name/fr:Part Union
   MenuLocation:Pièce → Opération booléenne → Union
   Workbenches:[Part](Part_Workbench/fr.md)
   SeeAlso:[Part Opération booléenne](Part_Boolean/fr.md), [Part Soustraction](Part_Cut/fr.md), [Part Intersection](Part_Common/fr.md), 
---


</div>

## Description

L\'outil **![](images/)_[Union](Part_Fuse/fr.md)** fusionne les objets Part sélectionnés en un seul. Cette opération est entièrement paramétrique et les composants peuvent être modifiés et le résultat recalculé.

**Remarque :** Cette commande est une forme automatisée de <img alt="" src=images/Part_Boolean.svg  style="width:24px;"> [Part Opération booléenne](Part_Boolean/fr.md).

## Utilisation

1.  Sélectionnez deux formes
2.  Plusieurs manières pour lancer cette commande :
    -   Appuyez sur le bouton **![](images/) Exécuter l'union de plusieurs formes** de la barre d**\'outils Part**
    -   Utilisez l\'entrée {{MenuCommand|Pièce → Opération booléenne → Union}} depuis le menu Part

## Entrées prises en charge {#entrées_prises_en_charge}

L\'objet doit être un objet (forme) [OpenCascade](OpenCascade/fr.md). Exemples: les objets créés avec un des ateliers Part, PartDesign, Sketcher. Ne peut pas être un objet Mesh (sauf s\'il est converti en forme (shape)) - pour les objets Mesh, utilisez l\'outil booléen spécifique dans l\'atelier MeshDesign.

-   Solide + Solide : le résultat est un solide qui occupe tout le volume couvert par les volumes d\'origine.

-   Coque (shell) + coque, coque + face, face + face: le résultat est une coque. Lorsque les faces se croisent, elles sont séparées. Les coques peuvent être non-manifold. Après la fusion, les faces peuvent être unies en [affinant](Part_RefineShape/fr.md) le résultat.

-   Fil (wire) + fil, arête + fil, arête + arête : le résultat est un fil. Les arêtes sont diviséss là où elles se croisent.

Les composés sont pris en charge ; cependant, il est supposé que les formes contenues dans un composé ne se touchent pas ou ne se croisent pas. Si c\'est le cas, la fusion échouera probablement ou produira un résultat incorrect.

## Options

Les éléments peuvent être ajoutés et supprimés à partir de la fusion, en les faisant glisser dans ou hors de la fonction de fusion dans l\'arborescence, avec la souris. Un recalcule manuel (appuyez sur la touche **F5** ou cliquez sur l\'icône de <img alt="" src=images/Std_Refresh.svg  style="width:24px;"> [Rafraichir/Recalculer](Std_Refresh/fr.md)) est nécessaire pour voir les résultats.

Après que cette opération soit complète, il peut être nécessaire de nettoyer la forme avec <img alt="" src=images/Part_RefineShape.svg  style="width:24px;"> [Affiner la forme](Part_RefineShape/fr.md).


<div class="mw-translate-fuzzy">





</div>


  
