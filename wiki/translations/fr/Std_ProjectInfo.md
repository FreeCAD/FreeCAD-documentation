---
 GuiCommand:
   Name: Std ProjectInfo
   Name/fr: Std Informations sur le document
   MenuLocation: Fichier , Informations sur le document
   Workbenches: Tous
   SeeAlso: Std_New/fr
---

# Std ProjectInfo/fr

## Description

La commande **Informations sur le document** affiche une fenêtre de dialogue contenant les détails du document actif. Certaines de ces informations peuvent être modifiées.



## Utilisation

1.  Sélectionnez l\'option **Fichier → <img src="images/Std_ProjectInfo.svg" width=16px> Informations sur le document...** du menu.
2.  Une fenêtre de dialogue contenant les informations suivantes apparaît :
    -   **Nom** : nom du document. Correspond à la propriété Label du document. *Non modifiable.*
    -   **Chemin d\'accès** : chemin complet du fichier. Vide si le fichier n\'a pas été sauvegardé. *Non modifiable.*
    -   **UUID** : FreeCAD met automatiquement une valeur de checksum. *Non modifiable.*
    -   **Version du programme** : version de FreeCAD utilisée pour sauvegarder le fichier. Vide si le fichier n\'a pas été sauvegardé. *Non éditable.*
    -   **Système d\'unités** : système d\'unités du document. *La valeur initiale dépend du [système d\'unités par défaut](Preferences_Editor/fr#Général_2.md).* {{Version/fr|1.0}}
    -   **Crée par** : entrez un nom d\'auteur. *Peut être prédéfini.*
    -   **Date de création** : FreeCAD entre automatiquement la date correcte. *Non modifiable.*
    -   **Dernière modification par** : entrez un nom d\'auteur. *Peut être prédéfini.*
    -   **Date de dernière modification** : FreeCAD entre automatiquement la bonne date. *Non modifiable.*
    -   **Société** : entrez un nom de société. *Peut être prédéfini.*
    -   **Informations sur la licence** : sélectionnez une licence dans le menu déroulant. *Peut être prédéfini.*
    -   **URL de la licence** : l\'URL changera en fonction de la licence sélectionnée, mais peut être écrasée. *Peut être prédéfini.*
    -   **Commentaire** : entrez tout commentaire qui pourrait s\'appliquer.
3.  Entrez les informations requises et appuyez sur le bouton **OK**.

## Options

-   Appuyez sur **Échap** ou sur le bouton **Annuler** pour annuler la commande.



## Préférences

Voir aussi : [Réglage des préférences](Preferences_Editor/fr.md).

-   Certaines propriétés du document : nom de l\'auteur, nom de la société et informations de licence, peuvent être prédéfinies : **Édition → Préférences... → Général → Document → Création et licence**.



---
⏵ [documentation index](../README.md) > Std ProjectInfo/fr
