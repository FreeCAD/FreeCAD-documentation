---
- GuiCommand:
   Name: Part Section
   Name/de: Part Schnittkurve
   MenuLocation: Formteil -> Schnittkurve
   Workbenches: Part_Workbench/de
   SeeAlso: Part_CrossSections/de
---

# Part Section/de



## Beschreibung

Der Befehl <img alt="" src=images/Part_Section.svg  style="width:24px;"> **Part Schnittkurve** erstellt Drahtgeometrien (Linienzüge) an den Schnittkanten zweier Objekte. Das Ergebnis ist vollständig parametrisch.

-   Der Schnitt zweier Festkörper oder Flächen resultiert in einer oder mehreren Schnittlinien.
-   Der Schnitt zweier Linien oder einer Linie mit einem Festkörper oder einer Fläche resultiert in einem oder mehreren Punkten.

![](images/PartSection1_it.png ) 
*Ein Würfel mit einem Zylinder geschnitten*



## Anwendung

1.  Zwei Objekte Auswählen.
2.  Das erste Objekt wird zur {{PropertyData/de|Basis}} des Schnitts, aber die Auswahlreihenfolge hat keinen Einfluss auf das Ergebnis.
3.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **![](images/)_[Schnittkurve](Part_Section/de.md)** drücken.
    -   Den Menüeintrag **Part → ![](images/)_Schnittkurve**_auswählen.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein PartDesign-Section-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{Properties_Title|Base}}

-    **Base|Link**: Link to the first object.

-    **Tool|Link**: Link to the second object.


{{Properties_Title|Boolean}}

-    **History|ShapeHistory|hidden**: \"Shape history\".

-    **Refine|Bool**: \"Refine shape (clean up redundant edges) after this boolean operation\". The default value is determined by the **Automatically refine model after sketch-based operation** preference. See [PartDesign Preferences](PartDesign_Preferences#General.md).


{{Properties_Title|Section}}

-    **Approximation|Bool**: Approximate the output edges.



## Verknüpfungen

Zum Erzeugen von Querschnitten mit Schnittebenen siehe <img alt="" src=images/Part_CrossSections.svg  style="width:16px;"> [Querschnitte](Part_CrossSections/de.md).



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Section/de
