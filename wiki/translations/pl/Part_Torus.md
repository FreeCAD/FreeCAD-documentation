---
- GuiCommand:/pl
   Name:Part Torus
   Name/pl:Część: Torus
   MenuLocation:Część  → Bryła pierwotna → Torus
   Workbenches:[Część](Part_Workbench/pl.md)
   SeeAlso:[Bryły pierwotne](Part_Primitives/pl.md)
---

# Part Torus/pl

## Opis

Tworzy torus parametryczny, którego parametrami są: pozycja, kąt1, kąt2, kąt3, promień1 i promień2.

<img alt="" src=images/SimpleTorus.jpg  style="width:400px;">

## Użycie

1.  Otwórz środowisko pracy **<img src="images/Workbench_Part.svg" width=16px> [Część](Part_Workbench/pl.md)**.
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Part_Torus.svg" width=16px> Torus** na pasku narzędzi,
    -   Użyj pozycji menu głównego **Część → Bryła pierwotna → <img src="images/Part_Torus.svg" width=16px> Torus**.

**Wynik:** Torus przy tworzeniu zostanie umieszczony w punkcie początkowym *(punkt 0,0,0)*.
Parametry kątów *(kąt1, kąt2, kąt3)*, jak również parametry promienia *(promień1, promień2)* pozwalają sparametryzować bryłę, patrz następna sekcja.

## Opcje

![](images/TorusExampleOverviewParameters.jpg )

**Parametry**

Torus można przyrównać do małego dysku, który porusza się po orbicie kołowej wokół umownej osi. W ten sposób parametryczny torus jest zdefiniowany przez następujące wielkości:

-    {{Parameter|Promień1}}: Promień okręgu, wokół którego krąży dysk.

-    {{Parameter|Promień2}}Promień tarczy definiującej kształt torusa

-    {{Parameter|Kąt1}}Pierwszy kąt do przecięcia / zdefiniowania dysku torusa

-    {{Parameter|Kąt2}}Drugi kąt do przecięcia / zdefiniowania dysku torusa

-    {{Parameter|Kąt3}}Trzeci kąt do wyznaczenia obwodu torusa.

jak również standardowy zestaw parametrów rozmieszczania. Poniższe ilustracje przedstawiają wizualny przegląd parametrów, o których była mowa powyżej:

![](images/TorusExampleRadius1.jpg ) Parametr Promień1 ma wartość 20mm.

![](images/TorusExampleRadius2.jpg ) Parametr Promień2 ma wartość 2mm.

![](images/TorusExampleAngle1.jpg ) Parametr Kąt1 ma wartość -90°. Zauważ, że narzędzie \"Miara kąta\" nie może wyświetlić kąta ujemnego. Potraktuj wartość wyświetlaną na rysunku jako **-**90°.

![](images/TorusExampleAngle2.jpg ) Parametr Kąt2 ma wartość 90°.

![](images/TorusExampleAngle3.jpg ) Parametr Kąt3 ma wartość 90°. 

## Scripting

A Part Torus can be created using the following function:


```python
torus = FreeCAD.ActiveDocument.addObject("Part::Torus", "myTorus")
```

-   Where {{Incode|"myTorus"}} is the name for the object.
-   The function returns the newly created object.

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Torus/pl
