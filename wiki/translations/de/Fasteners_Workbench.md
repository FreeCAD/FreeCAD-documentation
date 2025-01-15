# <img alt="Arbeitsbereichssymbol Verbindungselemente" src=images/Fasteners_workbench_icon.svg  style="width:64px;"> Fasteners Workbench/de






## Einführung

Der <img alt="" src=images/Fasteners_workbench_icon.svg  style="width:24px;"> [Arbeitsbereich Verbindungselemente](Fasteners_Workbench/de.md) ist ein [externer Arbeitsbereich](External_workbenches/de.md), der Bauteilen bzw. Baugruppen unterschiedliche Verbindungselemente hinzufügen kann.

<img alt="" src=images/Fasteners_Toolbars.png  style="width:500px;"> 
*Das optionale Layout des Arbeitsbereichs mit einer Symbolleiste.<br> Verbindungselemente mit metrischen Abmessungen haben orangefarbene Symbole.<br> Verbindungselemente mit Abmessungen in Zoll haben türkisfarbene Symbole.*



## Einrichtung

1.  Arbeitsbereich Verbindungselemente über den [Addon-Manager](Std_AddonMgr/de.md) installieren. Zur manuellen Installation siehe: [Weitere Arbeitsbereiche installieren](Installing_more_workbenches/de.md).
2.  FreeCAD neu starten.
3.  Den Arbeitsbereich <img alt="" src=images/Fasteners_workbench_icon.svg  style="width:24px;"> [Fasteners](Fasteners_Workbench/de.md) (Verbindungselemente) aus der Auswahlliste [Arbeitsbereich](Std_Workbench/de.md) auswählen.
4.  Bei Bedarf kann die Symbolleiste und die Menüanordnung geändert werden:
    1.  
        **Bearbeiten → Einstellungen... → Fasteners → General settings**
        
        .

    2.  Eine der vorhandenen Optionen unter **Toolbar screw icons grouping** auswählen:
        -   
            **Keine**
            
            : Alle Verbindungselemente befinden sich in einer einzigen Symbolleiste. Um sie zu erweitern und alle vorhandenen Schaltflächen zu sehen, benutzt man die Schaltfläche **&gt;&gt;**.

        -   
            **Separate toolbars**
            
            : Die Verbindungselemente werden in mehreren Symbolleisten gruppiert. Dies ist das Standardlayout.

        -   
            **Dropdown buttons**
            
            : Die Verbindungselemente werden in einer Symbolleiste mit Ausklappmenüs gruppiert.

    3.  Wahlweise einen oder mehrere Optionen unter **Fastener standards shown in toolbars** deaktivieren. Deaktivierte Normen sind noch immer über das Menü erreichbar.

    4.  FreeCAD neu starten.



## Anwendung

Verbindungselemente können zugeordnet oder lose sein. Zugeordnete Verbindungselemente haben ein {{PropertyData/de|Base Object}}, eine kreisförmige Kante, und ihre {{PropertyData/de|Placement}} ist dynamisch mit dem Objekt verknüpft. Der Befehl <img alt="" src=images/Fasteners_Move.svg  style="width:16px;"> [Fasteners Bewegen](Fasteners_Move/de.md) kann dazu benutzt werden, ein Verbindungselement zu befestigen oder zu lösen.



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
2.  Auswahl einer oder mehrerer kreisförmiger Kanten und/oder Flächen mit kreisförmigen Kanten. Für Senkschrauben muss die obere Kante der Lochsenkung ausgewählt werden.
3.  Das gewünschte Verbindungselement auswählen, durch anklicken seiner Schaltfläche oder durch Auswahl aus dem Menü.
4.  Jeder kreisförmigen Kante wird ein Verbindungselement zugeordnet.
5.  Die vorgegebenen Abmessungen jedes einzelnen Verbindungselements sind von dem Radius der jeweiligen kreisförmigen Kante abhängig, der es zugeordnet wurde. Senkschrauben werden nach Kopfdurchmesser ausgewählt, andere Verbindungselemente nach ihrem Schaftdurchmesser.
6.  Optional können die Abmessungen und andere Eigenschaften der Verbindungselemente verändert werden. Siehe oben.
7.  Verbindungselemente, die verkehrt herum erscheinen, können mit dem Befehl <img alt="" src=images/Fasteners_Flip.svg  style="width:16px;"> [Fasteners Umdrehen](Fasteners_Flip/de.md) umgedreht werden oder durch Ändern ihrer {{PropertyData/de|Invert}}.
8.  Optional kann die {{PropertyData/de|Offset}} geändert werden, um einen Abstand zwischen den Verbindungselementen und den Kanten, denen sie zugeordnet sind, herzustellen.



## Hinweise

-   Um Gewinde zu erzeugen, muss die {{PropertyData/de|Thread}} eines Verbindungselements auf `True` geändert werden. Gewinde zu erzeugen ist aufwändig. Eine Neuberechnung dauert viel länger, wenn ein Dokument viele Verbindungselemente mit Gewinden enthält.
-   Die {{PropertyData/de|Invert}} und die {{PropertyData/de|Offset}} werden für nicht befestigte Verbindungselemente ignoriert.



## Befehle

-   <img alt="" src=images/Fasteners_Flip.svg  style="width:32px;"> [Verbindungselement Umdrehen](Fasteners_Flip/de.md): Ausrichtung der zugeordneten Verbindungselemente umkehren.

-   <img alt="" src=images/Fasteners_Move.svg  style="width:32px;"> [Verbindungselement Bewegen](Fasteners_Move/de.md): Ein Verbindungselement auf eine kreisförmige Kante bewegen und mit dieser zu verbinden. Kann auch zum Lösen der Verbindung verwendet werden.

-   <img alt="" src=images/Fasteners_Simplify.svg  style="width:32px;"> [Form vereinfachen](Fasteners_Simplify/de.md): Erstellt nichtparametrische Kopien von Verbindungselementen.

-   <img alt="" src=images/Fasteners_MatchTypeInner.svg  style="width:32px;"> [Match tap hole](Fasteners_MatchTypeInner/de.md): Kreisförmige Kanten werden als Gewindebohrungen angesehen, wenn neue Verbindungselemente mit ihnen verbunden werden.

-   <img alt="" src=images/Fasteners_MatchTypeOuter.svg  style="width:32px;"> [Match for pass hole](Fasteners_MatchTypeOuter/de.md): Kreisförmige Kanten werden als Durchgangslöcher angesehen, wenn neue Verbindungselemente mit ihnen verbunden werden.

-   <img alt="" src=images/Fasteners_BOM.svg  style="width:32px;"> [Stückliste generieren](Fasteners_BOM/de.md): Erstellt eine Tabelle mit einer Stückliste für die im Dokument verwendeten Verbindungselemente.

-   <img alt="" src=images/Fasteners_ScrewCalculator.svg  style="width:32px;"> [Schraubenberechner](Fasteners_ScrewCalculator/de.md): Zeigt einen Rechner zum Ermitteln des Kernlochdurchmessers einer Gewindebohrung an.

-   <img alt="" src=images/Fasteners_ChangeParameters.svg  style="width:32px;"> [Parameter der Verbindungselemente ändern](Fasteners_ChangeParameters/de.md): Ändert die Parameter der Verbindungselemente.



## Verbindungselemente

Verbindungselemente mit metrischen Maßen haben orangefarbene Symbole. Befestigungselemente mit Zollmaßen haben türkisfarbene Symbole.



### Sechskantschrauben und -Bolzen 

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.6.svg  style="width:32px;"> **ASME B18.2.1.6** UNC Sechskantschraube.

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.8.svg  style="width:32px;"> **ASME B18.2.1.8** UNC Sechskantschraube mit Flansch.

-   <img alt="" src=images/Fasteners_DIN571.svg  style="width:32px;"> **DIN 571** Sechskantholzschraube.

-   <img alt="" src=images/Fasteners_DIN933.svg  style="width:32px;"> **DIN 933** Sechskantschraube.

-   <img alt="" src=images/Fasteners_DIN961.svg  style="width:32px;"> **DIN 961** Sechskantschraube.

-   <img alt="" src=images/Fasteners_EN1662.svg  style="width:32px;"> **EN 1662** Sechskantschrauben mit Flansch, leichte Reihe.

-   <img alt="" src=images/Fasteners_EN1665.svg  style="width:32px;"> **EN 1665** Sechskantschrauben mit Flansch, schwere Reihe.

-   <img alt="" src=images/Fasteners_ISO4014.svg  style="width:32px;"> 
**ISO 4014** Sechskantschrauben. *Produktklassen A und B.*

-   <img alt="" src=images/Fasteners_ISO4015.svg  style="width:32px;"> **ISO 4015** Hexagon head bolt with reduced shank.

-   <img alt="" src=images/Fasteners_ISO4016.svg  style="width:32px;"> 
**ISO 4016** Hexagon head bolt. *Product grade C.*

-   <img alt="" src=images/Fasteners_ISO4017.svg  style="width:32px;"> 
**ISO 4017** Sechskantschrauben. *Produktklassen A und B.*

-   <img alt="" src=images/Fasteners_ISO4018.svg  style="width:32px;"> 
**ISO 4018** Hexagon head screw. *Product grade C.*

-   <img alt="" src=images/Fasteners_ISO4162.svg  style="width:32px;"> 
**ISO 4162** Hexagon bolt with flange, small series. *Product grade A with driving feature of product grade B.*

-   <img alt="" src=images/Fasteners_ISO8676.svg  style="width:32px;"> 
**ISO 8676** Sechskantschraube mit Feingewinde. *Produktklassen A und B.*

-   <img alt="" src=images/Fasteners_ISO8765.svg  style="width:32px;"> **ISO 8765** Hexagon head bolt with fine pitch thread.

-   <img alt="" src=images/Fasteners_ISO15071.svg  style="width:32px;"> 
**ISO 15071** Hexagon bolt with flange, small series. *Product grade A.*

-   <img alt="" src=images/Fasteners_ISO15072.svg  style="width:32px;"> 
**ISO 15072** Hexagon bolt with flange and fine pitch thread, small series. *Product grade A.*



### Schrauben mit Innensechskant 

-   <img alt="" src=images/Fasteners_ASMEB18.3.1A.svg  style="width:32px;"> **ASME B18.3.1A** UNC hexagon socket head cap screw.

-   <img alt="" src=images/Fasteners_ASMEB18.3.1G.svg  style="width:32px;"> **ASME B18.3.1G** UNC hexagon socket head cap screw with low head.

-   <img alt="" src=images/Fasteners_ASMEB18.3.2.svg  style="width:32px;"> **ASME B18.3.2** UNC hexagon socket countersunk head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.3.3A.svg  style="width:32px;"> **ASME B18.3.3A** UNC hexagon socket button head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.3.3B.svg  style="width:32px;"> **ASME B18.3.3B** UNC hexagon socket button head screw with flange.

-   <img alt="" src=images/Fasteners_ASMEB18.3.4.svg  style="width:32px;"> **ASME B18.3.4** UNC hexagon socket head shoulder screw.

-   <img alt="" src=images/Fasteners_DIN6912.svg  style="width:32px;"> **DIN 6912** Zylinderschrauben mit Innensechskant und Schlüsselführung niedriger Kopf.

-   <img alt="" src=images/Fasteners_DIN7984.svg  style="width:32px;"> **DIN 7984** Zylinderschrauben mit Innensechskant, niedriger Kopf.

-   <img alt="" src=images/Fasteners_ISO2936.svg  style="width:32px;"> **ISO 2936** Hexagon socket screw key.

-   <img alt="" src=images/Fasteners_ISO4762.svg  style="width:32px;"> **ISO 4762** Zylinderschrauben mit Innensechskant.

-   <img alt="" src=images/Fasteners_ISO7379.svg  style="width:32px;"> **ISO 7379** Zylinderkopfschrauben mit Innensechskant und Ansatzschaft.

-   <img alt="" src=images/Fasteners_ISO7380-1.svg  style="width:32px;"> **ISO 7380-1** Halbrundkopfschrauben mit Innensechsrund.

-   <img alt="" src=images/Fasteners_ISO7380-2.svg  style="width:32px;"> **ISO 7380-2** Halbrundkopfschrauben mit Innensechsrund und Bund.

-   <img alt="" src=images/Fasteners_ISO10642.svg  style="width:32px;"> **ISO 10642** Senkschrauben mit Innensechskant.



### Schrauben mit Innensechsrund 

-   <img alt="" src=images/Fasteners_ISO14579.svg  style="width:32px;"> **ISO 14579** Zylinderschr. mit Innensechsrund.

-   <img alt="" src=images/Fasteners_ISO14580.svg  style="width:32px;"> **ISO 14580** Zylinderschrauben mit Innensechsrund, niedriger Kopf.

-   <img alt="" src=images/Fasteners_ISO14581.svg  style="width:32px;"> **ISO 14581** Hexalobular socket countersunk flat head screw.

-   <img alt="" src=images/Fasteners_ISO14582.svg  style="width:32px;"> **ISO 14582** Senkschrauben mit Innensechsrund, hoher Kopf.

-   <img alt="" src=images/Fasteners_ISO14583.svg  style="width:32px;"> **ISO 14583** Flachkopfschrauben mit Innensechsrund.

-   <img alt="" src=images/Fasteners_ISO14584.svg  style="width:32px;"> **ISO 14584** Linsensenkschrauben mit Innensechsrund.



### Schlitzschrauben

-   <img alt="" src=images/Fasteners_ASMEB18.6.1.2.svg  style="width:32px;"> **ASME B18.6.1.2** Slotted flat countersunk head wood screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.1.4.svg  style="width:32px;"> **ASME B18.6.1.4** Slotted oval countersunk head wood screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.1A.svg  style="width:32px;"> **ASME B18.6.3.1A** UNC Senkkopfschraube mit Schlitz.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.4A.svg  style="width:32px;"> **ASME B18.6.3.4A** UNC slotted oval countersunk head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.9A.svg  style="width:32px;"> **ASME B18.6.3.9A** UNC slotted pan head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.10A.svg  style="width:32px;"> **ASME B18.6.3.10A** UNC Slotted fillister head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.12A.svg  style="width:32px;"> **ASME B18.6.3.12A** UNC Slotted truss head screws.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.16A.svg  style="width:32px;"> **ASME B18.6.3.16A** UNC Slotted round head screw.

-   <img alt="" src=images/Fasteners_DIN84.svg  style="width:32px;"> 
**DIN 84 (superseded by ISO 1207)** Slotted cheese head screw. *Product grade A.*

-   <img alt="" src=images/Fasteners_DIN96.svg  style="width:32px;"> **DIN 96** Slotted half round head wood screw.

-   <img alt="" src=images/Fasteners_GOST1144-1.svg  style="width:32px;"> **GOST 1144-1** Slotted half round head wood screw.

-   <img alt="" src=images/Fasteners_GOST1144-2.svg  style="width:32px;"> **GOST 1144-2** Slotted half round head wood screw.

-   <img alt="" src=images/Fasteners_ISO1207.svg  style="width:32px;"> 
**ISO 1207** Zylinderschrauben mit Schlitz. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_ISO1580.svg  style="width:32px;"> 
**ISO 1580** Flachkopfschrauben mit Schlitz. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_ISO2009.svg  style="width:32px;"> 
**ISO 2009** Senkschrauben mit Schlitz. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_ISO2010.svg  style="width:32px;"> 
**ISO 2010** Linsensenkschrauben mit Schlitz. *Produktklasse A.*



### Kreuzschlitzschrauben

-   <img alt="" src=images/Fasteners_ASMEB18.6.1.3.svg  style="width:32px;"> **ASME B18.6.1.3** Flat countersunk head wood screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.1.5.svg  style="width:32px;"> **ASME B18.6.1.5** Oval countersunk head wood screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.1B.svg  style="width:32px;"> **ASME B18.6.3.1B** UNC flat countersunk head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.4B.svg  style="width:32px;"> **ASME B18.6.3.4B** UNC oval countersunk head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.9B.svg  style="width:32px;"> **ASME B18.6.3.9B** UNC pan head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.10B.svg  style="width:32px;"> **ASME B18.6.3.10B** UNC fillister head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.12C.svg  style="width:32px;"> **ASME B18.6.3.12C** UNC truss head screws.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.16B.svg  style="width:32px;"> **ASME B18.6.3.16B** UNC round head screw.

-   <img alt="" src=images/Fasteners_DIN967.svg  style="width:32px;"> **DIN 967** Linsenkopfschrauben mit Bund.

-   <img alt="" src=images/Fasteners_DIN7996.svg  style="width:32px;"> **DIN 7996** Pan head wood screw.

-   <img alt="" src=images/Fasteners_GOST1144-3.svg  style="width:32px;"> **GOST 1144-3** Pan head wood screw.

-   <img alt="" src=images/Fasteners_GOST1144-4.svg  style="width:32px;"> **GOST 1144-4** Pan head wood screw.

-   <img alt="" src=images/Fasteners_ISO7045.svg  style="width:32px;"> 
**ISO 7045** Linsenkopfschraube. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_ISO7046.svg  style="width:32px;"> 
**ISO 7046** Senkschrauben. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_ISO7047.svg  style="width:32px;"> 
**ISO 7047** Linsensenkschrauben. *Produktklasse A.*

-   <img alt="" src=images/Fasteners_ISO7048.svg  style="width:32px;"> **ISO 7048** Zylinderschrauben.

-   <img alt="" src=images/Fasteners_ISO7049-C.svg  style="width:32px;"> **ISO 7049-C** Pan head self tapping screws with conical point.

-   <img alt="" src=images/Fasteners_ISO7049-F.svg  style="width:32px;"> **ISO 7049-F** Pan head self tapping screws with flat point.

-   <img alt="" src=images/Fasteners_ISO7049-R.svg  style="width:32px;"> **ISO 7049-R** Pan head self tapping screws with rounded point.

### Other head bolts 

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.1.svg  style="width:32px;"> **ASME B18.2.1.1** UNC square head bolt.

-   <img alt="" src=images/Fasteners_ASMEB18.5.2.svg  style="width:32px;"> **ASME B18.5** UNC Round head square neck bolt.

-   <img alt="" src=images/Fasteners_DIN478.svg  style="width:32px;"> **DIN 478** Square head bolt with collar.

-   <img alt="" src=images/Fasteners_DIN603.svg  style="width:32px;"> **DIN 603** Round head square neck bolt.

-   <img alt="" src=images/Fasteners_ISO2342.svg  style="width:32px;"> **ISO 2342** Headless screw with shank

### Set screws 

-   <img alt="" src=images/Fasteners_ASMEB18.3.5A.svg  style="width:32px;"> **ASME B18.3.5A** UNC hexagon socket set screw with flat point.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5B.svg  style="width:32px;"> **ASME B18.3.5B** UNC hexagon socket set screw with cone point.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5C.svg  style="width:32px;"> **ASME B18.3.5C** UNC hexagon socket set screw with dog point.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5D.svg  style="width:32px;"> **ASME B18.3.5D** UNC hexagon socket set screw with cup point.

-   <img alt="" src=images/Fasteners_ISO4026.svg  style="width:32px;"> **ISO 4026** Gewindestifte mit Innensechskant und Kegelstumpf.

-   <img alt="" src=images/Fasteners_ISO4027.svg  style="width:32px;"> **ISO 4027** Gewindestifte mit Innensechskant und Spitze.

-   <img alt="" src=images/Fasteners_ISO4028.svg  style="width:32px;"> **ISO 4028** Gewindestifte mit Innensechskant und Zapfen.

-   <img alt="" src=images/Fasteners_ISO4029.svg  style="width:32px;"> **ISO 4029** Gewindestifte mit Innensechskant und Ringschneide.

-   <img alt="" src=images/Fasteners_ISO4766.svg  style="width:32px;"> **ISO 4766** Slotted socket set screw with flat point.

-   <img alt="" src=images/Fasteners_ISO7434.svg  style="width:32px;"> **ISO 7434** Slotted socket set screw with cone point.

-   <img alt="" src=images/Fasteners_ISO7435.svg  style="width:32px;"> **ISO 7435** Slotted socket set screw with long dog point.

-   <img alt="" src=images/Fasteners_ISO7436.svg  style="width:32px;"> **ISO 7436** Slotted socket set screw with cup point.

### Thumb screws 

-   <img alt="" src=images/Fasteners_DIN464.svg  style="width:32px;"> **DIN 464** Knurled thumb screw, high type.

-   <img alt="" src=images/Fasteners_DIN465.svg  style="width:32px;"> **DIN 465** Slotted knurled thumb screw, high type.

-   <img alt="" src=images/Fasteners_DIN653.svg  style="width:32px;"> **DIN 653** Knurled thumb screw, low type.



### Muttern

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.1A.svg  style="width:32px;"> **ASME B18.2.2.1A** UNC hexagon machine screw nut.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.1B.svg  style="width:32px;"> **ASME B18.2.2.1B** UNC square machine screw nut.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.2.svg  style="width:32px;"> **ASME 18.2.2.2** UNC square nut.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.4A.svg  style="width:32px;"> **ASME B18.2.2.4A** UNC hexagon nut.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.4B.svg  style="width:32px;"> **ASME B18.2.2.4B** UNC hexagon thin nut.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.5.svg  style="width:32px;"> **ASME 18.2.2.5** UNC hexagon castle nut.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.12.svg  style="width:32px;"> **ASME 18.2.2.12** UNC hexagon nut with flange.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.13.svg  style="width:32px;"> **ASME 18.2.2.13** UNC hexagon coupling nut.

-   <img alt="" src=images/Fasteners_ASMEB18.6.9A.svg  style="width:32px;"> **ASME 18.6.9A** Wing nut, type A.

-   <img alt="" src=images/Fasteners_DIN315.svg  style="width:32px;"> **DIN 315** Wing nut.

-   <img alt="" src=images/Fasteners_DIN557.svg  style="width:32px;"> **DIN 557** Vierkantmuttern.

-   <img alt="" src=images/Fasteners_DIN562.svg  style="width:32px;"> **DIN 562** Vierkantmuttern.

-   <img alt="" src=images/Fasteners_DIN917.svg  style="width:32px;"> **DIN 917** Cap nut, low form.

-   <img alt="" src=images/Fasteners_DIN928.svg  style="width:32px;"> **DIN 928** Square weld nut.

-   <img alt="" src=images/Fasteners_DIN929.svg  style="width:32px;"> **DIN 929** Hexagon weld nut.

-   <img alt="" src=images/Fasteners_DIN934.svg  style="width:32px;"> 
**DIN 934 (superseded by ISO 4035 and ISO 8673)** Hexagon thin nut chamfered. *Product grades A and B.*

-   <img alt="" src=images/Fasteners_DIN935.svg  style="width:32px;"> **DIN 935** Hexagon castle nut.

-   <img alt="" src=images/Fasteners_DIN985.svg  style="width:32px;"> **DIN 985** Sechskantsicherungsmuttern mit Kunststoffring.

-   <img alt="" src=images/Fasteners_DIN1587.svg  style="width:32px;"> **DIN 1587** Cap nut.

-   <img alt="" src=images/Fasteners_DIN6330.svg  style="width:32px;"> **DIN 6330** Hexagon nut 1.5d high.

-   <img alt="" src=images/Fasteners_DIN6331.svg  style="width:32px;"> **DIN 6331** Hexagon with collar 1.5d high.

-   <img alt="" src=images/Fasteners_DIN6334.svg  style="width:32px;"> **DIN 6334** Hexagon coupling nut.

-   <img alt="" src=images/Fasteners_DIN7967.svg  style="width:32px;"> **DIN 7967** Self-locking counter nut.

-   <img alt="" src=images/Fasteners_EN1661.svg  style="width:32px;"> **EN 1661** Sechskantmuttern mit Flansch.

-   <img alt="" src=images/Fasteners_GOST11860-1.svg  style="width:32px;"> **GOST 11860-1** Cap nut.

-   <img alt="" src=images/Fasteners_ISO4032.svg  style="width:32px;"> 
**ISO 4032** Sechskantmuttern (Typ 1). *Produktklassen A und B.*

-   <img alt="" src=images/Fasteners_ISO4033.svg  style="width:32px;"> 
**ISO 4033** Hohe Sechskantmuttern (Typ 2). *Produktklassen A und B.*

-   <img alt="" src=images/Fasteners_ISO4034.svg  style="width:32px;"> **ISO 4034** Hexagon nut, style 1.

-   <img alt="" src=images/Fasteners_ISO4035.svg  style="width:32px;"> 
**ISO 4035** Sechskantmuttern mit Fase, niedrige Form (Typ 0). *Produktklassen A und B.*

-   <img alt="" src=images/Fasteners_ISO4161.svg  style="width:32px;"> **ISO 4161** Hexagon nut with flange.

-   <img alt="" src=images/Fasteners_ISO7040.svg  style="width:32px;"> **ISO 7040** Prevailing torque type hexagon nut (with non-metallic insert).

-   <img alt="" src=images/Fasteners_ISO7041.svg  style="width:32px;"> **ISO 7041** Prevailing torque type hexagon nut (with non-metallic insert), style 2.

-   <img alt="" src=images/Fasteners_ISO7043.svg  style="width:32px;"> **ISO 7043** Prevailing torque type hexagon nut with flange (with non-metallic insert).

-   <img alt="" src=images/Fasteners_ISO7044.svg  style="width:32px;"> **ISO 7044** Prevailing torque type all-metal hexagon nut with flange.

-   <img alt="" src=images/Fasteners_ISO7719.svg  style="width:32px;"> **ISO 7719** Prevailing torque type all-metal hexagon nut.

-   <img alt="" src=images/Fasteners_ISO7720.svg  style="width:32px;"> **ISO 7720** Prevailing torque type all-metal hexagon nut, style 2.

-   <img alt="" src=images/Fasteners_ISO8673.svg  style="width:32px;"> 
**ISO 8673** Hexagon nut with fine pitch thread, style 1. *Product grades A and B.*

-   <img alt="" src=images/Fasteners_ISO8674.svg  style="width:32px;"> 
**ISO 8674** Hexagon high nut with fine pitch thread, style 2. *Product grades A and B.*

-   <img alt="" src=images/Fasteners_ISO8675.svg  style="width:32px;"> 
**ISO 8675** Hexagon thin nut with fine pitch thread, style 0. *Product grades A and B.*

-   <img alt="" src=images/Fasteners_ISO10511.svg  style="width:32px;"> **ISO 10511** Prevailing torque type hexagon thin nut (with non-metallic insert).

-   <img alt="" src=images/Fasteners_ISO10512.svg  style="width:32px;"> **ISO 10512** Prevailing torque type hexagon nut with fine pitch thread (with non-metallic insert).

-   <img alt="" src=images/Fasteners_ISO10513.svg  style="width:32px;"> **ISO 10513** Prevailing torque type all-metal hexagon nut with fine pitch thread.

-   <img alt="" src=images/Fasteners_ISO10663.svg  style="width:32px;"> **ISO 10663** Hexagon nut with flange and fine pitch thread.

-   <img alt="" src=images/Fasteners_ISO12125.svg  style="width:32px;"> **ISO 12125** Prevailing torque type hexagon nut with flange and fine pitch thread (with non-metallic insert).

-   <img alt="" src=images/Fasteners_ISO12126.svg  style="width:32px;"> **ISO 12126** Prevailing torque type all-metal hexagon nut with flange and fine pitch thread.

-   <img alt="" src=images/Fasteners_ISO21670.svg  style="width:32px;"> **ISO 21670** Hexagon weld nut with flange.

-   <img alt="" src=images/Fasteners_SAEJ483a1.svg  style="width:32px;"> **SAE J483a 1** Low cap nut.

-   <img alt="" src=images/Fasteners_SAEJ483a2.svg  style="width:32px;"> **SAE J483a 2** High cap nut.

### T-slot fasteners 

-   <img alt="" src=images/Fasteners_DIN508.svg  style="width:32px;"> **DIN 508** Mutter für T-Nut.

-   <img alt="" src=images/Fasteners_GN505.svg  style="width:32px;"> **GN 505** Serrated quarter-turn T-slot nut.

-   <img alt="" src=images/Fasteners_GN505.4.svg  style="width:32px;"> **GN 505.4** Serrated T-slot bolt.

-   <img alt="" src=images/Fasteners_GN506.svg  style="width:32px;"> **GN 506** T-Slot swivel nut.

-   <img alt="" src=images/Fasteners_GN507.svg  style="width:32px;"> **GN 507** Mutter für T-Nut.

-   <img alt="" src=images/Fasteners_ISO299.svg  style="width:32px;"> **ISO 299** T-Slot nut.



### Scheiben

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12A.svg  style="width:32px;"> **ASME B18.21.1.12A** UN Unterlegscheibe, schmale Reihe.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12B.svg  style="width:32px;"> **ASME B18.21.1.12B** UN Scheibe, normale Reihe.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12C.svg  style="width:32px;"> **ASME B18.21.1.12C** UN Scheibe, breite Reihe.

-   <img alt="" src=images/Fasteners_DIN6319C.svg  style="width:32px;"> **DIN 6319C** Spherical washer.

-   <img alt="" src=images/Fasteners_DIN6319D.svg  style="width:32px;"> **DIN 6319D** Conical seat.

-   <img alt="" src=images/Fasteners_DIN6319G.svg  style="width:32px;"> **DIN 6319G** Conical seat.

-   <img alt="" src=images/Fasteners_DIN6340.svg  style="width:32px;"> **DIN 6340** Washer for clamping devices.

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

-   <img alt="" src=images/Fasteners_ISO8738.svg  style="width:32px;"> **ISO 8738** Plain washer for clevis pins.

-   <img alt="" src=images/Fasteners_NFE27-619.svg  style="width:32px;"> **NFE27-619** Countersunk washer.

### Rods, taps and dies 

-   <img alt="" src=images/Fasteners_ScrewTapInch.svg  style="width:32px;"> Zöllige Gewindestange zum Schneiden von Innengewinden.

-   <img alt="" src=images/Fasteners_ScrewDieInch.svg  style="width:32px;"> Gewindewerkzeug zum Schneiden von zölligen Außengewinden.

-   <img alt="" src=images/Fasteners_ThreadedRodInch.svg  style="width:32px;"> Zöllige Gewindestange **UNC**.

-   <img alt="" src=images/Fasteners_ThreadedRod.svg  style="width:32px;"> Metrische Gewindestange **DIN 975**.

-   <img alt="" src=images/Fasteners_ScrewTap.svg  style="width:32px;"> Metrische Gewindestange zum Schneiden von Innengewinden.

-   <img alt="" src=images/Fasteners_ScrewDie.svg  style="width:32px;"> Gewindewerkzeug zum Schneiden von metrischen Außengewinden.



### Einsätze

-   <img alt="" src=images/Fasteners_IUTHeatInsert.svg  style="width:32px;"> Einsätze zum Warmeinbetten.

-   <img alt="" src=images/Fasteners_PEMPressNut.svg  style="width:32px;"> Einpressmutter.

-   <img alt="" src=images/Fasteners_PEMStandoff.svg  style="width:32px;"> Einpressbuchse mit Gewinde.

-   <img alt="" src=images/Fasteners_PEMStud.svg  style="width:32px;"> Einpressbolzen.

-   <img alt="" src=images/Fasteners_PCBSpacer.svg  style="width:32px;"> Abstandshalter für Leiterplatten, Innengewinde beidseitig.

-   <img alt="" src=images/Fasteners_PCBStandoff.svg  style="width:32px;"> Abstandshalter für Leiterplatten mit Außen- und Innengewinde.

-   <img alt="" src=images/Fasteners_4PWTI.svg  style="width:32px;"> 4 prong threaded wood insert (DIN 1624 Tee nuts).



### Sicherungsringe

-   <img alt="" src=images/Fasteners_DIN471.svg  style="width:32px;"> **DIN 471** Sicherungsring für Wellen.

-   <img alt="" src=images/Fasteners_DIN472.svg  style="width:32px;"> **DIN 472** Sicherungsring für Bohrungen.

-   <img alt="" src=images/Fasteners_DIN6799.svg  style="width:32px;"> **DIN 6799** Sicherungsscheibe.



### Nägel

-   <img alt="" src=images/Fasteners_DIN1143.svg  style="width:32px;"> **DIN 1143** Round plain head nail for use in automatic nailing machines.

-   <img alt="" src=images/Fasteners_DIN1144-A.svg  style="width:32px;"> **DIN 1144-A** Nail for the installation of wood wool composite panels, 20mm round head.

-   <img alt="" src=images/Fasteners_DIN1151-A.svg  style="width:32px;"> **DIN 1151-A** Round plain head wire nail.

-   <img alt="" src=images/Fasteners_DIN1151-B.svg  style="width:32px;"> **DIN 1151-B** Round countersunk head wire nail.

-   <img alt="" src=images/Fasteners_DIN1152.svg  style="width:32px;"> **DIN 1152** Round lost head wire nail.

-   <img alt="" src=images/Fasteners_DIN1160-A.svg  style="width:32px;"> **DIN 1160-A** Clout or slate nail.

-   <img alt="" src=images/Fasteners_DIN1160-B.svg  style="width:32px;"> **DIN 1160-B** Clout or slate wide head nail.

### Pins

-   <img alt="" src=images/Fasteners_ISO1234.svg  style="width:32px;"> **ISO 1234** Split pin.

-   <img alt="" src=images/Fasteners_ISO2338.svg  style="width:32px;"> **ISO 2338** Parallel pin.

-   <img alt="" src=images/Fasteners_ISO2339.svg  style="width:32px;"> **ISO 2339** Taper pin.

-   <img alt="" src=images/Fasteners_ISO2340A.svg  style="width:32px;"> **ISO 2340A** Clevis pin.

-   <img alt="" src=images/Fasteners_ISO2340B.svg  style="width:32px;"> **ISO 2340B** Clevis pin without head (with split pin holes).

-   <img alt="" src=images/Fasteners_ISO2341A.svg  style="width:32px;"> **ISO 2341A** Clevis pin with head.

-   <img alt="" src=images/Fasteners_ISO2341B.svg  style="width:32px;"> **ISO 2341B** Clevis pin with head (with split pin hole).

-   <img alt="" src=images/Fasteners_ISO8733.svg  style="width:32px;"> **ISO 8733** Parallel pin with internal thread, unhardened.

-   <img alt="" src=images/Fasteners_ISO8734.svg  style="width:32px;"> **ISO 8734** Dowel pin.

-   <img alt="" src=images/Fasteners_ISO8735.svg  style="width:32px;"> **ISO 8735** Parallel pin with internal thread, hardened.

-   <img alt="" src=images/Fasteners_ISO8736.svg  style="width:32px;"> **ISO 8736** Taper pin with internal thread, unhardened.

-   <img alt="" src=images/Fasteners_ISO8737.svg  style="width:32px;"> **ISO 8737** Taper pin with external thread, unhardened.

-   <img alt="" src=images/Fasteners_ISO8739.svg  style="width:32px;"> **ISO 8739** Full-length grooved pin with pilot.

-   <img alt="" src=images/Fasteners_ISO8740.svg  style="width:32px;"> **ISO 8740** Full-length grooved pin with chamfer.

-   <img alt="" src=images/Fasteners_ISO8741.svg  style="width:32px;"> **ISO 8741** Half-length reverse taper grooved pin.

-   <img alt="" src=images/Fasteners_ISO8742.svg  style="width:32px;"> **ISO 8742** Third-length center grooved pin.

-   <img alt="" src=images/Fasteners_ISO8743.svg  style="width:32px;"> **ISO 8743** Half-length center grooved pin.

-   <img alt="" src=images/Fasteners_ISO8744.svg  style="width:32px;"> **ISO 8744** Full-length taper grooved pin.

-   <img alt="" src=images/Fasteners_ISO8745.svg  style="width:32px;"> **ISO 8745** Half-length taper grooved pin.

-   <img alt="" src=images/Fasteners_ISO8746.svg  style="width:32px;"> **ISO 8746** Grooved pin with round head.

-   <img alt="" src=images/Fasteners_ISO8747.svg  style="width:32px;"> **ISO 8747** Grooved pin with countersunk head.

-   <img alt="" src=images/Fasteners_ISO8748.svg  style="width:32px;"> **ISO 8748** Coiled spring pin, heavy duty.

-   <img alt="" src=images/Fasteners_ISO8750.svg  style="width:32px;"> **ISO 8750** Coiled spring pin, standard duty.

-   <img alt="" src=images/Fasteners_ISO8751.svg  style="width:32px;"> **ISO 8751** Coiled spring pin, light duty.

-   <img alt="" src=images/Fasteners_ISO8752.svg  style="width:32px;"> **ISO 8752** Slotted spring pin, heavy duty.

-   <img alt="" src=images/Fasteners_ISO13337.svg  style="width:32px;"> **ISO 13337** Slotted spring pin, light duty.



## Veraltet

-   <img alt="" src=images/Fasteners_ChamferHole.svg  style="width:32px;"> [Senkungen vornehmen](Fasteners_ChamferHole/de.md): Erstellt eine Senkung an einem Loch für Senkschrauben. Steht in {{VersionPlus/de|0.5.13}} nicht mehr zur Verfügung.



## Referenzen

-   Autor: (http://theseger.com/projects/author/shaise/ shaise)
    -   SchraubenErsteller: Ulrich Brammer
    -   Arbeitsbereichsumgebung: Shai Seger
-   Quellcode: <https://github.com/shaise/FreeCAD_FastenersWB>
-   Bug-Reports und Feature-Requests: <https://github.com/shaise/FreeCAD_FastenersWB/issues>
-   Forumsbeitrag: <https://forum.freecadweb.org/viewtopic.php?t=11429>



## Verweise

-   [BOLTS](https://github.com/jreinhardt/BOLTS): Eine offene Bibliothek für technische Spezifikationen.


{{Fasteners_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [User_Documentation](Category_User_Documentation.md) > [External_Workbenches](Category_External_Workbenches.md) > [Fasteners](Category_Fasteners.md) > Fasteners Workbench/de
