


{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

FreeCAD are capacitatea uimitoare de a fi importabil ca modul python în alte programe sau într-o consolă python autonomă, împreună cu toate modulele și componentele sale. Este posibil chiar să importați interfața grafică GUI-ul FreeCAD ca modul python - cu [some restrictions](Embedding_FreeCAD_#_Caveats.md), dar cu anumite restricții.


</div>


<div class="mw-translate-fuzzy">

### Utilizarea FreeCAD fără interfață grafică/GUI {#utilizarea_freecad_fără_interfață_graficăgui}


</div>


<div class="mw-translate-fuzzy">

O primă aplicație directă, ușoară și utilă pe care o puteți face este importul documentelor FreeCAD în programul dvs. În următorul exemplu, vom importa geometria pieselor unui document FreeCAD în [blender](http://www.blender.org). Iată scenariul complet. Sper că veți fi impresionat de simplitatea sa:


</div>


{{Code|lang=python|code=
<nowiki>
FREECADPATH = '/opt/FreeCAD/lib' # path to your FreeCAD.so or FreeCAD.dll file
import Blender, sys
sys.path.append(FREECADPATH)
 
def import_fcstd(filename):
   try:
       import FreeCAD
   except ValueError:
       Blender.Draw.PupMenu('Error%t|FreeCAD library not found. Please check the FREECADPATH variable in the import script is correct')
   else:
       scene = Blender.Scene.GetCurrent()
       import Part
       doc = FreeCAD.open(filename)
       objects = doc.Objects
       for ob in objects:
           if ob.Type[:4] == 'Part':
               shape = ob.Shape
               if shape.Faces:
                   mesh = Blender.Mesh.New()
                   rawdata = shape.tessellate(1)
                   for v in rawdata[0]:
                       mesh.verts.append((v.x,v.y,v.z))
                   for f in rawdata[1]:
                       mesh.faces.append.append(f)
                   scene.objects.new(mesh,ob.Name)
       Blender.Redraw()

def main():
   Blender.Window.FileSelector(import_fcstd, 'IMPORT FCSTD', 
                        Blender.sys.makename(ext='.fcstd'))    
 
# This lets you import the script without running it
if __name__=='__main__':
   main()
</nowiki>
}}


<div class="mw-translate-fuzzy">

Prima parte importantă este să vă asigurați că Python va găsi biblioteca noastră FreeCAD. Odată ce o găsește, toate modulele FreeCAD, cum ar fi Part, pe care o vom folosi, vor fi disponibile automat. Așa că luăm pur și simplu variabila sys.path, care este unde Python caută module și adăugăm calea FreCAD.Lib. Această modificare este doar temporară și se va pierde atunci când închidem interpretorul nostru python. Un alt mod ar putea fi să faceți o legătură cu biblioteca dvs. FreeCAD într-una din căile de căutare python. Am păstrat calea într-o constantă (FREECADPATH) astfel încât un alt utilizator al scriptului îi va fi mai ușor să configureze propriul sistem


</div>


{{Code|lang=python|code=
FREECADPATH = '/opt/FreeCAD/lib' # path to your FreeCAD.so or FreeCAD.dll file
import Blender, sys
sys.path.append(FREECADPATH)
}}


<div class="mw-translate-fuzzy">

Odată ce suntem siguri că biblioteca este încărcată (secvența try/except), acum putem lucra cu FreeCAD, la fel ca și cum am fi în interiorul interpretului Python al FreeCAD. Deschidem documentul FreeCAD care ne este transmis prin funcția principală main() și facem o listă a obiectelor sale. Apoi, pe măsură ce alegem doar să ne pese de geometria piesei, verificăm dacă proprietatea Type a fiecărui obiect conține \"Part\", apoi o mozaicăm (tessellation).


</div>


{{Code|lang=python|code=
       import Part
       doc = FreeCAD.open(filename)
       objects = doc.Objects
       for ob in objects:
           if ob.Type[:4] == 'Part':
}}

Mozaicarea (Tessellation) produce o listă de vârfuri(vertex) și o listă de fasțete definite de indici de vârfuri. Acest lucru este perfect, deoarece este exact același mod în care programul Blender definește ochiurile de plasă. Deci, sarcina noastră este ridicol de simplă, adăugăm ambele conținuturi ale listelor la vârfurile și fețetele unei rețele de tip Blender. Când totul este realizat, noi redesenăm ecranul și gata "c\'est fini" !


{{Code|lang=python|code=
           if ob.Type[:4] == 'Part':
               shape = ob.Shape
               if shape.Faces:
                   mesh = Blender.Mesh.New()
                   rawdata = shape.tessellate(1)
                   for v in rawdata[0]:
                       mesh.verts.append((v.x,v.y,v.z))
                   for f in rawdata[1]:
                       mesh.faces.append.append(f)
                   scene.objects.new(mesh,ob.Name)
       Blender.Redraw()
}}


<div class="mw-translate-fuzzy">

Bineînțeles, ați văzut că acest script este foarte simplu (de fapt am făcut unul mai avansat aici [here](http://yorik.orgfree.com/scripts/import_freecad.py)),ați putea dori să-l extindeți, de exemplu importarea obiectelor de tip plasă, sau importarea "Part Geometry" care nu are fațete sau importul altor formate de fișiere pe care FreeCAD le poate citi. De asemenea, ați putea dori să exportați forme geometrice într-un document FreeCAD, care se poate face în același mod. S-ar putea să doriți, de asemenea, să construiți un dialog, astfel încât utilizatorul să poată alege ce să importe, etc\.... Frumusețea tuturor acestor lucruri constă de fapt că l-ai lăsat pe FreeCAD să efectueze în totalitate, prezentându-și în același timp rezultatele în programul pe care l-ai ales .


</div>


**Note:**

checkout [Headless FreeCAD](Headless_FreeCAD.md) for running FreeCAD without the GUI.


<div class="mw-translate-fuzzy">

### Utilizarea FreeCAD cu interfață grafică(GUI) {#utilizarea_freecad_cu_interfață_graficăgui}


</div>

De la versiunea 4.2 cu Qt are capacitatea de a încorpora plugin-urile dependente de Qt-GUI în aplicații gazdă non-Qt și de a partaja bucla evenimentului gazdei.

Mai presus de toate, pentru FreeCAD, aceasta înseamnă că poate fi importat dintr-o altă aplicație cu interfața sa completă de utilizator (GUI) și în consecință aplicația gazdă controlează pe deplin FreeCAD.

Tot codul python pentru a obține aceasta are numai 2 linii


```python
import FreeCADGui 
FreeCADGui.showMainWindow()
```

Dacă aplicația se bazează pe Qt, atunci aceasta soluție ar trebui să funcționeze pe toate platformele suportate de către Qt . Cu toate acestea, gazda ar trebui să conecteze aceeași versiune QT ca și FreeCAD, deoarece altfel ați putea obține erori de execuție neașteptate.

Cu toate acestea, pentru aplicațiile non-Qt există câteva limitări pe care trebuie să le cunoașteți. Această soluție probabil nu funcționează împreună cu toate celelalte seturi de instrumente(toolkit). Pentru Windows funcționează atât timp cât aplicația gazdă este compatibilă și se bazează direct pe Win32 sau pe orice alt set de instrumente care utilizează intern API-ul Win32, cum ar fi wxWidgets, MFC sau WinForms. Pentru ca aceasta să funcționeze sub X11(Linux), aplicația gazdă trebuie să conecteze biblioteca \"glib\".

Notă, pentru orice aplicație consolă această soluție, această soluție, nu va funcționa deoarece nu este o funcționare în buclă de evenimente (event loop running) în acest sistem.


<div class="mw-translate-fuzzy">

### Avertismente


</div>

Deși este posibil să importați FreeCAD la un interpretor extern Python, acesta este un scenariu de utilizare obișnuit și necesită o atenție deosebită. În general, este mai bine să folosiți Python inclus în FreeCAD, via o linia de comandă sau ca pe un subproces. Vedeți [Start up and Configuration](Start_up_and_Configuration.md) pentru mai multe informații asupra ultimelor două opțiuni.

Deoarece modulul FreeCAD Python este compilat din C ++ (mai degrabă decât de a fi un modul Python pur), acesta poate fi importat numai de la un interpretorul Python compatibil. În general, acest lucru înseamnă că interpretorul Python trebuie să fie compilat cu același compilator C, cum a fost cel folosit pentru a construi FreeCAD. Informații despre compilatorul folosit pentru a construi un interpretor Python (inclusiv cel construit cu FreeCAD), pot fi găsite la: 
```python
>>> import sys
>>> sys.version
'2.7.13 (default, Dec 17 2016, 23:03:43) \n[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)]'
```

## Related

-   [Headless FreeCAD](Headless_FreeCAD.md)


{{Powerdocnavi

}} 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md)
