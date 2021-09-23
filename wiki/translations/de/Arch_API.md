# Arch API/de
**(November 2018) Diese Information kann unvollständig und veraltet sein. Für die letzte API siehe die (engl.) [https://www.freecadweb.org/api autogenerierte API-Dokumentation].**

Die Funktionen der API sind Teil des [Arch-Arbeitsbereichs](Arch_Workbench/de.md) und können in [Makros](macros/de.md) und in der [Python](Python/de.md)-Konsole verwendet werden, sobald das `Arch`-Modul importiert wurde. Das [Reinforcement-Addon](Reinforcement_Addon/de.md) hat seine eigene [Reinforcement-API](Reinforcement_API/de.md).

Beispiel: 
```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)

Arch.makeWall(baseline, length=None, width=200, height=2000)
```


 

[Category:API](Category:API.md) [Category:Poweruser Documentation](Category:Poweruser_Documentation.md)

---
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch API/de
