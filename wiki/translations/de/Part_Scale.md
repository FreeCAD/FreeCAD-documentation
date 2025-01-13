---
 GuiCommand:
   Name: Part Scale
   Name/de: Part Scale
   MenuLocation: Part , Skalieren...
   Workbenches: Part_Workbench/de
   Version: 1.0
   SeeAlso: Draft_Clone/de, Draft_Scale/de
---

# Part Scale/de



## Beschreibung

**Part Skalieren** skaliert Formen entweder mit einem bestimmten Faktor einheitlich in alle Richtungen oder mit unterschiedlichen Faktoren für jede Hauptrichtung. Im Falle von unterschiedlichen Faktoren kann die Form verzerrt werden.

![400px](images/Part_Scale_demo.png) 
*Beispiel für Skalieren*



## Anwendung

1.  Eine oder mehrere Formen in der [3D-Ansicht](3D_view/de.md) oder in der [Baumansicht](Tree_view/de.md) auswählen.

2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Part_Scale.svg" width=16px> [Skalieren...](Part_Scale/de.md)** drücken.
    -   Den Menüeintrag **Part → <img src="images/Part_Scale.svg" width=16px> Skalieren...** auswählen.

3.  Ein [Aufgaben-Dialog](#Task_panel/de.md) wird geöffnet.

4.  
    **Einheitliche Skalierung**oder **Uneinheitliche Skalierung** auswählen.

5.  Skalierungsfaktor(en) eingeben.

6.  
    **OK**anklicken.

Alternativ kann die Auswahl auch nach dem Start des Befehls erfolgen, durch Auswahl einer oder mehrerer Formen aus der Liste im [Aufgaben-Dialog](Task_panel/de.md).

In der Baumansicht werden so viele Scale-Objekte aufgelistet, wie Formen ausgewählt wurden. Jede ausgewählte Form wird unterhalb ihres Scale-Objekts abgelegt.



## Aufgaben-Dialog 

![](images/Part_Scale_dialog.png )

-   Die Schaltfläche **OK** erstellt das skalierte Objekt und schließt den Aufgaben-Dialog.

-   Die Schaltfläche **Schließen** schließt den Aufgaben-Dialog, ohne etwas zu tun.

-   Die Schaltfläche **Anwenden** erstellt das skalierte Objekt, aber schließt den Aufgaben-Dialog nicht. Jetzt können weitere Formen aus der Liste unten ausgewählt und weitere skalierte Objekte erstellt werden.

-    **Shape**-Liste: hier können weitere Formen zum Skalieren ausgewählt werden. Werden mehrere Formen ausgewählt, werden auch entsprechend viele Scale-Objekte erstellt.



## Hinweise

-   Uneinheitliche Skalierung wandelt alle Kanten in B-Spline-Kurven und alle Flächen in B-Spline-Oberflächen. Diese sind schwieriger zu berechnen.
-   Punkte bzw. Knoten können nicht skaliert werden, da sie dimensionslos sind.
-   [AppLink](App_Link/de.md)-Objekte, die auf geeignete Objektarten verweisen, und [AppPart](App_Part/de.md)-Container, die geeignete sichtbare Objekte enthalten, können auch skaliert werden.
-   Der Aufgaben-Dialog enthält bisher keine Vorschaufunktion. Jeder Klick auf **Anwenden** erstellt ein neues Objekt, das als Vorschau dienen kann. Diese bleiben bestehen und ein weiteres skaliertes Objekt wird erstellt, sobald **OK** angeklickt wird. [Rückgängig](Std_Undo/de.md) kann nützlich sein, um sie zu entfernen, bevor **OK** angeklickt wird.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Part-Scale-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{TitleProperty|Scale}}

-    {{PropertyData/de|Base|Link}}: Die Eingangsform (die Form, auf die Part Scale angewendet wurde).

-    {{PropertyData/de|Uniform|Bool}}: Steuert, ob einheitlich oder uneinheitlich skaliert wird.

-    {{PropertyData/de|Uniform Scale|Float}}: Skalierungsfaktor für einheitliches Skalieren.

-    {{PropertyData/de|XScale|Float}}: Der X-Skalierungsfaktor für uneinheitliches Skalieren.

-    {{PropertyData/de|YScale|Float}}: Der Y-Skalierungsfaktor für uneinheitliches Skalieren.

-    {{PropertyData/de|ZScale|Float}}: Der Z-Skalierungsfaktor für uneinheitliches Skalieren.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Scale/de
