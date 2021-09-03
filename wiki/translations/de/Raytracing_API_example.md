

## Einleitung

Die `Raytracing` und `RaytracingGui` Module bieten mehrere Methoden, um Szeneinhalte als Povray- oder Luxrender Daten zu schreiben.

Die nützlichsten Befehle sind `Raytracing.getPartAsPovray()` und `Raytracing.getPartAsLux()`, um ein FreeCAD Part Objekt in eine Povray oder Luxrender Definition und `RaytracingGui zu rendern.povViewCamera()` und `RaytracinGui.luxViewCamera()`, um den aktuellen Blickwinkel des 3D Ansichtsfensters in das Povray- oder Luxrender Format zu bringen.

## Ausgabe von Renderdateien 

Hier ist, wie man eine povray-Datei aus Python schreibt, vorausgesetzt, das Dokument enthält ein \"Box\"-Objekt:


```python
import Raytracing,RaytracingGui
OutFile = open('C:/Documents and Settings/jriegel/Desktop/test.pov','w')
OutFile.write(open(App.getResourceDir()+'Mod/Raytracing/Templates/ProjectStd.pov').read())
OutFile.write(RaytracingGui.povViewCamera())
OutFile.write(Raytracing.getPartAsPovray('Box',App.activeDocument().Box.Shape,0.800000,0.800000,0.800000))
OutFile.close()
del OutFile
```

Und das Gleiche für Luxrender:


```python
import Raytracing,RaytracingGui
OutFile = open('C:/Documents and Settings/jriegel/Desktop/test.lxs','w')
OutFile.write(open(App.getResourceDir()+'Mod/Raytracing/Templates/LuxClassic.lxs').read())
OutFile.write(RaytracingGui.luxViewCamera())
OutFile.write(Raytracing.getPartAsLux('Box',App.activeDocument().Box.Shape,0.800000,0.800000,0.800000))
OutFile.close()
del OutFile
```

## Erzeugen eines benutzerdefinierten Renderobjekts 

Neben den standardmäßigen Povray- und Luxrender Ansichtsobjekten, die eine Ansicht eines vorhandenen Part Objekts bieten und die jeweils in Povray- und Luxrender Projekte eingefügt werden können, existiert ein drittes Objekt, genannt RaySegment, das entweder in Povray- oder Luxrender Projekte eingefügt werden kann. Dieses RaySegment Objekt ist nicht mit einem der FreeCAD Objekte verknüpft und kann benutzerdefinierten Povray- oder Luxrender Code enthalten, den Sie möglicherweise in Ihr Raytracing Projekt einfügen möchten. Du kannst es auch verwenden, um z.B. deine FreeCAD Objekte auf eine bestimmte Weise auszugeben, wenn du mit dem Standardweg nicht zufrieden bist. Du kannst es so von der Python Konsole aus erstellen und verwenden:


```python
myRaytracingProject = FreeCAD.ActiveDocument.PovProject
myCustomRenderObject = FreeCAD.ActiveDocument.addObject("Raytracing::RaySegment","myRenderObject")
myRaytracingProject.addObject(myCustomRenderObject)
myCustomRenderObject.Result = "// Hello from python!"
```


{{Powerdocnavi

}} {{Raytracing Tools navi}} 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md)
