---
- GuiCommand:
   Name: Part Section
   Name/pl: Część: Przecięcie
   MenuLocation: Część - Operacje logiczne - Przecięcie
   Workbenches: [Część](Part_Workbench/pl.md)
   SeeAlso: [Przekrój poprzeczny](Part_CrossSections/pl.md)
---

# Part Section/pl



## Opis

Polecenie <img alt="" src=images/Part_Section.svg  style="width:24px;"> **Przecięcie** tworzy geometrię polilinii na przecięciach dwóch obiektów. Wynik jest w pełni parametryczny.

-   W wyniku przecięcia dwóch brył / powierzchni powstaje jeden lub więcej odcinków.
-   W wyniku przecięcia dwóch prostych lub prostej i bryły / powierzchni otrzymujemy jeden lub więcej punktów.

![](images/PartSection1_it.png ) 
*Sześcian przecięty walcem*



## Użycie

1.  Wybierz dwa obiekty.
2.  Pierwszym obiektem będzie **Baza** przekroju, ale kolejność wyboru nie ma wpływu na wynik.
3.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **![](images/)_[Przecięcie](Part_Section/pl.md)**.
    -   Wybierz z menu opcję **Część → ![](images/)_Przecięcie**.



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt Przecięcie wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{Properties_Title|Podstawowe}}

-    **Baza|Link**: Odnośnik do pierwszego obiektu.

-    **Narzędzie|Link**: Odnośnik do drugiego obiektu


{{Properties_Title|Boolean}}

-    **Histry|ShapeHistory|ukryty**: \"Historia kształtu\".

-    **Ulepsz|Bool**: \"Ulepsz kształt (usuń zbędne krawędzie) po tej operacji logicznej\". Wartość domyślna jest określana przez preferencję **Automatycznie dopracuj model po operacji opartej na szkicu**. Zobacz również stronę [ustawienia](PartDesign_Preferences/pl#Og.C3.B3lne.md) środowiska pracy Projekt Części.


{{Properties_Title|Przekrój}}

-    **Approksymacja|Bool**: Przybliż krawędzie wynikowe.



## Odnośniki internetowe 

Aby utworzyć przekroje za pomocą płaszczyzny przekroju, zobacz stronę <img alt="" src=images/Part_CrossSections.svg  style="width:24px;">

[Przekrój poprzeczny](Part_CrossSections/pl.md).



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Section/pl
