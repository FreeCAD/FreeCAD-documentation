# Manual:Creating renderings/ru
{{Manual:TOC}}


<div class="mw-translate-fuzzy">

В разговорах компьютерщиков слово [рендеринг](https://ru.wikipedia.org/wiki/Рендеринг) означает красивое изображение, получаемое из трёхмерной модели. Разумеется, мы можем сказать что трёхмерный вид FreeCAD уже красив. Однако всякий, кто видел современные голливудские картины, знает, что с помощью компьютера возможно создавать изображения, которые почти неотличимы от фотографий.


</div>


<div class="mw-translate-fuzzy">

Разумеется, создание фотореалистичных изображений требует большой работы, кроме приложений, предлагающих специффичные инструменты для этой задачи, вроде точной настройки материалов и света. Поскольку FreeCAD это приложение для технического моделирования, он не имеет каких-либо совершенных инструментов рендеринга.


</div>


<div class="mw-translate-fuzzy">

По счастью, мир открытых исходников предлагает много приложений для создания фотореалистичных изображений. Наиболее известный из них, вероятно, [Blender](http://www.blender.org), очень популярный и широко используемый в создании фильмов и игр. Объёмные модели могут быть легко экспортированы из FreeCAD в Blender, где Вы можете добавить реалистичные материалы и освещение, и создать окончательные изображения или даже анимацию.


</div>


<div class="mw-translate-fuzzy">

Некоторые другие инструменты визуализации с открытым исходным кодом предназначены для использования в других приложениях и обеспечивают выполнение сложных вычислений для создания реалистичных изображений. Из этих инструментов FreeCAD с помощью [верстака Raytracing](Raytracing_Workbench/ru.md) может использовать два: [POV-Ray](https://ru.wikipedia.org/wiki/POV-Ray) и [Luxrender](https://ru.wikipedia.org/wiki/LuxRender). POV-Ray - очень старый проект, считающийся классическим движком [трассировки лучей](https://ru.wikipedia.org/wiki/Трассировка_лучей), в то время как Luxrender намного новее и производит [рендеринг без допущений](https://en.wikipedia.org/wiki/Рендеринг_без_допущений). У обоих есть свои сильные и слабые стороны, в зависимости от типа изображения, которое нужно визуализировать. Лучший способ узнать это посмотреть на примеры на веб-сайте каждого движка.


</div>



### Установка


<div class="mw-translate-fuzzy">

Чтобы можно было использовать в FreeCAD верстак Raytracing, одно из этих приложений визуализации должно быть установлено в вашей системе. Обычно это просто. У обоих или есть установщики для многих платформ, или они уже включены в репозитории большинства дистрибутивов Linux.


</div>


<div class="mw-translate-fuzzy">

Когда POV-Ray или Luxrender установлен, требуется установить путь к их исполняемому файлу в настройках FreeCAD. Это обычно требуется только в Windows или Mac. В Linux FreeCAD возьмёт их из стандартного местоположения. Положение исполняемых файлов povray или luxrender можно найти поиском файлов povray (или povray.exe в Windows) и luxrender (или luxrender.exe в Windows).


</div>

![](images/FreeCAD_Render_Preferences.png )



### Визуализация с помощью PovRay 


<div class="mw-translate-fuzzy">

Мы будем использовать стол, смоделированный в главе, посвящённой [традиционному моделированию](Manual:Traditional_modeling,_the_CSG_way/ru.md), для создания фотореалистичных изображений с помощью PovRay и Luxrender.


</div>


<div class="mw-translate-fuzzy">

-   Начнём с загрузки файла table.FCStd, который был создан ранее или загружен по ссылке внизу этой главы.
-   Нажмём маленькую стрелку вниз возле кнопки <img alt="" src=images/Raytrace_New.svg  style="width:16px;"> [New Povray project](Raytracing_New/ru.md), выбрав шаблон **RadiosityNormal**.
-   Появится сообщение, предупреждающее что текущий трёхмерный вид не в перспективной проекции, и визуализация будет выглядеть иначе. Скорректируйте это, выбрав **Нет**, затем выбрав в меню **Вид-\>Перспективная проекция** и выбрав шаблон RadiosityNormal снова.
-   Вы можете так же попробовать другие шаблоны после создания нового проекта, просто редактируя параметр **Template**.
-   Новый проект теперь создан:


</div>

![](images/FreeCAD_Render_Project.png )


<div class="mw-translate-fuzzy">

-   Новый проект получает точку зрения трёхмерного вида в момент нажатия кнопки. Мы можем в любой момент изменить вид и обновить сохранённую в проекте Povray точку зрения, нажав кнопку <img alt="" src=images/Raytrace_ResetCamera.svg  style="width:16px;"> [Сброс камеры](Raytracing_ResetCamera/ru.md).
-   Верстак Raytracing работает так же, как и [Верстак Drawing](Drawing_Workbench/ru.md): как только папка проекта создана, мы должны добавить в него **Views** нашего проекта. Мы можем сделать это выбором всех объектов, составляющих стол, и нажав кнопку <img alt="" src=images/Raytrace_NewPartSegment.svg  style="width:16px;"> [Вставить деталь](Raytracing_InsertPart/ru.md):


</div>

![](images/FreeCAD_Render_Bodies.png )


<div class="mw-translate-fuzzy">

-   Вид получает значения цвета и прозрачности из оригинальных частей, но вы можете, при желании, изменить это в параметрах каждого вида.
-   Теперь мы готовы создать нашу первую визуализацию Povray. Нажмём кнопку <img alt="" src=images/Raytrace_Render.svg  style="width:16px;"> [Визуализировать](Raytracing_Render/ru.md).
-   Примечание для пользователей Windows: при получении (в Povray) предупреждения о том, что «I/O restrictions prohibit write access \...»
    -   откройте Povray
    -   выберите «\"Options \> Script I/O Restrictions\"» и убедитесь, что для него установлено значение «No Restrictions»
    -   повторить рендеринг
-   У Вас запросят имя и путь к файлу с изображением в формате .png, который создаст Povray.
-   Теперь Povray запустится и вычислит изображение.
-   Когда это будет готово, для закрытия окна Povray кликните изображение. Полученное изображение будет загружено в FreeCAD:


</div>

![](images/FreeCAD_Render_Result.png )


<div class="mw-translate-fuzzy">

-   Визуализация с помощью Luxrender работает примерно так же. Мы можем оставить наш файл открытым и создать новый проект Luxrender в том же файле, или перезагрузить его, чтобы начать с нуля.
-   Нажмём маленькую стрелку вниз около кнопки <img alt="" src=images/Raytrace_Lux.svg  style="width:16px;"> [New Luxrender project](Raytracing_Lux/ru.md) и выберем шаблон **LuxOutdoor**.
-   Выберем все компоненты стола. Если у Вас в документе имеется проект Povray, выделите так же сам проект Luxrender, чтобы вид, созданный на следующем шаге, не выбрал по ошибке неправильный проект.
-   Нажмите кнопку <img alt="" src=images/Raytrace_NewPartSegment.svg  style="width:16px;"> [Вставить деталь](Raytracing_InsertPart/ru.md).
-   Выделите проект Luxrender, и нажмите кнопку <img alt="" src=images/Raytrace_Render.svg  style="width:16px;"> [Render](Raytracing_Render/ru.md).
-   Luxrender работает не так, как Povray. Когда Вы запустите визуализатор, приложение Luxrender откроется и немедленно начнёт рендеринг:


</div>

**Загрузки**

-   Модель стола: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/table.FCStd>
-   Файл, полученный в ходе упражнения: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/render.FCStd>

**Читать далее**


<div class="mw-translate-fuzzy">

-   [Верстак Raytracing (рендеринга)](Raytracing_Workbench/ru.md)
-   [Blender](http://www.blender.org)
-   [POV-Ray](http://www.povray.org)
-   [Luxrender](https://ru.wikipedia.org/wiki/LuxRender)


</div>




{{Raytracing Tools navi}}



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Raytracing](Category_Raytracing.md) > Manual:Creating renderings/ru
