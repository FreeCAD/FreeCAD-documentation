# Material/de
}

## Überblick


{{TOCright}}

Diese Seite erklärt das Materialdatensystem in FreeCAD.

## Überblick 

Weil es schwierig bis unmöglich ist, einen festen oder vollständigen Satz an Materialeigenschaften festzulegen, wählen wir einen offeneren Weg. Jedes Objekt in FreeCad, das mit Materialien zu tun hat, hat eine Eigenschaft, die mit \"Material\" benannt ist. Diese besteht aus einer Schlüssel/Wert-Liste, die eine unendliche Zahl an Materialeigenschaften enthalten kann. Weil dieser Weg mit solchen Daten umzugehen, sehr offen und erweiterbar ist, besteht auch die Gefahr von Unordnung und Chaos. Deswegen beschreibt diese Seite einige Regeln und grundsätzliche Eigenschaften, um mit solchen Materialeigenschaften-Listen umzugehen.

## Regeln

Jeder Eigenschaftssatz hat nur einen notwendigen Eintrag, der \"Name\" benannt ist. Dies ist der primäre Schlüssel des Materials. Die restlichen Materialeigenschaften sind optional oder können aus einer Materialdatenbank bezogen werden.

Eigenschaftsnamen (Schlüssel) werden nach Wörtern geordnet, die durch Unterstriche getrennt sind. Der erste Teil-String wird nach der Anwendung oder Standard (standard) benannt, das Folgende kann benutzt werden, um die Eigenschaften weiter zu gruppieren. Die Werte können ebenfalls durch Unterstriche gruppiert werden, z.B. um verschiedene Stahlsorten zu unterscheiden. Beispiele:

-   Name=Steel\_Cast
-   SpecificWeight=7.85 (at 20° in kg/mm3)
-   EN10027\_name = S235JR+AR (steel standard EN 10027-1)
-   FEM\_YoungsModulus = xx ( in mm−1·kg·s−2)
-   FEM\_YoungsModulus\_Z
-   FEM\_YoungsModulus\_X

Jede Eigenschaft auf dieser Seite hat eine für Menschen lesbare Beschreibung, mit Verbindungen zu weiteren Informationen (z.B. Wikipedia).

Für jede Eigenschaft muss eine Maßeinheit angegeben werden, basierend auf dem FreeCAD-internen Einheitensystem mm-kg-s! Dies ermöglichte eine einheitliche Nutzung und Übersetzung.

Der Schlüssel (Name) und der Wert der Eigenschaft darf nur ASCII-Zeichen (7-Bit) beinhalten. Die Schlüssel werden in Camel-Case (Binnenmajuskel) geschrieben, aber case-insensitiv (unabhängig von der Groß- und Kleinschreibung) interpretiert.

Die Unterstriche ermöglichen später einen Eigenschaftseditor in Baumansicht, der eine Faltung erlaubt.

## Werkzeuge

Es gibt einige Quellen, um Materialien einfacher zu handhaben:

-   [Einheitenrechner](http://www.dimensionengine.com/), um Deine Materialinformationen in einer Einheit passend für FreeCAD zu erhalten
-   [<http://www.matweb.com/>](http://www.matweb.com/) freie Materialdatenbank mit tausenden Materialwerten

## Material-Datenbank 

Sobald der obige Standard implementiert ist, wäre es dumm, die Eigenschaften wieder und wieder in den Objekten zu speichern. Grundsätzlich können wir eine Material-DB mit den Namen als Primärschlüssel aufbauen. Falls du dann keine speziellen Voraussetzungen an das Material hast, gibst du einfach z.B. Name=Steel an und FreeCAD holt sich die entsprechenden Eigenschaften aus der Datenbank. Jede zusätzliche Eigenschaft, die du in der Liste (map) setzt, überschreibt die entsprechende aus der DB.

Zukünftig können wir die DB irgendwo im Netz ablegen und daraus eine grundsätzliche Open-Source Material-DB machen.

Momentan denke ich an einen einkompilierten Minidatensatz, mit einem Satz \"Basis\"-Materialien und ihren Grundeigenschaften und einer SQLite-basierten Vollversion.

## Material.py

Da die Handhabung von Materialeigenschaften mühselig ist, sollten wir ein Python-Frontend-Modul mit Namen {{FileName|Material.py}} entwickeln. Dies wäre der Platz, um alle möglichen Helfermethoden zur Materialhandhabung zu implementieren.

-   Berechnung von Masse aus Volumen und Dichte
-   Umrechnung in verschiedene Einheitensysteme
-   Berechnungen, die in speziellen Anwendungen benötigt werden (z.B. FEM)
-   und alles weitere, von dem wir momentan noch nichts wissen

Das Modul sollte so entwickelt sein, dass es sowohl in FreeCAD als auch unabhängig auf der Kommandozeile laufen kann (Material-Eigenschafts-Liste gegeben als Python-Liste (map)).

## Das FreeCAD Material-Karten Dateiformat 

Mit Materialien zu arbeiten heißt häufig Material-Definitionen zu importieren und exportieren. Dafür wird ein Dateiformat benötigt. Da wir nur Schlüssel-Wert-Paare haben, können wir ein einfaches und leicht zu lesendes und parsendes Dateiformat wählen. Hierfür wurde das [Initialisierungsdatei](http://de.wikipedia.org/wiki/Initialisierungsdatei)-Format gewählt. Es ist standardisiert und Parser sind bereits verfügbar. Z.B. das [Konfigparser-Modul in Python](http://docs.python.org/2/library/configparser.html).

Jede Materialbeschreibung befindet sich in einer Datei mit der Endung {{FileName|.FCMat}}. Einige dieser Dateien sind Bestandteil der FreeCAD-Quellen und werden in die Binärdatei eincompiliert. Dies wird gemacht um zusätzlichen Aufwand bei der Verteilung und beim Zugang zu vermeiden. Außerdem können Dateien an verschieden Orten abgelegt und gesucht werden, um nicht-Standard Material-Definitionen zu ermöglichen.

### Beispiel .FCMat-Datei 


```python      
 ; last modified 1 April 2001 by John Doe
 
 Name=Steel_Cast
 Father=Steel
 Source=Some material book everyone knows (or not) ;Some comment
  
 [EN10027]
 ; steel standard EN 10027-1
 Name=S235JR+AR      
 
 [Graphic]
 EmissivColor = 255,255,255
```

## Materialeigenschaften

Hier nun die Beschreibung von beschlossenen Materialeigenschaften. Du kannst gerne einen Unterabschnitt für die Materialeigenschaften des Bereichs einfügen, in dem Du Dich auskennst.

## Allgemein

  Eigenschaftsname   Beschreibung                                                                                                                                                                                            Einheit/Datentyp
  ------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------
  Name               Eindeutiger Name der Eigenschaft, gemäß den o.g. Regeln                                                                                                                                                 ASCII-String 7-bit
  Father             Name der Materialgruppe, zu der dieses Material gehört. Falls definiert, erbt dieses Material alle Vatereigenschaften. Das bedeutet, falls nicht definiert, werden die Vater-Eigenschaften verwendet.   ASCII-String 7-bit
  Description        Ein Platzhalter für eine längere Materialbeschreibung                                                                                                                                                   ASCII-String 7-bit
  SpecificWeight     Das spezifische Gewicht (auch als Gewicht pro Einheit (unit weight) bekannt) ist das Gewicht pro Volumeneeinheit eines Materials. Siehe: [Wichte](https://de.wikipedia.org/wiki/Wichte)                 kg/mm$^3$
  Vendor             Gibt die Marke oder den Hersteller des Materials an                                                                                                                                                     ASCII-String 7-bit
  ProductURL         Eine URL, wo Informationen über das Material zu finden sind                                                                                                                                             ASCII-String 7-bit
  SpecificPrice      Der Preis pro Einheit dieses Materials. Einheiten können sehr variieren (USD/m$^3$, EUR/Stück, etc\...)                                                                                                 ASCII-String 7-bit

  : Allgemeine Materialeigenschaften

**ToDos:** füge einige Eigenschaften mit einem Ordnungssystem für Materialen (Metall, Aluminium, Mineralien, Holz, \...) hinzu

### Mechanisch

  property name                         Description                                                                                                                                                                                                                                                                                                                            Unit/Data-Type
  ------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------
  Young\'s Modulus                      Young\'s modulus, also known as the tensile modulus or elastic modulus, is a measure of the stiffness of an elastic material and is a quantity used to characterize materials. See: [Young\'s modulus](http://en.wikipedia.org/wiki/Young%27s_modulus)                                                                                 kg\*mm\^-1\*s\^-2 (kPa)
  Poisson\'s Ratio                      The lateral contraction of materials under tension as a fraction of their elongation. See: [Poisson\'s Ratio](https://en.wikipedia.org/wiki/Poisson%27s_ratio)                                                                                                                                                                         Dimensionless (-)
  Yield Strength                        The stress at which a ductile material (like steel) starts to develop plastic (irreversible) deformation. See: [Yield Strength](https://en.wikipedia.org/wiki/Yield_(engineering))                                                                                                                                                     N\'\*mm\^-2 (MPa)
  Ultimate Tensile Strength (UTS)       The stress at which the material ruptures. For ductile materials this may be after experiencing significant plastic deformation (see Yield Strength). For brittle material Yield strength and Ultimate Tensile Strength coincide. See: [UTS](https://en.wikipedia.org/wiki/Ultimate_tensile_strength)                                  N\'\*mm\^-2 (MPa)
  Yield Points                          Used in a FEM non-linear material object to describe a ductile uni-axial stress-strain curve of a material. The values are entered as (yield stress, plastic strain) tuples, where the first combination is (Yield Strength, 0) and the last (UTS, Fracture Strain) See: [YieldPoints](https://en.wikipedia.org/wiki/Work_hardening)   (N\'\*mm\^-2 (MPa), dimensionless (-)
  Uniaxial Compressive Strength (FCK)   The compressive strength of concrete, defined as the strength of a 150 mm size cube tested at 28 days. See [FCK](http://eurocodes.jrc.ec.europa.eu/doc/WS2008/EN1992_1_Walraven.pdf)                                                                                                                                                   N\'\*mm\^-2 (MPa)
  Friction Angle (PHI)                  The angle of internal friction of a granular material like sand or concrete, as used in the Mohr-Coulomb yield criterion. See [PHI](https://en.wikipedia.org/wiki/Mohr%E2%80%93Coulomb_theory)                                                                                                                                         degrees (-)
  Hardness                              Des\...                                                                                                                                                                                                                                                                                                                                
  EN-10027-1                            In case of steel material the [Steel grade](http://en.wikipedia.org/wiki/Steel_grades) as defined in the [European standard](http://en.wikipedia.org/wiki/European_Committee_for_Standardization) No. 10027-1.                                                                                                                         string ASCII 7-bit

  : Material properties used in mechanical or structural engineering

**ToDos:** weitere Eigenschaften für mechanisches Design hinzufügen.

### Grafisch

Dieser Abschnitt definiert Materialeigenschaften, die die visuelle Erscheinung des Materials betreffen. Die

  Eigenschaftenname            Beschreibung                                                                                         Einheit/Datentyp
  ---------------------------- ---------------------------------------------------------------------------------------------------- ----------------------------------
  AmbientColor                 Umgebungsfarbe im Coin3D Farbmodell                                                                  float,float,float range: 0.0-1.0
  DiffuseColor                 Diffuse Farbe im Coin3D Farbmodell                                                                   float,float,float range: 0.0-1.0
  SpecularColor                Spiegelfarbe im Coin3D Farbmodell                                                                    float,float,float range: 0.0-1.0
  EmissiveColor                Emittierende Farbe im Coin3D Farbmodell                                                              float,float,float range: 0.0-1.0
  SectionColor                 Farbe, die angezeigt wird, wenn das Material im Coin3D-Farbmodell geschnitten wird                   float,float,float range: 0.0-1.0
  Shininess (Glanz)            Umgebungs?farbe im Coin3D Farbmodell                                                                 float range: 0.0-1.0
  Transparency (Transparenz)   Umgebungs?farbe im Coin3D Farbmodell                                                                 float range: 0.0-1.0
  VertxShader                  Vertex shader program as defined in [GlSl](http://de.wikipedia.org/wiki/OpenGL_Shading_Language)     Multi line string ASCII 7-bit
  FragmentShader               Fragment shader program as defined in [GlSl](http://de.wikipedia.org/wiki/OpenGL_Shading_Language)   Multi line string ASCII 7-bit

  : visuelle Erscheinung

### Thermisch

  Eigenschaftsname              Beschreibung                                                                                                                       Einheit/Datentyp
  ----------------------------- ---------------------------------------------------------------------------------------------------------------------------------- ------------------
  ThermalConductivity           Die [Wärmeleitfähigkeit (R oder Lambda-Koeffizient)](https://de.wikipedia.org/wiki/W%C3%A4rmeleitf%C3%A4higkeit) eines Materials   W/m²K
  ThermalExpansionCoefficient                                                                                                                                      
  SpecificHeat                                                                                                                                                     

  : Thermische Eigenschaften

### Architektur und Gebäudedatenmodellierung 


<div class="mw-translate-fuzzy">

  Eigenschaftsname    Beschreibung                                                                                                   Einheit/Datentyp
  ------------------- -------------------------------------------------------------------------------------------------------------- --------------------
  StandardFormat      Das für dieses Material benutzte Standard-Spezifikationssystem (ASTM, MasterFormat, CSI, OmniClass, etc\...)   String ASCII 7-bit
  StandardCode        Der spezifische Code dieses Materials im o.g. Standardformat                                                   String ASCII 7-bit
  FireStandard        Die Feuerwiderstandsklasse für dieses Material                                                                 String ASCII 7-bit
  FireClass           Die [Feuerschutzklasse](https://de.wikipedia.org/wiki/Feuerwiderstand) des Materials nach o.g. Standard        String ASCII 7-bit
  SoundTransmission   Der Schallübertragungskoeffizient dieses Materials                                                             W/m²K
  Finish              Die Art des Oberflächenzustands/Überzugs des Materials                                                         String ASCII 7-bit
  Color               Die Farbe des Materials                                                                                        String ASCII 7-bit
  UnitsArea           Die benötige Anzahl von Einheiten dieses Materials, um eine bestimmte Fläche zu füllen                         String ASCII 7-bit

  : Im Architekturdesign verwendete Materialeigenschaften

**ToDos:** Nachhaltigkeit und [LEED](https://de.wikipedia.org/wiki/Leadership_in_Energy_and_Environmental_Design)-Eigenschaften


</div>

## TODO

-   add sustainability & LEED properties

 {{FEM Tools navi}} 

[Category:Developer](Category:Developer.md) [Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Roadmap](Category:Roadmap.md) [Category:BIM](Category:BIM.md) [Category:File\_Formats](Category:File_Formats.md)

---
[documentation index](../README.md) > [Developer](Category:Developer.md) > Material/de
