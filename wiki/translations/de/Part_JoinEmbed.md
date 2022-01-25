---
- GuiCommand:/de
   Name/de:Part VerbindeEinbetten
   MenuLocation:Part → Verbinden → Objekt einbinden
   Workbenches:[Part](Part_Workbench/de.md)
   Version:0.16
   SeeAlso:[Part VerbindeEinbetten](Part_JoinEmbed/de.md), [Part FügeAusschnitt](Part_JoinCutout.md), [Part Bool'sche Operationen](Part_Boolean/de.md), [Part Dicke](Part_Thickness/de.md)
---

# Part JoinEmbed/de


</div>

## Beschreibung

Embed tool embeds a walled object (e.g., a pipe) into another walled object.

![600px](images/JoinFeatures_Embed.png)

## Anwendung

1.  Wähle zuerst das Basisobjekt, dann das Objekt, um den Ausschnitt zu definieren.
    Die Reihenfolge der Auswahl ist wichtig. Es reicht aus, nur eine Teilform jedes Objekts (z.B. Flächen) auszuwählen.
2.  Führe den Part-Objekt einbinden-Befehl aus.

A Part JoinFeature object is created, with Mode set to \'Embed\'. Original objects are hidden, and the result of embedding is shown in 3D view.

## Properties


{{TitleProperty|Base}}

-    **Base**: Reference to base object (the one the other object is to be embedded into). The object should be a single solid.

-    **Tool**: Reference to tool object (the object to be embedded). The object can be a single solid, or a [valid compound](Part_Compound.md) of solids.

-    **Mode**: The mode of operation, equals \'Embed\' (Changing that will transform the tool into another Part\_JoinXXX). The value of \'bypass\' can be used to temporarily disable the long computations (a compound of Base and Tool will be created, which is a fast operation).

-    **Refine**: Sets whether to apply [Refine](Part_RefineShape.md) operation or not, to the final shape. The default value is determined by a \'Automatically refine shape after boolean operation\' checkbox in PartDesign preferences. When Mode property is \'bypass\', Refine is ignored (never applied).

## Example


<div class="mw-translate-fuzzy">

## Beispiel

1.  Erstelle ein Rohr durch anwenden einer [Dicke](Part_Thickness/de.md) auf einen [Zylinder](Part_Cylinder/de.md):
    <img alt="" src=images/JoinFeatures_Example_step1.png  style="width:320px;">
2.  Erstelle ein weiteres Rohr mit kleinerem Durchmesser und [positioniere](Placement/de.md) es so, dass es die Wand des ersten Rohres durchstößt:
    ![320px](images/JoinFeatures_Example_step2.png)
3.  Wähle das erste Rohr, dass das zweite (die Reihenfolge der Auswahl ist wichtig), und klicke die \'Objekt einbetten\'-Option aus den Verbinden-Werkzeugen in der Werkzeugleiste.
    ![320px](images/JoinFeatures_Example_step3_Embed.png)
4.  Benutze ein Querschnitt-Werkzeug ([Std Schnittebene](Std_ToggleClipPlane/de.md), [Arch Schnittebene](Arch_SectionPlane/de.md), [Arch SchneideEbene](Arch_CutPlane/de.md)), um Schnitte darzustellen. Auf dem folgenden Bild wurde Arch Schnittebene benutzt.
    ![320px](images/JoinFeatures_Example_step4_Embed.png)


</div>

## Algorithm


<div class="mw-translate-fuzzy">

## Algorithmus

Die Algorithmen hinter den Verbindungswerkzeugen sind ziemlich einfach und es ist wichtig, sie zu verstehen, um die Werkzeuge richtig einzusetzen.


</div>

1\. Basisobjekt ist [boolesches Schneiden](Part_Cut/de.md) mit einem Tool-Objekt. Die entstandene Form ist ein Satz ([Verbund](Part_Compound/de.md)) von nicht überschneidenden Volumenkörpern (typischerweise zwei).

2\. Der entstandene Verbund ist gefiltert: nur der größte Volumenkörper bleibt übrig.

3\. Dieser größte Volumenkörper wird [verschmolzen](Part_Fuse/de.md) mit dem Werkzeug-Objekt.

3\. Falls **Refine** den Wert `True` hat, ist die entstandene Form [verfeinert](Part_RefineShape/de.md).
![800px](images/JoinFeatures-Algo-Embed.png)

### Notes


<div class="mw-translate-fuzzy">

### Hinweise

-   Falls das Objekt nach Schritt 1 ein Stück bliebt, ist das Ergebnis des Ausschnitts äquivalent zu [booleschem Schneiden](Part_Cut/de.md) der Basis mit dem Werkzeug.
-   Das Werkzeug wird nun unerwartete Ergebnisse liefern, falls ein Verbund als Basis dient. Dies könnte sich in der Zukunft ändern.
-   Weil das größte Objekt durch Volumenvergleich der Teile festgelegt wird, kann das Werkzeug nur mit Volumenkörpern arbeiten. Da

Because the largest piece is determined by comparing volumes of pieces, the tool can only work with solids. Dies könnte sich in der Zukunft ändern.


</div>

## Skripten

Die Verbinden-Werkzeuge können in [macros/de](macros/de.md) und von der Python-Konsole aus mit der folgenden Funktion verwendet werden:


```pythonJoinFeatures.makePartJoinFeature(name = 'Embed', mode = 'Embed')```

-   Creates an empty Embed feature (or other Join feature, depending on mode passed). The properties Base and Tool must be assigned explicitly, afterwards.
-   Returns the newly created object.

Beispiel:


{{code|code=
import JoinFeatures
j = JoinFeatures.makePartJoinFeature(name = 'Embed', mode = 'Embed' )
j.Base = FreeCADGui.Selection.getSelection()[0]
j.Tool = FreeCADGui.Selection.getSelection()[1]
}}

Das Werkzeug selbst ist in Python implementiert, siehe {{FileName|/Mod/Part/JoinFeatures.py}} ([GitHub link](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Part/JoinFeatures.py)) innerhalb des FreeCAD-Installationsverzeichnisses.


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part JoinEmbed/de
