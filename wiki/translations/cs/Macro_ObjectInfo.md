 {{Macro/cs
|Name=Macro ObjectInfo
|Translate=Macro ObjectInfo
|Description=Poskytuje informace o vybraném objektu
|Author=keithsloan52
|Version=1.0
|Date=2012-11-09
|FCVersion=Until 0.17 '''and PyQt4'''
|Download=Ово није макро него једна ВоркБенцх, декомпримирајте .зип датотеку и налепите комплетан директоријум у Мод корисничком именику [https://github.com/KeithSloan/FreeCAD_Info/archive/master.zip Info]
|SeeAlso=<img src=images/Arch_Survey.svg style="width:Arch Survey|24px"> [Arch Survey](Arch_Survey/cs.md)
}}

## Popis

Toto WorkBench vám umožňuje znát informační plochu objemu, střed hmoty a okamžik intertiktury vybraného objektu.

<img alt="" src=images/ObjectInfoIt.png  style="width:480px;">

## Instalace

Pokud používáte Linux, musíte vytvořit složku s názvem \"Mod\" ve skryté složce .FreeCAD, která se nachází ve složce Home. Pak vytvořte složku s názvem \"Info\" ve složce \"Mod\" a extrahujte obsah archivu do něj. V systému Windows nemám tušení, kde to bude. Stejný postup použijte v systému Windows C:\\Program Files\\FreeCAD\\Mod.


<div class="mw-translate-fuzzy">

## Jak používat {#jak_používat}

Pak spusťte aplikaci FreeCAD, otevřete soubor STEP a přejděte na pracovním stole \"Info\" pomocí přepínače pracovních stolů nebo přejděte do nabídky Zobrazit → Workbench. Nyní vyberte své pevné a klikněte na ikonu \"Info\"; levý panel úloh zobrazí některé informace o modelu, včetně objemu, plochy povrchu, středu hmotnosti a momentu intertia.


</div>

## Kód


{{MacroCode|code=
import webbrowser 

##########
# WorkBenche
# Code used to download the zip file from FreeCAD
##########

FreeCAD.Console.PrintMessage("\n" + "You must download the Info.zip file in the author github KeithSloan/FreeCAD_Infosite" + "\n")
FreeCAD.Console.PrintMessage("http://keithsloan.dynu.com/Keith&Jenny/" + "\n")
webbrowser.open("https://github.com/KeithSloan/FreeCAD_Info/archive/master.zip")

}}

## Odkazy

Uživatel FreeCAD vytvořil uživatelsky přívětivý modul \"Info\", který můžete získat zde: <http://www.sloan-home.co.uk/FreeCAD/Info/Info.html>

Z fóra [Info Workbench - Help with icons please.](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185)




