# <img alt="Arbeitsbereichssymbol Verbindungselemente" src=images/Fasteners_workbench_icon.svg  style="width:64px;"> Fasteners Workbench/de


{{TOCright}}



## Einführung

Der <img alt="" src=images/Fasteners_workbench_icon.svg  style="width:24px;"> [Arbeitsbereich Verbindungselemente](Fasteners_Workbench/de.md) ist ein [externer Arbeitsbereich](External_workbenches/de.md), der Bauteilen bzw. Baugruppen unterschiedliche Verbindungselemente hinzufügen kann.

![](images/Fasteners_toolbars.png ) 
*Das optionale Layout des Arbeitsbereichs mit einer Symbolleiste.<br> Verbindungselemente mit metrischen Abmessungen haben orangefarbene Symbole.<br> Verbindungselemente mit Abmessungen in Zoll haben türkisfarbene Symbole.*



## Einrichtung

1.  Arbeitsbereich Verbindungselemente über den [Addon-Manager](Std_AddonMgr/de.md) installieren. Zur manuellen Installation siehe: [Weitere Arbeitsbereiche installieren](Installing_more_workbenches/de.md).
2.  FreeCAD neu starten.
3.  Den Arbeitsbereich <img alt="" src=images/Fasteners_workbench_icon.svg  style="width:24px;"> [Fasteners](Fasteners_Workbench/de.md) (Verbindungselemente) aus der Auswahlliste [Arbeitsbereich](Std_Workbench/de.md) auswählen.
4.  Bei Bedarf kann die Symbolleiste und die Menüanordnung geändert werden:
    1.  
        **Bearbeiten → Einstellungen... → Fasteners → General settings → Toolbar screw icons grouping**
        
        .

    2.  Eine der vorhandenen Möglichkeiten auswählen:
        -   
            **Keine**
            
            : Alle Verbindungselemente befinden sich in einer einzigen Symbolleiste. Um sie zu erweitern und alle vorhandenen Schaltflächen zu sehen, benutzt man die Schaltfläche **&gt;&gt;**.

        -   
            **Separate toolbars**
            
            : Die Verbindungselemente werden in mehreren Symbolleisten gruppiert. Dies ist das Standardlayout.

        -   
            **Dropdown buttons**
            
            : Die Verbindungselemente werden in einer Symbolleiste mit Ausklappmenüs gruppiert.

    3.  FreeCAD neu starten.



## Anwendung

Verbindungselemente können zugeordnet oder lose sein. Zugeordnete Verbindungselemente haben ein {{PropertyData/de|base Object}}, eine kreisförmige Kante, und ihre {{PropertyData/de|Placement}} ist dynamisch mit dem Objekt verknüpft. Der Befehl <img alt="" src=images/Fasteners_Move.svg  style="width:16px;"> [Fasteners Bewegen](Fasteners_Move/de.md) kann dazu benutzt werden, ein Verbindungselement zuzuordnen oder zu lösen.



### Lose Verbindungselemente 

1.  Das gewünschte Verbindungselement auswählen, durch anklicken seiner Schaltfläche oder durch Auswahl aus dem Menü.
2.  Ein Verbindungselement wird im Ursprung erstellt.
3.  Optional können die Abmessungen und andere Eigenschaften der Verbindungselemente verändert werden:
    1.  Verbindungselement auswählen.
    2.  Den Reiter **Data** des [Eigenschafteneditors](Property_editor/de.md) aktivieren.
    3.  Die erforderlichen Eigenschaften ändern.



### Zugeordnete Verbindungselemente 

<img alt="" src=images/Fasteners_Attached_Selected.png  style="width:200px;"> <img alt="" src=images/Fasteners_Attached_Created.png  style="width:200px;"> 
*Links: Zwei ausgewählte kreisförmige Kanten. Rechts: Die (ihnen) zugeordneten Verbindungselemente.*

1.  Festlegen, ob die ausgewählten Löcher Kernlöcher oder Durchgangslöcher sind, durch Auswahl von <img alt="" src=images/Fasteners_MatchTypeInner.svg  style="width:16px;"> [AuswahlNachInnenmaß](Fasteners_MatchTypeInner/de.md) oder <img alt="" src=images/Fasteners_MatchTypeOuter.svg  style="width:16px;"> [AuswahlNachAußenmaß](Fasteners_MatchTypeOuter/de.md) (wird für Senkschrauben nicht verwendet).
2.  Auswahl einer oder mehrerer kreisförmiger Kanten und/oder Flächen mit kreisförmigen Kanten. Für Senkschrauben muss die obere Kante der [Lochsenkung](Fasteners_ChamferHole/de.md) ausgewählt werden.
3.  Das gewünschte Verbindungselement auswählen, durch anklicken seiner Schaltfläche oder durch Auswahl aus dem Menü.
4.  Jeder kreisförmigen Kante wird ein Verbindungselement zugeordnet.
5.  Die vorgegebenen Abmessungen jedes einzelnen Verbindungselements sind von dem Radius der jeweiligen kreisförmigen Kante abhängig, der es zugeordnet wurde. Senkschrauben werden nach Kopfdurchmesser ausgewählt, andere Verbindungselemente nach ihrem Schaftdurchmesser.
6.  Optional können die Abmessungen und andere Eigenschaften der Verbindungselemente verändert werden. Siehe oben.
7.  Verbindungselemente, die verkehrt herum erscheinen, können mit dem Befehl <img alt="" src=images/Fasteners_Flip.svg  style="width:16px;"> [Fasteners Umdrehen](Fasteners_Flip/de.md) umgedreht werden oder durch Ändern ihrer {{PropertyData/de|invert}}.
8.  Optional kann die {{PropertyData/de|offset}} geändert werden, um einen Abstand zwischen den Verbindungselementen und den Kanten, denen sie zugeordnet sind, herzustellen.



## Hinweise

-   Um Gewinde zu erzeugen, muss die {{PropertyData/de|thread}} eines Verbindungselements auf `True` geändert werden. Gewinde zu erzeugen ist aufwändig. Eine Neuberechnung dauert viel länger, wenn ein Dokument viele Verbindungselemente mit Gewinden enthält.
-   Die {{PropertyData/de|invert}} und die {{PropertyData/de|offset}} werden für nicht zugeordnete Verbindungselemente ignoriert.



## Befehle

-   <img alt="" src=images/Fasteners_Flip.svg  style="width:32px;"> [Verbindungselement Umdrehen](Fasteners_Flip/de.md): Ausrichtung der zugeordneten Verbindungselemente umkehren.

-   <img alt="" src=images/Fasteners_Move.svg  style="width:32px;"> [Verbindungselement Bewegen](Fasteners_Move/de.md): Ein Verbindungselement auf eine kreisförmige Kante bewegen und mit dieser zu verbinden. Kann auch zum Lösen der Verbindung verwendet werden.

-   <img alt="" src=images/Fasteners_Shape.svg  style="width:32px;"> [Form vereinfachen](Fasteners_Shape/de.md): Erstellt nichtparametrische Kopien der Verbindungselemente.

-   <img alt="" src=images/Fasteners_MatchTypeInner.svg  style="width:32px;"> [Match tap hole](Fasteners_MatchTypeInner/de.md): Kreisförmige Kanten werden als Gewindebohrungen angesehen, wenn neue Verbindungselemente mit ihnen verbunden werden.

-   <img alt="" src=images/Fasteners_MatchTypeOuter.svg  style="width:32px;"> [Match for pass hole](Fasteners_MatchTypeOuter/de.md): Kreisförmige Kanten werden als Durchgangslöcher angesehen, wenn neue Verbindungselemente mit ihnen verbunden werden.

-   <img alt="" src=images/Fasteners_BOM.svg  style="width:32px;"> [Stückliste generieren](Fasteners_BOM/de.md): Erstellt eine Tabelle mit einer Stückliste für die im Dokument verwendeten Verbindungselemente.

-   <img alt="" src=images/Fasteners_ScrewCalculator.svg  style="width:32px;"> [Schraubenberechner](Fasteners_ScrewCalculator/de.md): Zeigt einen Rechner zum Ermitteln des Kernlochdurchmessers einer Gewindebohrung an.

-   <img alt="" src=images/Fasteners_ChamferHole.svg  style="width:32px;"> [Senkungen vornehmen](Fasteners_ChamferHole/de.md): Erstellt eine Senkung an einem Loch für Senkschrauben.

-   <img alt="" src=images/Fasteners_ChangeParameters.svg  style="width:32px;"> [Parameter der Verbindungselemente ändern](Fasteners_ChangeParameters/de.md): Ändert die Parameter der Verbindungselemente.



## Verbindungselemente

Verbindungselemente mit metrischen Maßen haben orangefarbene Symbole. Befestigungselemente mit Zollmaßen haben türkisfarbene Symbole.



### Einpresselemente und Verbindungselemente für Leiterplatten 

-   <img alt="" src=images/Fasteners_PEMPressNut.svg  style="width:32px;"> Einpressmutter.

-   <img alt="" src=images/Fasteners_PEMTHStandoff.svg  style="width:32px;"> Einpressbuchse mit Gewinde.

-   <img alt="" src=images/Fasteners_PEMStud.svg  style="width:32px;"> Einpressbolzen.

-   <img alt="" src=images/Fasteners_PCBStandoff.svg  style="width:32px;"> Abstandshalter für Leiterplatten mit Außen- und Innengewinde.

-   <img alt="" src=images/Fasteners_PCBSpacer.svg  style="width:32px;"> Abstandshalter für Leiterplatten, Innengewinde beidseitig.

-   <img alt="" src=images/Fasteners_IUTHeatInsert.svg  style="width:32px;"> Einsätze zum Warmeinbetten.



### Sechskantschrauben und -Bolzen 

-   <img alt="" src=images/Fasteners_DIN933.svg  style="width:32px;"> **DIN 933** Sechskantschraube.

-   <img alt="" src=images/Fasteners_ISO4017.svg  style="width:32px;"> 
**ISO 4017** Sechskantschrauben. *Produktklassen A und B.*

-   <img alt="" src=images/Fasteners_ISO4014.svg  style="width:32px;"> 
**ISO 4014** Sechskantschrauben. *Produktklassen A und B.*

-   <img alt="" src=images/Fasteners_EN1662.svg  style="width:32px;"> **EN 1662** Sechskantschrauben mit Flansch, leichte Reihe.

-   <img alt="" src=images/Fasteners_EN1665.svg  style="width:32px;"> **EN 1665** Sechskantschrauben mit Flansch, schwere Reihe.

-   <img alt="" src=images/Fasteners_DIN571.svg  style="width:32px;"> **DIN 571** Sechskantholzschraube.

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.6.svg  style="width:32px;"> **ASME B18.2.1.6** UNC Sechskantschraube.

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.8.svg  style="width:32px;"> **ASME B18.2.1.8** UNC Sechskantschraube mit Flansch.



### Schrauben mit Innensechskant 

-   <img alt="" src=images/Fasteners_ISO4762.svg  style="width:32px;"> **ISO 4762** Zylinderschrauben mit Innensechskant.

-   <img alt="" src=images/Fasteners_DIN7984.svg  style="width:32px;"> **DIN 7984** Zylinderschrauben mit Innensechskant, niedriger Kopf.

-   <img alt="" src=images/Fasteners_DIN6912.svg  style="width:32px;"> **DIN 6912** Zylinderschrauben mit Innensechskant und Schlüsselführung niedriger Kopf.

-   <img alt="" src=images/Fasteners_ISO7380-1.svg  style="width:32px;"> **ISO 7380-1** Halbrundkopfschrauben mit Innensechsrund.

-   <img alt="" src=images/Fasteners_ISO7380-2.svg  style="width:32px;"> **ISO 7380-2** Halbrundkopfschrauben mit Innensechsrund und Bund.

-   <img alt="" src=images/Fasteners_ISO10642.svg  style="width:32px;"> **ISO 10642** Senkschrauben mit Innensechskant.

-   <img alt="" src=images/Fasteners_ISO7379.svg  style="width:32px;"> **ISO 7379** Zylinderkopfschrauben mit Innensechskant und Ansatzschaft.

-   <img alt="" src=images/Fasteners_ISO4026.svg  style="width:32px;"> **ISO 4026** Gewindestifte mit Innensechskant und Kegelstumpf.

-   <img alt="" src=images/Fasteners_ISO4027.svg  style="width:32px;"> **ISO 4027** Gewindestifte mit Innensechskant und Spitze.

-   <img alt="" src=images/Fasteners_ISO4028.svg  style="width:32px;"> **ISO 4028** Gewindestifte mit Innensechskant und Zapfen.

-   <img alt="" src=images/Fasteners_ISO4029.svg  style="width:32px;"> **ISO 4029** Gewindestifte mit Innensechskant und Ringschneide.

-   <img alt="" src=images/Fasteners_ASMEB18.3.1A.svg  style="width:32px;"> **ASME B18.3.1A** UNC Hexagon socket head cap screw.

-   <img alt="" src=images/Fasteners_ASMEB18.3.1G.svg  style="width:32px;"> **ASME B18.3.1G** UNC Hexagon socket head cap screw with low head.

-   <img alt="" src=images/Fasteners_ASMEB18.3.2.svg  style="width:32px;"> **ASME B18.3.2** UNC Hexagon socket countersunk head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.3.3A.svg  style="width:32px;"> **ASME B18.3.3A** UNC Hexagon socket button head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.3.3B.svg  style="width:32px;"> **ASME B18.3.3B** UNC Hexagon socket button head screw with flange.

-   <img alt="" src=images/Fasteners_ASMEB18.3.4.svg  style="width:32px;"> **ASME B18.3.4** UNC Hexagon socket head shoulder screw.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5A.svg  style="width:32px;"> **ASME B18.3.5A** UNC Hexagon socket set screw with flat point.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5B.svg  style="width:32px;"> **ASME B18.3.5B** UNC Hexagon socket set screw with cone point.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5C.svg  style="width:32px;"> **ASME B18.3.5C** UNC Hexagon socket set screw with dog point.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5D.svg  style="width:32px;"> **ASME B18.3.5D** UNC Hexagon socket set screw with cup point.



### Schrauben mit Innensechsrund 

-   <img alt="" src=images/Fasteners_ISO14579.svg  style="width:32px;"> **ISO 14579** Zylinderschr. mit Innensechsrund.

-   <img alt="" src=images/Fasteners_ISO14580.svg  style="width:32px;"> **ISO 14580** Zylinderschrauben mit Innensechsrund, niedriger Kopf.

-   <img alt="" src=images/Fasteners_ISO14582.svg  style="width:32px;"> **ISO 14582** Senkschrauben mit Innensechsrund, hoher Kopf.

-   <img alt="" src=images/Fasteners_ISO14583.svg  style="width:32px;"> **ISO 14583** Flachkopfschrauben mit Innensechsrund.

-   <img alt="" src=images/Fasteners_ISO14584.svg  style="width:32px;"> **ISO 14584** Linsensenkschrauben mit Innensechsrund.



### Schlitzschrauben

-   <img alt="" src=images/Fasteners_ISO2009.svg  style="width:32px;"> 
**ISO 2009** Senkschrauben mit Schlitz. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_ISO2010.svg  style="width:32px;"> 
**ISO 2010** Linsensenkschrauben mit Schlitz. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_ISO1580.svg  style="width:32px;"> 
**ISO 1580** Flachkopfschrauben mit Schlitz. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_ISO1207.svg  style="width:32px;"> 
**ISO 1207** Zylinderschrauben mit Schlitz. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_DIN96.svg  style="width:32px;"> **DIN 96** Slotted half round head wood screw.

-   <img alt="" src=images/Fasteners_GOST1144-1.svg  style="width:32px;"> **GOST 1144-1** Slotted half round head wood screw.

-   <img alt="" src=images/Fasteners_GOST1144-2.svg  style="width:32px;"> **GOST 1144-2** Slotted half round head wood screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.1A.svg  style="width:32px;"> **ASME B18.6.3.1A** UNC Senkkopfschraube mit Schlitz.



### Kreuzschlitzschrauben

-   <img alt="" src=images/Fasteners_DIN967.svg  style="width:32px;"> **DIN 967** Linsenkopfschrauben mit Bund und Kreuzschlitz.

-   <img alt="" src=images/Fasteners_ISO7045.svg  style="width:32px;"> 
**ISO 7045** Linsenkopfschrauben mit Kreuzschlitz H. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_ISO7046.svg  style="width:32px;"> 
**ISO 7046** Senkschrauben mit Kreuzschlitz H. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_ISO7047.svg  style="width:32px;"> 
**ISO 7047** Linsensenkschrauben mit Kreuzschlitz H. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_ISO7048.svg  style="width:32px;"> **ISO 7048** Zylinderschrauben mit Kreuzschlitz.

-   <img alt="" src=images/Fasteners_GOST1144-3.svg  style="width:32px;"> **GOST 1144-3** Half round head wood screw with type H cross recess.

-   <img alt="" src=images/Fasteners_GOST1144-4.svg  style="width:32px;"> **GOST 1144-4** Half round head wood screw with type H cross recess.

### Other head bolts 

-   <img alt="" src=images/Fasteners_DIN603.svg  style="width:32px;"> **DIN 603** Round head square neck bolt.

-   <img alt="" src=images/Fasteners_DIN478.svg  style="width:32px;"> **DIN 478** Square head bolt with collar.

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.1.svg  style="width:32px;"> **ASME B18.2.1.1** UNC square head bolt.

-   <img alt="" src=images/Fasteners_ASMEB18.5.2.svg  style="width:32px;"> **ASME B18.5** UNC Round head square neck bolt.



### Muttern

-   <img alt="" src=images/Fasteners_ISO4032.svg  style="width:32px;"> 
**ISO 4032** Sechskantmuttern (Typ 1). *Produktklassen A und B.*

-   <img alt="" src=images/Fasteners_ISO4033.svg  style="width:32px;"> 
**ISO 4033** Hohe Sechskantmuttern (Typ 2). *Produktklassen A und B.*

-   <img alt="" src=images/Fasteners_ISO4035.svg  style="width:32px;"> 
**ISO 4035** Sechskantmuttern mit Fase, niedrige Form. *Produktklassen A und B.*

-   <img alt="" src=images/Fasteners_EN1661.svg  style="width:32px;"> **EN 1661** Sechskantmuttern mit Flansch.

-   <img alt="" src=images/Fasteners_DIN917.svg  style="width:32px;"> **DIN 917** Cap nut, low form.

-   <img alt="" src=images/Fasteners_DIN928.svg  style="width:32px;"> **DIN 928** Square weld nut.

-   <img alt="" src=images/Fasteners_DIN929.svg  style="width:32px;"> **DIN 929** Hexagon weld nut.

-   <img alt="" src=images/Fasteners_DIN935.svg  style="width:32px;"> **DIN 935** Hexagon castle nut.

-   <img alt="" src=images/Fasteners_DIN6334.svg  style="width:32px;"> **DIN 6334** Hexagon coupling nut.

-   <img alt="" src=images/Fasteners_DIN7967.svg  style="width:32px;"> **DIN 7967** Self-locking counter nut.

-   <img alt="" src=images/Fasteners_DIN1587.svg  style="width:32px;"> **DIN 1587** Cap nut.

-   <img alt="" src=images/Fasteners_GOST11860-1.svg  style="width:32px;"> **GOST 11860-1** Cap nut.

-   <img alt="" src=images/Fasteners_DIN315.svg  style="width:32px;"> **DIN 315** Wing nut.

-   <img alt="" src=images/Fasteners_DIN557.svg  style="width:32px;"> **DIN 557** Vierkantmuttern.

-   <img alt="" src=images/Fasteners_DIN562.svg  style="width:32px;"> **DIN 562** Vierkantmuttern.

-   <img alt="" src=images/Fasteners_DIN985.svg  style="width:32px;"> **DIN 985** Sechskantsicherungsmuttern mit Kunststoffring.

-   <img alt="" src=images/Fasteners_DIN1624.svg  style="width:32px;"> **DIN 1624** Tee nut.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.1A.svg  style="width:32px;"> **ASME B18.2.2.1A** UNC Hexagon machine screw nut.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.1B.svg  style="width:32px;"> **ASME B18.2.2.1B** UNC Square machine screw nut.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.2.svg  style="width:32px;"> **ASME 18.2.2.2** UNC Square nut.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.4A.svg  style="width:32px;"> **ASME B18.2.2.4A** UNC Hexagon nut.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.4B.svg  style="width:32px;"> **ASME B18.2.2.4B** UNC Hexagon thin nut.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.5.svg  style="width:32px;"> **ASME 18.2.2.5** UNC Hexagon castle nut.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.12.svg  style="width:32px;"> **ASME 18.2.2.12** UNC Hexagon nut with flange.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.13.svg  style="width:32px;"> **ASME 18.2.2.13** UNC Hexagon coupling nut.

-   <img alt="" src=images/Fasteners_ASMEB18.6.9A.svg  style="width:32px;"> **ASME 18.6.9A** Wing nut, type A.

-   <img alt="" src=images/Fasteners_SAEJ483a1.svg  style="width:32px;"> **SAE J483a 1** Low cap nut.

-   <img alt="" src=images/Fasteners_SAEJ483a2.svg  style="width:32px;"> **SAE J483a 2** High cap nut.



### Muttern für T-Nuten (T-Nutensteine) 

-   <img alt="" src=images/Fasteners_DIN508.svg  style="width:32px;"> **DIN 508** Mutter für T-Nut.

-   <img alt="" src=images/Fasteners_GN507.svg  style="width:32px;"> **GN 507** Mutter für T-Nut.



### Scheiben

-   <img alt="" src=images/Fasteners_ISO7089.svg  style="width:32px;"> 
**ISO 7089** Scheiben, Form A. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_ISO7090.svg  style="width:32px;"> 
**ISO 7090** Scheiben mit Fase, Form B. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_ISO7092.svg  style="width:32px;"> 
**ISO 7092** Scheiben, kleine Reihe. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_ISO7093-1.svg  style="width:32px;"> 
**ISO 7093-1** Flache Scheiben, große Reihe. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_ISO7094.svg  style="width:32px;"> 
**ISO 7094** Scheiben, extra große Reihe. *Produktklasse C.*

-   <img alt="" src=images/Fasteners_NFE27-619.svg  style="width:32px;"> **NFE27-619** Countersunk washer.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12A.svg  style="width:32px;"> **ASME B18.21.1.12A** UN Unterlegscheibe, schmale Reihe.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12B.svg  style="width:32px;"> **ASME B18.21.1.12B** UN Scheibe, normale Reihe.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12C.svg  style="width:32px;"> **ASME B18.21.1.12C** UN Scheibe, breite Reihe.



### Sicherungsringe

-   <img alt="" src=images/Fasteners_DIN471.svg  style="width:32px;"> **DIN 471** Sicherungsring für Wellen.

-   <img alt="" src=images/Fasteners_DIN472.svg  style="width:32px;"> **DIN 472** Sicherungsring für Bohrungen.

-   <img alt="" src=images/Fasteners_DIN6799.svg  style="width:32px;"> **DIN 6799** Sicherungsscheibe.



### Verschiedenes

-   <img alt="" src=images/Fasteners_ScrewTap.svg  style="width:32px;"> Gewindestange beliebiger Länge für das Gewindeschneiden von Bohrungen.

-   <img alt="" src=images/Fasteners_ScrewTapInch.svg  style="width:32px;"> Gewindestange beliebiger Länge für das Gewindeschneiden von Bohrungen.

-   <img alt="" src=images/Fasteners_ScrewDie.svg  style="width:32px;"> Gewinderohr beliebiger Länge zum Schneiden von Außengewinden.

-   <img alt="" src=images/Fasteners_ScrewDieInch.svg  style="width:32px;"> Gewinderohr beliebiger Länge zum Schneiden von Außengewinden.

-   <img alt="" src=images/Fasteners_ThreadedRod.svg  style="width:32px;"> Gewindestange **DIN 975** beliebiger Länge.

-   <img alt="" src=images/Fasteners_ThreadedRodInch.svg  style="width:32px;"> Gewindestange beliebiger Länge **UNC**.



## Referenzen

-   Autor: (http://theseger.com/projects/author/shaise/ shaise)
    -   SchraubenErsteller: Ulrich Brammer
    -   Arbeitsbereichsumgebung: Shai Seger
-   Heimseite: <http://theseger.com/projects/2015/06/fasteners-workbench-for-freecad/>
-   Quellcode: <https://github.com/shaise/FreeCAD_FastenersWB>
-   Bug-Reports und Feature-Requests: <https://github.com/shaise/FreeCAD_FastenersWB/issues>
-   Forumsbeitrag: <https://forum.freecadweb.org/viewtopic.php?t=11429>



## Verweise

-   [Generating holes for countersunk screws in freecad](http://theseger.com/projects/2015/07/generating-holes-for-countersunk-screws-in-freecad/) (Erstellung von Bohrungen für Senkschrauben)
-   [BOLTS](https://github.com/jreinhardt/BOLTS): Eine offene Bibliothek für technische Spezifikationen
-   [Externe Arbeitsbereiche](External_workbenches/de.md)
-   [Makro Rezepte](Macros_recipes/de.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > [External Workbenches](Category_External Workbenches.md) > [Fasteners](Category_Fasteners.md) > Fasteners Workbench/de
