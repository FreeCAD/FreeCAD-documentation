---
- GuiCommand:/fr
   Name:Std FreezeViews
   Name/fr:Std Figer l'affichage
   MenuLocation:Affichage → Figer l'affichage → ...
   Workbenches:Tous
   SeeAlso:[Std Position de la caméra](Std_ViewIvIssueCamPos/fr.md)
   SeeAlso:[Std Enregistrer la vue](Std_StoreWorkingView/fr.md), [Std Rappel de vue](Std_RecallWorkingView/fr.md), [Std Position de la caméra](Std_ViewIvIssueCamPos/fr.md)
---

# Std FreezeViews/fr

## Introduction

FreeCAD peut stocker les paramètres de la caméra dans jusqu\'à 50 «vues figées». Les options de menu relatives aux vues figées se trouvent dans le sous-menu **Affichage → Figer l'affichage**. Les vues figées ne sont pas stockées dans le document et si elles ne sont pas enregistrées avec l\'option de menu **[Enregistrer les vues](#Enregistrer_les_vues.md)** seront perdues à la fermeture de l\'application FreeCAD.

## Enregistrer les vues 

### Description

L\'option de menu **Enregistrer les vues\...** enregistre toutes les vues figées existantes dans un fichier avec l\'extension \*.cam.

### Utilisation

1.  Pour utiliser cette option, une ou plusieurs vues figées doivent exister. Une vue figée est créée avec l\'option de menu **[Figer l\'affichage](#Figer_l.27affichage.md)**.
2.  Sélectionnez l\'option **Affichage → Figer l'affichage → Enregistrer les vues...** dans le menu.
3.  Entrez un nom de fichier dans la boîte de dialogue.
4.  Appuyez sur le bouton **Enregistrer**.

### Options

-   Appuyez sur **Echap** ou sur le bouton **Annuler** pour annuler la commande.

## Charger les vues 

### Description 

L\'option du menu **Charger les vues\...** charge les vues figées à partir d\'un fichier avec l\'extension \*.cam. Toutes les vues figées existantes seront supprimées.

### Utilisation 

1.  Sélectionnez l\'option **Affichage → Figer l'affichage → Charger les vues...** dans le menu.
2.  Appuyez sur le bouton **Oui** dans la boîte de dialogue Restaurer les vues pour confirmer que vous souhaitez perdre toutes les vues figées existantes.
3.  Sélectionner un fichier.
4.  Appuyez sur le bouton **Ouvrir**.

### Options 

-   Si la boîte de dialogue Restaurer les vues s\'affiche, appuyez sur **Echap** ou sur le bouton **Non** pour annuler la commande.
-   Si la boîte de dialogue du fichier s\'affiche, appuyez sur **Echap** ou sur le bouton **Annuler** pour abandonner la commande.

## Figer l\'affichage 

### Description 

L\'option de menu **Figer l\'affichage** enregistre les paramètres actuels de la caméra (direction, zoom, etc.) de la [vue 3D](3D_view/fr.md) dans une nouvelle entrée de la liste des vues figées. La liste des vues figées peut contenir jusqu\'à 50 vues figées.

### Utilisation 

1.  Il existe plusieurs façons de lancer cette option :
    -   Sélectionnez l\'option **Affichage → Figer l'affichage → Charger les vues...** dans le menu.
    -   Utilisez le raccourci clavier : **Shift**+**F**.
2.  La nouvelle vue figée peut être sélectionnée dans le sous-menu **Affichage → Figer l'affichage**.

## Effacer les vues 

### Description 

L\'option de menu **Effacer les vues** supprime toutes les vues figées existantes.

### Utilisation 

1.  Sélectionnez l\'option **Affichage → Figer l'affichage → Effacer les vues** dans le menu.

## Restaurer la vue 

### Description 

Pour chaque vue figée, une option **Vue de restauration** est ajoutée avec laquelle elle peut être restaurée. Les options sont numérotées: **Restore view 1** - **Restore view 50**.

### Utilisation 

1.  Il existe plusieurs façons de lancer cette option :
    -   Sélectionnez l\'option **Affichage → Figer l'affichage → Restaurer la vue** dans le menu.
    -   Pour les 9 premières vues figées: utilisez le raccourci clavier : **Ctrl**+**1** - **Ctrl**+**9**.





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std FreezeViews/fr
