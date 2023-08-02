---
- GuiCommand:
   Name: Std PythonHelp
   Name/fr: Std Documentation automatique des modules Python 
   MenuLocation: Aide -> Documentation automatique des modules Python
   Workbenches: Tous
   SeeAlso: Std_FreeCADPowerUserHub/fr
---

# Std PythonHelp/fr

## Description

La commande **Std Documentation des modules Python** démarre un serveur Web qui communique avec le navigateur Internet par défaut du système via un socket local. Le serveur Web affiche des informations sur les modules, classes et fonctions [Python](Python/fr.md) disponibles de FreeCAD. Les pages requises sont générées automatiquement.

Le serveur Web est basé sur le module [pydoc](https://docs.python.org/3.8/library/pydoc.html#module-pydoc) de Python et extrait ainsi les docstrings (chaîne de caractères) des fichiers Python (`.py`) et la documentation textuelle définie dans les wrappers Python (`.xml`) qui exposent le code C++ sous-jacent.

## Utilisation

1.  Sélectionnez l\'option **Aide → <img src="images/Std_PythonHelp.svg" width=16px> Documentation automatique des modules python** dans le menu.
2.  Cliquez sur l\'un des liens pour accéder à la documentation d\'une classe ou d\'une fonction spécifique.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std PythonHelp/fr
