# WebTools Git/ro
---
- GuiCommand:   Name:Arch Git‏‎   Workbenches:[[Arch_Workbench/ro   Arch]]|MenuLocation:Arch → Utilities → Git   Shortcut:‏‎   SeeAlso:---


</div>


<div class="mw-translate-fuzzy">

**Notă:** Începând cu FreeCAD v0.17, acest instrument a fost eliminat din Arch Workbench și face parte acum din [WebTools Workbench](WebTools_Workbench.md) pe care îl puteți instala prin meniul Tools → Addons Manager.


</div>

## Descriere

Această comandă permite administrarea documentului curent cu [GIT](https://en.wikipedia.org/wiki/Git_%28software%29). GIT este un sistem puternic de control al versiunilor de fișiere, care poate gestiona diferite versiuni ale fișierelor și să țină evidența modificărilor..

Git este un instrument complex, înainte de a folosi acest instrument să ia în considerare învățarea elementelor de bază, pentru a evita operațiile greșite care pot cauza pierderea datelor. O literatură abundentă despre GIT este disponibilă și este ușor de găsit pe internet.


<div class="mw-translate-fuzzy">

**Notă:** Pentru a putea să utilizați această comandă pachetul [gitpython](https://github.com/gitpython-developers/GitPython) trebuie să fie instalat pe sistemul dvs. Pe majoritatea distribuțiilor linux, gitpython este disponibil din depozitele standard de software ca \'\' gitpython \'\' sau \'\' python-git \'\'.


</div>

## Cum se folosește 


<div class="mw-translate-fuzzy">

1.  Save the current active document
2.  Make sure the saved file is inside an existing git repository
3.  Select menu Arch -\> Utilities -\> **<img src="images/Arch_CommitGit.png" width=16px> [Git](Arch_Git.md)
**


</div>

## Opţiuni


<div class="mw-translate-fuzzy">

![](images/Arch_Git_panel.jpg )


</div>


<div class="mw-translate-fuzzy">

-   Asigurați-vă că **Report Window** este deschis deoarece mesajele Git vor fi tipărite acolo.
-   Instrumentul Git se va deschide numai dacă fișierul curent este salvat într-un depozit Git. Poate fi într-un subdirector.
-   Butonul \'\'\' Log \'\'\'va afișa un dialog care prezintă cele mai recente înregistrări din jurnal.
-   Butonul \'\'\' Refresh \'\'\' va re-scana depozitul pentru fișierele modificate.
-   Butonul \'\'\' Diff \'\'\' va afișa diferențele dintre versiunea curentă a unui fișier selectat și versiunea anterioară stocată în depozit.
-   Butonul **Select all** va selecta toate fișierele care urmează să fie angajate.
-   Butonul \'\'\' Commit \'\'\'va angaja fișierele selectate. Asigurați-vă că ați scris un mesaj de comitere care descrie schimbările pe care le comiteți.
-   Butonul *Pull*\' va **downloada** \'orice modificări noi în depozit de pe telecomanda selectată. Dacă fișierul deschis în prezent în FreeCAD este modificat printr-o tragere, un mesaj de avertizare vă va informa astfel încât să puteți salva din nou fișierul sau să îl salvați în altă parte.
-   Butonul \'\'\' Push **va** uploada \'\'\'cel mai recent comitet (e) pe telecomanda selectată.


</div>


<div class="mw-translate-fuzzy">

-   Instrumentul încă nu poate crea depozite noi. Trebuie să aveți deja un depozit local existent (FreeCAD va verifica dacă fișierul documentului curent se află în interiorul unui depozit Git)
-   Instrumentul nu poate schimba sau crea ramuri. Trebuie să faceți acest lucru manual cu instrumentele standard Git.


</div>


<div class="mw-translate-fuzzy">

## Abilitarea citirii umane a fișierelor diff for FCStd 


</div>


<div class="mw-translate-fuzzy">

FreeCAD [Fcstd format de fișier](Fcstd_format_de_fișier.md) este un format binar bazat pe zip, pentru care Git nu poate produce diferențe corecte. Aceasta înseamnă că nu puteți vedea ce s-a schimbat între o versiune și o altă versiune și că fiecare nouă versiune stocată în repozitoriul Git este o copie completă a fișierului.


</div>

Deși a doua problemă nu are în prezent o soluție, prima poate fi rezolvată cu un mic instrument disponibil din codul sursă FreeCAD, numit [fcinfo](https://github.com/FreeCAD/FreeCAD/blob/master/src/Tools/fcinfo). Poate fi spus lui Git să folosească utilitarul fcinfo pentru a tipări un raport prietenos cu oamenii despre un fișier FCStd și, atunci când este rugat să producă un diff între două fișiere FCStd, va produce o diferență între cele două rapoarte fcinfo. Rețineți că acesta este doar un feedback vizual, o copie completă a fișierului va fi în continuare stocată intern.

Examplu de diff produs cu fcinfo:


```python
diff --git a/testhouse.FcStd b/testhouse.FcStd
index 08077b6..985b1d8 100644
--- a/testhouse.FcStd
+++ b/testhouse.FcStd
@@ -1,26 +1,25 @@
-Document: /tmp/43un09_testhouse.FcStd (442K)
-   SHA1: 67c1985a45d93cba57d5bf44490897aba460100d
+Document: /tmp/zfXoDd_testhouse.FcStd (370K)
+   SHA1: db1cb5fca18af7bfdca849028f40550df4d845cb
    Comment : This is a test house to showcase FreeCAD's BIM worflow and IFC export capabilities
    Company : uncreated.net
    CreatedBy : Yorik van Havre
    CreationDate : Fri May  9 12:05:54 2014 
    FileVersion : 1
    Id : 
-   Label : testhouse
-   LastModifiedBy : Yorik van Havre
-   LastModifiedDate : 2016-06-28T17:05:57-03:00
+   Label : testhouse2
+   LastModifiedBy : Yorik van Havre
+   LastModifiedDate : Sat Sep 13 20:46:36 2014
+
    License : CC-BY 3.0
    LicenseURL : http://creativecommons.org/licenses/by/3.0/
-   ProgramVersion : 0.17R7800 (Git)
-   TipName : 
+   ProgramVersion : 0.15R3989 (Git)
    Uid : 67e62d8a-6674-4358-92fe-615443be887a
-   Objects: (231)
+   Objects: (221)
        Annotation : Drawing::FeatureViewAnnotation
        Annotation001 : Drawing::FeatureViewAnnotation
        Annotation002 : Drawing::FeatureViewAnnotation
        Annotation003 : Drawing::FeatureViewAnnotation
-       Annotation004 : Drawing::FeatureViewAnnotation
-       Annotation005 : Drawing::FeatureViewAnnotation
        Array : Part::FeaturePython (9K)
        Box : Part::Box (2K)
        Building : App::DocumentObjectGroupPython
@@ -110,7 +109,7 @@ Document: /tmp/43un09_testhouse.FcStd (442K)
        Floor : App::DocumentObjectGroupPython
        Floor001 : App::DocumentObjectGroupPython
        Floor002 : App::DocumentObjectGroupPython
-       Frame : Part::FeaturePython (89K)
```

Fiecare fișier FreeCAD conține un număr de control SHA1, care se va schimba de fiecare dată când fișierul este salvat, chiar dacă nu s-au schimbat conținutul său. În concluzie fcinfo va tipări întotdeauna ceva, indiferent de schimbarea conținutul său.

Pentru a permite utilizarea fcinfo (numai Linux și Mac - TODO: adăugați instrucțiuni Windows)


<div class="mw-translate-fuzzy">

1.  Salvați fișierul fcinfo undeva în sistem
2.  Faceți-l executabil
3.  Creați un fișier .gitattributes în depozitul dvs. Git
4.  Adăugați următoarea linie în ea:

* .FCStd diff = fcinfo


</div>

---
[documentation index](../README.md) > WebTools Git/ro
