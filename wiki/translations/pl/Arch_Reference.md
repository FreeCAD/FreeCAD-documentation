---
 GuiCommand:
   Name: Arch Reference
   Name/pl: BIM: Odniesienie
   MenuLocation: 3D / BIM , Narzędzia ogólne 3D , Odniesienie
   Workbenches: BIM_Workbench/pl
   SeeAlso: 
---

# Arch Reference/pl



## Opis

Narzędzie **Odniesienie** umożliwia umieszczenie w bieżącym dokumencie obiektu, który kopiuje swój kształt i kolory z obiektu opartego na [Części](Part_Workbench/pl.md) *(w tym [Części budynku](Arch_BuildingPart/pl.md))* przechowywanego w innym pliku FreeCAD. Jeśli ten plik ulegnie zmianie, obiekt referencyjny zostanie oznaczony do ponownego załadowania.

<img alt="" src=images/Arch_reference_screenshot.png  style="width:600px;">



## Użycie

1.  Naciśnij przycisk **<img src="images/Arch_Reference.svg" width=16px> '''Odniesienie'''**,
2.  Naciśnij przycisk \"Wybierz plik \...\" i wybierz istniejący plik FreeCAD,
3.  Wybierz jeden z dołączonych obiektów opartych na częściach z rozwijanej listy,
4.  Naciśnij przycisk **OK**.



## Opcje

-   Obiekt referencyjny można przesuwać i obracać, bieżąca pozycja zostanie zachowana po ponownym załadowaniu obiektu.
-   Jeśli oryginalny obiekt zostanie przeniesiony w pliku zawierającym, ruch ten zostanie odzwierciedlony w obiekcie referencyjnym.
-   Klikając prawym przyciskiem myszy obiekt odniesienia w widoku drzewa, można przeładować oryginalny obiekt lub otworzyć plik zawierający.
-   Aby odwołać się do kilku obiektów jednocześnie, umieść je wewnątrz [części budynku](Arch_BuildingPart/pl.md).
-   Po wyłączeniu właściwości widoku **Aktualizuj kolory** obiektu referencyjnego, nie będzie on już przeładowywał oryginalnych kolorów, więc można je bezpiecznie zmienić.



## Właściwości

-    **Plik**: Plik bazowy, na którym zbudowany jest ten komponent.

-    **Część**: Część do użycia z pliku bazowego.

-    **Aktualizuj kolory**: Jeśli wartość ta zostanie ustawiona na {{true/pl}}, kolory z połączonego pliku będą aktualizowane.



## Tworzenie skryptów 

Narzędzie Odniesienie może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji:


```python
reference = makeReference([filepath], [partname], [name])
```

Tworzy obiekt `reference` nazwany `name` z obiektu `partname` w pliku `filepath`. Wszystkie argumenty są opcjonalne.

Przykład:


```python
import Arch
Arch.makeReference("/path/to/some/file.FSCtd", "myPart")
```





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch Reference/pl
