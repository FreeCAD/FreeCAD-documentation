---
 GuiCommand:
   Name: FCGear HypoCycloidGear
   Name/pl: FCGear: Zębatka hipocykloidalna
   MenuLocation: Gear , Zębatka hipocykloidalna
   Workbenches: FCGear_Workbench/pl
   Shortcut: Brak
   Version: 0.22
   SeeAlso: 
---

# FCGear HypoCycloidGear/pl



## Opis

Polecenie <img alt="" src=images/FCGear_HypoCycloidGear.svg  style="width:16px;"> **Zębatka hipocykloidalna** tworzy dwie wielowypustowe tarcze krzywkowe i zestaw rolek, które pozostają w kontakcie z zewnętrznymi powierzchniami tarcz podczas ruchu.

<img alt="" src=images/FCGear_FCGear_HypoCycloidGear-04.png  style="width:200px;"> <img alt="" src=images/FCGear_FCGear_HypoCycloidGear-05.png  style="width:200px;"> 
*Po lewej: Przekładnia hipocykloidalna. Po prawej: Przekładnia i przejrzyście pokazana przekładnia odwrotna i zestaw rolek.*

Prosimy o krótki opis tego, co można osiągnąć za pomocą takiego układu przekładni.



## Użycie

1.  Przejdź do środowiska pracy <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear](FCGear_Workbench/pl.md).
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **[<img src=images/FCGear_HypoCycloidGear.svg style="width:16px"> '''Zębatka hipocykloidalna'''** na pasku narzędzi.
    -   Wybierz z menu opcję **Gear → [<img src=images/FCGear_HypoCycloidGear.svg style="width:16px"> Zębatka hipocykloidalna**.
3.  Zmień parametry zębatki na wymagane *(patrz [Właściwości](#Właściwości.md))*.



## Właściwości



## Uwagi

Domyślnie koła zębate są wyświetlane w następujący sposób:

<img alt="" src=images/FCGear_FCGear_HypoCycloidGear-01.png  style="width:200px;">

Aby wyświetlić tarcze krzywkowe i zestaw rolek *(sworzni)* w różnych kolorach, potrzebujemy trzech identycznych obiektów Zębatka hipocykloidalna. Ich widoczność można przełączać:

-    **show_disk0|Bool**dla głównego dysku krzywki.

-    **show_disk1|Bool**dla odwróconej tarczy krzywkowej na górze.

-    **show_pins|Bool**dla zestawu rolek.

<img alt="" src=images/FCGear_FCGear_HypoCycloidGear-02.png  style="width:200px;"> <img alt="" src=images/FCGear_FCGear_HypoCycloidGear-03.png  style="width:200px;"> 
*Po lewej: Utworzone obiekty Zębatka hipocykloidalna. Po prawej: Zmiana położenia obiektów w celu uzyskania lepszego widoku każdego z nich.*



## Tworzenie skryptów



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear HypoCycloidGear/pl
