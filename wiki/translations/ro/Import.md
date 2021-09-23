# Import/Export IFC - compiling IfcOpenShell/ro
<div class="mw-translate-fuzzy">


{{TutorialInfo/ro
|Topic=Arch Workbench
|Level=Advanced
|Time=120 minutes
|Author=Pablo Gil
|FCVersion=
|Files=
}}


</div>

## Introducere

A fost o anchetă foarte dificilă până am obținut o copie de lucru a IfcOpenShell-python pe OSX / macOS pentru a importa / exporta fișierele IFC pe care le partajăm în acest tutorial cu speranța că ajută mai mulți oameni. Sistemul nostru de operare OSX 10.11.6, 64bits cu Python 2.7.11, ar putea funcționa pentru dvs. dacă aveți OSX, de asemenea, deoarece acestea sunt adesea 64bits dar pot diferi de a mea. Procedura ar putea fi foarte asemănătoare dacă rulați sub Linux sau Windows, dar probabil există unele diferențe.

## Requirements

-   [IfcOpenShell](IfcOpenShell.md)
-   FreeCAD v0.19 or higher


<div class="mw-translate-fuzzy">

## Pași de urmat 

1\. Descărcați sau clonați întregul proiect GitHub de la <https://github.com/IfcOpenShell/IfcOpenShell> (va conține întotdeauna cea mai nouă versiune)


</div>


<div class="mw-translate-fuzzy">

2\. De la un terminal mergeți în directorul **/ nix /** și lansați scriptul. În OSX este rulat cu: 
```python
./build-all.sh
``` Va dura între 30 și 120 de minute pentru a compila totul. IfcOpenShell nu este modul cel mai inteligent de compilare, dar acest script simplu va compila toate dependențele, versiunile Python și așa mai departe.


</div>


<div class="mw-translate-fuzzy">

3\. După ce termină (nu-mi amintesc acum, dar va fi tipărit ceva de genul \"Built IfcOpenShell \...\" și se va întoarce la promptul dvs.) veți avea un nou dosar **/IfcOpenShell/build/** plin de fișiere și foldere. From my personal experience, two weeks ago the nix \"build-all.sh\" script didn\'t finished successfully but after trying it yesterday with the newest updates it worked fine so I guess you might experience something similar in case the development goes further\... So now you have everything you need but you have to do some manual work in order to get it working: 4. Open FreeCAD and open the Python console and Report view. Then write into the Python console the following: 
```python
import sys
print sys.path
``` You will get a looong line with all the paths that FreeCAD reads. You may be able to install ifcopenshell in any of them but I suggest you to place it inside one where you find a **/site-packages/** after a **/Python/** or **/python-something/**. In my case it was */Library/Python/2.7/site-packages*. (you will find paths inside your app directory but I suggest you to not use them because then IfcOpenShell will only be available for this app)


</div>

4\. Open FreeCAD and open the [Python console](Python_console.md) and [Report view](Report_view.md). Then write into the Python console the following: 
```python
import sys
print sys.path
``` You will get a looooong line with all the paths that FreeCAD reads. You may be able to install IfcOpenShell in any of them but I suggest you to place it inside one where you find a {{FileName|/site-packages/}} after a {{FileName|/Python/}} or {{FileName|/python-something/}}. In my case it was {{FileName|/Library/Python/2.7/site-packages}}. (Note: you will find paths inside your app directory but I suggest you to not use them because then IfcOpenShell will only be available for this app)


<div class="mw-translate-fuzzy">

5\. Deci, odată localizat unde doriți / trebuie să-l instalați, mergeți acolo cu browser-ul de fișiere (Finder în OSX). That is, go inside **/site-packages/** folder


</div>

6\. Deschideți o nouă fereastră de browser de fișiere și navigați la proiectul GitHub descărcat: **/IfcOpenShell/src/ifcopenshell-python/** and copy the full **/ifcopenshell/** folder

7\. Lipiți-l (din copy/paste) în interior **/site-packages/** folder. Now you should have something like: 
```python
/site-packages/ifcopenshell/__init__.py
/site-packages/ifcopenshell/entity_instance.py
/site-packages/ifcopenshell/file.py
/site-packages/ifcopenshell/geom/app.py
/site-packages/ifcopenshell/geom/main.py
/site-packages/ifcopenshell/geom/occ_utils.py
/site-packages/ifcopenshell/geom/__init__.py
/site-packages/ifcopenshell/guid.py
```


<div class="mw-translate-fuzzy">

8\. Acum trebuie să alegem fișierele din directorul / build /, acestea sunt: 
```python
_ifcopenshell_wrapper.so
ifcopenshell_wrapper.py
``` but as we have compiled everything you will have to pick the one that matches with your FreeCAD Python version. Check it easily reading the first line inside your FreeCAD Python console view. In my case it was Python 2.7.11.


</div>

9\. Acum mergeți să copiați fișierele în interiorul locului care corespunde versiunii dumneavoastră Python. În cazul meu, a fost: 
```python
/IfcOpenShell/build/Darwin/x86_64/build/ifcopenshell/[b]python-2.7[/b].10/ifcwrap/
```


<div class="mw-translate-fuzzy">

10\. Lipiți-l în inside/site-packages/ifcopenshell/


</div>

11\. Verificați totul: 
```python
/site-packages/ifcopenshell/__init__.py                  (1)
/site-packages/ifcopenshell/entity_instance.py           (1)
/site-packages/ifcopenshell/_ifcopenshell_wrapper.so     (2)
/site-packages/ifcopenshell/file.py                      (1)
/site-packages/ifcopenshell/geom/__init__.py             (1)
/site-packages/ifcopenshell/geom/app.py                  (1)
/site-packages/ifcopenshell/geom/main.py                 (1)
/site-packages/ifcopenshell/geom/occ_utils.py            (1)
/site-packages/ifcopenshell/guid.py                      (1)
/site-packages/ifcopenshell/ifcopenshell_wrapper.py      (2)
```

\(1\) from GitHub project
(2) from /build/ folder

12\. Închideți și redeschideți FreeCAD

## Testarea

Acum, că este instalat, să verificăm dacă totul funcționează așa cum era de așteptat:

12.1 în consola Python console scriem: 
```python
import ifcopenshell
from ifcopenshell import geom
``` if it doesn\'t throw any error it means it may be correctly installed


<div class="mw-translate-fuzzy">

12.2 Mergeți la manualul FreeCAD a lui Yorik , navigați în partea de jos a paginii și descărcați următoarele fișiere pentru test: 
```python
house.FCStd
house.ifc
```


</div>


<div class="mw-translate-fuzzy">

12.3 Deschideți **house.FCStd**, selectați rădăcina \"Building\" obiect și exportați-l (menu File/export/) setting the File type to \"Industry Foundation Classes (\*.ifc)\". Press \"save\" and if it works and it doesn\'t throw an error in the Report view then it\'s working


</div>


<div class="mw-translate-fuzzy">

12.4 Testul final, importați **house.ifc** intr-un nou fișier astfel încât deschideți un nou fișier și importați acel fișier\... vă va lua ceva timp.


</div>

13\. Bucurați-vă de Atelierul Construcții/BIM cu FreeCAD!

## Gânduri de sfârșit 

În opinia mea FreeCAD în sine ar trebui să aibă versiuni precompilate ale IfcOpenShell incluse în distribuție, deoarece construirea de către dvs. este o durere totală și utilizatorul mediu nu o va face (ei nu știu cum să compileze, să gestioneze GitHub, etc), în fine, poate în viitor.

Sper că vă va ajuta.

Noroc!


<div class="mw-translate-fuzzy">

## Legături

Subiectul este pe Forum la [here](http://forum.freecadweb.org/viewtopic.php?f=23&t=17536)


</div>

-   Related forum thread [discussion](http://forum.freecadweb.org/viewtopic.php?f=23&t=17536)
-   [IfcOpenShell](IfcOpenShell.md)




[Category:BIM](Category:BIM.md) [Category:Arch](Category:Arch.md) [Category:3rd Party](Category:3rd_Party.md) [Category:File\_Formats](Category:File_Formats.md)

---
[documentation index](../README.md) > [BIM](Category:BIM.md) > Import/Export IFC - compiling IfcOpenShell/ro
