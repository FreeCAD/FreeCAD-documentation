# Installing on Windows/bg






Най-лесния начин за инсталиране на FreeCAD на Windows е да свалите инсталаторът по-долу.


{{DownloadWindowsStable}}

След като свалите .msi (Microsoft Installer) файлът кликнете 2 пъти върху него за да стартирате инсталацията.

По-доли има други опции за инсталация. Ако ви се струват трудни не се притеснявайте! За повечето потребители на Windows е достатъчно да инсталират със гореописаният инсталатор и да следват инструкциите в страницата **[Първи Стъпки](Getting_started/bg.md)**!

### Проста Инсталация с Microsoft Installer 

Най-лесния начин за инсталация на FreeCad е с гореописаният инсталатор. Тази страница описва различните опции на \"Microsoft Installer\".

The easiest way to **install FreeCAD on Windows** is by using the downloadable installer bundle above. This page describes the usage and features of the *NSIS Installer* for more installation options.

Ако искате да свалите или 64-битова версия, или нестабилна \"най-нова\" версия (development version) вижте страницата [Downloads](Downloads/bg.md).

## Chocolatey

However, it is highly recommended that you use a package manager such as Chocolatey to keep your software updated. You can installed Chocolatey following [these instructions](https://chocolatey.org/install) and then open a PowerShell terminal as admin and run:


```python
choco install freecad
```

every once in a while you can update your software with


```python
choco upgrade freecad
```

to get the latest version available on Chocolatey repository. If there are any issues with the chocolatey package, you may contact maintainers on [this page](https://chocolatey.org/packages/freecad).

### Инсталация през командния ред 

Използвайки командата \"msiexec.exe\" имате достъп то допълнителни опции като инсталация без човешка намеса и административна инсталация.

With the *msiexec.exe* command line utility, additional features such as non-interactive installation and administrative installation are available. See examples below.

#### Инсалация без човешка намеса 

Използвайки командния ред

With the command line


```python
msiexec /i FreeCAD<version>.msi
```

инсталацията може да се стартира от програма или скрипт. Допълнителни параметри могат да се добавят на края на командния ред. Например:


```python
msiexec /i FreeCAD-2.5.msi TARGETDIR=R:\FreeCAD25
```

#### Ограничен потребителски интерфейс 

С /q опциите на инсталаторът може да контролирате колко се показва на потребителя по време на инсталация. По точно:

The amount of user control permitted by the installer can be controlled with /q options:


<div class="mw-translate-fuzzy">

-   /qn - без интерефейс (не се показва нищо)
-   /qb - основен интерфейс - само малък прогрес бар
-   /qb! - Подобно на /qb, но без бутона Cancel
-   /qr - Улекотен интерфейс - показва всички прозорци които не изискват действия от потребителя (пропускаме всички прозорци с бутони)
-   /qn+ - Подобно на /qn, но показва диалогът \"Completed\" накрая
-   /qb+ - Подобно на /qb, но показва диалогът \"Completed\" накрая


</div>

#### Директория за Инсталация 

Опцията TARGETDIR определя директория където ще се инсталира FreeCAD. Например различен диск за инсталация може да бъде определен чрез TARGETDIR ето така:

The property TARGETDIR determines the root directory of the FreeCAD installation. For example, a different installation drive can be specified with


```python
TARGETDIR=R:\FreeCAD25
```

Директорията за инсталация по подразбиране (TARGETDIR) е \[WindowsVolume\\Programm Files\\\]FreeCAD.

#### Инсталация за всички потребители 

Ако добавите

Adding


```python
ALLUSERS=1
```

към командия ред, програмата ще се инсталира за всички потребители. По подразбиране инсталацията без човешка намеса (non-interactive) инсталира програмата само за настоящия потребител, а инсталацията с човешка намеса (interactive) предлага прозорец с избора който по подразбиране е за всички потребители (стига настоящия потребител да е администратор).

#### Избор на компоненти 

Някой опции позволяват определни части от FreeCAD да се инсталират, пре-инсталират или махат. Възможните избори за компоненти са:

A number of properties allow selection of features to be installed, reinstalled, or removed. The set of features for the FreeCAD installer is

-   DefaultFeature - инстлиране на програмата заедно с основните библиотеки
-   Documentation - инсталиране на документацията
-   Source code - инсталриане на сорс-кода на програмата
-   \... ToDo

Опцията ALL определя всички компоненти. Всеки компонент изисква поне DefaultFeature (тоест самата програма). Следните опции дават и по-голям контрол върху инсталацията на компоненти:

-   ADDLOCAL - списък от компоненти за инсталация на локалната машина
-   REMOVE - списък от компоненти за махане
-   ADDDEFAULT - списък от компоненти които се добавят в конфигурацията си по подразбиране (на локалната машина)
-   REINSTALL - списък от компоненти които да се преинсталират.
-   ADVERTISE - списък от компоненти за които да се направи \"advertisе\" инсталация.

За други опции моля вижте MSDN документацията.

Ако с тези опции добавим


```python
ADDLOCAL=Extensions
```

се инсталира само интерпретаторът (?) и се регистрират файловите разширения, но не се инсталира нищо друго.

### Деинсталация

С

With


```python
msiexec /x FreeCAD<version>.msi
```

FreeCAD може да се махне. Не е нужно да имате MSI файлът за деинсталация. Алтернативно, пакетът или кодът на продукта може да се даде. Можете да намерите кодът на продуктът като видите свойствата на Uninstall иконата която FreeCAD инсталира в Старт менюто.

### Административна Инсталация 

С

With


```python
msiexec /a FreeCAD<version>.msi
```

можете да направите \"административна\" (мрежова) инсталация. Файловете ще бъдат разопаковани в определената директория (която трябва да е споделена мрежова директория), но никакви други промени няма да бъдат извършени върху локалната машина (например REGISTRY няма да бъде променена). Също нов по-малък msi инсталатор ще бъде генериран в мрежовата директория. Други компютри в мрежата могат да направят локална инсталация използвайки този инсталатор (в бъдещи версии ще е възможно някой компоненти да останат върхи мрежовата директория, но да бъдат споделени от локалните инсталации).

В момента няма графичен интерфейс за административна инсталация и затова директорията за инсталация при административната инсталация трябва да бъде дадена на командния ред.

Няма специфична процедура за деинсталация на административна инсталация - просто изтрийте мрежовата директория стига никой друг компютър в мрежата да я ползва.

### Advertisement

С

With


```python
msiexec /jm FreeCAD<version>.msi
```

може да се рекламира FreeCAD на една машина (за реклама на специфичен потребител използвайте опцията /ju). Това ще постави иконите на FreeCAD в Старт менюто, и ще регистрира файловите разширения свързани с FreeCAD, без да инсталира самата програма. Първият път когато се старира програмата тя се инсталира.

В момента инсталаторът на FreeCAD поддържа само реклама чрез икони в старт менюто. Не поддържа реклама чрез други препратки(shortcuts).

### Автоматична инсталация на група машини 

Чрез Windows Group Policy е възможно автоматично да се инсталира FreeCAD на група машини, следвайки следните стъпки:

1.  Влезте в вашия domain controller
2.  Копирайте MSI файлът в споделена директория достъпна за всички машини в групата.
3.  Отворете MMC snapin \"Active Directory users and computers\"
4.  Отидете в групата компютри в които ще инсталирате FreeCAD
5.  Отворете Properties
6.  Отворете Group Policies
7.  Добавте нова policy и я редактирайте.
8.  В Computer Configuration/Software Installation, изберете New/Package
9.  Изберете MSI файлът използвайки неговия мрежов път(network path)
10. Можете да изберете дали искате FreeCAD да се деинсталира от компютър който напусне тази група.

With Windows Group Policy, it is possible to automatically install FreeCAD on a group of machines. To do so, perform the following steps:

1.  Log on to the domain controller
2.  Copy the MSI file into a folder that is shared with access granted to all target machines.
3.  Open the MMC snapin \"Active Directory users and computers\"
4.  Navigate to the group of computers that need FreeCAD
5.  Open Properties
6.  Open Group Policies
7.  Add a new policy, and edit it
8.  In Computer Configuration/Software Installation, choose New/Package
9.  Select the MSI file through the network path
10. Optionally, select that you want FreeCAD to be de-installed if the computer leaves the scope of the policy.

Разпространяването на така създадената group policy отнема време. За да сте сигурни че FreeCAD e успешно инсталиран трябва да рестартирате всички машини.

### Инсталация на Linux чрез Crossover Office 

Можете да инсталирате Windows весията на FreeCAD на Linux използвайки *CXOffice 5.0.1*. Просто пуснете *msiexec* от командния ред на CXOffice, след като сложите инсталаторът в директорията \"software\" (която е вързна с диск \"Y:\": в CXOffice)


```python
msiexec /i Y:\\software\\FreeCAD<version>.msi
```

FreeCAD работи но прозорците с OpenGL понякога не работят под [Wine](wikipedia:Wine_(software).md) подобно на други програми (например Google [SketchUp](wikipedia:SketchUp.md)).


```python
msiexec /i Y:\\software\\FreeCAD<version>.msi
```

FreeCAD is running, but it has been reported that the OpenGL display does not work, like with other programs running under [Wine](wikipedia:Wine_(software).md) i.e. Google [SketchUp](wikipedia:SketchUp.md).


<div class="mw-translate-fuzzy">


{{docnav|Feature list/bg|Install on Unix/bg}}


</div>



