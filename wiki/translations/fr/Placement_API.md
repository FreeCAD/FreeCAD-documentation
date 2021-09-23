# Placement API/fr
 **(Octobre 2019) Ne modifiez pas cette page. L'information est incomplète et obsolète. Pour la dernière API, consultez la [https://www.freecadweb.org/api documentation de l'API générée automatiquement], ou générez la documentation vous-même, voir [Source documentation](Source_documentation/fr.md).**

Dans FreeCAD,le Placement définit la position et la rotation d\'un objet. Le concept de placement est expliqué en détail ici: [ Placement](Placement.md).

Exemple de réglage du placement d\'un document objet: 
```python
myObj = FreeCAD.ActiveDocument.ActiveObject
pl = FreeCAD.Placement()
pl.move(FreeCAD.Vector(2,0,0))
myObj.Placement = pl
```


{{APIClass | Placement |) ou (Placement) ou (Matrice) ou (Base, Rotation) ou (Base, Rotation, Centre) ou (Base, Axes, Angle | Construit un placement, vide ou avec les arguments donnés, ou une copie de l'emplacement donné.}}


{{APIProperty | Base  |. Un vecteur représentant la position du Placement}}

{{APIProperty | Rotation |. Un quaternion ( nombre complexe formé de quatre unités scalaires)  représentant la rotation du Placement}} {{APIFunction | inverse | | calcule le placement inverse |. Un placement}} {{APIFunction | move | Vecteur | déplace le placement le long du vecteur donnée | rien}} {{APIFunction | multVec | Vecteur | applique le placement au vecteur donné | le vecteur résultant}.} {{APIFunction | multipliez | Placement | multiplie ce placement avec l'autre | le placement résultant}.} {{APIFunction | toMatrix | | |. Une matrice représentant la transformation du placement}}


[[Category:API\]\] 

[Category:Poweruser Documentation](Category:Poweruser_Documentation.md)
