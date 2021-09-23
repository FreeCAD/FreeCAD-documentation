# Raytracing API example/it
## Introduzione

I moduli `Raytracing` e `RaytracingGui` forniscono diversi metodi per scrivere i contenuti della scena come dati povray o luxrender.

I comandi più utili sono `Raytracing.getPartAsPovray()` e `Raytracing.getPartAsLux()` per rendere un oggetto Part di FreeCAD in una definizione povray o luxrender e `RaytracingGui.povViewCamera( )` e `RaytracinGui.luxViewCamera()` per ottenere il punto di vista corrente della finestra della vista 3D in formato povray o luxrender.

## Emissione dei file di rendering 

Ecco come utilizzare le funzionalità tramite Python, supponendo che il documento contenga un oggetto \"Box\":


```python
import Raytracing,RaytracingGui
OutFile = open('C:/Documents and Settings/jriegel/Desktop/test.pov','w')
OutFile.write(open(App.getResourceDir()+'Mod/Raytracing/Templates/ProjectStd.pov').read())
OutFile.write(RaytracingGui.povViewCamera())
OutFile.write(Raytracing.getPartAsPovray('Box',App.activeDocument().Box.Shape,0.800000,0.800000,0.800000))
OutFile.close()
del OutFile
```

E la stessa cosa per luxrender:


```python
import Raytracing,RaytracingGui
OutFile = open('C:/Documents and Settings/jriegel/Desktop/test.lxs','w')
OutFile.write(open(App.getResourceDir()+'Mod/Raytracing/Templates/LuxClassic.lxs').read())
OutFile.write(RaytracingGui.luxViewCamera())
OutFile.write(Raytracing.getPartAsLux('Box',App.activeDocument().Box.Shape,0.800000,0.800000,0.800000))
OutFile.close()
del OutFile
```

## Creare un oggetto render personalizzato 

Oltre agli oggetti di vista standard povray e luxrender che forniscono una vista di un oggetto Part esistente e che possono essere inseriti rispettivamente in progetti povray e luxrender, esiste un terzo oggetto, chiamato RaySegment, che può essere inserito in progetti povray o luxrender. L\'oggetto RaySegment non è collegato ad alcuno degli oggetti di FreeCAD e può contenere del codice povray o luxrender personalizzato, che può essere inserito in un progetto raytracing. Ad esempio, può essere usato per generare gli oggetti di FreeCAD in un certo modo, se non si è soddisfatti del modo standard. Dalla console di Python può essere creato e usato in questo modo:


```python
myRaytracingProject = FreeCAD.ActiveDocument.PovProject
myCustomRenderObject = FreeCAD.ActiveDocument.addObject("Raytracing::RaySegment","myRenderObject")
myRaytracingProject.addObject(myCustomRenderObject)
myCustomRenderObject.Result = "// Hello from python!"
```


{{Powerdocnavi

}} {{Raytracing Tools navi}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)

---
[documentation index](../README.md) > [Raytracing](Raytracing_Workbench.md) > Raytracing API example/it
