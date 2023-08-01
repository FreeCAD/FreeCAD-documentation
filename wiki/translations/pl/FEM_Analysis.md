---
- GuiCommand:/pl
   Name:FEM Analysis
   Name/pl:MES Analiza
   MenuLocation:Model → Analiza MES
   Workbenches:[MES](FEM_Workbench/pl.md)
   Shortcut:**S** **A**
   SeeAlso:[Poradnik MES](FEM_tutorial/pl.md)
---

# FEM Analysis/pl

## Opis

Analiza MES może być postrzegana jako kontener, który przechowuje wszystkie obiekty analizy elementów skończonych. Konieczne jest posiadanie kontenera analizy, który przechowuje wszystkie potrzebne obiekty. Przynajmniej jeden z poniższych obiektów jest potrzebny do analizy mechanicznej:

-   [materiał](FEM_MaterialSolid/pl.md).
-   [zdefiniowane ograniczenie](FEM_ConstraintFixed/pl.md).
-   [ograniczenie siły](FEM_ConstraintForce/pl.md) lub [ograniczenie ciśnienia](FEM_ConstraintPressure/pl.md).

## Użycie

1.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/FEM_Analysis.svg" width=16px> [Analiza MES](FEM_Analysis/pl.md)**.
    -   Wybierz z menu **Model → <img src="images/FEM_Analysis.svg" width=16px> Analiza MES**.
    -   Użyj skrótu klawiaturowego: **S** następnie **A**.
2.  Zostanie utworzona nowa Analiza i ustawiona jako aktywna.
3.  Inne obiekty mogą być dodawane lub usuwane do kontenera analizy metodą \"przeciągnij i upuść\".
4.  Aby dodać nowe obiekty MES do dokumentu, analiza musi być aktywna. Podwójne kliknięcie na analizie powoduje jej aktywację.

## Opcje

-   Do chwili obecnej nie ma możliwości wyboru.

## Właściwości

-    **OutpuDir**: Określa katalog roboczy dla analizy.

## Tworzenie skryptów 

większość kodu tutaj jest przestarzała w wersji 0.17.

-   Utworzenie nowej analizy:


```python
MechanicalAnalysis.makeMechanicalAnalysis( name )
```

-   Dodanie obiektu do analizy:


```python
App.ActiveDocument.MechanicalAnalysis.Member = App.ActiveDocument.MechanicalAnalysis.Member + [ (object) ]
```

-   Usunięcie obiektu z analizy:


```python
member = App.ActiveDocument.MechanicalAnalysis.Member
member.remove( documentobject )
 App.ActiveDocument.MechanicalAnalysis.Member = member
```

Przykład: 
```python
import MechanicalAnalysis
analysis = MechanicalAnalysis.makeMechanicalAnalysis("MechanicalAnalysis")
FemGui.setActiveAnalysis(analysis)

addobj = App.ActiveDocument.getObject("MechanicalMaterial")
App.ActiveDocument.MechanicalAnalysis.Member = App.ActiveDocument.MechanicalAnalysis.Member + [addobj]

removeobj = App.ActiveDocument.getObject("MechanicalMaterial")
member = App.ActiveDocument.MechanicalAnalysis.Member
member.remove(removeobj)
App.ActiveDocument.MechanicalAnalysis.Member = member
```





{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM Analysis/pl
