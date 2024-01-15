---
 GuiCommand:
   Name: FEM ConstraintSelfWeight
   Name/fr: FEM Charge de gravité
   MenuLocation: Modèle , Conditions limites et charges mécaniques , Charge de gravité
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_tutorial/fr
---

# FEM ConstraintSelfWeight/fr

## Description

Cette commande définit une accélération gravitationnelle de 9,81 m/s\^2 agissant sur l\'ensemble du modèle dans la direction prescrite.



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyer sur le bouton **<img src="images/FEM_ConstraintSelfWeight.svg" width=16px> [Charge de gravité](FEM_ConstraintSelfWeight/fr.md)**.
    -   Sélectionner l\'option **Modèle → Conditions limites et charges mécaniques → <img src="images/FEM_ConstraintSelfWeight.svg" width=16px> Charge de gravité** du menu.
2.  Vous pouvez modifier la direction de la charge de gravité en modifiant ses coordonnées vectorielles dans la barre des propriétés du nouvel objet ConstraintSelfWeight.



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
-   Le poids propre est appliqué à l\'élément Eall qui comprend le modèle entier.



### Modification du fichier d'entrée CalculiX 

La constante d\'accélération peut être éditée manuellement après avoir généré le fichier d\'entrée de CalculiX.

Exemple de lignes dans le fichier .inp :


```python
*DLOAD
Eall,GRAV,9810,0.0,0.0,-1.0
```

où 9810 est la magnitude de l\'accélération de la pesanteur en \[mm/s\^2\], et 0,0,-1 est le vecteur de direction. La valeur peut être définie comme un multiple de l\'accélération standard de la pesanteur pour simuler une charge de 4g par exemple.



## Solveur Z88 

-   Pour le moment, non implémenté dans le solveur Z88.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintSelfWeight/fr
