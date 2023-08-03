---
 GuiCommand:
   Name: Part Mirror
   Name/de: Part Spiegeln
   MenuLocation: Formteil , Spiegeln
   Workbenches: Part_Workbench/de
---

# Part Mirror/de



## Beschreibung

**Objekt spiegeln** erzeugt ein neues Objekt (Bild), das eine Spiegelung des ursprünglichen Objekts (Quelle) ist. Das Bildobjekt wird hinter einer Spiegelebene erzeugt. Die Spiegelebene kann eine Standardebene (**XY**, **YZ** oder **XZ**) oder eine beliebige Ebene parallel zu einer Standardebene sein.

Ein Beispiel:

![Vorher](images/PARTMirrorBeforev11.png )

![Nachher (gespiegelt an der **YZ** Ebene)](images/PARTMirrorAfterv11.png ) 



## Anwendung

![](images/PARTMirrorDialogv11.png )

1.  Wähle das Quellobjekt aus der Spiegelungspaneel Liste aus.
2.  Wähle eine Standard **Spiegelebene** aus dem Aufklappmenü.
3.  Drücke **OK**, um das Bildobjekt zu erstellen.






## Optionen

Die **Basispunkt** Felder können verwendet werden, um die Spiegelebene parallel zur Standardspiegelebene zu verschieben. Nur eins der **X** , **Y** oder **Z** Felder ist für eine bestimmte Standardebene wirksam.

  Standardebene   Basispunkt-Feld   Auswirkung
    
  **XY**          **Z**             Verschiebt die Spiegelebene entlang der **Z**-Achse.
  **XY**          **X**, **Y**      Keine Auswirkung.
  **XZ**          **Y**             Verschiebt die Spiegelebene entlang der **Y**-Achse.
  **XZ**          **X**, **Z**      Keine Auswirkung.
  **YZ**          **X**             Verschiebt die Spiegelebene entlang der **X**-Achse.
  **YZ**          **Y**, **Z**      Keine Auswirkung.



## Hinweise

-   [App Link](App_Link.md)-Objekte, die mit den zugehörigen Objekttypen und [App Part](App_Part.md)-Behältern mit deren zugehörigen, sichtbaren, Objekten innerhalb verknüpft sind, können auch als Quellobjekte verwendet werden. <small>(v0.20)</small> 
-   Beliebige Spiegelebenen (d.h. nicht parallel zu einer Standardebene) werden nicht unterstützt



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Mirror/de
