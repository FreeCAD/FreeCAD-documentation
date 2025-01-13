---
 GuiCommand:
   Name: Part JoinCutout
   Name/de: Part Ausschneiden
   MenuLocation: Formteil , Verbinden , Für Objekt ausschneiden
   Workbenches: Part_Workbench/de
   Version: 0.16
   SeeAlso: Part_JoinConnect/de, Part_JoinEmbed/de, Part_Boolean/de, Part_Thickness/de
---

# Part JoinCutout/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Part_JoinCutout.svg  style="width:24px;"> **Part Ausschneiden** erstellt einen Ausschnitt in einem Hohlkörper (z.B. einem Rohr), in den ein anderer Hohlkörper passt.

![600px](images/JoinFeatures_Cutout.png)



## Anwendung

1.  Zuerst das Basisobjekt auswählen, dann das Objekt zum Einbetten. Die Reihenfolge der Auswahl ist wichtig. Es reicht aus, nur eine Teilform jedes Objekts (z.B. Flächen) auszuwählen.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltflächen **<img src="images/Part_JoinCutout.svg" width=16px> [Für Objekt ausschneiden](Part_JoinCutout/de.md)** drücken.
    -   Den Menüeintrag **Part → Verbinden → <img src="images/Part_JoinCutout.svg" width=16px> Für Objekt ausschneiden** auswählen.
3.  Ein JoinFeature-Objekt wird erstellt, dessen Modus auf \'Embed\' eingestellt ist. Die originalen Objekte werden ausgeblendet und das Ergebnis des Einbettens wird in der [3D-Ansicht](3D_view/de.md) angezeigt.



## Eigenschaften


{{TitleProperty|Basis}}

-    **Base**: Reference to base object (the one to make the cutout in). The object should be a single solid.

-    **Tool**: Reference to tool object (the object that is to fit into the cutout). The object can be a single solid, or a [valid compound](Part_Compound.md) of solids.

-    **Mode**: The mode of operation, equals \'Cutout\' (Changing that will transform the tool into another Part_JoinXXX). The value of \'bypass\' can be used to temporarily disable the long computations (a compound of Base and Tool will be created, which is a fast operation).

-    **Refine**: Sets whether to apply [Refine](Part_RefineShape.md) operation or not, to the final shape. The default value is determined by a \'Automatically refine shape after boolean operation\' checkbox in PartDesign preferences. When Mode property is \'bypass\', Refine is ignored (never applied).



## Beispiel

1.  Create a pipe by applying [thickness](Part_Thickness.md) to a [cylinder](Part_Cylinder.md):
    ![320px](images/JoinFeatures_Example_step1.png)
2.  Create another, smaller diameter pipe, and [place](Placement.md) it so that it pierces the wall of the first pipe:
    ![320px](images/JoinFeatures_Example_step2.png)
3.  Select the first pipe, then the second pipe (order of selection is important), and click the \'Cutout for object\' option from the Join tools dropdown toolbar button.
    ![320px](images/JoinFeatures_Example_step3_Cutout.png)



## Algorithmus

Die Algorithmen hinter den Verbindungswerkzeugen sind ziemlich einfach und es ist wichtig, sie zu verstehen, um die Werkzeuge richtig einzusetzen.

1\. Basisobjekt ist [boolesches Schneiden](Part_Cut/de.md) mit einem Tool-Objekt. Die entstandene Form ist ein Satz ([Verbund](Part_Compound/de.md)) von nicht überschneidenden Volumenkörpern (typischerweise zwei).

2\. Der entstandene Verbund ist gefiltert: nur der größte Volumenkörper bleibt übrig.

3\. Falls **Refine** den Wert `True` hat, ist die entstandene Form [verfeinert](Part_RefineShape/de.md).
![800px](images/JoinFeatures-Algo-Cutout.png)



### Hinweise

-   Falls das Objekt nach Schritt 1 ein Stück bliebt, ist das Ergebnis des Ausschnitts äquivalent zu [booleschem Schneiden](Part_Cut/de.md) der Basis mit dem Werkzeug.
-   Das Werkzeug wird nun unerwartete Ergebnisse liefern, falls ein Verbund als Basis dient. Dies könnte sich in der Zukunft ändern.
-   Weil das größte Objekt durch Volumenvergleich der Teile festgelegt wird, kann das Werkzeug nur mit Volumenkörpern arbeiten. Da

Because the largest piece is determined by comparing volumes of pieces, the tool can only work with solids. Dies könnte sich in der Zukunft ändern.



## Skripten

Die Verbinden-Werkzeuge können in [macros/de](macros/de.md) und von der Python-Konsole aus mit der folgenden Funktion verwendet werden:


```pythonJoinFeatures.makePartJoinFeature(name = 'Cutout', mode = 'Cutout')```

-   Creates an empty Cutout feature (or other Join feature, depending on mode passed). The properties Base and Tool must be assigned explicitly, afterwards.
-   Returns the newly created object.

Beispiel: {{code|code=
import JoinFeatures
j = JoinFeatures.makePartJoinFeature(name = 'Cutout', mode = 'Cutout' )
j.Base = FreeCADGui.Selection.getSelection()[0]
j.Tool = FreeCADGui.Selection.getSelection()[1]
}}

Das Werkzeug selbst ist in Python implementiert, siehe **/Mod/Part/JoinFeatures.py** ([GitHub link](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Part/JoinFeatures.py)) innerhalb des FreeCAD-Installationsverzeichnisses.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part JoinCutout/de
