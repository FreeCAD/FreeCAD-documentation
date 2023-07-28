---
- GuiCommand:/de
   Name:Mesh BuildRegularSolid
   Name/de:Mesh RegelgeometrieErstellen
   MenuLocation:Netze → Regelgeometrie...
   Workbenches:[Mesh](Mesh_Workbench/de.md)
---

# Mesh BuildRegularSolid/de



## Beschreibung

Der Befehl **Mesh RegelgeometrieErstellen** erstellt ein regelmäßiges parametrisches Festkörper-Netzobjekt.



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Mesh_BuildRegularSolid.svg" width=16px> [Regelgeometrie...](Mesh_BuildRegularSolid/de.md)** drücken.
    -   Den Menüeintrag **Meshes → <img src="images/Mesh_BuildRegularSolid.svg" width=16px> Regelgeometrie...** auswählen.
2.  Das Dialogfenster **Regelgeometrie** wird geöffnet.
3.  Zuerst den Typ des Netzobjekts aus der Ausklappliste auswählen:
    -   
        **<img src="images/Mesh_Cube.svg" width=16px> Würfel
**
        

    -   
        **<img src="images/Mesh_Cylinder.svg" width=16px> Zylinder
**
        

    -   
        **<img src="images/Mesh_Cone.svg" width=16px> Kegel
**
        

    -   
        **<img src="images/Mesh_Sphere.svg" width=16px> Kugel
**
        

    -   
        **<img src="images/Mesh_Ellipsoid.svg" width=16px> Ellipsoid
**
        

    -   
        **<img src="images/Mesh_Torus.svg" width=16px> Torus
**
        
4.  Die erforderlichen Einstellungen festlegen. Welche Einstellungen angezeigt werden, hängt vom Typ des Netzobjekts ab. Siehe [Eigenschaften](#Eigenschaften.md).
5.  Für Netze mit geschwungenen oberflächen: ein höherer **Sampling**-Wert ergibt ein feineres Netz.
6.  Die Schaltfläche {{button|Erstellen}} drücken, um ein Netzobjekt zu erstellen.
7.  Wahlweise mehr Netzobjekte erstellen.
8.  Die Schaltfläche {{button|Close}} drücken, um das Dialogfenster zu schließen und den Befehl zu beenden.



## Hinweise

-   Die mit diesem Befehl erstellten Netzobjekte sind parametrisch. Immer wenn sie neu berechnet werden, z.B. nach dem Ändern eines Parameters, wird ihr Netz neu aufgebaut. Das bedeutet, dass die Anwendung von Befehlen wie [Mesh NeuVernetzenGmsh](Mesh_RemeshGmsh/de.md), [Mesh Skalieren](Mesh_Scale.md) usw. bei ihnen normalerweise nicht sinnvoll ist.



## Eigenschaften

Netzobjekte, die mit diesem Befehl erstellt werden erben sämtliche Einstellungen eines [Mesh Formelements](Mesh_Feature/de.md). Zusätzlich besitzt jeder Typ der Netzobjekte einige Einstellungen zur Steuerung seines parametrischen Verhaltens:



### <img alt="" src=images/Mesh_Cube.svg  style="width:32px;"> Würfel 



#### Daten


{{TitleProperty|Cube}}

-    {{PropertyData/de|Height|FloatConstraint}}: die Höhe des Würfels

-    {{PropertyData/de|Length|FloatConstraint}}: die Länge des Würfels

-    {{PropertyData/de|Width|FloatConstraint}}: die Breite des Würfels



### <img alt="" src=images/Mesh_Cylinder.svg  style="width:32px;"> Zylinder 



#### Daten 


{{TitleProperty|Basis}}

-    {{PropertyData/de|Closed|Bool}}: wenn auf `False`, bleiben die ebenen Enden des Zylinders offen.

-    {{PropertyData/de|Edge Length|FloatConstraint}}: die Kantenlänge der Flächen im Netz.

-    {{PropertyData/de|Length|FloatConstraint}}: die Länge des Zylinders.

-    {{PropertyData/de|Radius|FloatConstraint}}: der Radius des Zylinders.

-    {{PropertyData/de|Sampling|IntegerConstraint}}: die Anzahl der Flächen entlang der gekrümmten Oberfläche.



### <img alt="" src=images/Mesh_Cone.svg  style="width:32px;"> Kegel 



#### Daten 


{{TitleProperty|Basis}}

-    {{PropertyData/de|Closed|Bool}}: wenn auf `False` gesetzt, bleiben ebene Enden von Kegeln offen.

-    {{PropertyData/de|Edge Length|FloatConstraint}}: die Kantenlänge der Flächen im Netz.

-    {{PropertyData/de|Length|FloatConstraint}}: die Länge des Kegels

-    {{PropertyData/de|Radius 1|FloatConstraint}}: der erste Radius des Kegels. Kann {{value|0}} sein.

-    {{PropertyData/de|Radius 2|FloatConstraint}}: der zweite Radius des Kegels. Kann {{value|0}} sein.

-    {{PropertyData/de|Sampling|IntegerConstraint}}: die Anzahl der Flächen entlang der gekrümmten Oberfläche.



### <img alt="" src=images/Mesh_Sphere.svg  style="width:32px;"> Kugel 



#### Daten 


{{TitleProperty|Basis}}

-    {{PropertyData/de|Radius|FloatConstraint}}: der Radius der Kugel.

-    {{PropertyData/de|Sampling|IntegerConstraint}}: die Anzahl der Flächen entlang beider Richtungen der gekrümmten Oberfläche.

### <img alt="" src=images/Mesh_Ellipsoid.svg  style="width:32px;"> Ellipsoid 



#### Daten 


{{TitleProperty|Basis}}

-    {{PropertyData/de|Radius 1|FloatConstraint}}: der erste Radius des Ellipsoids.

-    {{PropertyData/de|Radius 2|FloatConstraint}}: der zweite Radius des Ellipsoids.

-    {{PropertyData/de|Sampling|IntegerConstraint}}: die Anzahl der Flächen entlang beider Richtungen der gekrümmten Oberfläche.

### <img alt="" src=images/Mesh_Torus.svg  style="width:32px;"> Torus 



#### Daten 


{{TitleProperty|Basis}}

-    {{PropertyData/de|Radius 1|FloatConstraint}}: der erste (Haupt-) Radius des Torus.

-    {{PropertyData/de|Radius 2|FloatConstraint}}: der zweite Radius des Torus.

-    {{PropertyData/de|Sampling|IntegerConstraint}}: die Anzahl der Flächen entlang beider Richtungen der gekrümmten Oberfläche.





{{Mesh Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh BuildRegularSolid/de
