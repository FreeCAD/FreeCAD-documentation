# Arch API/pl
**''(Listopad 2018)'' Arch API jest wymieniony w [https://www.freecadweb.org/api automatycznie generowanej dokumentacji API].**

Funkcje API są częścią Środowiska pracy [Architektura](Arch_Workbench/pl.md) i mogą być używane w [makrodefinicjach](macros/pl.md) i z konsoli [Python](Python/pl.md) po zaimportowaniu modułu `Arch`. Dodatek [Zbrojenie](Reinforcement_Workbench/pl.md) ma swoje własne [skrypty](Reinforcement_API/pl.md).

Przykład: 
```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)

Arch.makeWall(baseline, length=None, width=200, height=2000)
```



---
⏵ [documentation index](../README.md) > [API](Category_API.md) > [Poweruser_Documentation](Category_Poweruser_Documentation.md) > [BIM](Category_BIM.md) > Arch API/pl
