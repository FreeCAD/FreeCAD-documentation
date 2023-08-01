---
- GuiCommand:
   Name: PartDesign PolarPattern
   Name/de: PartDesign PolaresMuster
   MenuLocation: Part Design - Muster anwenden - Polares Muster
   Workbenches: [PartDesign](PartDesign_Workbench/de.md)
   SeeAlso: [PartDesign MehrfachTransformation](PartDesign_MultiTransform/de.md)
---

# PartDesign PolarPattern/de



## Beschreibung

Das Werkzeug <img alt="" src=images/PartDesign_PolarPattern.svg  style="width:24px;"> **PolaresMuster** erstellt aus einem Formelement ein polares Muster (d.h. eine Reihe von Kopien, die auf einer Ebene um eine Achse (Pol) herum angeordnet werden.)

![](images/PartDesign_PolarPattern_example.png ) 
*Eine schlitzförmige Tasche (B), die in einem Grundkörper (A, auch als Träger bezeichnet) eingebracht ist, wird für ein polares Muster verwendet. Das Ergebnis (C) ist rechts dargestellt.*



## Anwendung



### Erstellen

1.  Optional [Aktiviere](PartDesign_Body#Active_status.md) den gewünschten Körper.
2.  Optional wähle eine oder mehrere Features im [Modellbaum](Tree_view.md) oder in der [3D Ansicht](3D_view.md).
3.  Es gibt mehrere Möglichkeiten um das Werkzeug zu starten:
    -   Drücke die **<img src="images/PartDesign_PolarPattern.svg" width=16px> [PolarPattern](PartDesign_PolarPattern.md)** Schaltfläche.
    -   Wähle die **Part Design → Apply a pattern → <img src="images/PartDesign_PolarPattern.svg" width=16px> PolarPattern** Option aus dem Menü.
4.  Wenn es keinen aktiven Körper gibt, oder mehr als zwei Körper im Dokument vorhanden sind, dann öffnet der **Active Body Required** Dialog und zeigt an, dass einer aktiviert werden muss. Wenn es einen einzelnen Körper gibt, dann wird dieser automatisch aktiviert.
5.  Wenn keine Features ausgewählt wurden, dann öffnet das **Select feature** [Eingabefenster](Task_panel.md): wähle eine oder mehrere (drücke die **Ctrl** Taste) aus der Liste und wähle die **OK** Schaltfläche.
6.  Das **PolarPattern parameters** [Eingabefenster](Task_panel.md) öffnet. Siehe [Optionen](#Options.md) für weitere Informationen.
7.  Drücke die **OK** Schaltfläche um zu beenden.



### Bearbeiten

1.  Mache eines aus dem Folgenden:
    -   Doppel-Klicke das PolarPattern Objekt im [Modellbaum](Tree_view.md).
    -   Rechts-Klicke das PolarPattern Objekt im [Modellbaum](Tree_view.md) und wähle **Edit PolarPattern** aus dem Kontextmenü.
2.  Das **PolarPattern parameters** [Eingabefenster](Task_panel.md) öffnet. Siehe [Optionen](#Options.md) für weitere Informationen.
3.  Drücke die **OK** Schaltfläche um zu beenden.



## Optionen

-   Um Features hinzuzufügen:
    1.  Betätige die **Add feature** Schaltfläche.
    2.  Wähle ein Feature im [Modellbaum](Tree_view/de.md) oder in der [3D Ansicht](3D_view.md).
    3.  Wieder hole alles um weitere Features hinzuzufügen.
-   Um Features zu entfernen:
    1.  Betätige die **Remove feature** Schaltfläche.
    2.  Mache eines der Folgenden:
        -   Wähle eine Feature im [Modellbaum](Tree_view/de.md) oder in der [3D Ansicht](3D_view.md).
        -   Wähle eine Feature in der Liste und betätige die **Del** Taste.
        -   Rechts-Klicke eine Feature in der Liste und wähle **Remove** aus dem Kontextmenü.
    3.  Wieder hole alles um weitere Features zu entfernen.
-   Falls es im Muster mehrere Features gibt, kann ihre Reihenfolge wichtig sein. Siehe [Ordering features](#Ordering_features.md).
-   Lege die **Achse** des Musters fest:
    -   
        **Normal zur Skizzenachse**
        
        : Die Z Achse der Skizze (nur bei skizzenbasierten Features möglich).

    -   
        **Vertikale Skizzenachse**
        
        : Die Y Achse der Skizze (idem).

    -   
        **Horizontale Skizzenachse**
        
        : Die X Achse der Skizze (idem).

    -   
        **Konstruktionslinie**
        
        : Ein eigener Zugang für jede Konstruktionslinie in der Skizze (idem).

    -   
        **Basis X Achse**
        
        : Die X Achse des Körpers.

    -   
        **Basis Y Achse**
        
        : Die Y Achse des Körpers.

    -   
        **Basis Z Achse**
        
        : Die Z Achse des Körpers.

    -   
        **Wähle Referenz...**
        
        : Wähle eine [Datum Linie](PartDesign_Line.md) im [Modellbaum](Tree_view.md) oder eine [Datum Linie](PartDesign_Line.md) oder Kante in der [3D Ansicht](3D_view.md).
-   Überprüfe die **Richtung umkehren** Checkbox um das Muster umzukehren.
-   Lege den **Winkel** fest, der vom Muster überdeckt wird. Wenn der Winkel kleiner als 360° ist, dann werden die Objekte gleichmäßig von 0° (erstes Objekt) bis zum angegebenen Winkel (letztes Objekt) aufgeteilt. Wenn der Winkel ein ganzer 360° Kreis ist, dann werden die Objekte gleichmäßig auf dem gesamten Kreis aufgeteilt. Das bedeutet für n Objekte, das ein 360° Winkel gleich dem Winkel 360°\*(1-1/n) ist.
-   Lege die Anzahl der **Vorkommen** (inklusive des original Objektes) fest.
-   Wenn die **Update Ansicht** Checkbox gewählt ist, dann wird die Ansicht in Echtzeit nachgebildet.



## Formelemente ordnen 

Wenn einige der ausgewählten Formelemente additiv und andere subtraktiv sind, kann ihre Reihenfolge letztlich das Ergebnis beeinflussen. Die Reihenfolge kann durch bewegen einzelner Formelemente innerhalb der Liste verändert werden.

![](images/PartDesign_feature-order.gif ) 
*Auswirkung der Formelement-Reihenfolge*



## Einschränkungen

-   Jede Oberfläche im Muster die nicht mit dem Elternteil überlappt, wird ausgeschlossen. Dadurch wird sichergestellt, dass der PartDesign Teil immer nur aus einem zusammenhängenden Körper besteht.
-   Die PartDesign Muster sind nicht so ausgereift wie ihre Draft Gegenstücke. Bei einer großen Anzahl von Objekten sollte man überlegen [Draft PolarArray](Draft_PolarArray.md) in Kombination mit einer logischen Part Operation, zu verwenden. Da man dazu PartDesign verläßt, können erhebliche Änderungen im Modell notwendig sein. Man kann nicht einfach im PartDesign Modell im gleichen Körper weitermachen. Ein Beispiel findet man in [this Forum topic](https://forum.freecadweb.org/viewtopic.php?f=3&t=55192).
-   Ein Muster kann nicht direkt wiederum gemustert werden, um ein polares oder lineares Muster, oder ein Spiegelbild zu bilden. Um dies zu machen verwende [PartDesign MultiTransform](PartDesign_MultiTransform.md).





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign PolarPattern/de
