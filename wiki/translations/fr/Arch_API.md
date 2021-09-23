# Arch API/fr
 **(November 2018) L'API Arch est répertoriée dans la [https://www.freecadweb.org/api documentation API générée automatiquement].**

Les fonctions de l\'API font partie de l\'atelier [Arch](Arch_Workbench/fr.md) et peuvent être utilisées dans des [macros](macros/fr.md) et à partir de la console [Python](Python/fr.md) une fois que le module `Arch` a été importé. L\'atelier [renforcement](Reinforcement_Addon/fr.md) a ses propres [API de renforts](Reinforcement_API/fr.md).

Exemple: 
```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)

Arch.makeWall(baseline, length=None, width=200, height=2000)
```


 

[Category:API](Category:API.md) [Category:Poweruser Documentation](Category:Poweruser_Documentation.md)
