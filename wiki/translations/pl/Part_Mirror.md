---
- GuiCommand:
   Name: Part Mirror
   Name/pl: Część: Odbicie lustrzane
   MenuLocation: Część - Odbicie lustrzane ...
   Workbenches: [Część](Part_Workbench/pl.md)
---

# Part Mirror/pl



## Opis

**Odbicie lustrzane** tworzy nowy obiekt *(obraz)*, który jest odbiciem oryginalnego obiektu *(źródła)*. Obiekt obrazu jest tworzony za płaszczyzną lustrzaną. Płaszczyzna lustrzana może być płaszczyzną standardową *(**XY**, **YZ** lub **XZ**)* lub dowolną płaszczyzną równoległą do płaszczyzny standardowej.

Dla przykładu:

![Wcześniej](images/PARTMirrorBeforev11.png )

![Po *(odbicie lustrzane przez płaszczyznę **YZ**)*](images/PARTMirrorAfterv11.png ) 



## Użycie

![](images/PARTMirrorDialogv11.png )

1.  Wybierz obiekt źródłowy z listy Panelu Odbicie lustrzane.
2.  Wybierz standardową **płaszczyznę odbicia lustrzanego** z menu rozwijanego.
3.  Naciśnij **OK**, aby utworzyć obiekt obrazu.






## Opcje

Pola **Punkt odniesienia** można użyć do przesunięcia płaszczyzny lustra równolegle do wybranej standardowej płaszczyzny lustra. Tylko jedno z pól **X**, **Y** lub **Z** może być użyte dla danej płaszczyzny standardowej.

  Standardowa płaszczyzna   Pole punktu bazowego   Efekt
    
  **XY**                    **Z**                  Przesuń płaszczyznę lustra wzdłuż osi **Z**.
  **XY**                    **X**, **Y**           Nie ma żadnego efektu.
  **XZ**                    **Y**                  Przesuń płaszczyznę lustra wzdłuż osi **Y**.
  **XZ**                    **X**, **Z**           Nie ma żadnego efektu.
  **YZ**                    **X**                  Przesuń płaszczyznę lustra wzdłuż osi **X**.
  **YZ**                    **Y**, **Z**           Nie ma żadnego efektu.



## Uwagi

-   Obiekty [Odnośników](App_Link/pl.md) powiązane z odpowiednimi typami obiektów i kontenery [Część: App](App_Part/pl.md) z odpowiednimi widocznymi obiektami wewnątrz mogą być również używane jako obiekty źródłowe. {{Version/pl|0.20}}
-   Arbitralne płaszczyzny lustrzane *(tj. nie równoległe do standardowej płaszczyzny)* nie są obsługiwane.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Mirror/pl
