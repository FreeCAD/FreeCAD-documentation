---
- GuiCommand:/fr
   Name:Std ProjectInfo
   Name/fr:Std Information sur le projet
   MenuLocation:Fichier → Information sur le projet
   Workbenches:Tous
   SeeAlso:[Std Nouveau](Std_New/fr.md)
---

# Std ProjectInfo/fr

## Description

La commande **Information sur le projet** affiche une boîte de dialogue avec des informations sur le projet appartenant au document actif. Certaines de ces informations peuvent être modifiées.

## Utilisation

1.  Sélectionnez l\'option **Fichier → <img src="images/Std_ProjectInfo.svg" width=16px> Information sur le projet...** dans le menu.
2.  Une boîte de dialogue contenant les informations suivantes apparaît:
    -   **Name**: nom du document. **Non modifiable**. Correspond à la propriété Label du document qui peut être modifiée dans l\'[Editeur des propriétés](Property_editor/fr.md).
    -   **Path**: chemin complet du fichier. Vide si le document n\'a pas été enregistré. **Non modifiable**.
    -   **UUID**: FreeCAD entre automatiquement une valeur de somme de contrôle. **Non modifiable**.
    -   **Created by**: entrez un nom d\'auteur. **Peut être prédéfini**.
    -   **Creation date**: FreeCAD entre automatiquement la date correcte. **Non modifiable**.
    -   **Last modified by**: entrez un nom d\'auteur. **Peut être prédéfini**.
    -   **Last modification date**: FreeCAD entre automatiquement la date correcte. **Non modifiable**.
    -   **Company**: entrez un nom de société. **Peut être prédéfini**.
    -   **License Information**: sélectionnez une licence dans le menu déroulant. **Peut être prédéfini**.
    -   **License URL**: l\'URL changera avec la licence sélectionnée, mais peut être écrasée. **Peut être prédéfini**.
    -   **Comment**: entrez tout commentaire qui pourrait s\'appliquer.
3.  Saisissez les informations requises et appuyez sur le bouton **OK**.

## Options

-   Appuyez sur **Echap** ou sur le bouton **Annuler** pour annuler la commande.

## Préférences

-   Les valeurs des noms d\'auteur, du nom de l\'entreprise et des informations de licence peuvent être prédéfinies dans [Editeur de préférences](Preferences_Editor/fr#Document.md).





{{Std Base navi

}}

---
[documentation index](../README.md) > Std ProjectInfo/fr
