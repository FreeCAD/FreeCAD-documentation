 {{Macro/it
|Name=Rotate View Free
|Icon=Text_console_python.png
|Description=Questa def incollata nella console Python FreeCAD (o la tua macro) ti permette di ruotare la vista in 3 assi e l'angolo (in gradi) dà interesse a creare un piano per una posizione desiderata
|Author=Yorik
|Version=01.00
|Date=2010-11-17
|FCVersion=All
|SeeAlso=<img src=images/Macro_Rotate_View_view_90_Degrees.png style="width:Macro Rotate View](Macro_Rotate_View/it.md) [24px"><br /><img src=images/Macro_Rotate_View_with_Y_pointing_upwards_.png style="width:Macro_Rotate_ViewAxonometric](Macro_Rotate_ViewAxonometric/it.md) [24px"> <img src=images/Macro_Rotate_View_with_Z_pointing_upwards_.png style="width:24px">
}}

## Descrizione

Questa def incollata nella console Python FreeCAD (o la tua macro) ti permette di ruotare la vista in 3 assi e l\'angolo (in gradi) dà interesse a creare un piano per una posizione desiderata


<div class="mw-translate-fuzzy">

## Utilizzo


</div>

Incolla il codice nella console di Python FreeCAD e digita **Enter** → **Enter** (per validare) e entra ex: {{ColoredText|**RotateView(0,1,0,45)** }}

## Script

**Macro\_Rotate\_View\_Free.FCMacro**


{{MacroCode|code=
#Paste in the Python console and tip ex:
#RotateView(0,1,0,45)
def RotateView(axisX=1.0,axisY=0.0,axisZ=0.0,angle=45.0):
    import math
    from pivy import coin
    try:
        cam = Gui.ActiveDocument.ActiveView.getCameraNode()
        rot = coin.SbRotation()
        rot.setValue(coin.SbVec3f(axisX,axisY,axisZ),math.radians(angle))
        nrot = cam.orientation.getValue() * rot
        cam.orientation = nrot
        print( axisX," ",axisY," ",axisZ," ",angle)
    except Exception:
        print( "Not ActiveView ")


}}

entra nelle consola Python esempio :


{{MacroCode|code=
RotateView(0,1,0,45)
}}

Se non ci sono documenti aperti viene restituito un errore.




