# Introduction to Python/de
{{TOCright}}

## Einführung

Dies ist ein kurzes Tutorium für diejenigen, die neu bei [Python](https   *//en.wikipedia.org/wiki/Python_%28programming_language%29) sind. Python ist eine quelloffene, plattformübergreifende [Programmiersprache](https   *//en.wikipedia.org/wiki/Programming_language). Sie verfügt über mehrere Funktionen, die sie von anderen Programmiersprachen unterscheidet, und ist für neue Benutzer sehr zugänglich   *

-   Sie wurde so gestaltet, dass sie für Menschen lesbar ist, so dass sie relativ leicht zu erlernen und zu verstehen ist.
-   Sie wird interpretiert, das bedeutet, dass Programme nicht erst kompiliert werden müssen, bevor sie ausgeführt werden können. Python Code kann sofort ausgeführt werden, auch Zeile für Zeile, wenn du es wünschst.
-   Sie kann als Skriptsprache in andere Programme eingebettet werden. FreeCAD hat einen eingebetteten Python Interpreter. Du kannst Python Code schreiben, um Teile von FreeCAD zu verändern. Dies ist sehr mächtig, es bedeutet, daß du deine eigenen Werkzeuge bauen kannst.
-   Sie ist erweiterbar, du kannst einfach neue Module in deine Python Installation einbauen und deren Funktionalität erweitern. Zum Beispiel gibt es Module, die es Python erlauben, Bilder zu lesen und zu schreiben, mit Twitter zu kommunizieren, Aufgaben zu planen, die von deinem Betriebssystem ausgeführt werden sollen, usw.

Das Folgende ist eine sehr grundlegende Einführung und keineswegs ein vollständiges Tutorium. Aber sie wird hoffentlich einen guten Ausgangspunkt für die weitere Erforschung von FreeCAD und seinen Mechanismen bieten. Wir empfehlen dir dringend, die untenstehenden Code Schnipsel in einen Python Interpreter einzugeben.

## Der Interpreter 

Gewöhnlich öffnest du beim Schreiben von Computerprogrammen einen Texteditor oder deine spezielle Programmierumgebung (die im Grunde ein Texteditor mit einigen zusätzlichen Werkzeugen ist), schreibst dein Programm, kompilierst und führst es dann aus. Oftmals wurden bei der Eingabe ein oder mehrere Fehler gemacht, so dass dein Programm nicht funktioniert. Möglicherweise erhälst du sogar eine Fehlermeldung, die dir mitteilt, was schief gelaufen ist. Dann gehe zurück zu deinem Texteditor, korrigiere die Fehler, laufe erneut durch und wiederhole dies, bis dein Programm wie beabsichtigt funktioniert.

In Python kann dieser ganze Prozess transparent im Python Interpreter ausgeführt werden. Der Interpreter ist ein Python Fenster mit einer Eingabeaufforderung, wo du einfach Python Code eintippen kannst. Wenn du Python auf deinem Computer installiert hast (Herunterladen von der [Python Webseite](https   *//www.python.org/), wenn du es auf Windows- oder Mac benutzt, installiere es von deinem Paket Repositorium, wenn du auf GNU/ Linux installierst). Aber, wie bereits erwähnt, hat FreeCAD auch einen eingebauten Python Interpreter   * die [Python Konsole](Python_console/de.md).

![](images/FreeCAD_Python_console.png ) 
*Die FreeCAD Python Konsole*

Wenn du sie nicht siehst, klicke auf **Ansicht → Paneele → Python Konsole**. Die Python Konsole kann in der Größe verändert und auch wieder abgedockt werden.

Der Interpreter zeigt die Python Version, dann ein `>>>` Symbol, das ist die Eingabeaufforderung, das heißt, hier geben Sie Python-Code ein. Schreiben von Code im Interpreter ist einfach   * eine Zeile ist eine Anweisung. Wenn du **Enter** drückst, wird dein Code Zeile ausgeführt (nachdem sie sofort und unsichtbar kompiliert wurde). Zum Beispiel, versuche dies zu schreiben   *


```python
print("hello")
```


`print()`

ist ein Python Befehl, der natürlich, etwas auf den Bildschirm druckt. Wenn du die **Eingabetaste** drückst, wird die Operation ausgeführt, und die Nachricht `"Hallo"` wird gedruckt. Wenn du einen Fehler machst, schreiben wir zum Beispiel   *


```python
print(hello)
```

Python wird dir dies sofort mitteilen. In diesem Fall weiß Python nicht, was `hallo` ist. Die `" "` Zeichen geben an, dass der Inhalt eine Zeichenfolge ist, d.h. Programmierjargon für ein Stück Text. Ohne diese Zeichen erkennt der `print()` Befehl nicht `hello`. Durch Drücken des Pfeils nach oben kannst du zur letzten Codezeile zurückgehen und diese korrigieren.

Der Python Interpreter hat auch ein eingebautes Hilfesystem. Nehmen wir an, wir verstehen nicht, was mit `print(hello)` schief gelaufen ist, und wir wollen konkrete Informationen über den Befehl   *


```python
help("print")
```

Du erhältst eine lange und vollständige Beschreibung von allem, was der `print()` Befehl tun kann.

Jetzt, da du den Python Interpreter verstehst, können wir mit den ernsteren Dingen fortfahren. {{Top}}

## Variablen

Sehr oft musst du beim Programmieren einen Wert unter einem Namen speichern. An dieser Stelle kommen Variablen ins Spiel. Gib zum Beispiel dies ein   *


```python
a = "hello"
print(a)
```

Du verstehst wahrscheinlich, was hier passiert ist, wir haben die Zeichenfolge `"hello"` unter dem Namen `a` gespeichert. Jetzt, da `a` bekannt ist, können wir sie überall verwenden, zum Beispiel im `print()` Befehl. Wir können jeden beliebigen Namen verwenden, wir müssen nur einige einfache Regeln befolgen, wie z.B. keine Leerzeichen oder Interpunktion und keine Python Schlüsselwörter verwenden. Wir können zum Beispiel schreiben   *


```python
hello = "my own version of hello"
print(hello)
```

Nun ist `hallo` nicht mehr undefiniert. Variablen können jederzeit geändert werden, deshalb nennt man sie Variablen, ihr Inhalt kann variieren. Zum Beispiel   *


```python
myVariable = "hello"
print(myVariable)
myVariable = "good bye"
print(myVariable)
```

Wir haben den Wert von `myVariable` geändert. Wir können auch Variablen kopieren   *


```python
var1 = "hello"
var2 = var1
print(var2)
```

Es ist ratsam, deinen Variablen aussagekräftige Namen zu geben. Nach einer Weile wirst du dich nicht mehr daran erinnern, was deine Variable mit dem Namen `a` darstellt. Aber wenn du sie zum Beispiel `myWelcomeMessage` genannt hast, wirst du dich leicht an ihren Zweck erinnern. Außerdem ist dein Code einen Schritt näher an der Selbst-erklärend.

Der Fall ist sehr wichtig, `myVariable` ist nicht dasselbe wie `myvariable`. Wenn du `print(myvariable)` eingeben würdest, würde es mit einem Fehler als nicht definiert zurückgegeben werden. {{Top}}

## Zahlen

Natürlich können Python Programme mit allen Arten von Daten umgehen, nicht nur mit Textzeichenfolgen. Eine Sache ist wichtig, Python muss wissen, mit welcher Art von Daten es zu tun hat. Wir haben in unserem Hallo Druck Beispiel gesehen, dass der Befehl `print()` unsere `"hallo"` Zeichenfolge erkannt hat. Durch die Verwendung von `" "` Zeichen haben wir festgelegt, dass das, was folgt, eine Textzeichenfolge ist.

Wir können immer den Datentyp einer Variablen überprüfen, mit dem `type()` Befehl   *


```python
myVar = "hello"
type(myVar)
```

Es wird uns sagen, der Inhalt von `myVar` ist ein `'str'`, was die Kurzform für Zeichenfolge ist. Wir haben auch andere grundlegende Datentypen wie Integer und Gleitkomma Zahlen   *


```python
firstNumber = 10
secondNumber = 20
print(firstNumber + secondNumber)
type(firstNumber)
```

Python weiß, dass 10 und 20 ganze Zahlen sind, also werden sie als `'int'` gespeichert, und Python kann mit ihnen alles machen, was es mit ganzen Zahlen machen kann. Schaue dir die Ergebnisse davon an   *


```python
firstNumber = "10"
secondNumber = "20"
print(firstNumber + secondNumber)
```

Hier haben wir Python gezwungen, zu bedenken, dass unsere beiden Variablen keine Zahlen, sondern Textstücke sind. Python kann zwei Textstücke zusammenfügen, obwohl es in diesem Fall natürlich keine Arithmetik ausführt. Aber wir sprachen über ganze Zahlen. Es gibt auch Gleitkommazahlen. Der Unterschied ist, dass Gleitkommazahlen einen Dezimalteil haben können und Ganzzahlen nicht   *


```python
var1 = 13
var2 = 15.65
print("var1 is of type ", type(var1))
print("var2 is of type ", type(var2))
```

Ganzzahlen und Gleitkommazahlen können problemlos miteinander gemischt werden   *


```python
total = var1 + var2
print(total)
print(type(total))
```

Da `var2` ein Gleitkommawert ist, entscheidet Python automatisch, dass das Ergebnis ebenfalls ein Gleitkommawert sein muss. Aber es gibt Fälle, in denen Python nicht weiß, welchen Typ es verwenden soll. Zum Beispiel   *


```python
varA = "hello 123"
varB = 456
print(varA + varB)
```

Dies führt zu einem Fehler, `varA` ist eine Zeichenfolge und `varB` ist eine ganze Zahl, und Python weiß nicht, was zu tun ist. Wir können Python jedoch zwingen, zwischen den Typen zu konvertieren   *


```python
varA = "hello"
varB = 123
print(varA + str(varB))
```

Nun, da beide Variablen Zeichenfolgen sind, funktioniert die Operation. Beachte, dass wir `varB` zum Zeitpunkt des Drucks \"zeichenfolgenfiziert\" haben, aber `varB` selbst nicht geändert haben. Wenn wir `varB` dauerhaft in eine Zeichenfolge verwandeln wollten, müssten wir dies tun   *


```python
varB = str(varB)
```

Wir können auch `int()` und `float()` einsetzen, um Werte zu konvertieren in Ganzzahlen und Gleitkommazahlen, wenn wir wollen   *


```python
varA = "123"
print(int(varA))
print(float(varA))
```

Du hast sicher bemerkt, dass wir den Befehl `print()` auf verschiedene Weise verwendet haben. Wir haben Variablen, Summen, verschiedene durch Kommas getrennte Dinge und sogar das Ergebnis eines anderen Pythonbefehls gedruckt. Vielleicht hast du auch gesehen, dass diese beiden Befehle   *


```python
type(varA)
print(type(varA))
```

das gleiche Ergebnis haben. Das liegt daran, dass wir uns im Interpreter befinden, und alles wird automatisch ausgedruckt. Wenn wir komplexere Programme schreiben, die außerhalb des Interpreters laufen, werden sie nicht automatisch gedruckt, so dass wir den Befehl `print()` verwenden müssen. Mit diesem Gedanken im Hinterkopf sollten wir ihn hier nicht mehr verwenden. Von nun an werden wir einfach schreiben   *


```python
myVar = "hello friends"
myVar
```


{{Top}}

## Listen

Ein weiterer nützlicher Datentyp ist eine Liste. Eine Liste ist eine Sammlung von anderen Daten. Um eine Liste zu definieren, verwenden wir `[ ]`   *


```python
myList = [1, 2, 3]
type(myList)
myOtherList = ["Bart", "Frank", "Bob"]
myMixedList = ["hello", 345, 34.567]
```

Wie du siehst, kann eine Liste jede Art von Daten enthalten. Mit einer Liste kannst du viele Dinge tun. Zum Beispiel kannst du deine Elemente zählen   *


```python
len(myOtherList)
```

Oder ein Element abrufen   *


```python
myName = myOtherList[0]
myFriendsName = myOtherList[1]
```

Während der `len()` Befehl die Gesamtzahl der Elemente in einer Liste zurückgibt, steht das erste Element in einer Liste immer an der Position `len|0`, so dass in unserer `myOtherList` `"Bob"` wird an der Position `2` stehen. Mit Listen können wir viel mehr tun, z.B. Artikel sortieren und Artikel entfernen oder hinzufügen.

Interessanterweise ist eine Textzeichenfolge einer Liste von Zeichen in Python sehr ähnlich. Versuche dies zu tun   *


```python
myvar = "hello"
len(myvar)
myvar[2]
```

Normalerweise kann das, was du mit Listen machen kannst, auch mit Zeichenketten gemacht werden. Tatsächlich sind sowohl Listen als auch Zeichenketten Sequenzen.

Neben Zeichenketten, Ganzzahlen, Gleitkommazahlen und Listen gibt es weitere eingebaute Datentypen, wie z.B. Wörterbücher, und du kannst sogar eigene Datentypen mit Klassen erstellen. {{Top}}

## Einrückung

Ein wichtiger Nutzen von Listen ist die Möglichkeit, sie \"durchzublättern\" und mit jedem Punkt etwas zu tun. Sieh dir zum Beispiel das hier an   *


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
for dalton in alldaltons   *
    print(dalton + " Dalton")
```

Wir iterierten (Programmierjargon) durch unsere Liste mit dem Befehl `for in` und machten etwas mit jedem der Punkte. Beachte die spezielle Syntax   * Der Befehl `for` endet mit `   *` und zeigt an, dass es sich bei dem folgenden Befehl um einen Block mit einem oder mehreren Befehlen handelt. Im Interpreter wechselt die Eingabeaufforderung unmittelbar nach der Eingabe der Befehlszeile, die mit `   *` endet, zu `...`, was bedeutet, dass Python weiß, dass noch mehr kommen wird.

Woher wird Python wissen, wie viele der nächsten Zeilen innerhalb der Operation `for in` ausgeführt werden müssen? Python verlässt sich dabei auf Einrückung. Die nächsten Zeilen müssen mit einem Leerzeichen, oder mehreren Leerzeichen, oder einem Tabulator, oder mehreren Tabulatoren beginnen. Und solange die Einrückung gleich bleibt, werden die Zeilen als Teil des `for in` Blocks betrachtet. Wenn du eine Zeile mit 2 Leerzeichen und die nächste mit 4 beginnst, gibt es einen Fehler. Wenn du fertig bist, schreibe einfach eine weitere Zeile ohne Einrückung, oder drücke **Enter**, um vom `for in` Block zurückzukehren

Die Einrückung trägt auch zur Lesbarkeit des Programms bei. Wenn du beim Schreiben eines großen Programms große Einrückungen verwendest (z.B. Tabulatoren anstelle von Leerzeichen verwendest), hast du einen klaren Überblick darüber, was innerhalb von was ausgeführt wird. Wir werden sehen, dass auch andere Befehle eingerückte Codeblöcke verwenden.

Der `for in` Befehl kann für viele Dinge verwendet werden, die mehr als einmal ausgeführt werden müssen. Er kann z.B. mit dem Befehl `range()` kombiniert werden   *


```python
serie = range(1, 11)
total = 0
print("sum")
for number in serie   *
    print(number)
    total = total + number
print("")
print(total)
```

Wenn du die Code Beispiele in einem Interpreter durch Kopieren und Einfügen ausgeführt hast, wirst du feststellen, dass der vorherige Textblock einen Fehler auslöst. Kopiere stattdessen an das Ende des eingerückten Blocks, d.h. an das Ende der Zeile `total <nowiki>=</nowiki> total + number` und füge dann im Interpreter ein. Drücke im Interpreter **Enter**, bis die Eingabeaufforderung mit den drei Punkten verschwindet und der Code ausgeführt wird. Kopiere dann die letzten beiden Zeilen, gefolgt von einer weiteren **Enter**. Die endgültige Antwort sollte erscheinen.

Wenn du in den Interpreter `help(range)` eintippst, wirst du sehen   *


```python
range(...)
    range(stop) -> list of integers
    range(start, stop[, step]) -> list of integers
```

Hier bezeichnen die eckigen Klammern einen optionalen Parameter. Es wird jedoch erwartet, dass es sich bei allen Parametern um ganze Zahlen handelt. Im Folgenden erzwingen wir mit `int()`, dass der Schrittparameter eine ganze Zahl ist   *


```python
number = 1000
for i in range(0, 180 * number, int(0.5 * number))   *
    print(float(i) / number)
```

Ein weiteres `range()` Beispiel   *


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
for n in range(4)   *
    print(alldaltons[n], " is Dalton number ", n)
```

Der `range()` Befehl hat auch die seltsame Besonderheit, dass er mit `0` beginnt (wenn du die Startnummer nicht angibst) und dass seine letzte Nummer um eins kleiner ist als die von dir angegebene Endnummer. Das ist natürlich, damit es gut mit anderen Python Befehlen funktioniert. Zum Beispiel   *


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
total = len(alldaltons)
for n in range(total)   *
    print(alldaltons[n])
```

Eine weitere interessante Verwendung von eingerückten Blöcken ist der Befehl `if`. Dieser Befehl führt einen Codeblock nur dann aus, wenn z.B. eine bestimmte Bedingung erfüllt ist   *


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
if "Joe" in alldaltons   *
    print("We found that Dalton!!!")
```

Natürlich wird dabei immer der Satz gedruckt, aber versuche, die zweite Zeile zu ersetzen mit   *


```python
if "Lucky" in alldaltons   *
```

Dann wird nichts ausgegeben. Wir können auch eine `else` Anweisung angeben   *


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
if "Lucky" in alldaltons   *
    print("We found that Dalton!!!")
else   *
    print("Such Dalton doesn't exist!")
```


{{Top}}

## Funktionen

Es gibt nur sehr wenige [Standard Python Befehle](https   *//docs.python.org/3/reference/lexical_analysis.html#identifiers) und wir kennen bereits einige davon. Aber du kannst deine eigenen Befehle erstellen. Tatsächlich tun die meisten Zusatzmodule, die du in deine Python Installation einbinden kannst, genau das, sie fügen Befehle hinzu, die du verwenden kannst. Ein benutzerdefinierter Befehl wird in Python als Funktion bezeichnet und ist wie folgt aufgebaut   *


```python
def printsqm(myValue)   *
    print(str(myValue) + " square meters")

printsqm(45)
```

Der `def()` Befehl definiert eine neue Funktion, du gibst ihr einen Namen, und innerhalb der Klammer definierst du die Argumente, die die Funktion verwenden wird. Argumente sind Daten, die an die Funktion übergeben werden. Sieh dir zum Beispiel den `len()` Befehl an. Wenn du einfach `len()` schreibst, wird Python dir sagen, dass es ein Argument braucht. Was offensichtlich ist   * du willst die Länge von etwas wissen. Wenn du `len(myList)` schreibst, ist `myList` das Argument, das du an die `len()` Funktion übergibst. Und die `len()` Funktion ist so definiert, dass sie weiß, was sie mit diesem Argument tun soll. Wir haben dasselbe mit unserer `printsqm` Funktion getan.

Der `myValue` Name kann alles sein, und er wird nur innerhalb der Funktion verwendet. Es ist nur ein Name, den du dem Argument gibst, damit du etwas damit machen kannst. Indem du Argumente definierst, teilst du der Funktion auch mit, wie viele zu erwarten sind. Wenn du das zum Beispiel tust   *


```python
printsqm(45, 34)
```

gibt es einen Fehler. Unsere Funktion wurde programmiert, nur ein Argument zu erhalten, aber es erhielt zwei, `45` und `34`. Versuchen wir ein anderes Beispiel   *


```python
def sum(val1, val2)   *
    total = val1 + val2
    return total

myTotal = sum(45, 34)
```

Hier haben wir eine Funktion erstellt, die zwei Argumente empfängt, sie summiert und diesen Wert zurückgibt. Etwas zurückzugeben ist sehr nützlich, da wir mit dem Ergebnis etwas tun können, wie es z.B. in der Variablen `myTotal` speichern können. {{Top}}

## Module

Nun, da du eine gute Vorstellung davon hast, wie Python funktioniert, musst du noch eine weitere Sache wissen   * Wie man mit Dateien und Modulen arbeitet.

Bis jetzt haben wir Python Anweisungen Zeile für Zeile in den Interpreter geschrieben. Diese Methode ist für größere Programme offensichtlich nicht geeignet. Normalerweise wird der Code für Python Programme in Dateien mit der Erweiterung **.py** gespeichert. Dabei handelt es sich nur um einfache Textdateien, die mit einem beliebigen Texteditor (Linux gedit, emacs, vi oder sogar Windows Notepad) erstellt und bearbeitet werden können.

Es gibt mehrere Möglichkeiten, ein Python Programm auszuführen. Unter Windows klicke einfach mit der rechten Maustaste auf deine Datei, öffne sie mit Python und führe sie aus. Du kannst sie aber auch aus dem Python Interpreter selbst heraus ausführen. Dazu muss der Interpreter wissen, wo sich dein Programm befindet. In FreeCAD ist es am einfachsten, dein Programm in einem Ordner abzulegen, den der Python Interpreter von FreeCAD standardmäßig kennt, z.B. im Ordner **Mod** des FreeCAD Anwenders   *

-   Unter Linux ist es normalerweise **/home/<username>/.local/share/FreeCAD/Mod/** ({{VersionPlus/de|0.20}}) or **/home/<username>/.FreeCAD/Mod/** ({{VersionMinus/de|0.19}}).
-   Unter Windows ist es **%APPDATA%\FreeCAD\Mod\**, was normalerweise **C   *Users\<username>\Appdata\Roaming\FreeCAD\Mod\** ist.
-   Unter Mac OSX ist dies normalerweise **/Users/<username>/Library/Preferences/FreeCAD/Mod/**.

Fügen wir dort einen Unterordner namens **scripts** hinzu und schreiben dann eine Datei wie diese   *


```python
def sum(a,b)   *
    return a + b

print("myTest.py succesfully loaded")
```

Speichere die Datei als **myTest.py** im **scripts** Ordner und schreibe in das Interpreterfenster   *


```python
import myTest
```

ohne die **.py** Erweiterung. Dadurch wird der Inhalt der Datei Zeile für Zeile so ausgeführt, als ob wir ihn im Interpreter geschrieben hätten. Die Summenfunktion wird erstellt, und die Nachricht wird gedruckt. Dateien, die Funktionen enthalten, wie unsere, werden Module genannt.

Wenn wir eine `sum()` Funktion im Interpreter schreiben, führen wir sie so aus   *


```python
sum(14, 45)
```

Aber wenn wir ein Modul importieren, das eine `sum()` Funktion enthält, ist die Syntax etwas anders   *


```python
myTest.sum(14, 45)
```

Das heißt, das Modul wird als \"Container\" importiert, und alle seine Funktionen befinden sich innerhalb dieses Containers. Das ist sehr nützlich, denn wir können viele Module importieren und alles gut organisiert halten. Wenn du `something.somethingElse`, mit einem Punkt dazwischen, siehst, dann bedeutet dies, dass `somethingElse` sich innerhalb von `something` befindet.

Wir können unsere sum() Funktion auch direkt in den Hauptinterpreterraum importieren   *


```python
from myTest import *
sum(12, 54)
```

Fast alle Module tun dies   * Sie definieren Funktionen, neue Datentypen und Klassen, die du im Interpreter oder in deinen eigenen Python Modulen verwenden kannst, denn nichts hindert dich daran, andere Module innerhalb deines Moduls zu importieren!

Woher wissen wir, welche Module wir haben, welche Funktionen darin enthalten sind und wie sie zu verwenden sind (d.h. welche Art von Argumenten sie brauchen)? Wir haben bereits gesehen, dass Python eine `help()` Funktion hat. Mache   *


```python
help("modules")
```

wird uns eine Liste aller verfügbaren Module geben. Wir können jedes von ihnen importieren und ihren Inhalt mit dem Befehl `dir()` durchsuchen   *


```python
import math
dir(math)
```

Wir werden alle Funktionen sehen, die im `math` modul enthalten sind, sowie seltsame Dinge namens `__doc__`, `__file__`, `__name__`. Jede Funktion in einem gut gemachten Modul hat eine `__doc__`, die erklärt, wie man sie benutzt. Zum Beispiel sehen wir, dass es eine `sin()` Funktion innerhalb des Mathematikmoduls gibt. Möchtest Du wissen, wie man sie benutzt? 
```python
print(math.sin.__doc__)
```

Es mag nicht offensichtlich sein, aber auf beiden Seiten von `doc` sind zwei Unterstreichungszeichen.

Und zum Schluss noch ein letzter Tipp   * Bei der Arbeit an neuem oder bestehendem Code ist es besser, nicht die FreeCAD Makro Dateierweiterung **.FCMacro** zu verwenden, sondern stattdessen die Standard Erweiterung **.py**. Der Grund dafür ist, dass Python die Erweiterung **.FCMacro** nicht kennt. Wenn du **.py** verwendest, kann dein Code einfach mit `import` geladen werden, wie wir bereits gesehen haben, und auch mit `importlib.reload()` neu geladen werden   *


```python
import importlib
importlib.reload(myTest)
```

Es gibt jedoch eine Alternative   *


```python
exec(open("C   */PathToMyMacro/myMacro.FCMacro").read())
```


{{Top}}

## Loslegen mit FreeCAD 

Hoffentlich hast du nun eine gute Vorstellung davon, wie Python funktioniert, und du kannst damit beginnen, zu erkunden, was FreeCAD zu bieten hat. Die Python Funktionen von FreeCAD sind alle gut in verschiedenen Modulen organisiert. Einige von ihnen sind bereits geladen (importiert), wenn du FreeCAD startest. Probiere einfach   *


```python
dir()
```


{{Top}}

## Hinweise

-   FreeCAD wurde ursprünglich für die Arbeit mit Python 2 entwickelt. Da Python 2 im Jahr 2020 das Ende seiner Lebensdauer erreicht hat, wird die zukünftige Entwicklung von FreeCAD ausschließlich mit Python 3 erfolgen, und Rückwärtskompatibilität wird nicht unterstützt.
-   Viele weitere Informationen über Python findest du im [offiziellen Python Tutorium](https   *//docs.python.org/3/tutorial/index.html) und in der [offiziellen Python Referenz](https   *//docs.python.org/3/reference/).


{{Top}}







[Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Python Code](Category_Python_Code.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Introduction to Python/de
