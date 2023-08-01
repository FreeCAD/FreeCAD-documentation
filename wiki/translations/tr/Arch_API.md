# Arch API/tr
**(Kasım 2018) YAPI API, [https://www.freecadweb.org/api otomatikleştirilmiş API belgelerinde] listelenmiştir.**

API\'nin işlevleri [Yapı tezgahın](Arch_Workbench/tr.md) \'ın bir parçasıdır ve `Arch` modülü alındıktan sonra [makrolar](macros/tr.md) ve [Python](Python.md) konsolundan kullanılabilir. [Takviye Eklentisi](Reinforcement_Addon.md) kendi [Reinforcement API](Reinforcement_API.md) \'ye sahiptir.

Örnek: 
```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)

Arch.makeWall(baseline, length=None, width=200, height=2000)
```



---
⏵ [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Arch](Arch_Workbench.md) > Arch API/tr
