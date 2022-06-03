---
- GuiCommand   */fr
   Name   *Std Quit
   Name/fr   *Std Quitter
   MenuLocation   *Fichier → Quitter
   Workbenches   *Tous
   Shortcut   ***Alt**+**F4**
   SeeAlso   *[Std Fermer](Std_CloseActiveWindow/fr.md)
---

# Std Quit/fr

## Description

La commande **Std Quitter** ferme l\'application FreeCAD et enregistre éventuellement les documents non enregistrés.

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande   *
    -   Sélectionnez l\'option **Fichier → <img src="images/Std_Quit.svg" width=16px> Quitter** dans le menu.
    -   Utilisez le raccourci clavier   * **Alt**+**F4**.
2.  Si le document actif n\'a pas été enregistré, une boîte de dialogue vous invite à l\'enregistrer   *
    -   Appuyez sur le bouton **Enregistre le document actif** pour enregistrer le document. Si nécessaire, entrez d\'abord un nom de fichier.
    -   Appuyez sur le bouton **Fermer sans enregistrer** pour supprimer le document et perdre toutes les modifications.

## Options

-   S\'il existe plusieurs documents non enregistrés   * cochez la case {{CheckBox|TRUE|Appliquer la réponse à tous}} pour éviter d\'être invité à chaque fois pour chaque document non enregistré.
-   S\'il y a des documents non enregistrés   * appuyez sur **Echap** ou sur le bouton **Annuler** pour abandonner la commande.

## Préférences

-   Le dernier emplacement de fichier utilisé est stocké   * **Outils → Editer les paramètres... → BaseApp → Preferences → General → FileOpenSavePath**.





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std Quit/fr
