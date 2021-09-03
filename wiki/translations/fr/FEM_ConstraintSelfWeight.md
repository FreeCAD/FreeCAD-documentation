---
- GuiCommand:/fr
   Name:FEM ConstraintSelfWeight
   Name/fr:FEM Contrainte de poids
   MenuLocation:Model → Mechanical Constraints → Contraindre le poids propre
   Workbenches:[FEM](FEM_Workbench/fr.md)
   SeeAlso:[Tutoriel FEM](FEM_tutorial/fr.md)
---

## Description

La contrainte de son propre poids est définie par l\'accélération gravitationnelle de 9,81 m/s\^2 qui agit sur l\'ensemble du modèle dans la direction prescrite.

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande:
2.  \* Appuyez sur le bouton **<img src="images/FEM_ConstraintSelfWeight.svg" width=16px> [Créer une contrainte de poids propre](FEM_ConstraintSelfWeight.md)**.
3.  \* Sélectionnez l\'option {{MenuCommand|Model → Mechanical Constraints → <img src="images/FEM_ConstraintSelfWeight.svg" width=16px> Contraindre le poids propre}} dans le menu.
4.  Vous pouvez modifier la direction de la gravitation en modifiant ses coordonnées vectorielles dans la barre de propriétés du nouvel objet ConstraintSelfWeight.

## Script

**Nouvel objet** 
```python
import ObjectsFem
ObjectsFem.makeConstraintSelfWeight( name )
```

**Ajouter un objet à l\'analyse nommée Analysis** 
```python
App.ActiveDocument.Analysis.Member = App.ActiveDocument.Analysis.Member + [ (object) ]
```

**Exemple:** 
```python
import ObjectsFem
selfweight_obj = ObjectsFem.makeConstraintSelfWeight( 'MySelfWeightObject' )
App.ActiveDocument.Analysis.Member = App.ActiveDocument.Analysis.Member + [selfweight_obj]

```

## Solveur CalculiX {#solveur_calculix}

### Limitations

-   Vous devez modifier le fichier .inp pour modifier l\'accélération de la gravité.
-   Le poids propre est appliqué à l\'ensemble d\'éléments Eall signifie à l\'ensemble du modèle.

### Modification du fichier d'entrée CalculiX {#modification_du_fichier_dentrée_calculix}

La constante d\'accélération peut être modifiée manuellement à la suite de la génération du fichier d\'entrée CalculiX.

Exemple de lignes dans le fichier .inp: 
```python
*DLOAD
Eall,GRAV,9810,0.0,0.0,-1.0
``` où 9810 est la magnitude de l\'accélération de la gravité en \[mm/s\^2\] et 0,0,-1 est le vecteur de direction.

## Solver Z88 {#solver_z88}

-   non implémenté dans le solveur Z88 (March 2017)





{{FEM Tools navi

}}  
