---
 GuiCommand:
   Name: Std RestartInSafeMode
   Name/fr: Std Redémarrer en mode sans échec
   MenuLocation: Aide , Redémarrer en mode sans échec
   Workbenches: Tous
   Version: 1.0
   SeeAlso: 
---

# Std RestartInSafeMode/fr



## Description

La commande **Std Redémarrer en mode sans échec** redémarre FreeCAD dans un état **réinitialisation d\'usine** pour le débogage. Elle désactive temporairement les configurations de l\'utilisateur, les extensions, les thèmes et autres personnalisations.



## Utilisation

1.  Sélectionnez l\'option **Aide → <img src="images/Std_RestartInSafeMode.svg" width=16px> Redémarrer en mode sans échec** du menu.
2.  Une fenêtre de dialogue d\'avertissement s\'ouvre.
3.  Appuyez sur le bouton **Oui** pour confirmer.
4.  FreeCAD est redémarré en mode sans échec.
5.  Redémarrez FreeCAD à nouveau pour quitter le mode sans échec.



## Remarques

-   Le mode sans échec peut également être lancé à partir de l\'interface de ligne de commande (CLI) en utilisant le drapeau {{Incode|--safe-mode}}. Voir [Démarrage et configuration](Start_up_and_Configuration/fr.md).



---
⏵ [documentation index](../README.md) > Std RestartInSafeMode/fr
