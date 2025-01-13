---
 GuiCommand:
   Name: BIM Frame
   Name/pl: BIM: Rama
   MenuLocation: 3D / BIM , Rama
   Workbenches: BIM_Workbench/pl
   Shortcut: **F** **R**
   SeeAlso: 
---

# Arch Frame/pl



## Opis

Narzędzie **Rama** służy do tworzenia wszelkiego rodzaju obiektów ramowych na podstawie profilu i układu. Profil jest wyciągnięty wzdłuż krawędzi układu, który może być dowolnym obiektem 2D, takim jak [szkic](Sketcher_Workbench/pl.md) lub [rysunek roboczy](Draft_Workbench/pl.md). Jest to szczególnie przydatne do tworzenia balustrad lub ścian szkieletowych. Obiekty szkieletowe można następnie łatwo przekształcić w obiekty [ścian](Arch_Wall/pl.md) lub [konstrukcji](Arch_Structure/pl.md).

<img alt="" src=images/Arch_Frame_example.jpg  style="width:640px;"> 
*Obiekt Ramy utworzony z [szyku ortogonalnego](Draft_OrthoArray/pl.md) [linii](Draft_Line/pl.md), przy użyciu [okręgu](Draft_Circle/pl.md) jako profilu.*



## Użycie

1.  Utwórz obiekt układu i obiekt profilu, na przykład za pomocą środowiska [Rysunek Roboczy](Draft_Workbench/pl.md) lub [Szkicownik](Sketcher_Workbench/pl.md).
2.  Wybierz najpierw obiekt układu, a następnie, przy wciśniętym przycisku **Ctrl**, wybierz obiekt profilu.
3.  Naciśnij przycisk **<img src="images/Arch_Frame.svg" width=16px> '''Rama'''** lub naciśnij **F**, a następnie **R**.



## Opcje

-   Ramy dzielą wspólne właściwości i zachowania wszystkich [komponentów](Arch_Component/pl.md).
-   Obiekt ramy można umieścić w pewnej odległości od obiektu układu, ustawiając jego właściwość Odsunięcie.
-   Profil zostanie skopiowany u podstawy każdej krawędzi obiektu układu, a następnie wyciągnięty wzdłuż niej. Można kontrolować sposób umieszczenia profilu u podstawy każdej krawędzi za pomocą właściwości Wyrównanie i Obrót.



## Właściwości



### Dane


{{TitleProperty|Komponent}}

-    **Base|Link**: Układ, na którym oparta jest ta rama.

Informacje o innych właściwościach w tej grupie można znaleźć na stronie [Komponent](Arch_Component/pl#Właściwości.md).


{{TitleProperty|Rama}}

-    **Wyrównaj|Bool**: Określa, czy profil musi zostać obrócony, aby jego oś normalna była wyrównana z każdą krawędzią.

-    **Punkt bazowy|Integer**: Indeks bazujący na zerze, wskazujący punkt przecięcia ścieżki na profilu:

 ** {{Value|0}}: **Podstawa** **Umiejscowienia** profilu. Ten punkt jest również używany w przypadku nieprawidłowego indeksu.
 ** {{Value|1}}: Środek pierwszej krawędzi profilu.
 ** {{Value|2}}: Punkt końcowy pierwszej krawędzi profilu.
 ** {{Value|3}}: Środek drugiej krawędzi profilu.
 ** {{Value|4}}: Punkt końcowy drugiej krawędzi profilu.
 ** ...
 ** {{Value|n*2-1}}: Środek n-tej krawędzi profilu.
 ** {{Value|n*2}}: Punkt końcowy n-tej krawędzi profilu.

-    **Krawędzie|Enumeration**: Typ krawędzi do rozważenia. Opcje to:

 ** {{Value|Wszystkie krawędzie}}
 ** {{Value|Pionowe krawędzie}}
 ** {{Value|Poziome krawędzie}}
 ** {{Value|Dolne poziome krawędzie}}: Na podstawie globalnej współrzędnej Z środka masy krawędzi.
 ** {{Value|Górne poziome krawędzie}}: Jak wyżej.

-    **Scal|Bool**: Jeśli prawda, zachodzące na siebie bryły są scalane.

-    **Odsunięcie|VectorDistance**: Opcjonalna odległość między obiektem układu a obiektem ramy.

-    **Profil|Link**: Profil, na którym oparta jest ta rama.

-    **Umiejscowienie profilu|Placement**: Opcjonalne dodatkowe umiejscowienie do dodania do profilu przed jego wyciągnięciem. Używana jest tylko **Rotacja** **Umiejscowienia**. Ignorowane, jeśli **Wyrównaj** ma wartość {{TRUE/pl}}.

-    **Obrót|Angle**: Obrót profilu wokół jego osi wyciągania.



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Rama** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
Frame = makeFrame(baseobj, profile)
```

-   Tworzy obiekt `Frame` z podanego `baseobj` i `profile`.
    -   
        `baseobj`
        
        jest dowolnym obiektem zawierającym polilinie, takim jak [polilinia](Draft_Wire/pl.md) środowiska Rysunek Roboczy lub [szyk ortogonalny](Draft_OrthoArray/pl.md) z ich kolekcją.

    -   
        {{Incode|profile}}
        
        jest wytłaczanym obiektem 2D zawierającym ściany lub zamknięte przewody.

Przykład:


```python
import Draft, Arch

Line = Draft.makeLine(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 2000))
baseobj = Draft.makeArray(Line, FreeCAD.Vector(1000, 0, 0), FreeCAD.Vector(0, 1, 0), 6, 1)

profile = Draft.makeCircle(200)
Frame = Arch.makeFrame(baseobj, profile)
FreeCAD.ActiveDocument.recompute()
```





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch Frame/pl
