---
- GuiCommand:
   Name: Part Compound‏‎
   Name/fr: Part Composé
   MenuLocation: Part -> Composés -> Créer un composé
   Workbenches: Part_Workbench/fr
   Version: 0.14
   SeeAlso: Part_Fuse/fr, Part_CompoundFilter/fr, Part_ExplodeCompound/fr
---

# Part Compound/fr

## Description

Cette commande crée un composé d\'objets ayant une forme topologique tels que des objets solides et d\'autres objets avec des faces et/ou des bords. Elle ne peut pas traiter les maillages car ils n\'ont pas de forme topologique.

## Utilisation

1.  Sélectionnez les formes dans la [vue en arborescence](Tree_view/fr.md) qui seront ajoutées au composé
2.  Faites **Part → Composés → Créer un composé** dans le menu Part ou cliquez sur le bouton <img alt="" src=images/Part_Compound.svg  style="width:24px;">.

## Remarques

Un composé contenant des pièces qui se croisent ou qui se touchent est **invalide** pour créer des opérations booléennes. En raison de problèmes de performances, vérifier si les pièces qui se croisent ne sont pas terminée. L\'option Vérifier la géométrie automatique (disponible pour les opérations booléennes) est également désactivée pour le composé.

Pour activer cette vérification, allez sur **Outils → Éditer Paramètres... → Préférences → Mod → Part → CheckGeometry → RunBOPCheck** et réglez le paramètre sur `true`.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Compound/fr
