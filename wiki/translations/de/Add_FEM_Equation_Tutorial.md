# Add FEM Equation Tutorial/de
{{TutorialInfo/de
|Topic=FEM Gleichung hinzufügen
|Level=Fortgeschritten
|Time=1 Tag
|Author=[JohnWang](User_JohnWang.md)
|FCVersion=0.19
}}

## Einführung

In diesem Tutorium werden wir die Fließgeschwindigkeit zu FreeCAD hinzufügen und die Unterstützung für den Elmer-Löser einführen. Bitte stelle sicher, dass du [Extend FEM Module](Extend_FEM_Module/de.md) gelesen und verstanden hast, bevor du dieses Tutorium liest.

Die Aufgabe kann in fünf Teile aufgeteilt werden.

-   **Neuer Gleichungstyp**. Dieser Schritt muss nur durchgeführt werden, wenn die Gleichung in FreeCAD bisher nicht existiert (im Gegensatz zu einer Gleichung, die bereits in FreeCAD existiert, aber vom Ziellöser nicht unterstützt wird).
-   **Neues Gleichungsobjekt**. Hinzufügen eines konkreten Dokumentobjekts, das die Elmer-spezifische Gleichung repräsentiert.
-   **Löserobjekt erweitern**. Dem Elmer-Löserobjekt Unterstützung für die neue Gleichung hinzufügen.
-   **Writer-Objekt erweitern**. Erweitern des Elmer-Analyseexports zur Unterstützung des neuen Gleichungstyps.
-   **GUI-Werkzeug zum Erstellen einer Gleichung**. Zugriff auf die neue Gleichungsfunktion über den GUI-Arbeitsbereich.

## Neuer Gleichungstyp 

In diesem Schritt werden wir die folgende Datei modifizieren:

-    {{FileName|src/Mod/Fem/femsolver/equationbase.py}}
    

Der Gleichungstyp wird von allen Gleichungsobjekten der verschiedenen Löser gemeinsam verwendet. Jeder Typ hat einen Zeichenfolgenspezifizierer (z.B. \"Heat\") und einen zugeordneten Befehl, der die Gleichung dem ausgewählten Gleichungslöser hinzufügt. Dies ermöglicht eine einfachere GUI, bei der wir nur eine Schaltfläche für die Wärmegleichung haben, die für alle unterstützten Löser verwendet wird.

Füge zuerst die neue Gleichung zum `equationbase.py`-Modul hinzu. Jede Gleichung erfordert zwei Klassen, ein Dokument-Proxy und ein Ansicht-Proxy. Diese zwei Klassen werden später als Basisklassen für die Elmer-spezifischen Gleichungsklassen benutzt. Kopiere sie einfach von einem existierenden Gleichungstyp und passe den Icon-Pfad in {{Incode|getIcon(self)}} des Ansicht-Proxy an.


```python
class FlowProxy(BaseProxy):
    pass

class FlowViewProxy(BaseViewProxy):
    def getIcon(self):
        return ":/icons/FEM_EquationFlow.svg"
```

## Neues Elmers Gleichungs Objekt 

In diesem Schritt werden wir das Dokumentobjekt implementieren. Wir müssen eine neue Datei {{Incode|flow.py}} hinzufügen unter:

-    {{FileName|src/Mod/Fem/femsolver/elmer/equations/flow.py}}
    

und die folgenden Dateien ändern:

-    {{FileName|src/Mod/Fem/ObjectsFem.py}}
    

-    {{FileName|src/Mod/Fem/CMakeLists.txt}}
    

Beginnen wir dem Hinzufügen der neuen Datei {{Incode|flow.py}}. Diese Datei kann aus einer bestehenden Gleichung kopiert werden.

### Schlüsselwörter

-   Falls die neue Gleichung nur Schlüsselworte für **lineare** Systeme unterstützt, kopiere das {{Incode|femsolver/elmer/equations/elasticity.py}}-Modul.
-   Falls die neue Gleichung Schlüsselworte für **lineare** und **nicht-lineare** Systeme unterstützt, kopiere das {{Incode|femsolver/elmer/equations/heat.py}}-Modul.

Die Strömungsgleichung ist eine potenziell nicht-lineare Gleichung. Das bedeutet, dass unsere Arbeit auf `heat.py` basieren wird.

### Dateien bearbeiten 

Nach dem Kopieren von `heat.py` nach `flow.py` passe letztere Datei an folgenden Stellen an:

-   das Namensargument der {{Incode|create}}-Modulfunktion,
-   die Basisklassen der {{Incode|Proxy}}-Klasse,
-   das {{Incode|Type}}-Attribut der {{Incode|Proxy}}-Klasse,
-   die `ViewProxy`-Klassen.


```python
def create(doc, name="'''Flow'''"):
    return femutils.createObject(
        doc, name, Proxy, ViewProxy)

class Proxy(nonlinear.Proxy, equationbase.'''Flow'''Proxy):

    Type = "Fem::EquationElmer'''Flow'''"

    def __init__(self, obj):
        super(Proxy, self).__init__(obj)
        obj.Priority = 10

class ViewProxy(nonlinear.ViewProxy, equationbase.'''Flow'''ViewProxy):
    pass
```

Dann musst du die über die `obj.addProperty(..)`-Funktion hinzugefügten Eigenschaften auf die von der Gleichung benötigten anpassen.

Zum Zeitpunkt des Schreibens dieses Tutoriums hat die Elmer-Strömungsgleichung keine besonderen Eigenschaften. Siehe Elmer-Elastizitätsgleichung für ein Beispiel mit Eigenschaften.

Schließlich muss man eine **makeEquationFlow**-Definition in {{Incode|src/Mod/Fem/ObjectsFem.py}} durch Duplizieren eines verfügbaren Eintrags registrieren.

FreeCAD benutzt **make** zur Erstellung des Programms. Deshalb müssen wir die neue Moduldatei ({{Incode|flow.py}}) in `src/Mod/Fem/CMakeLists.txt` registrieren, wie in [FEM Modul erweitern](https://www.freecadweb.org/wiki/Extend_FEM_Module) beschriebenen. Die passenden Listen lassen sich leicht finden, indem man nach vorhandenen Gleichungsmoduldateien von Elmer sucht.

## Löser Objekt erweitern 

In diesem Schritt werden wir die folgenden Dateien modifizieren:

-    {{FileName|src/Mod/Fem/femsolver/elmer/solver.py}}
    

Gerade jetzt haben wir FreeCAD darauf aufmerksam gemacht, dass es einen neuen Gleichungstyp gibt, und sogar einen Befehl hinzugefügt, der diese Gleichung dem ausgewählten Löserobjekt hinzufügt. Wir haben auch ein konkretes Gleichungsobjekt für Elmer implementiert. Was jetzt noch zu tun bleibt, ist die Verbindung zwischen Elmer und der Strömungsgleichung herzustellen. Dies muss direkt im Elmer-Lösungsobjekt erfolgen.

Registriere das Modul, in dem wir gerade unser neues Gleichungsobjekt ({{Incode|flow.py}}) implementiert haben, mit dem Gleichungsspezifizierer aus Schritt 1 (\"Flow\") in der {{Incode|_EQUATIONS}} Liste in {{Incode|elmer/solver.py}}.


```python
from .equations import electrostatic
+from .equations import flow

...

_EQUATIONS = {
    "Heat": heat,
    "Elasticity": elasticity,
+    "Flow": flow,
}
```

## Schreiber Objekt erweitern 

In diesem Schritt werden wir die folgende Datei modifizieren:

-    {{FileName|src/Mod/Fem/femsolver/elmer/writer.py}}
    

Diese Datei enthält die Klasse {{Incode|Writer}}, die die Analyse in das Elmer-SIF Format exportiert.

Für jede unterstützte Gleichung gibt es zwei Methoden für den Export der jeweiligen Gleichung. Kopiere einfach alle von einer bestehenden Gleichung und passe sie an deine Bedürfnisse an.

-    {{Incode|_getFlowSolver}}
    

-    {{Incode|_handleFlow}}
    

Du musst die `_handleFlow`-Methode in der `Writer`-Klasse registrieren:


```python
class Writer(object):
...
    def write(self):
...
        self._handleFlow()

...

```


{{Incode|_handleFlow}}

kann eine Reihe weiterer detaillierter Methoden kontrollieren. Unsere Fließ-Gleichung benutzt die folgenden detaillierten Methoden:

-    {{Incode|_handleFlowConstants}}
    

-    {{Incode|_handleFlowMaterial}}
    

-    {{Incode|_handleFlowInitialVelocity}}
    

-    {{Incode|_handleFlowBndConditions}}
    

-    {{Incode|_handleFlowEquation}}
    

Nun haben wir den Funktionsteil der neuen Gleichung beendet. Nun werden wir die neue Gleichung an die GUI anbinden.

## GUI Werkzeug zum Erstellen einer Gleichung 

Wir haben gerade eine neue Gleichungsklasse erstellt. Um sie über die FEM-GUI anzusprechen, müssen wir eine Schaltfläche erstellen und sie mit der neuen Gleichungsklasse verbinden. Hier ist ein Tutorium: [Tutorium Schaltfläche zur FEM Werkzeugleiste hinzufügen](Add_Button_to_FEM_Toolbar_Tutorial/de.md).

[<img src="images/Property.png" style="width:16px"> FEM](Category_FEM.md) [<img src="images/Property.png" style="width:16px"> Developer Documentation](Category_Developer_Documentation.md)

---
[documentation index](../README.md) > [FEM](Category_FEM.md) > Add FEM Equation Tutorial/de
