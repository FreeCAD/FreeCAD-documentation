# Macro Stairs/it
{{Macro/it
|Name=Macro Stairs
|Translate=Scala a chiocciola
|Icon=Macro_Stairs.png
|Description=Crea una scala a chiocciola.
|Author=Mario52
|Version=00.05
|Date=2023-08-11
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/a/a3/Macro_Stairs.png ToolBar Icon]
}}



## Descrizione

Crea una scala a chiocciola

<img alt="" src=images/Macro_CircularStair.png  style="width:480px;">



## Utilizzo

Creare lo scalino modello, selezionare l\'oggetto e avviare la macro

-   **Hmarche** : alzata dello scalino
-   **nombre** : numero di scalini per giro
-   **rayon** : raggio (rispetto all\'asse dello scalino)
-   **tours** : numero di giri
-   **cloner** : 1=crea cloni 0=crea copie
-   **cylindre** : 1=crea cilindro 0=senza cilindro (piantone)
-   **degres** : 360 \# numero di gradi di rotazione (default 360)

## Script

Icona barra strumenti ![](images/Macro_Stairs.png )

**Macro_Stairs.FCMacro**


{{MacroCode|code=

# Select your object(s) give :
#     head marche
#     number objects for 1 turn
#     radius (axe to object)
#     number turns
# the original object is not modify
# Macro_Stairs.FCMacro
# 
#01/03/2015 2019/07/24
import FreeCAD, Draft, Part

__title__   = "CircularStair"
__author__  = "Mario52"
__date__    = "2023/08/11"
__url__     = "http://www.freecadweb.org/index-fr.html"
__wiki__    = "https://www.freecadweb.org/wiki/Macro_Stairs"
__version__ = "00.05"

############## Modify here ####################
Hmarche  = 5  # head marche
nombre   = 5  # number objects for 1 turn
rayon    = 20  # radius (axe to object)
tours    = 2  # nomber turns pitch 
cloner   = 1   # 1=clone    0=copy
cylindre = 1   # 1=create cylinder  0=not cylinder
degres   = 360  # number of degrees  (default 360)
###############################################


try:
    sel = FreeCADGui.Selection.getSelection()[0]

    vecligne=[FreeCAD.Vector(0.0,0.0,0.0),FreeCAD.Vector(rayon,0.0,0.0)]   # vector for line directrice
    ligne = Draft.makeWire(vecligne,closed=False,face=False,support=None)  # creation de la ligne de base
    FreeCAD.ActiveDocument.openTransaction("Stair: Line")    # memorise les actions (avec annuler restore)

    coor_X = coor_Y = coor_Z = 0.0
    for i0 in range(tours):
        for i in range(0,degres,(int(degres/nombre))):                                  # boucle principale 0 to 360 degrees
            FreeCAD.ActiveDocument.openTransaction("Stair:" + str(i0) + "/" + str(i))    # memorise les actions (avec annuler restore)

            FreeCAD.ActiveDocument.getObject(ligne.Name).Placement=App.Placement(App.Vector(0,0,coor_Z), App.Rotation(App.Vector(0,0,1),i), App.Vector(0,0,0))
            try:
                a = ligne.Shape.Edges[0].Vertexes[1]       # fin de la ligne
                coor_X = (a.Point.x)
                coor_Y = (a.Point.y)
            except Exception:
                a = ligne.End         
                coor_X = (ligne.End.x)                      # fin de la ligne X
                coor_Y = (ligne.End.y)                      # fin de la ligne Y        if cloner == 1:
                obj=Draft.clone(sel)
            else:
                obj = Draft.scale(sel,delta=App.Vector(1, 1, 1),center=App.Vector(),copy=True,legacy=True)
            try:
                for io in range(len(obj)):
                    obj[io].Placement=App.Placement(App.Vector(coor_X,coor_Y,coor_Z), App.Rotation(i,0,0), App.Vector(0,0,0))
            except Exception:
                obj.Placement=App.Placement(App.Vector(coor_X,coor_Y,coor_Z), App.Rotation(i,0,0), App.Vector(0,0,0))        coor_Z += Hmarche
    App.ActiveDocument.removeObject(ligne.Name)                            # remove ligne de base directrice# create cylinder
    if cylindre == 1:
        FreeCAD.ActiveDocument.openTransaction("Stair: Cylinder")    # memorise les actions (avec annuler restore)
        App.ActiveDocument.addObject("Part::Cylinder","Cylinder")
        App.ActiveDocument.ActiveObject.Label = "Cylindre"
        FreeCAD.ActiveDocument.ActiveObject.Height = (Hmarche * nombre * tours)    # heigth of cylinder
        FreeCAD.ActiveDocument.ActiveObject.Radius = (rayon)                       # radius of cylinderFreeCAD.ActiveDocument.recompute()
except Exception:
    App.Console.PrintError(u"Select the stair treads")

}}



## Collegamenti

La discussione nel forum [Newbie question - spiral stairs reloaded](http://forum.freecadweb.org/viewtopic.php?f=3&t=9921)



---
⏵ [documentation index](../README.md) > Macro Stairs/it
