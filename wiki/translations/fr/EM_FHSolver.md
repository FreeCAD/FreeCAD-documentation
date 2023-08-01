---
- GuiCommand:
   Name:EM FHSolver
   Name/fr:EM Solveur FH
   MenuLocation:EM → FHSolver
   Workbenches:[EM](EM_Workbench/fr.md)
   Shortcut:**E** **X**
   Version:0.17
   SeeAlso:[EM  Fichier entrée FH](EM_FHInputFile/fr.md), [EM Noeud FH](EM_FHNode/fr.md), [EM Segment FH](EM_FHSegment/fr.md), [EM Chemin Fh](EM_FHPath/fr.md), [EM Plan FH](EM_FHPlane/fr.md), [EM Equivalence FH](EM_FHEquiv/fr.md), [EM Port FH](EM_FHPort/fr.md)
---

# EM FHSolver/fr

## Description

L\'outil Solveur FH insère un objet de type Solveur FH.

![](images/EM_FHSolver_Example.png )



*Objet Solveur FH*

## Utilisation

Pour insérer un objet de type Solveur FH dans le document:

1.  Appuyez sur le bouton **<img src="images/EM_FHSolver.svg" width=16px> [EM FHSolver](EM_FHSolver/fr.md)** ou appuyez sur les touches **E** puis **X**.

### Remarques

-   L\'objet Solveur FH représente les directives FastHenry qui sont nécessaires dans les sections communes du fichier d\'entrée FastHenry pour définir les paramètres de simulation, comme par exemple la liste des points de fréquence auxquels la simulation doit être exécutée, les unités de mesure par défaut, etc\... ainsi que le nom du fichier de sortie et le dossier de création du fichier d\'entrée FastHenry.

-   Vous ne devez avoir qu\'un seul objet Solveur FH par document. Si plusieurs objets Solveur FH sont présents, seul le premier sera pris en compte.

## Propriétés

-    **Units**: le \'.units\' de FastHenry. Chaque unité dans FreeCad sera une unité de l\'unité de mesure correspondante dans FastHenry. Remarque: cela signifie que vous pouvez par exemple avoir un dessin 3D dans FreeCAD avec des unités définies en mètres, et spécifier une unité de mesure différente pour FastHenry, par ex. millimètres. Ainsi, la valeur \'1.0m\' dans FreeCAD sera en fait \'1.0mm\' pour la simulation FastHenry.

-    **Sigma**: la conductivité de segment par défaut (paramètre de segment \'sigma\' dans l\'instruction FastHenry \'.default\')

-    **nhinc**: le nombre par défaut de filaments dans le sens de la hauteur (paramètre de segment \'nhinc\' dans l\'instruction FastHenry \'.default\')

-    **nwinc**: le nombre par défaut de filaments dans le sens de la largeur (paramètre de segment \'nwinc\' dans l\'instruction FastHenry \'.default\')

-    **rh**: le rapport par défaut des filaments adjacents dans le sens de la hauteur (paramètre de segment \'rh\' dans l\'instruction FastHenry \'.default\')

-    **rw**: le rapport par défaut des filaments adjacents dans le sens de la hauteur (paramètre de segment \'rw\' dans l\'instruction FastHenry \'.default\')

-    **fmin**: la fréquence de simulation la plus basse (paramètre de segment \'fmin\' dans l\'instruction FastHenry \'.freq\')

-    **fmax**: la fréquence de simulation la plus élevée (paramètre de segment \'fmax\' dans l\'instruction FastHenry \'.freq\')

-    **ndec**: le nombre de points de fréquence souhaités par décennie (paramètre de segment \'ndec\' dans l\'instruction FastHenry \'.freq\')

-    **Folder**: le chemin du dossier pour exporter le fichier au format de fichier d\'entrée FastHenry

-    **Filename**: le nom du fichier de simulation lors de l\'exportation au format de fichier d\'entrée FastHenry

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

L\'outil Solveur FH peut-être utilisé dans des [macros](Macros/fr.md) et depuis la console [Python](Python/fr.md) en utilisant la fonction suivante:


```python
node = makeFHSolver(units=None, sigma=None, nhinc=None, nwinc=None, rh=None, rw=None, fmin=None, fmax=None, ndec=None, folder=None, filename=None, name='FHSolver')
```

-   Crée un objet `FHSolver`.

-    `units`est l\'unité de mesure FastHenry. Chaque unité dans FreeCad sera une unité de l\'unité de mesure correspondante dans FastHenry. Les valeurs autorisées sont: \"km\", \"m\", \"cm\", \"mm\", \"um\", \"in\", \"mils\". La valeur par défaut est `EMFHSOLVER_DEFUNITS`

-    `sigma`est la conductivité par défaut du flotteur. La valeur par défaut est `EMFHSOLVER_DEF_SEGSIGMA`.

-    `nhinc`est le paramètre nhinc entier par défaut dans FastHenry, pour définir la discrétisation de la hauteur du segment en filaments. La valeur par défaut est `EMFHSOLVER_DEFNHINC`.

-    `nwinc`est le paramètre nwinc entier par défaut dans FastHenry, pour définir la discrétisation de la largeur du segment en filaments. La valeur par défaut est `EMFHSOLVER_DEFNWINC`.

-    `rh`est le paramètre entier par défaut rh dans FastHenry, pour définir le rapport de discrétisation de la hauteur du segment. La valeur par défaut est `EMFHSOLVER_DEFRH`.

-    `rw`est le paramètre rw par défaut entier dans FastHenry, pour définir le rapport de discrétisation de hauteur de segment. La valeur par défaut est `EMFHSOLVER_DEFRW`.

-    `fmin`est la fréquence minimale de simulation flottante

-    `fmax`est la fréquence de simulation maximale du flotteur

-    `ndec`est la valeur flottante définissant le nombre de points de fréquence par décennie qui seront simulés.

-    `folder`est le dossier dans lequel le fichier FastHenry sera enregistré. Par défaut, le chemin d\'accès à la maison de l\'utilisateur (par exemple sous Windows \"C:\\Documents and Settings\\username\\My Documents\", in Linux \"/home/username\").

-    `filename`est le nom du fichier qui sera exporté. La valeur par défaut est `EMFHSOLVER_DEF_FILENAME`.

-    `name`est le nom de l\'objet

Exemple:


```python
import FreeCAD, EM

fhsolver = EM.makeFHSolver()
```





{{EM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [EM](Category_EM.md) > EM FHSolver/fr
