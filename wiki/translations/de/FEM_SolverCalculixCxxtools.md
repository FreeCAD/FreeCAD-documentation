---
 GuiCommand:
   Name: FEM SolverCalculixCxxtools
   Name/de: FEM LöserCalculixCxxtools
   MenuLocation: Lösen , Solver CalculiX Standard
   Workbenches: FEM_Workbench/de
   Shortcut: **S** **X**
   SeeAlso: FEM_tutorial/de
---

# FEM SolverCalculixCxxtools/de



## Beschreibung

[CalculiXccxTools](FEM_SolverCalculixCxxtools/de.md) ermöglicht die Verwendung des [CalculiX](https://en.wikipedia.org/wiki/Calculix) Solvers. Es kann verwendet werden für:

1.  Einstellung der Analyseparameter
2.  Auswahl des Arbeitsverzeichnisses
3.  Ausführen des CalculiX-Solvers



## Anwendung

1.  Ein <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:16px;"> CalculiXcxxTools Solver-Objekt wird automatisch bei der Erstellung eines <img alt="" src=images/FEM_Analysis.svg  style="width:16px;"> [Analysis-Container](FEM_Analysis/de.md) erstellt.
    Um es manuell zu erstellen, verwenden Sie eine der folgenden Alternativen:
    -   Drücken Sie den **<img src="images/FEM_SolverCalculixCxxtools.svg" width=16px> [Löser CalculiX Standard](FEM_SolverCalculixCxxtools/de.md)** Schaltfläche.
    -   Wählen Sie **Löser → <img src="images/FEM_SolverCalculixCxxtools.svg" width=16px> Löser CalculiX Standard** aus dem Menü.

-   Drücken Sie die Tastenkombinationen **S** und dann **X**.

1.  Ändern Sie optional die Eigenschaften der <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:16px;"> CalculiXcxxTools-Löser-Objekts im [Eigenschaftseditor](Property_editor/de.md).
2.  Doppelklicken Sie auf das <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:16px;"> CalculiXcxxTools-Löser-Objekt.
3.  Wählen Sie den **Analysetyp**.
4.  Klicken Sie auf die Schaltfläche **Write .inp file**.
5.  Klicken Sie auf die Schaltfläche **Run CalculiX**.



## Optionen

Klicken Sie auf die Schaltfläche **Edit .inp file**, um die CalculiX-Eingabedatei anzuzeigen und manuell zu bearbeiten, bevor Sie die Analyse ausführen. In diesem Fall kann es nützlich sein, die Eigenschaft **Split Input Writer** auf {{True}} zu setzen.



## Eigenschaften

Standardwerte können im Menü **Bearbeiten → Einstellungen → FEM → CalculiX** eingestellt werden.

-    **Analysis Type**:

    -   static - statische Spannungsanalyse
    -   frequency - Modalanalyse (Eigenfrequenz)
    -   thermomech - thermo-mechanische Analyse
    -   check - keine Berechnung, führt Eingangsdeckprüfungen durch
    -   buckling - lineare Knickanalyse <small>(v0.20)</small> 

-    **Beam Reduced Integration**\- <small>(v1.0)</small> :

    -   true - verwendet Balkenelemente mit reduzierter Integration (B31R oder B32R), erforderlich bei Verwendung von Rohrträgerprofilen, kann auch [genaue Ergebnisse mit Plastizität](https://forum.freecad.org/viewtopic.php?t=61233) ermöglichen
    -   false - verwendet reguläre (vollintegrierte) Balkenelemente

-    **Beam Shell Result Output 3D**: beachten Sie, dass CalculiX intern 1D- und 2D-Elemente in 3D-Elemente erweitert, um eine Finite-Elemente-Analyse durchzuführen

    -   true - das resultierende Netz enthält 1D- und 2D-Elemente, die zu 3D-Elementen erweitert werden
    -   false - Ergebnisse von 1D- und 2D-Elementen werden auf die Knoten des ursprünglichen 1D- oder 2D-Netzes gemittelt (d.h. ein rein gekrümmter Balken wird aufgrund der Mittelung 0 Knotenspannungen aufweisen)

-    **Buckling Accuracy**\- <small>(v1.1)</small> : defines the accuracy of buckling eigenvalue evaluation. In most cases it can be left with the default value (0.01) but sometimes it might be necessary to lower it (e.g. to 0.0001) to capture the first eigenvalue.

-    **Eigenmode High Limit**: Eigenwerte oberhalb dieser Grenze werden nicht berechnet; **Hinweis**: wenn die Eigenwerte des Modells oberhalb der oberen Grenze liegen, wird CalculiX ohne Ausgabe beendet

-    **Eigenmode Low Limit**: Eigenwerte unterhalb dieser Grenze werden nicht berechnet

-    **Eigenmodes Count**: Anzahl der niedrigsten zu berechnenden Eigenmoden

-    **Geometric Nonlinearity**:

    -   linear - es wird eine lineare Analyse durchgeführt, wenn das Modell kein nichtlineares Material enthält
    -   nichtlinear - es wird eine nichtlineare Analyse durchgeführt

-    **Iterations Control parameter Cutb**: definiert die zweite Zeile der [CalculiX\' advanced iteration parameters](http://www.dhondt.de/ccx_2.17.pdf#subsection.8.24). Wird verwendet, wenn **Iterations Control Parameter Time Use** auf *true* gesetzt ist.

-    **Iterations Control Parameter Iter**: definiert die erste Zeile der [CalculiX\' advanced iteration parameters](http://www.dhondt.de/ccx_2.17.pdf#subsection.8.24). Wird verwendet, wenn **Iterations Control Parameter Time Use** auf *true* gesetzt ist.

-    **Iterations Control Parameter Time Use**-   true - aktiviert den **Iterations Control Parameter Cutb** und den **Iterations Control Parameter Iter**
    -   falsch

-    **Iterations Maximum**: maximale Anzahl von Inkrementen, nach denen der Auftrag angehalten wird.

-    **Iterations User Defined Incrementations**:

    -   true - automatische Inkrementierungssteuerung wird durch den Parameter DIRECT ausgeschaltet
    -   false - Inkrementierungssteuerung erfolgt automatisch

-    **terations User Defined Time Step Length**:

    -   true - aktiviert die Parameter **Time End** und **Time Initial Step**
    -   falsch

-    **Material Nonlinearity**:

    -   linear - nur lineare Materialeigenschaften werden in die Analyse einbezogen
    -   nichtlinear - es werden nichtlineare Materialeigenschaften aus **<img src="images/FEM_MaterialMechanicalNonlinear.svg" width=24px> verwendet [Nichtlineares mechanisches Material](FEM_MaterialMechanicalNonlinear/de.md)** Objekt

-    **Matrix Solver Type**: Typ des Solvers zur Lösung von Gleichungssystemen in der Finite-Elemente-Analyse. Er kann die Berechnungsgeschwindigkeit und den Speicherbedarf erheblich beeinflussen. Die Eignung hängt von Ihrem Finite-Elemente-Modell und der verfügbaren Hardware ab

    -   Standard - wählt automatisch den Matrix-Solver aus, abhängig von den verfügbaren Solvern (typischerweise ist es Spooles)

    -   
        {{Version/de|1.0}}
        
        : pastix - einer der schnellsten Solver (zusammen mit Pardiso), verfügbar (und Standard) in offiziellen Builds seit ccx 2.18, kann dennoch gelegentlich Probleme verursachen

    -   
        {{Version/de|1.0}}
        
        : pardiso - einer der schnellsten Solver (zusammen mit PaStiX), aber nicht quelloffen, erfordert ein anderes Build von CalculiX (ccx_dynamic) und zusätzliche Bibliotheken, die nicht mit FreeCAD geliefert werden, zuverlässiger als PaStiX

    -   spooles - direkter Solver mit der Unterstützung mehrerer CPUs. Die Anzahl der CPUs muss in den [FEM Einstellungen](FEM_Preferences/de#CalculiX.md) unter *Solver-Standardwerte → Anzahl der zu verwendenden CPUs* eingestellt werden.

    -   iterativescaling - iterativer Solver mit dem geringsten Speicherbedarf, geeignet, wenn das Modell überwiegend 3D-Elemente enthält

    -   iterativecholesky - iterativer Löser mit Vorkonditionierung und geringem Speicherbedarf, geeignet, wenn das Modell überwiegend 3D-Elemente enthält

-    **Model Space**\- <small>(v1.0)</small> : schaltet zwischen 3D- und 2D-Analysen um, letztere erfordern eine Oberflächengeometrie in der XY-Ebene (im achsensymmetrischen Fall rechts von der Y-Achse) mit [Dickendefinition](FEM_ElementGeometry2D/de.md) (Wert wird im achsensymmetrischen Fall ignoriert) und geeigneten Randbedingungen ([Verschiebungsrandbedingung](FEM_ConstraintDisplacement/de.md) mit Freiheitsgraden X und Y muss anstelle von [fixed boundary condition](FEM_ConstraintFixed/de.md) verwendet werden) sowie in der Ebene wirkende Lasten auf Kanten

    -   3D - dreidimensionale Volumen-/Schalen-/Stabelemente werden verwendet
    -   plane stress - 2D-Volumenelemente mit ebener Spannung werden verwendet
    -   plane strain - plane strain 2D-Volumenelemente werden verwendet
    -   Achsensymmetrisch - es werden achsensymmetrische 2D-Volumenelemente verwendet

-    **Output Frequency**\- <small>(v1.0)</small> : legt die Häufigkeit des Schreibens von Ergebnissen in Inkrementen fest (die Standardeinstellung 1 bedeutet, dass die Ergebnisse bei jedem Inkrement geschrieben werden, die Einstellung 2 würde die Ergebnisse alle 2 Inkremente speichern usw.), besonders nützlich für nichtlineare und instationäre Simulationen, hilft, das Durcheinander im Baum zu reduzieren, da derzeit ein Paar von Ergebnisobjekten (CCX_Results und Pipeline_CCX_Results) für jeden Ergebnisrahmen erstellt wird

-    **Split Input Writer**:

    -   false - die gesamte Eingabe in eine \*.inp Datei schreiben, die vom CalculiX Solver verwendet werden kann
    -   true - Solver-Eingaben in mehrere \*.inp-Dateien aufteilen, was die manuelle Bearbeitung verdeutlichen kann

-    **Thermo Mech Steady State**:

    -   true - thermomechanische Analyse im stationären Zustand
    -   false - instationäre thermo-mechanische Analyse

-    **Thermo Mech Type**\- <small>(v1.0)</small> :

    -   gekoppelt - gekoppelte thermo-mechanische Analyse
    -   ungekoppelt - ungekoppelte thermo-mechanische Analyse
    -   reine Wärmeübertragung - rein thermische Analyse (*\*WÄRMETRANSFER*)

-    **Time End**: Zeitspanne des Schritts, verwendet, wenn der Parameter **Iterations User Defined Incrementations** oder **Iterations User Defined Time Step Length** *true* ist

-    **Time Initial Step**: anfängliches Zeitinkrement des Schritts, wenn der Parameter **Iterations User Defined Incrementations** oder **Iterations User Defined Time Step Length** *true* ist

-    **Time Maximum Step**\- <small>(v1.0)</small> : maximales Zeitinkrement des Schrittes, wird verwendet, wenn der Parameter **Iterations User Defined Incrementations** oder **Iterations User Defined Time Step Length** *true* ist

-    **Time Minimum Step**\- <small>(v1.0)</small> : minimale Zeitschrittweite des Schritts, wird verwendet, wenn der Parameter **Iterations User Defined Incrementations** oder **Iterations User Defined Time Step Length** *true* ist

-    **Working Dir**: Pfad zum Arbeitsverzeichnis, das für CalculiX-Analysedateien verwendet werden soll.



## Limitierungen

Wenn Sie CalculiX ausführen, kann es sein, dass Sie den **Fehler 4294977295** erhalten. Dies bedeutet, dass Sie nicht genug RAM-Speicherplatz haben. Sie haben dann 2 Möglichkeiten:

1.  Reduzieren Sie die Anzahl der Netzknoten, vorzugsweise durch Weglassen von Geometrie, die für Ihre Analyse nicht unbedingt notwendig ist
2.  Kaufen Sie mehr RAM für Ihren PC



## Hinweise

Die Originaldokumentation von CalculiX finden Sie unter <http://dhondt.de/> im Abschnitt \"ccx\".



## Skripten





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM SolverCalculixCxxtools/de
