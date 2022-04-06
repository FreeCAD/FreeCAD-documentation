---
- GuiCommand:/fr
   Name:Part Compound‏‎
   Name/fr:Part Composé
   MenuLocation:Part → Composé → Créer un composé
   Workbenches:[Part](Part_Workbench/fr.md)
   Version:0.14
   SeeAlso:[Part Union](Part_Fuse/fr.md), [Part Filtre composé](Part_CompoundFilter/fr.md), [Part Éclater le composé](Part_ExplodeCompound/fr.md)
---

# Part Compound/fr

## Description

Cette commande crée un composé de toutes formes topologiques. Celles-ci peuvent être des solides des mailles ou tout autre type de forme topologique.

Un compound est un ensemble de formes groupées dans un seul objet.

## Utilisation

1.  Sélectionnez les formes dans la [vue en arborescence](Tree_view/fr.md) qui seront ajoutées au composé
2.  Faites **Part → Composé → Créer un composé** dans le menu Pièce ou cliquez sur le bouton <img alt="" src=images/Part_Compound.svg  style="width:24px;">.

## Remarques

Un composé contenant des pièces qui se croisent ou qui se touchent est **invalide** pour créer des opérations booléennes. En raison de problèmes de performances, vérifier si les pièces qui se croisent ne sont pas terminée. L\'option Vérifier la géométrie automatique (disponible pour les opérations booléennes) est également désactivée pour le composé.

Pour activer cette vérification, allez sur **Outils → Éditer Paramètres... → Préférences → Mod → Part → CheckGeometry → RunBOPCheck** et réglez le paramètre sur `true`.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Compound/fr
