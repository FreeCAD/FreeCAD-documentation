---
- GuiCommand:/fr
   Name:FEM Analysis
   Name/fr:FEM Conteneur d'analyse
   MenuLocation:Model → Conteneur d'analyse
‎   Workbenches:[FEM](FEM_Workbench/fr.md)
   Shortcut:**S** **A**
   SeeAlso:[Tutoriel FEM](FEM_tutorial/fr.md)
---

## Description

Le module FEM ([Méthode d\'éléments finis](https://fr.wikipedia.org/wiki/M%C3%A9thode_des_%C3%A9l%C3%A9ments_finis)) peut être considéré comme un conteneur qui contient tous les composants utiles servants à l\'analyse d\'éléments finis. Il est nécessaire de posséder un conteneur qui détient tous les objets nécessaires pour l\'analyse. Au moins un des objets suivants est nécessaire pour une analyse mécanique:

-   [matériau](FEM_MaterialSolid/fr.md)
-   [contrainte fixée](FEM_ConstraintFixed/fr.md)
-   [contrainte de force](FEM_ConstraintForce/fr.md) ou [contrainte de pression](FEM_ConstraintPressure/fr.md)

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/FEM_Analysis.svg" width=16px> [Créer un conteneur d'analyse...](FEM_Analysis/fr.md)**.
    -   Sélectionnez l\'option **Model → <img src="images/FEM_Analysis.svg" width=16px> Conteneur d'analyse** dans le menu.
    -   Utilisez le raccourci clavier: **S** puis **A**.
2.  Une nouvelle analyse est créée et définie sur active.
3.  D\'autres objets peuvent être ajoutés ou retirés du conteneur d\'analyse par glisser-déposer.
4.  Pour ajouter un nouvel objet à analyser dans le conteneur, le conteneur FEM doit être actif. Double cliquez sur l\'élément dans le conteneur permet d\'activer l\'analyse.

## Options

-   A ce jour il n\'y a pas d\'option de choix.
-   le module FEM est toujours en développement. Rendez vous sur le forum [1](http://forum.freecadweb.org/viewtopic.php?f=18&t=12189) pour plus d\' informations.

## Propriétés

-    {{PropertyData/fr|OutpuDir}}: Spécifie le répertoire de travail pour l\'analyse

## Script

La plupart des codes ci dessous sont obsolète dans la version 0.17.

-   nouvelle analyse


```python
MechanicalAnalysis.makeMechanicalAnalysis( name )
```

-   ajouter un objet à analyser


```python
App.ActiveDocument.MechanicalAnalysis.Member = App.ActiveDocument.MechanicalAnalysis.Member + [ (object) ]
```

-   effacer un objet du conteneur


```python
member = App.ActiveDocument.MechanicalAnalysis.Member
member.remove( documentobject )
 App.ActiveDocument.MechanicalAnalysis.Member = member
```

Exemples: 
```python
import MechanicalAnalysis
analysis = MechanicalAnalysis.makeMechanicalAnalysis("MechanicalAnalysis")
FemGui.setActiveAnalysis(analysis)

addobj = App.ActiveDocument.getObject("MechanicalMaterial")
App.ActiveDocument.MechanicalAnalysis.Member = App.ActiveDocument.MechanicalAnalysis.Member + [addobj]

removeobj = App.ActiveDocument.getObject("MechanicalMaterial")
member = App.ActiveDocument.MechanicalAnalysis.Member
member.remove(removeobj)
App.ActiveDocument.MechanicalAnalysis.Member = member
```





{{FEM Tools navi

}} 
