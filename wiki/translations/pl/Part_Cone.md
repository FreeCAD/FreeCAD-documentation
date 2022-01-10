---
- GuiCommand:/pl
   Name:Part Cone
   Name/pl:Część: Stożek
   MenuLocation:Część → Bryła pierwotna → Stożek
   Workbenches:[Część](Part_Workbench/pl.md)
   SeeAlso:[Bryły pierwotne](Part_CreatePrimitives/pl.md)
---

# Part Cone/pl

## Opis

Parametrycznie obcięty element pierwotny **Stożek** jest dostępny w Środowisku pracy Część, z paska narzędzi Część → Bryła pierwotna → Stożek.

<img alt="" src=images/Otherwisedefault270degree_Part_Cone.png  style="width:300px;"> 
*Poniższy obrazek przedstawia fragment stożka z parametrem '''Kąt''' ustawionym na wartość 270°, a pozostałe parametry pozostają ustawione na wartościach domyślnych*.

## Użycie

1.  Otwórz środowisko pracy **<img src="images/Workbench_Part.svg" width=16px> [Część](Part_Workbench/pl.md)**.
2.  Istnieją dwa sposoby na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Part_Cone.svg" width=16px> Utwórz stożek** na pasku narzędzi,
    -   Użyj pozycji menu głównego **Część → Bryła pierwotna → <img src="images/Part_Cone.svg" width=16px> Stożek**.

**Wynik:** Wartości domyślne tworzą ścięty stożek parametryczny, który jest umieszczony w punkcie odniesienia położenia *(punkt 0,0,0)* i dołączony do globalnej płaszczyzny xy. Jego wysokość wynosząca 10mm jest położona wzdłuż globalnej osi z. Dolny **Promień 1** wynosi 2mm, górny **Promień 2** wynosi 4mm.

Właściwości stożka mogą być później edytowane w [edytorze właściwości](Property_editor/pl.md) lub przez podwójne kliknięcie stożka w [widoku drzewa](Tree_view/pl.md).

## Właściwości

-    **Promień 1**: promień łuku lub okręgu określającego dolną ścianę.

-    **Promień 2**: promień łuku lub okręgu określającego górną ścianę.

-    **Wysokość**: wysokość stożka.

-    **Kąt**: liczba stopni dla długości łuku lub okręgu określającego górną i dolną powierzchnię ściętego stożka. Domyślna wartość 360° tworzy okrągłe powierzchnie, niższa wartość utworzy fragment stożka zdefiniowany przez górną i dolną powierzchnię. Każda z tych powierzchni ma krawędzie zdefiniowane przez łuk *(o długości w liczbie stopni)* i dwóch promieniach.

## Scripting

A Part Cone can be created using the following function:


```python
cone = FreeCAD.ActiveDocument.addObject("Part::Cone", "myCone")
```

-   Where {{Incode|"myCone"}} is the name for the object.
-   The function returns the newly created object.

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cone/pl
