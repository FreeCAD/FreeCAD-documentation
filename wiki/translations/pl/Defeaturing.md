# Defeaturing/pl
## Wprowadzenie

Usuwanie cech modelu 3D zostało dodane w Open CASCADE 7.3 [1](https://dev.opencascade.org/index.php?q=node/1211) i może być używane do edycji modeli STEP poprzez usuwanie cech z modelu.

Możliwe jest również bezpośrednie modelowanie modelu, gdy historia operacji jest niedostępna. *(Tak jest w przypadku modeli 3D STEP)*. Usuwanie cech może być również przydatne do usuwania zastrzeżonych szczegółów modelu przed jego udostępnieniem.

Najprostszym sposobem na użycie usuwania cech jest użycie środowiska pracy [Defeaturing](Defeaturing_Workbench/pl.md).

## Wycinek kodu 

Środowisko pracy Defeaturing może być również używane w środowisku Python: 
```python
box = Part.makeBox(10,10,10)
box2 = Part.makeBox(5,5,5,FreeCAD.Vector(5,5,0))
box3 = box.cut(box2)
Part.show(box3)
faces = App.ActiveDocument.ActiveObject.Shape.Faces[6:] #the faces of box3 that are part of the corner pocket
box4 = App.ActiveDocument.ActiveObject.Shape.defeaturing(faces) #defeature the shape
Part.show(box4) #show defeatured shape
```

<img alt="" src=images/box3.PNG  style="width:200px;"> 
*Kształt Box3 użyty w kodzie Pythona, przed usunięciem cech* <img alt="" src=images/box4.PNG  style="width:200px;"> 
*Kształt Box4 używany w kodzie Pythona, zdegradowany*



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > Defeaturing/pl
