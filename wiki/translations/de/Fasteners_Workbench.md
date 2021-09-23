# Fasteners Workbench/de


<img alt="Arbeitsbereichssymbol Verbindungselemente" src=images/Fasteners_workbench_icon.svg  style="width:128px;">


{{TOCright}}

## Einführung

Der <img alt="" src=images/Fasteners_workbench_icon.svg  style="width:24px;"> [Arbeitsbereich Verbindungselemente](Fasteners_Workbench/de.md) ist ein [Externer Arbeitsbereich](External_workbenches/de.md), der verschiedene Verbindungselemente zu Teilen hinzufügen/anhängen kann.

## Anwendung

Die Verwendung ist ziemlich unkompliziert:

1.  Installiere den Arbeitsbereich Verbindungselemente über den [Erweiterungsverwalter](Addon_Manager/de.md).
2.  Starte ein neues Dokument in FreeCAD.
3.  Wähle den <img alt="" src=images/Fasteners_workbench_icon.svg  style="width:24px;"> [Arbeitsbereich Verbindungselemente](Fasteners_Workbench/de.md) aus der [Arbeitsbereich Aufklappliste](Std_Workbench/de.md) aus.
4.  Die zum Arbeitsbereich gehörenden [Werkzeugleisten](#Toolbars/de.md) werden angezeigt.

Einfache Anwendung: Wenn Du auf eine der Verbindungselemente klickst, wird dieses Verbindungselement an der Ursprungsposition mit den Standardeigenschaften erstellt. Um die Eigenschaften eines Verbindungselements zu ändern, wähle es und gehe dann zum **Daten** Reiter des [Eigenschaftseditors](Property_editor/de.md).

## Bekannte Probleme 

-   Andere Probleme/Funktionsanforderungen findest Du unter [Fastener Workbench GitHub issue queue](https://github.com/shaise/FreeCAD_FastenersWB/issues?utf8=✓&q=is%3Aissue)

## Referenzen

-   Autor: (http://theseger.com/projects/author/shaise/ shaise)
    -   SchraubenErsteller: Ulrich Brammer
    -   Arbeitsbereichsumgebung: Shai Seger
-   Heimseite: <http://theseger.com/projects/2015/06/fasteners-workbench-for-freecad/>
-   Quellcode auf github: <https://github.com/shaise/FreeCAD_FastenersWB>

## Einrichtung

Dieser Arbeitsbereich kann über den <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Erweiterungsverwalter](Addon_Manager/de.md) installiert werden. Für Informationen zu manuellen Installation siehe [Weitere Arbeitsbereiche installieren](Installing_more_workbenches/de.md).

## Werkzeugleisten

Der Arbeitsbereich Verbindungselemente hat zwei Werkzeugleisten. Die **FS Schauben** Werkzeugleiste hat viele Werkzeuge. Falls erforderlich kann sie durch drücken der **&gt;&gt;** Schaltfläche erweitert werden.

![](images/Fasteners_toolbars.png ) *Die Werkzeugleisten des Arbeitsbereichs Verbindungselemente*

## Werkzeuge

Für eine detaillierte Beschreibung siehe [1](http://theseger.com/projects/2015/06/fasteners-workbench-for-freecad/).

### Befehle

-   <img alt="" src=images/Fasteners_Flip.svg  style="width:32px;"> [Verbindungselement Umklappen](Fasteners_Flip/de.md): Ausrichtung Verbindungselement umkehren.

-   <img alt="" src=images/Fasteners_Move.svg  style="width:32px;"> [Verbindungselement Bewegen](Fasteners_Move/de.md): Verbindungselement an einen neuen Platz bewegen.

-   <img alt="" src=images/Fasteners_Shape.svg  style="width:32px;"> [Form vereinfachen](Fasteners_Shape/de.md): Objekt in einfache nichtparametrische Form ändern.

-   <img alt="" src=images/Fasteners_MatchTypeInner.svg  style="width:32px;"> [Schrauben nach Innengewindedurchmesser (Gewindebohrung) anpassen](Fasteners_MatchTypeInner/de.md): Schrauben nach Innengewindedurchmesser (Gewindebohrung) anpassen.

-   <img alt="" src=images/Fasteners_MatchTypeOuter.svg  style="width:32px;"> [Schrauben nach äußerem Gewindedurchmesser zuordnen (Passbohrung)](Fasteners_MatchTypeOuter/de.md): Schrauben nach äußerem Gewindedurchmesser zuordnen (Passbohrung).

-   <img alt="" src=images/Fasteners_BOM.svg  style="width:32px;"> [Stückliste generieren](Fasteners_BOM/de.md): Stücklisten für Verbindungselemente erstellen.

-   <img alt="" src=images/Fasteners_ScrewCalculator.svg  style="width:32px;"> [Schraubenberechner](Fasteners_ScrewCalculator/de.md): zeigt einen Schraubenloch Berechner an.

-   <img alt="" src=images/Fasteners_ChamferHole.svg  style="width:32px;"> [Senkungen vornehmen](Fasteners_ChamferHole/de.md): Löcher für Senkkopfschrauben anschrägen.

-   <img alt="" src=images/Fasteners_ChangeParameters.svg  style="width:32px;"> [Parameter der Verbindungselemente ändern](Fasteners_ChangeParameters/de.md): Parameter der ausgewählten Verbindungselemente ändern.

### Einpresselemente und Verbindungselemente für Leiterplatten 

-   <img alt="" src=images/Fasteners_PEMPressNut.svg  style="width:32px;"> Einpressmutter metrisch.

-   <img alt="" src=images/Fasteners_PEMTHStandoff.svg  style="width:32px;"> Einpressbuchse mit Gewinde metrisch.

-   <img alt="" src=images/Fasteners_PEMStud.svg  style="width:32px;"> Einpressgewindebolzen metrisch.

-   <img alt="" src=images/Fasteners_PCBStandoff.svg  style="width:32px;"> **Leiterplatten** Abstandshalter Außen/Innen Metrisch.

-   <img alt="" src=images/Fasteners_PCBSpacer.svg  style="width:32px;"> **Leiterplatten** Abstandshalter Innen/Innen Metrisch.

### DIN, EN und ISO Verbindungselemente 

-   <img alt="" src=images/Fasteners_ISO4017.svg  style="width:32px;"> 
**ISO 4017** Sechskantschrauben. *Produktklassen A und B.*

-   <img alt="" src=images/Fasteners_ISO4014.svg  style="width:32px;"> 
**ISO 4014** Sechskantschrauben. *Produktklassen A und B.*

-   <img alt="" src=images/Fasteners_EN1662.svg  style="width:32px;"> **EN 1662** Sechskantschrauben mit Flansch, leichte Reihe.

-   <img alt="" src=images/Fasteners_EN1665.svg  style="width:32px;"> **EN 1665** Sechskantschrauben mit Flansch, schwere Reihe.

-   <img alt="" src=images/Fasteners_ISO4762.svg  style="width:32px;"> **ISO 4762** Zylinderschrauben mit Innensechskant.

-   <img alt="" src=images/Fasteners_DIN7984.svg  style="width:32px;"> **DIN 7984** Zylinderschrauben mit Innensechskant, niedriger Kopf.

-   <img alt="" src=images/Fasteners_DIN6912.svg  style="width:32px;"> **DIN 6912** Zylinderschrauben mit Innensechskant und Schlüsselführung niedriger Kopf.

-   <img alt="" src=images/Fasteners_ISO7380-1.svg  style="width:32px;"> **ISO 7380-1** Halbrundkopfschrauben mit Innensechsrund.

-   <img alt="" src=images/Fasteners_ISO7380-2.svg  style="width:32px;"> **ISO 7380-2** Halbrundkopfschrauben mit Innensechsrund und Bund.

-   <img alt="" src=images/Fasteners_ISO10642.svg  style="width:32px;"> **ISO 10642** Senkschrauben mit Innensechskant.

-   <img alt="" src=images/Fasteners_ISO2009.svg  style="width:32px;"> 
**ISO 2009** Senkschrauben mit Schlitz. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_ISO2010.svg  style="width:32px;"> 
**ISO 2010** Linsensenkschrauben mit Schlitz. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_ISO1580.svg  style="width:32px;"> 
**ISO 1580** Flachkopfschrauben mit Schlitz. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_ISO1207.svg  style="width:32px;"> 
**ISO 1207** Zylinderschrauben mit Schlitz. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_DIN967.svg  style="width:32px;"> **DIN 967** Linsenkopfschrauben mit Bund und Kreuzschlitz.

-   <img alt="" src=images/Fasteners_ISO7045.svg  style="width:32px;"> 
**ISO 7045** Linsenkopfschrauben mit Kreuzschlitz H. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_ISO7046.svg  style="width:32px;"> 
**ISO 7046** Senkschrauben mit Kreuzschlitz H. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_ISO7047.svg  style="width:32px;"> 
**ISO 7047** Linsensenkschrauben mit Kreuzschlitz H. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_ISO7048.svg  style="width:32px;"> **ISO 7048** Zylinderschrauben mit Kreuzschlitz.

-   <img alt="" src=images/Fasteners_ISO14579.svg  style="width:32px;"> **ISO 14579** Zylinderschr. mit Innensechsrund.

-   <img alt="" src=images/Fasteners_ISO14580.svg  style="width:32px;"> **ISO 14580** Zylinderschrauben mit Innensechsrund, niedriger Kopf.

-   <img alt="" src=images/Fasteners_ISO14582.svg  style="width:32px;"> **ISO 14582** Senkschrauben mit Innensechsrund, hoher Kopf.

-   <img alt="" src=images/Fasteners_ISO14583.svg  style="width:32px;"> **ISO 14583** Flachkopfschrauben mit Innensechsrund.

-   <img alt="" src=images/Fasteners_ISO14584.svg  style="width:32px;"> **ISO 14584** Linsensenkschrauben mit Innensechsrund.

-   <img alt="" src=images/Fasteners_ISO7379.svg  style="width:32px;"> **ISO 7379** Zylinderkopfschrauben mit Innensechskant und Ansatzschaft.

-   <img alt="" src=images/Fasteners_ISO7089.svg  style="width:32px;"> 
**ISO 7089** Scheiben, Form A. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_ISO7090.svg  style="width:32px;"> 
**ISO 7090** Scheiben mit Fase, Form B. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_ISO7092.svg  style="width:32px;"> **ISO 7092** Scheiben, kleine Reihe.

-   <img alt="" src=images/Fasteners_ISO7093-1.svg  style="width:32px;"> 
**ISO 7093-1** Flache Scheiben, große Reihe. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_ISO7094.svg  style="width:32px;"> **ISO 7094** Scheiben, extra große Reihe.

-   <img alt="" src=images/Fasteners_ISO4026.svg  style="width:32px;"> **ISO 4026** Gewindestifte mit Innensechskant und Kegelstumpf.

-   <img alt="" src=images/Fasteners_ISO4027.svg  style="width:32px;"> **ISO 4027** Gewindestifte mit Innensechskant und Spitze.

-   <img alt="" src=images/Fasteners_ISO4028.svg  style="width:32px;"> **ISO 4028** Gewindestifte mit Innensechskant und Zapfen.

-   <img alt="" src=images/Fasteners_ISO4029.svg  style="width:32px;"> **ISO 4029** Gewindestifte mit Innensechskant und Ringschneide.

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

### ASME Verbindungselemente 

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.6.svg  style="width:32px;"> **ASME B18.2.1.6** UNC Hex head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.8.svg  style="width:32px;"> **ASME B18.2.1.8** UNC Hex head screw with flange.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.1A.svg  style="width:32px;"> **ASME B18.2.2.1A** UNC Machine screw nut.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.4A.svg  style="width:32px;"> **ASME B18.2.2.4A** UNC Hexagon nut.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.4B.svg  style="width:32px;"> **ASME B18.2.2.4B** UNC Hexagon thin nut.

-   <img alt="" src=images/Fasteners_ASMEB18.3.1A.svg  style="width:32px;"> **ASME B18.3.1A** UNC Hex socket head cap screw.

-   <img alt="" src=images/Fasteners_ASMEB18.3.2.svg  style="width:32px;"> **ASME B18.3.2** UNC Hex socket countersunk head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.3.3A.svg  style="width:32px;"> **ASME B18.3.3A** UNC Hex socket button head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.3.3B.svg  style="width:32px;"> **ASME B18.3.3B** UNC Hex socket button head screw with flange.

-   <img alt="" src=images/Fasteners_ASMEB18.3.4.svg  style="width:32px;"> **ASME B18.3.4** UNC Hexagon socket head shoulder screw.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5A.svg  style="width:32px;"> **ASME B18.3.5A** UNC Hexagon socket set screw with flat point.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5B.svg  style="width:32px;"> **ASME B18.3.5B** UNC Hexagon socket set screw with cone point.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5C.svg  style="width:32px;"> **ASME B18.3.5C** UNC Hexagon socket set screw with dog point.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5D.svg  style="width:32px;"> **ASME B18.3.5D** UNC Hexagon socket set screw with cup point.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.1A.svg  style="width:32px;"> **ASME B18.6.3.1A** UNC slotted countersunk flat head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12A.svg  style="width:32px;"> **ASME B18.21.1.12A** UN washer, narrow series.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12B.svg  style="width:32px;"> **ASME B18.21.1.12B** UN washer, regular series.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12C.svg  style="width:32px;"> **ASME B18.21.1.12C** UN washer, wide series.

### Verschiedenes

-   <img alt="" src=images/Fasteners_ScrewTap.svg  style="width:32px;"> Gewindestange beliebiger Länge für das Gewindeschneiden von Bohrungen (metrisch).

-   <img alt="" src=images/Fasteners_ScrewTapInch.svg  style="width:32px;"> Gewindestange beliebiger Länge für das Gewindeschneiden von Bohrungen (Zoll).

-   <img alt="" src=images/Fasteners_ScrewDie.svg  style="width:32px;"> Gewinderohr beliebiger Länge zum Schneiden von Außengewinden (metrisch).

-   <img alt="" src=images/Fasteners_ScrewDieInch.svg  style="width:32px;"> Gewinderohr beliebiger Länge zum Schneiden von Außengewinden (Zoll).

-   <img alt="" src=images/Fasteners_ThreadedRod.svg  style="width:32px;"> Gewindestange **DIN 975** beliebiger Länge (metrisch).

-   <img alt="" src=images/Fasteners_ThreadedRodInch.svg  style="width:32px;"> Gewindestange beliebiger Länge **UNC** (Zoll).

## Andere

-   <img alt="" src=images/preferences-fasteners.svg  style="width:32px;"> 
**Verbindungselemente Einstellungen**
-   <img alt="" src=images/Fasteners_workbench_icon.svg  style="width:32px;"> \'\'\'Symbol Arbeitsbereich Verbindungselemente \'\'\'

## Arbeitsbereichverwandte Verweise 

-   Arbeitsbereich Wiki: <http://theseger.com/projects/2015/06/fasteners-workbench-for-freecad/>
-   FreeCAD Wiki: <https://www.freecadweb.org/wiki/Fasteners_Workbench>
-   FreeCAD Forum: <https://forum.freecadweb.org/viewtopic.php?t=11429>
-   Tutorien - Wie anwenden: <http://theseger.com/projects/2015/06/fasteners-workbench-for-freecad/>
-   Videos:
-   Dateien:
-   Fehler berichten: Bitte melde Fehler unter <https://github.com/shaise/FreeCAD_FastenersWB/issues>
-   Installation: <http://theseger.com/projects/2015/06/fasteners-workbench-for-freecad/>

## Andere Verweise 

-   [Generating holes for countersunk screws in freecad](http://theseger.com/projects/2015/07/generating-holes-for-countersunk-screws-in-freecad/)
-   [BOLTS](https://github.com/jreinhardt/BOLTS): An Open Library for Technical Specifications
-   [Externe Arbeitsbereiche](External_workbenches/de.md)
-   [Makro Rezepte](Macros_recipes/de.md)



[Category:Addons](Category:Addons.md) [Category:External Command Reference](Category:External_Command_Reference.md) [Category:External Workbenches](Category:External_Workbenches.md) [Category:Fasteners](Category:Fasteners.md)
