---
 GuiCommand:
   Name: Std_DlgMacroRecord
   Name/fr: Std Enregistrer une macro
   MenuLocation: Macro , Enregistrer une macro...
   Workbenches: Tous
   SeeAlso: Std_MacroStopRecord/fr
---

# Std DlgMacroRecord/fr



## Description

La commande **Std Enregistrer une macro** démarre une session d\'enregistrement d\'une [macro](Macros/fr.md) pendant laquelle les actions de l\'utilisateur sont enregistrées dans une macro FreeCAD, un fichier avec l\'extension **.FCMacro**. Une macro peut ensuite être rejouée, exécutée, pour répéter les actions enregistrées.

![](images/Std_DlgMacroRecord_dialog.png ) 
*La fenêtre de dialogue d'enregistrement d'une macro*



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Std_DlgMacroRecord.svg" width=16px> [Enregistrer une macro...](Std_DlgMacroRecord/fr.md)**.
    -   Sélectionnez l\'option **Macro → <img src="images/Std_DlgMacroRecord.svg" width=16px> Enregistrer une macro...** du menu.
2.  La fenêtre de dialogue **Enregistrement d\'une macro** s\'ouvre.
3.  Saisissez un nom pour la macro dans la zone de saisie **Nom de la macro**.
4.  Vous pouvez modifiez le **Chemin d\'accès aux macros** en appuyant sur le bouton **...**.
5.  Le bouton **Arrêter** ne fonctionne pas pour le moment.
6.  Appuyez sur le bouton **Enregistrer** pour fermer la fenêtre de dialogue et démarrer la session d\'enregistrement.
7.  L\'image du bouton de la commande devient **<img src="images/Std_MacroStopRecord.svg" width=16px>** et le texte du menu devient **Arrêter l'enregistrement de la macro**.
8.  Effectuez les actions que vous souhaitez enregistrer.
9.  Pour terminer la session d\'enregistrement, effectuez l\'une des opérations suivantes :
    -   Appuyez sur le bouton **<img src="images/Std_MacroStopRecord.svg" width=16px> [Arrêter l'enregistrement de la macro](Std_DlgMacroRecord/fr.md)**.
    -   Sélectionnez l\'option **Macro → <img src="images/Std_MacroStopRecord.svg" width=16px> Arrêter l'enregistrement de la macro** du menu.

## Options

-   Lorsque la fenêtre de dialogue des macros s\'affiche : appuyez sur **Échap** ou sur le bouton **Fermer** pour abandonner la commande.



## Remarques

-   Pour exécuter la macro enregistrée, utilisez la commande [Lancer la macro](Std_DlgMacroExecute/fr.md).
-   Pour en savoir plus sur les macros, consultez la page [Macro](Macros/fr.md).



## Préférences

Voir aussi : [Réglage des préférences](Preferences_Editor/fr.md).

-   Le chemin d\'accès à la macro peut également être modifié dans les préférences : **Édition → Préférences... → Python → Macro → Chemin d'accès aux macros**.
-   Dans la plupart des cas, il n\'est pas souhaitable d\'enregistrer des actions qui ne modifient pas le modèle : sous **Édition → Préférences... → Python → Macro → Commandes de l'interface graphique**, effectuez l\'une des actions suivantes :
    -   Pour exclure ces actions, décochez la case **Enregistrer les commandes de l\'interface graphique**.
    -   Pour les inclure en tant que commentaires, cochez les cases **Enregistrer les commandes de l\'interface graphique** et **Enregistrer comme un commentaire**.



---
⏵ [documentation index](../README.md) > Std DlgMacroRecord/fr
