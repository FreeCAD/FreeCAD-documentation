# <img alt="Arbeitsbereichssymbol Verbindungselemente" src=images/Fasteners_workbench_icon.svg  style="width:64px;"> Fasteners Workbench/de


{{TOCright}}

## Einführung


<div class="mw-translate-fuzzy">

Der <img alt="" src=images/Fasteners_workbench_icon.svg  style="width:24px;"> [Arbeitsbereich Verbindungselemente](Fasteners_Workbench/de.md) ist ein [Externer Arbeitsbereich](External_workbenches/de.md), der verschiedene Verbindungselemente zu Teilen hinzufügen/anhängen kann.


</div>

![](images/Fasteners_toolbars.png )


<div class="mw-translate-fuzzy">

![](images/Fasteners_toolbars.png ) 
*Die Werkzeugleisten des Arbeitsbereichs Verbindungselemente*


</div>

## Einrichtung


<div class="mw-translate-fuzzy">

Die Verwendung ist ziemlich unkompliziert:

1.  Installiere den Arbeitsbereich Verbindungselemente über den [Erweiterungsverwalter](Std_AddonMgr/de.md).
2.  Starte ein neues Dokument in FreeCAD.
3.  Wähle den <img alt="" src=images/Fasteners_workbench_icon.svg  style="width:24px;"> [Arbeitsbereich Verbindungselemente](Fasteners_Workbench/de.md) aus der [Arbeitsbereich Aufklappliste](Std_Workbench/de.md) aus.
4.  Die zum Arbeitsbereich gehörenden [Werkzeugleisten](#Toolbars/de.md) werden angezeigt.


</div>

## Anwendung

Fasteners can be attached or unattached. Attached fasteners have a **base Object**, a circular edge, and their **Placement** is dynamically linked to that object. The <img alt="" src=images/Fasteners_Move.svg  style="width:16px;"> [Fasteners Move](Fasteners_Move.md) command can be used to attach or detach a fastener.

### Unattached fasteners 

1.  Select the desired fastener by clicking its button or by picking it from the menu.
2.  A fastener is created at the origin.
3.  Optionally change the dimensions and other properties of the fastener:
    1.  Select the fastener.
    2.  Go to the **Data** tab of the [Property editor](Property_editor.md).
    3.  Change the required properties.

### Attached fasteners 

<img alt="" src=images/Fasteners_Attached_Selected.png  style="width:200px;"> <img alt="" src=images/Fasteners_Attached_Created.png  style="width:200px;"> 
*On the left two selected circular edges. On the right the attached fasteners.*

1.  Specify if the selected holes are tap holes or pass holes by selecting <img alt="" src=images/Fasteners_MatchTypeInner.svg  style="width:16px;"> _ respectively (not used for countersunk screws).
2.  Select one or more circular edges and/or faces with circular edges. For countersunk screws the top edge of the [chamfered hole](Fasteners_ChamferHole.md) must be selected.
3.  Select the desired fastener by clicking its button or by picking it from the menu.
4.  A fastener is attached to each of the selected circular edges.
5.  The default dimensions of each fastener depend on the radius of the circular edge it is attached to. Countersunk screws are matched by their head diameter, other fasteners are matched by their shaft diameter.
6.  Optionally change the dimensions and other properties of the fasteners. See above.
7.  Fasteners that appear upside-down can be inverted with the <img alt="" src=images/Fasteners_Flip.svg  style="width:16px;"> [Fasteners Flip](Fasteners_Flip.md) command or by changing their **invert** property.
8.  Optionally change the **offset** property to create space between the fasteners and the edges they are attached to.

## Notes

-   To generate threads, the **thread** property of a fastener must be changed to `True`. Generating threads is costly. Recomputes take much longer if there are many fasteners with threads in a document.
-   The **invert** property and the **offset** property are ignored for unattached fasteners.


<div class="mw-translate-fuzzy">

### Befehle


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_Flip.svg  style="width:32px;"> [Verbindungselement Umklappen](Fasteners_Flip/de.md): Ausrichtung Verbindungselement umkehren.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_Move.svg  style="width:32px;"> [Verbindungselement Bewegen](Fasteners_Move/de.md): Verbindungselement an einen neuen Platz bewegen.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_Shape.svg  style="width:32px;"> [Form vereinfachen](Fasteners_Shape/de.md): Objekt in einfache nichtparametrische Form ändern.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_MatchTypeInner.svg  style="width:32px;"> [Schrauben nach Innengewindedurchmesser (Gewindebohrung) anpassen](Fasteners_MatchTypeInner/de.md): Schrauben nach Innengewindedurchmesser (Gewindebohrung) anpassen.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_MatchTypeOuter.svg  style="width:32px;"> [Schrauben nach äußerem Gewindedurchmesser zuordnen (Passbohrung)](Fasteners_MatchTypeOuter/de.md): Schrauben nach äußerem Gewindedurchmesser zuordnen (Passbohrung).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_BOM.svg  style="width:32px;"> [Stückliste generieren](Fasteners_BOM/de.md): Stücklisten für Verbindungselemente erstellen.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ScrewCalculator.svg  style="width:32px;"> [Schraubenberechner](Fasteners_ScrewCalculator/de.md): zeigt einen Schraubenloch Berechner an.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ChamferHole.svg  style="width:32px;"> [Senkungen vornehmen](Fasteners_ChamferHole/de.md): Löcher für Senkkopfschrauben anschrägen.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ChangeParameters.svg  style="width:32px;"> [Parameter der Verbindungselemente ändern](Fasteners_ChangeParameters/de.md): Parameter der ausgewählten Verbindungselemente ändern.


</div>


<div class="mw-translate-fuzzy">

### Verbindungselemente


</div>


<div class="mw-translate-fuzzy">

**Hinweis:** Verbindungselemente mit metrischen Abmessungen haben hellorangefarbene Symbole. Befestigungselemente mit zölligen Abmessungen haben grüne Symbole.


</div>


<div class="mw-translate-fuzzy">

#### Einpresselemente und Verbindungselemente für Leiterplatten 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_PEMPressNut.svg  style="width:32px;"> Einpressmutter metrisch.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_PEMTHStandoff.svg  style="width:32px;"> Einpressbuchse mit Gewinde metrisch.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_PEMStud.svg  style="width:32px;"> Einpressgewindebolzen metrisch.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_PCBStandoff.svg  style="width:32px;"> **Leiterplatten** Abstandshalter Außen/Innen Metrisch.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_PCBSpacer.svg  style="width:32px;"> **Leiterplatten** Abstandshalter Innen/Innen Metrisch.


</div>

-   <img alt="" src=images/Fasteners_IUTHeatInsert.svg  style="width:32px;"> Heat staked insert.

### Hexagon head screws and bolts 

-   <img alt="" src=images/Fasteners_ISO4017.svg  style="width:32px;"> 
**ISO 4017** Sechskantschrauben. *Produktklassen A und B.*

-   <img alt="" src=images/Fasteners_ISO4014.svg  style="width:32px;"> 
**ISO 4014** Sechskantschrauben. *Produktklassen A und B.*

-   <img alt="" src=images/Fasteners_EN1662.svg  style="width:32px;"> **EN 1662** Sechskantschrauben mit Flansch, leichte Reihe.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_EN1665.svg  style="width:32px;"> **EN 1665** Sechskantschrauben mit Flansch, schwere Reihe.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.6.svg  style="width:32px;"> **ASME B18.2.1.6** UNC Sechskantschraube.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.8.svg  style="width:32px;"> **ASME B18.2.1.8** UNC Sechskantschraube mit Flansch.


</div>

### Hexagon socket screws 

-   <img alt="" src=images/Fasteners_ISO4762.svg  style="width:32px;"> **ISO 4762** Zylinderschrauben mit Innensechskant.

-   <img alt="" src=images/Fasteners_DIN7984.svg  style="width:32px;"> **DIN 7984** Zylinderschrauben mit Innensechskant, niedriger Kopf.

-   <img alt="" src=images/Fasteners_DIN6912.svg  style="width:32px;"> **DIN 6912** Zylinderschrauben mit Innensechskant und Schlüsselführung niedriger Kopf.

-   <img alt="" src=images/Fasteners_ISO7380-1.svg  style="width:32px;"> **ISO 7380-1** Halbrundkopfschrauben mit Innensechsrund.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ISO7380-2.svg  style="width:32px;"> **ISO 7380-2** Halbrundkopfschrauben mit Innensechsrund und Bund.


</div>

-   <img alt="" src=images/Fasteners_ISO10642.svg  style="width:32px;"> **ISO 10642** Senkschrauben mit Innensechskant.

-   <img alt="" src=images/Fasteners_ISO7379.svg  style="width:32px;"> **ISO 7379** Zylinderkopfschrauben mit Innensechskant und Ansatzschaft.

-   <img alt="" src=images/Fasteners_ISO4026.svg  style="width:32px;"> **ISO 4026** Gewindestifte mit Innensechskant und Kegelstumpf.

-   <img alt="" src=images/Fasteners_ISO4027.svg  style="width:32px;"> **ISO 4027** Gewindestifte mit Innensechskant und Spitze.

-   <img alt="" src=images/Fasteners_ISO4028.svg  style="width:32px;"> **ISO 4028** Gewindestifte mit Innensechskant und Zapfen.

-   <img alt="" src=images/Fasteners_ISO4029.svg  style="width:32px;"> **ISO 4029** Gewindestifte mit Innensechskant und Ringschneide.

-   <img alt="" src=images/Fasteners_ASMEB18.3.1A.svg  style="width:32px;"> **ASME B18.3.1A** UNC Hexagon socket head cap screw.

-   <img alt="" src=images/Fasteners_ASMEB18.3.2.svg  style="width:32px;"> **ASME B18.3.2** UNC Hexagon socket countersunk head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.3.3A.svg  style="width:32px;"> **ASME B18.3.3A** UNC Hexagon socket button head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.3.3B.svg  style="width:32px;"> **ASME B18.3.3B** UNC Hexagon socket button head screw with flange.

-   <img alt="" src=images/Fasteners_ASMEB18.3.4.svg  style="width:32px;"> **ASME B18.3.4** UNC Hexagon socket head shoulder screw.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5A.svg  style="width:32px;"> **ASME B18.3.5A** UNC Hexagon socket set screw with flat point.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5B.svg  style="width:32px;"> **ASME B18.3.5B** UNC Hexagon socket set screw with cone point.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5C.svg  style="width:32px;"> **ASME B18.3.5C** UNC Hexagon socket set screw with dog point.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5D.svg  style="width:32px;"> **ASME B18.3.5D** UNC Hexagon socket set screw with cup point.

### Slotted head screws 

-   <img alt="" src=images/Fasteners_ISO2009.svg  style="width:32px;"> 
**ISO 2009** Senkschrauben mit Schlitz. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_ISO2010.svg  style="width:32px;"> 
**ISO 2010** Linsensenkschrauben mit Schlitz. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_ISO1580.svg  style="width:32px;"> 
**ISO 1580** Flachkopfschrauben mit Schlitz. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_ISO1207.svg  style="width:32px;"> 
**ISO 1207** Zylinderschrauben mit Schlitz. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.1A.svg  style="width:32px;"> **ASME B18.6.3.1A** UNC Senkkopfschraube mit Schlitz.

### H cross head screws 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_DIN967.svg  style="width:32px;"> **DIN 967** Linsenkopfschrauben mit Bund und Kreuzschlitz.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ISO7045.svg  style="width:32px;"> 
**ISO 7045** Linsenkopfschrauben mit Kreuzschlitz H. *Produktklasse A.*


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ISO7046.svg  style="width:32px;"> 
**ISO 7046** Senkschrauben mit Kreuzschlitz H. *Produktklasse A.*


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ISO7047.svg  style="width:32px;"> 
**ISO 7047** Linsensenkschrauben mit Kreuzschlitz H. *Produktklasse A.*


</div>

-   <img alt="" src=images/Fasteners_ISO7048.svg  style="width:32px;"> **ISO 7048** Zylinderschrauben mit Kreuzschlitz.

### Hexalobular socket head screws 

-   <img alt="" src=images/Fasteners_ISO14579.svg  style="width:32px;"> **ISO 14579** Zylinderschr. mit Innensechsrund.

-   <img alt="" src=images/Fasteners_ISO14580.svg  style="width:32px;"> **ISO 14580** Zylinderschrauben mit Innensechsrund, niedriger Kopf.

-   <img alt="" src=images/Fasteners_ISO14582.svg  style="width:32px;"> **ISO 14582** Senkschrauben mit Innensechsrund, hoher Kopf.

-   <img alt="" src=images/Fasteners_ISO14583.svg  style="width:32px;"> **ISO 14583** Flachkopfschrauben mit Innensechsrund.

-   <img alt="" src=images/Fasteners_ISO14584.svg  style="width:32px;"> **ISO 14584** Linsensenkschrauben mit Innensechsrund.

### Other head bolts 

-   <img alt="" src=images/Fasteners_ASMEB18.5.2.svg  style="width:32px;"> **ASME B18.5** UNC Round head square neck bolt.

### Washers

-   <img alt="" src=images/Fasteners_ISO7089.svg  style="width:32px;"> 
**ISO 7089** Scheiben, Form A. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_ISO7090.svg  style="width:32px;"> 
**ISO 7090** Scheiben mit Fase, Form B. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_ISO7092.svg  style="width:32px;"> **ISO 7092** Scheiben, kleine Reihe.

-   <img alt="" src=images/Fasteners_ISO7093-1.svg  style="width:32px;"> 
**ISO 7093-1** Flache Scheiben, große Reihe. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_ISO7094.svg  style="width:32px;"> **ISO 7094** Scheiben, extra große Reihe.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12A.svg  style="width:32px;"> **ASME B18.21.1.12A** UN Unterlegscheibe, schmale Reihe.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12B.svg  style="width:32px;"> **ASME B18.21.1.12B** UN Scheibe, normale Reihe.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12C.svg  style="width:32px;"> **ASME B18.21.1.12C** UN Scheibe, breite Reihe.

### Nuts

-   <img alt="" src=images/Fasteners_ISO4032.svg  style="width:32px;"> 
**ISO 4032** Sechskantmuttern (Typ 1). *Produktklassen A und B.*

-   <img alt="" src=images/Fasteners_ISO4033.svg  style="width:32px;"> 
**ISO 4033** Hohe Sechskantmuttern (Typ 2). *Produktklassen A und B.*

-   <img alt="" src=images/Fasteners_ISO4035.svg  style="width:32px;"> 
**ISO 4035** Sechskantmuttern mit Fase, niedrige Form. *Produktklassen A und B.*

-   <img alt="" src=images/Fasteners_EN1661.svg  style="width:32px;"> **EN 1661** Sechskantmuttern mit Flansch.

-   <img alt="" src=images/Fasteners_DIN557.svg  style="width:32px;"> **DIN 557** Vierkantmuttern.

-   <img alt="" src=images/Fasteners_DIN562.svg  style="width:32px;"> **DIN 562** Vierkantmuttern.

-   <img alt="" src=images/Fasteners_DIN985.svg  style="width:32px;"> **DIN 985** Sechskantsicherungsmuttern mit Kunststoffring.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.1A.svg  style="width:32px;"> **ASME B18.2.2.1A** UNC Machine screw nut.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.4A.svg  style="width:32px;"> **ASME B18.2.2.4A** UNC Hexagon nut.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.4B.svg  style="width:32px;"> **ASME B18.2.2.4B** UNC Hexagon thin nut.

### Verschiedenes


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ScrewTap.svg  style="width:32px;"> Gewindestange beliebiger Länge für das Gewindeschneiden von Bohrungen (metrisch).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ScrewTapInch.svg  style="width:32px;"> Gewindestange beliebiger Länge für das Gewindeschneiden von Bohrungen (Zoll).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ScrewDie.svg  style="width:32px;"> Gewinderohr beliebiger Länge zum Schneiden von Außengewinden (metrisch).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ScrewDieInch.svg  style="width:32px;"> Gewinderohr beliebiger Länge zum Schneiden von Außengewinden (Zoll).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ThreadedRod.svg  style="width:32px;"> Gewindestange **DIN 975** beliebiger Länge (metrisch).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ThreadedRodInch.svg  style="width:32px;"> Gewindestange beliebiger Länge **UNC** (Zoll).


</div>

## Referenzen


<div class="mw-translate-fuzzy">

-   Autor: (http://theseger.com/projects/author/shaise/ shaise)
    -   SchraubenErsteller: Ulrich Brammer
    -   Arbeitsbereichsumgebung: Shai Seger
-   Heimseite: <http://theseger.com/projects/2015/06/fasteners-workbench-for-freecad/>
-   Quellcode auf github: <https://github.com/shaise/FreeCAD_FastenersWB>


</div>

## Links


<div class="mw-translate-fuzzy">

-   [Generating holes for countersunk screws in freecad](http://theseger.com/projects/2015/07/generating-holes-for-countersunk-screws-in-freecad/)
-   [BOLTS](https://github.com/jreinhardt/BOLTS): An Open Library for Technical Specifications
-   [Externe Arbeitsbereiche](External_workbenches/de.md)
-   [Makro Rezepte](Macros_recipes/de.md)


</div>



_ _ _ _

---
[documentation index](../README.md) > [Addons](Category_Addons.md) > Fasteners Workbench/de
