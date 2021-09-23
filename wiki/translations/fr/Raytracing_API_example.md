# Raytracing API example/fr
## Introduction

Les modules `Raytracing` et `RaytracingGui` fournissent plusieurs méthodes pour écrire le contenu d\'une scène sous forme de données povray ou luxrender.

Les commandes les plus utiles sont `Raytracing.getPartAsPovray ()` et `Raytracing.getPartAsLux ()` pour restituer un objet Part FreeCAD dans une définition de type povray ou luxrender et `RaytracingGui.povViewCamera ()` et `RaytracinGui.luxViewCamera ()` pour obtenir le point de vue actuel de la fenêtre de vue 3D au format povray ou luxrender.

## Sortie de fichiers de rendu 

Voici comment écrire un fichier Povray à partir de python, en supposant que votre document contienne un objet \"Box\":


```python
import Raytracing,RaytracingGui
OutFile = open('C:/Documents and Settings/jriegel/Desktop/test.pov','w')
OutFile.write(open(App.getResourceDir()+'Mod/Raytracing/Templates/ProjectStd.pov').read())
OutFile.write(RaytracingGui.povViewCamera())
OutFile.write(Raytracing.getPartAsPovray('Box',App.activeDocument().Box.Shape,0.800000,0.800000,0.800000))
OutFile.close()
del OutFile
```

La même chose pour Luxrender:


```python
import Raytracing,RaytracingGui
OutFile = open('C:/Documents and Settings/jriegel/Desktop/test.lxs','w')
OutFile.write(open(App.getResourceDir()+'Mod/Raytracing/Templates/LuxClassic.lxs').read())
OutFile.write(RaytracingGui.luxViewCamera())
OutFile.write(Raytracing.getPartAsLux('Box',App.activeDocument().Box.Shape,0.800000,0.800000,0.800000))
OutFile.close()
del OutFile
```

## Créer un objet de rendu personnalisé 

Outre les objets de vue standard povray et luxrender qui fournissent une vue d\'un objet Part existant et qui peuvent être insérés dans des projets povray et luxrender, il existe un troisième objet, appelé RaySegment, pouvant être inséré dans des projets povray ou luxrender. Cet objet RaySegment n\'est lié à aucun des objets FreeCAD et peut contenir du code povray ou luxrender personnalisé que vous pourriez souhaiter insérer dans votre projet Raytracing. Vous pouvez également l\'utiliser, par exemple, pour générer vos objets FreeCAD d\'une certaine manière, si vous n\'êtes pas satisfait de la manière standard. Vous pouvez le créer et l\'utiliser comme ceci depuis la console python:


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
[documentation index](../README.md) > [Raytracing](Raytracing_Workbench.md) > Raytracing API example/fr
