# Macro Solid Sweep/de

 {{Macro/de
|Name=Solid Sweep
|Translate=Solid Sweep
|Icon=Macro_Solid_Sweep.png
|Description=Erzeugt einen Körper, indem ein Profil von einer Flugbahn gefegt wird.
|Author=Normandc
|Version=1.0
|Date=2011-12-03
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/6/6d/Macro_Solid_Sweep.png ToolBar Icon]
}}

## Beschreibung

Dieses Makro erstellt einen Körper, indem ein 2D-Profil entlang einer zuvor in der 3D-Ansicht ausgewählten Trajektorie gefegt wird. Die 2D-Elemente können mit den normalen Werkzeugen in FreeCADs GUI erstellt werden.

Mělo by být poznamenáno, že výsledná pevná látka nebude **parametrická**. Pokud se rozhodnete změnit profil nebo trajektorii, budete muset znovu spustit makro.

<img alt="Einige Beispiele für das Fegen mit dem gleichen länglichen Abschnitt und drei Arten von Flugbahnen." src=images/Solid_sweep.png‎  style="width:500px;">


<div class="mw-translate-fuzzy">

## Wie verwende ich 

-   Erstellen Sie zwei 2D-Elemente (eines für den Abschnitt und eines für die Flugbahn) der unten aufgeführten Typen.
-   Wählen Sie entweder in der Projektnavigation oder in der 3D-Ansicht zuerst die Flugbahn und dann das Profil aus. Die Reihenfolge ist wichtig!
-   Öffnen Sie den Makro-Manager, wählen Sie das Makro aus und klicken Sie auf \"Ausführen\".
-   Ein **Sweep** Objekt wird in der Projektnavigation erstellt.


</div>

## Unterstützte 2D-Elemente 

-   Leitungen
-   <img alt="" src=images/_Sketcher_NewSketch.svg  style="width:24px;"> [Sketches](Sketcher_Workbench/de.md)
-   <img alt="" src=images/_Draft_BSpline.svg  style="width:24px;"> [Entwurf BSpline](Draft_BSpline/de.md)
-   2D Grundelemente aus dem *Part → <img alt="" src=images/Part_Primitives.svg  style="width:24px;"> [Create Primitives](Part_Primitives/de.md) \...* menu (circle, helix)

## Tipps

-   Der Abschnitt muss ein geschlossenes Profil sein, oder das Ergebnis ist nicht solide.
-   Der Abschnitt muss nicht auf der Flugbahn liegen, es ist jedoch vorzuziehen, dass er normal (senkrecht) zur Flugbahn ist.
-   Die Flugbahn kann entweder ein offenes oder ein geschlossenes Profil sein (Kreis-, Linien- und Bogensegmente), aber alle Elemente müssen tangential sein, da sonst die Form unerwartet ist. Beispielsweise erzeugt eine Flugbahn mit geraden Ecken wie ein Rechteck keinen Volumenkörper.
-   Wenn der Volumenkörper verdreht wird, bearbeiten Sie das Makro, um den Wert \'\' isFrenet \'\' in 0 (Null) zu ändern, und versuchen Sie es erneut.
-   Wenn Sie die Variable \'\' makeSolid \'\' im Makro auf 0 (Null) setzen, werden mehrere Flächen mit offenen Enden erzeugt.

## Skript

ToolBar Icon ![](images/Macro_Solid_Sweep.png )

**Macro\_Solid\_Sweep.FCMacro**


{{MacroCode|code=
import Part, FreeCAD, math, PartGui, FreeCADGui
from FreeCAD import Base

# get the selected objects, with first selection for the trajectory and second for the section
s = FreeCADGui.Selection.getSelection()
try:
     shape1=s[0].Shape
     shape2=s[1].Shape
except:
     print "Wrong selection"

traj = Part.Wire([shape1])
section = Part.Wire([shape2])

# create Part objec in the current document
myObject=App.ActiveDocument.addObject("Part::Feature","Sweep")

# variable makeSolid = 1 to create solid, 0 to create surfaces
makeSolid = True #1
isFrenet = True #1

# create a 3D shape and assigh it to the current document
Sweep = Part.Wire(traj).makePipeShell([section],makeSolid,isFrenet)
myObject.Shape = Sweep

}}

## Credits

Vielen Dank an [Wmayer](User:_Wmayer.md) für seine Hilfe beim Schreiben dieses Skripts.

Zwei Anwendungsbeispiele finden Sie in [this forum topic](http://forum.freecadweb.org/viewtopic.php?f=8&t=1222&start=50#p11120), zusammen mit Download-Links zu den FCStd-Dateien. Bei Verwendung einer Helix als Flugbahn kann ein fester Durchlauf zum Erstellen eines Schraubengewindes verwendet werden.
