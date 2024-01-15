---
 GuiCommand:
   Name: TechDraw RadiusDimension
   Name/pl: Rysunek Techniczny: Wstaw wymiar promienia
   MenuLocation: Rysunek Techniczny , Wymiary , Wstaw wymiar promienia
   Workbenches: TechDraw_Workbench/pl
   SeeAlso: TechDraw_DiameterDimension/pl
---

# TechDraw RadiusDimension/pl



## Opis

Narzędzie **Wstaw wymiar promienia** dodaje wymiar promienia do widoku. Wymiar może być zastosowany do dowolnej krawędzi na rysunku, która jest okręgiem lub łukiem okręgu.

<img alt="" src=images/TechDraw_Dimension_Radius_example.png  style="width:130px;"> 
*Pomiar okręgu, wskazanie promienia*



## Użycie

Geometrię można wybrać w oknie [Widoku 3D](3D_view/pl.md) lub na rysunku. Niektóre łuki, które wydają się być koliste, są w rzeczywistości elipsami lub krzywymi złozonymi. W takich przypadkach nie można wprowadzić wymiaru promienia.

1.  Jeśli zaznaczyłeś geometrię w widoku 3D: dodaj właściwy widok Rysunku Technicznego do zaznaczenia, wybierając go w oknie [Widoku drzewa](Tree_view/pl.md).
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw_RadiusDimension.svg" width=16px> '''Wstaw wymiar promienia'''**.
    -   Wybierz opcję z menu **Rysunek Techniczny → Wymiary → <img src="images/TechDraw_RadiusDimension.svg" width=16px> Wstaw wymiar promienia**.
3.  Wymiar zostanie dodany do widoku.
4.  Wymiar można przeciągnąć do żądanej pozycji.
5.  W razie potrzeby dodaj tolerancje zgodnie z opisem na stronie [Wymiarowanie geometrii i tolerancja](TechDraw_Geometric_dimensioning_and_tolerancing/pl#Tolerancja.md).



### Wyświetlanie pomiarów 3D 

Zapoznaj się również z informacjami na stronie [Wstaw wymiar długości](TechDraw_LengthDimension/pl#Wyświetlanie_pomiarów_3D.md)



### Zmiana właściwości 

Aby zmienić właściwości obiektu wymiaru, kliknij dwukrotnie na niego w rysunku lub w [widoku drzewa](Tree_view/pl.md). Spowoduje to otwarcie okna [dialogowego wymiaru](TechDraw_LengthDimension/pl#Okno_dialogowe.md).



## Ograniczenia

Obiekty wymiarowe są podatne na \"[problem nazewnictwa topologicznego](Topological_naming_problem/pl.md)\". Zobacz stronę [Wstaw wymiar długości](TechDraw_LengthDimension/pl.md), aby uzyskać więcej informacji.



## Uwagi

Zapoznaj się również informacjami na stroni e[Wymiar długości](TechDraw_LengthDimension/pl#Uwagi.md).



## Właściwości

Zobacz stronę [Wymiar długości](TechDraw_LengthDimension/pl#W.C5.82a.C5.9Bciwo.C5.9Bci.md).



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Wstaw wymiar promienia** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
dim1 = FreeCAD.ActiveDocument.addObject("TechDraw::DrawViewDimension", "Dimension")
dim1.Type = "Radius"
dim1.References2D=[(view1, "Edge1")]
page.addView(dim1)
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw RadiusDimension/pl
