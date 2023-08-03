---
 GuiCommand:
   Name: Std_DlgMacroRecord
   Name/fr: Std Enregistrement de macro
   MenuLocation: Macro , Enregistrement de macro...
   Workbenches: Tous
   SeeAlso: Std_MacroStopRecord/fr
---

# Std DlgMacroRecord/fr



## Description

La commande **Std Enregistrement de macro** démarre une session d\'enregistrement de [macro](Macros/fr.md) pendant laquelle les actions de l\'utilisateur sont stockées dans une macro FreeCAD, un fichier avec l\'extension **.FCMacro**. Une macro peut ensuite être rejouée, exécutée, pour répéter les actions enregistrées.

![](images/Std_DlgMacroRecord_dialog.png ) 
*La boîte de dialogue d'enregistrement de macro*



## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande :
    -   Appuyez sur le bouton **<img src="images/Std_DlgMacroRecord.svg" width=16px> [Std Enregistrement de macro...](Std_DlgMacroRecord/fr.md)**.
    -   Sélectionnez l\'option **Macro → <img src="images/Std_DlgMacroRecord.svg" width=16px> Enregistrement de macro...** dans le menu.
2.  La boîte de dialogue Enregistrement de macro s\'ouvre.
3.  Saisissez un nom pour la macro dans la zone de saisie **Nom de la macro**.
4.  Modifiez éventuellement le **Chemin de la macro** en appuyant sur le bouton **...**.
5.  Le bouton **Arrêter** ne fonctionne pas pour le moment.
6.  Appuyez sur le bouton **Enregistrer** pour fermer la boîte de dialogue et démarrer la session d\'enregistrement.
7.  Effectuez les actions que vous souhaitez enregistrer.
8.  Pour terminer la session d\'enregistrement, effectuez l\'une des opérations suivantes:
    -   Appuyez sur le bouton **<img src="images/Std_MacroStopRecord.svg" width=16px> [Std Arrêter l'enregistrement de la macro](Std_MacroStopRecord/fr.md)**.
    -   Sélectionnez l\'option **Macro → <img src="images/Std_MacroStopRecord.svg" width=16px> Arrêter l'enregistrement de la macro** dans le menu.

## Options

-   Lorsque la boîte de dialogue des macros s\'affiche: appuyez sur **Echap** ou sur le bouton **Fermer** pour abandonner la commande.



## Remarques

-   Pour exécuter la macro enregistrée, utilisez la commande [Std Exécuter une macro](Std_DlgMacroExecute/fr.md).
-   Pour en savoir plus sur les macros, consultez la page [Macro](Macros/fr.md).



## Préférences

-   Le chemin de la macro peut également être modifié dans les préférences : **Édition → Préférences... → Python → Macro → Chemin de la macro**. Voir l\'[Éditeur de préférences](Preferences_Editor/fr#Macro.md).
-   Dans la plupart des cas, il n\'est pas souhaitable d\'enregistrer des actions qui ne modifient pas le modèle : sous **Edition → Préférences... → Python → Macro → Commandes de l'interface graphique**, effectuez l\'une des actions suivantes :
    -   Pour exclure ces actions, décochez la case {{CheckBox|FALSE|Enregistrer les commandes de l'interface graphique}}.
    -   Pour les inclure en tant que commentaires, cochez les cases {{CheckBox|TRUE|Enregistrer les commandes de l'interface graphique}} et {{CheckBox|TRUE|Enregistrer comme un commentaire}}.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std DlgMacroRecord/fr
