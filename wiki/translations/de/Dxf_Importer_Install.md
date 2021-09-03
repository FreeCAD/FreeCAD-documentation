


{{TutorialInfo/de
|Topic=Musterklasse
|Level=Durchschnittlicher Anwender
|Time=15 Minuten
|Author=[Mario52](User:Mario52.md)
|FCVersion=Alle
}}

### Beschreibung

Diese Seite erklärt Dir Schritt für Schritt dem Rand für die Installation des Pakets Draft-dxf-import yorikvanhavre zu folgen, um Dateien im DXF Format in FreeCAD hochzuladen und DWG Dateien unter Verwendung des teighafileconverter Hilfsprogramms zu importieren. Diese Installation wurde in der Windows Vista Umgebung durchgeführt, aber das Prinzip des Systems ist für Linux das gleiche.

#### Erster Schritt: {#erster_schritt}

den Makro Ordner in FreeCAD ermitteln

**1 :** FreeCAD öffnen


<div class="mw-collapsible mw-collapsed toccolours">

Wenn Du eine Version ab 0.15 hast, kannst Du das automatische Aktualisierungspaket für DXF verwenden (erweitern, um mehr zu sehen)


<div class="mw-collapsible-content">

<img alt="Automatic DXF install" src=images/Dxf_Importer_Install_01b.png  style="width:640px;"> 


</div>


</div>

**2 :** klicke **Menü \> Makro \> Makros** oder klicke auf den unteren Teil <img alt="" src=images/Std_DlgMacroExecuteDirect.svg  style="width:18px;"> \"Öffne einen Dialog, damit Du ein aufgezeichnetes Makro ausführen kannst\"

![open FreeCAD](images/Dxf_Importer_Install_01.png ) 

**3 :** ein Dialogfeld geöffnet

**4 :** kopiere die Adresse des \"Makro-Zielortes\" (hier **C:\\Benutzer\\d\\AppData\\Roaming\\FreeCAD\\**) In Ubuntu ist dies normalerweise **/home/Dein\_Benutzername /.FreeCAD**

![Open a dialog to let you execute a macro Recorded](images/Dxf_Importer_Install_02.png ) 

**5 :** füge die Adresse in Deinen Browser ein und bestätige

![paste the address into your browser](images/Dxf_Importer_Install_03.png ) 

**6 :** lasse den Explorer geöffnet

![](images/Dxf_Importer_Install_04.png ) 

**7 :** Schließe FreeCAD

#### Zweiter Schritt: {#zweiter_schritt}

Herunterladen der Dateien

**8 :** Dateien auf der Seite <https://github.com/yorikvanhavre/Draft-dxf-importer> herunterladen

**9 :** und klicke auf die Symbolschaltfläche **Download ZIP** für die Standardversion.


<div class="mw-collapsible mw-collapsed toccolours">

(oder Auswahl für deine Entwicklungsversion siehe unten) (erweitern, um mehr zu sehen)


<div class="mw-collapsible-content">

<img alt="Automatische DXF Installation" src=images/Dxf_Importer_Install_05b.png  style="width:640px;"> 


</div>


</div>

![download files](images/Dxf_Importer_Install_05.png ) 

**10 :** Du musst die Datei in ein temporäres Verzeichnis entpacken (hier **c:\\tmp**)

![extract the file](images/Dxf_Importer_Install_06.png ) 

**11 :** der Dekomprimierer erstellt einen neuen Ordner namens \"**Draft-dxf-import-master**\"

![Dekomprimierer legt einen neuen Ordner an](images/Dxf_Importer_Install_07.png ) 

**12 :** die Dateien befinden sich in diesem Ordner wählealle Dateien aus und \"Ausschneiden\".

![select all the files and Cut](images/Dxf_Importer_Install_08.png ) 

**13 :** füge die Dateien im Ordner FreeCAD Makros im geöffneten Explorer (Schritt 6) ein (**C:\\Benutzer\\d\\AppData\\Roaming\\FreeCAD\\**)

In Ubuntu ist dies normalerweise **/home/Dein\_Benutzername /.FreeCAD**

![paste the files in the folder](images/Dxf_Importer_Install_09.png ) 

**14 :** Öffne FreeCAD mit der Schaltfläche <img alt="" src=images/Std_DlgMacroExecuteDirect.svg  style="width:18px;"> die notwendigen Dateien im DXF Format sind vorhanden, schließe das Fenster \"Makro ausführen\".

![open FreeCAD](images/Dxf_Importer_Install_15.png ) 

**15 :** lade Deine DXF Datei

![load your DXF file](images/Dxf_Importer_Install_10.png ) 

**16 :** DXF Datei kann verwendet werden

![DXF file can be used](images/Dxf_Importer_Install_11.png ) 

**VERSIONEN**

Dieses Repositorium enthält mehrere Versionen des DXF Importeurs. Die Standardversion, die Du herunterlädst, wenn Du oben auf den \"download ZIP\" Knopf drückst, ist immer die Version, die von der aktuellen stabilen Version von FreeCAD benötigt wird.

Wenn du eine andere Version von FreeCAD verwendest, z.B. eine Entwicklungsversion oder eine ältere Version, brauchst du vielleicht auch eine andere Version dieser DXF Bibliothek. Du kannst herausfinden, welche Version der DXF Bibliothek von Deiner Version von FreeCAD benötigt wird, indem Du den folgenden Code in die FreeCAD Python Konsole eingibst: 
```python
import importDXF
print importDXF.CURRENTDXFLIB
```

#### Dritter Schritt: {#dritter_schritt}

Herunterladen des Teigha Konverters zur Verwendung von DWG Dateien

**17 :** teighafileconverter herunterladen auf [teighafileconverter page](http://www.opendesign.com/guestfiles/teighafileconverter)

![download Teigha](images/Dxf_Importer_Install_12.png ) 

**18 :** wähle die Version, die zu Deinem Qt und OS passt

![choose the version](images/Dxf_Importer_Install_13.png ) 

**19 :** und installiere es auf deinem System ![installiere es auf deinem System](images/Dxf_Importer_Install_14.png ) 

**20 :** öffne FreeCAD und klicke auf die Schaltfläche <img alt="" src=images/Std_DlgMacroExecuteDirect.svg  style="width:18px;"> \"Öffneeinen Dialog, damit Du ein aufgezeichnetes Makro ausführen kannst\"

**21 :** Schließe das Makrofenster

**22 :** und aktiviere den Arbeitsbereich Entwurf

![activate the Draft workbebch](images/Dxf_Importer_Install_16.png ) 

**23 :** jetzt gehen wir auf die Optionsseite DXF / DWG und klicken \"Menü \> Bearbeiten \> Einstellungen\"

![Menu \> Preferences](images/Dxf_Importer_Install_17.png ) 

**24 :** wähle die Registerkarte \"Entwurf \> DXF / DWG Optionen\".

**25 :** Klicke im Abschnitt mit den DWG Format Optionen auf die 3 Punkte *\'\...* ![Entwurf \> DXF / DWG Optionen](images/Dxf_Importer_Install_18.png ) 

**26 :**, um den Weg für den Teigha Konverter frei zu machen, das FreeCAD für die Konvertierung von DWG nach DXF ihn verwendet.

**27 :** im Verzeichnis hier im Fenster \"**C:/Programme/ODA/Teigha File Converter 4.00.1/**\" eingeben und TeighaFileConverter.exe auswählen und bestätigen

![DWG format option](images/Dxf_Importer_Install_19.png ) 

**28 :** der Vorgang ist abgeschlossen, klicke auf die **OK** Du kannst eine DWG Datei testen

![directory Teigha File Converter 4.00.1](images/Dxf_Importer_Install_20.png ) 

### Vierter Schritt: {#vierter_schritt}

Teigha verwenden. Teigha ist ein vollwertiges Programm und Du kannst es auch ohne FreeCAD verwenden

![directory Teigha File Converter 4.00.1](images/Dxf_Importer_Install_21.png ) 

**1 :** Eingabe Ordner: Ordnerpfad oder die zu konvertierenden DXF- oder DWG Dateien

**2 :** Ausgabeordner: Pfad zum Zielordner für die konvertierten Dateien

**3 :** Ordner zurückholen:

**4 :** Audit:

**5 :** Eingangsdateifilter: Filter nur für DXF, DWG oder DXF und DWG

**6 :** Ausgabe Freigabe: die Datei wird in das Format und die ausgewählte Version konvertiert

**7 :** Start: startet den Prozess

### Verweise

Video Anleitung [FreeCAD Tutorial 24 - DXF/DWG Import](https://www.youtube.com/watch?v=wHxTWuDhc3M)
