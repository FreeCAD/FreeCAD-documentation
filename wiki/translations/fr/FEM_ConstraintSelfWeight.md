---
- GuiCommand:/fr
   Name:FEM ConstraintSelfWeight
   Name/fr:FEM Contrainte du poids propre
   MenuLocation:Modèle → Contraintes mécaniques → Contrainte du poids propre
   Workbenches:[FEM](FEM_Workbench/fr.md)
   SeeAlso:[FEM Tutoriel](FEM_tutorial/fr.md)
---

# FEM ConstraintSelfWeight/fr

## Description

La contrainte du propre poids est définie par l\'accélération gravitationnelle de 9,81 m/s\^2 qui agit sur l\'ensemble du modèle dans la direction imposée.

## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
2.  \* Appuyez sur le bouton **<img src="images/FEM_ConstraintSelfWeight.svg" width=16px> [Contrainte du poids propre](FEM_ConstraintSelfWeight/fr.md)**.
3.  \* Sélectionnez l\'option **Modèle → Contraintes mécaniques → <img src="images/FEM_ConstraintSelfWeight.svg" width=16px> Contrainte du poids propre** dans le menu.
4.  Vous pouvez modifier la direction de la gravitation en modifiant ses coordonnées vectorielles dans la barre de propriétés du nouvel objet ConstraintSelfWeight.

## Script

Nouvel objet :


```python
import ObjectsFem
ObjectsFem.makeConstraintSelfWeight(name)
```

Ajoutez un objet à l\'analyse nommée Analysis :


```python
App.ActiveDocument.Analysis.Member = App.ActiveDocument.Analysis.Member + [(object)]
```

Exemple :


```python
import ObjectsFem
selfweight_obj = ObjectsFem.makeConstraintSelfWeight("MySelfWeightObject")
App.ActiveDocument.Analysis.Member = App.ActiveDocument.Analysis.Member + [selfweight_obj]
```

## Solveur CalculiX 

### Limitations

-   Vous devez modifier le fichier .inp pour modifier l\'accélération de la gravité.
-   Le poids propre est appliqué à l\'ensemble d\'éléments Eall signifie à l\'ensemble du modèle.

### Modification du fichier d'entrée CalculiX 

La constante d\'accélération peut être modifiée manuellement à la suite de la génération du fichier d\'entrée CalculiX.

Exemple de lignes dans le fichier .inp :


```python
*DLOAD
Eall,GRAV,9810,0.0,0.0,-1.0
```

où 9810 est la magnitude de l\'accélération de la gravité en \[mm/s\^2\], et 0,0,-1 est le vecteur directionnel.

## Solver Z88 

-   non implémenté dans le solveur Z88 (March 2017)





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintSelfWeight/fr
