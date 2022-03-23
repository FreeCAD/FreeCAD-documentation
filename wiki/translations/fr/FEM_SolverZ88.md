---
- GuiCommand:/fr
   Name:FEM SolverZ88
   Name/fr:FEM Solveur Z88
   MenuLocation:Solve → Solveur Z88
   Workbenches:[FEM](FEM_Workbench/fr.md)
   Shortcut:**S** **Z**
   SeeAlso:[FEM Tutoriel](FEM_tutorial/fr.md)
---

# FEM SolverZ88/fr

## Description

[Solveur Z88](FEM_SolverZ88/fr.md) permet d\'utiliser le solveur [Z88](https://en.wikipedia.org/wiki/Z88_FEM_software). Il peut être utilisé pour :

1.  Définir les paramètres d\'analyse
2.  Sélectionner le répertoire de travail
3.  Exécuter le solveur Z88

## Installation

Pour utiliser le solveur Z88, la version OpenSource de Z88 (Z88OS) doit être installée :

1.  Téléchargez le fichier ZIP à partir du [site web Z88OS](https://en.z88.de/download-z88os).
2.  Extraire le ZIP dans un dossier de votre choix.
3.  Dans les [FEM Préférences](FEM_Preferences/fr.md), allez dans l\'onglet Z88 et définissez le chemin vers le binaire **z88r**. Si vous êtes sous Windows, ce sera le chemin vers le fichier {{FileName|z88r.exe}} qui se trouve dans le sous-dossier {{FileName|~\bin\win64}} du dossier où vous avez extrait le ZIP.

## Utilisation

1.  Après la création d\'un <img alt="" src=images/FEM_Analysis.svg  style="width:16px;"> [Conteneur d\'analyse](FEM_Analysis/fr.md), utilisez l\'une des alternatives suivantes :
    -   Sélectionnez **Solveur → <img src="images/FEM_SolverZ88.svg" width=x16px> Solveur Z88** dans le menu.
    -   Appuyez sur les touches de raccourci **S** puis **Z**.
2.  Double-cliquez sur l\'objet <img alt="" src=images/FEM_SolverZ88.svg  style="width:" height="16px;"> SolverZ88.
3.  Sélectionnez le type d\'analyse.
4.  Cliquez sur le bouton **Écrire**.
5.  Cliquez sur le bouton **Exécuter**.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM SolverZ88/fr
