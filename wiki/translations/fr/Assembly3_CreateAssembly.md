---
 GuiCommand:
   Name: Assembly3 CreateAssembly
   Name/fr: Assembly3 Créer un assemblage
   Icon: Assembly_New_Assembly.svg
   MenuLocation: Assembly3 , Create assembly
   Workbenches: Assembly3_Workbench/fr
   Shortcut: **A** **N**
---

# Assembly3 CreateAssembly/fr



## Description

La commande <img alt="" src=images/Assembly_New_Assembly.svg‎‎  style="width:24px;"> **Créer un assemblage** ajoute un nouvel objet à la branche **Assembly** à l\'arborescence du modèle.

Chaque objet de la branche est un <img alt="" src=images/Assembly_Assembly_Tree.svg  style="width:24px;"> un conteneur **Assembly** et contient quatre conteneurs de groupe :

:   \- un pour les <img alt="" src=images/Assembly_Assembly_Constraints_Tree.svg  style="width:24px;"> **Contraintes** (caché tant qu\'il est vide)
:   \- Un pour les <img alt="" src=images/Assembly_Assembly_Element_Tree.svg  style="width:24px;"> 
**Eléments**
:   \- Un pour les <img alt="" src=images/Assembly_Assembly_Part_Tree.svg  style="width:24px;"> 
**Pièces**
:   \- Un pour les <img alt="" src=images/Assembly_Assembly_Relation_Tree.svg  style="width:24px;"> **Relations** (cachées par défaut et qui seront révélées lorsque <img alt="" src=images/Assembly_GotoRelation.svg  style="width:16px;"> [Relations](Assembly3_GoToRelation/fr.md) est utilisé.)

 L\'objet **Assembly** ajouté avec tous les conteneurs visibles ressemble à ceci (0.20.pre et Link Branch) :

<img alt="" src=images/Assembly3_Example-Tree-07.png  style="width:190px;"> <img alt="" src=images/Assembly3_Example-Tree-08.png  style="width:190px;">



## Utilisation

1.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Assembly_New_Assembly.svg" width=16px> [Create assembly](Assembly3_CreateAssembly/fr.md)**.
    -   Sélectionnez l\'option **Assembly3 → <img src="images/Assembly_New_Assembly.svg" width=16px> Create assembly** du menu.
    -   Utiliser le raccourci clavier **A** puis **N**
2.  Un conteneur Assembly est créé.



---
⏵ [documentation index](../README.md) > Assembly3 CreateAssembly/fr
