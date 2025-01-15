# License/es
<div class="mw-translate-fuzzy">

### Licencias utilizadas 

He aquí las tres licencias bajo las que se publica FreeCAD:


</div>

FreeCAD uses two different licenses, one for the application itself, and one for the documentation:


<div class="mw-translate-fuzzy">


[Lesser General Public Licence (LGPL2+)](wikipedia_LGPL.md): Para las bibliotecas principales como se indica en los fichero .h y .cpp en src/App, src/Gui, sic/Base, y muchos de los [módulos](Workbenches/es.md) en src/Mod y para el ejecutable como se indica en los archivos .h y .cpp en el directorio src/main. Los iconos y otro material gráfico también son LGPL.
[General Public Licence (GPL2+)](wikipedia_GPL.md): Para los archivo de guión de Python que construyen los binarios como se indica en los archivos .py en src/Tools
[Open Publication Licence](wikipedia_Open_Publication_License.md): Para la documentacion en <http://free-cad.sourceforge.net/> salvo que se indique lo contrario por su autor


</div>

**[Creative Commons Attribution 3.0 License (CC-BY-3.0)](http://creativecommons.org/licenses/by/3.0/)** For the [documentation](https://wiki.freecad.org) and the [website](https://www.freecad.org).


<div class="mw-translate-fuzzy">

Mira el archivo [debian copyright file](http://free-cad.git.sourceforge.net/git/gitweb.cgi?p=free-cad/free-cad;a=blob;f=package/debian/copyright;h=a97cf019d020edba596f2d0f614c9b09ce546b0f;hb=HEAD) de FreeCAD, para tener más detalles sobre las licencias utilizadas en FreeCAD


</div>




<div class="mw-translate-fuzzy">

### Alcance de las licencias 


</div>

Below is a friendlier explanation of what the LGPL license means for you:

#### All users 


<div class="mw-translate-fuzzy">

#### Usuarios particulares 

Los usuarios particulares pueden utilizar FreeCAD de manera gratuita y pueden hacer básicamente cualquier cosa que quieran hacer con él \....


</div>

#### Professional users 


<div class="mw-translate-fuzzy">

#### Usuarios profesionales 

Pueden usar libremente FreeCAD para cualquier tipo de trabajo particular o profesional. Se puede personalizar la aplicación como lo deseen. Pueden escribir extensiones para FreeCAD en código abierto o cerrado. Son siempre dueños de sus datos, no están obligados a actualizar FreeCAD, ni cambiar el uso que hacen de FreeCAD. El uso de FreeCAD no les vincula a ningún tipo de contrato u obligación.


</div>

#### Open-source software developers 


<div class="mw-translate-fuzzy">

#### Desarrolladores de código abierto (Open Source) 

Puede utilizar FreeCAD como base para sus propios módulos de extensión para usos especiales. Pueden elegir entre GPL o LGPL para permitir, o no, el uso de su trabajo en software propietario.


</div>

#### Closed-source software developers 


<div class="mw-translate-fuzzy">

#### Desarrolladores profesionales 

Los desarrolladores profesionales pueden utilizar FreeCAD como base para sus propios módulos de extensión para propósitos especiales y no están obligados a hacer sus módulos en código abierto. Pueden utilizar todos los módulos que utilizan LGPL. Se les permite distribuir FreeCAD junto con su software propietario. Se dará todo el apoyo del autor(es) siempre y cuando exista una actitud de correspondencia recíproca. Si quieres vender tu módulo necesitas una licencia de Coin3d, de lo contrario estás obligado por esta biblioteca a que tu módulo sea de código abierto.


</div>

1\) You must clearly **inform your users that your application is using FreeCAD** and that FreeCAD is LGPL.

2\) The LGPL license also stipulate your users must be able to swap your modified FreeCAD component with the original FreeCAD equivalent. That is would be done by dynamically linking to the FreeCAD components, so users are allowed to change it. However, this is often hard to achieve by today\'s requirements. At FreeCAD, we understand that the important point here is to not restrict the freedom given to FreeCAD users by the LGPL license. So an equivalent to dynamic linking is to offer the choice to your users, by **making your users aware of the possibility to use FreeCAD for free**. This can be done in a number of ways.

If any of the two conditions above are unacceptable to you or cannot be implemented, then you must make your FreeCAD component LGPL too and release the source code with all the modifications you made to it.

There is a special case called **derivatives**, which is when you publish basically a \"rebranded\" version of FreeCAD. Derivatives which are not open-source are prohibited by the LGPL license. The FreeCAD community is active and efficient in finding rebranded versions, reporting them to the platforms where they were found and exposing them until they are taken down.

#### Files

The models and other files produced with FreeCAD are not subject to any license stated above, nor bound to any kind of restriction or ownership. Your files are truly yours. You can set the owner of the file and specify your own license terms for the files you produce inside FreeCAD, via menu File → Project Information.

## Logo

The FreeCAD logo is a [trademark owned by the FPA (FreeCAD project association)](https://fpa.freecad.org/documents/Trademark.pdf). This means the [FPA](https://fpa.freecad.org) is the sole body authorized to say who has the right to use the FreeCAD logo or not. The logo files, which are part of the FreeCAD source code or available elsewhere, for example on this wiki, are still all under the same licenses as the rest of FreeCAD (LGPL for the source code and Creative Commons for this wiki). You are still free to use the FreeCAD logo anywhere, on the same terms as the rest of FreeCAD, which means, basically, that you must use it to reference FreeCAD, and not use it, for example, for your own product, or any other way that is not referencing FreeCAD.

## Statement of the main developer 


<div class="mw-translate-fuzzy">

### Declaración del conservador/mantenedor 

Sé que el debate sobre la licencia *\"adecuada\"* para el código abierto ocupa una parte importante del ancho de banda de Internet y esa es la razón por la que, en mi opinión, también FreeCAD debería tener aquí algo sobre el tema.


</div>


<div class="mw-translate-fuzzy">

Elegí el [LGPL](http://en.wikipedia.org/wiki/LGPL) y [GPL](http://en.wikipedia.org/wiki/GPL) para el proyecto y conozco los pros y los contras sobre LGPL, de modo que te explicaré algunos motivos para haber tomado esta elección.


</div>

FreeCAD es un híbrido entre una biblioteca y una aplicación, de modo que la licencia GPL sería demasiado fuerte para eso. No permitiría escribir módulos comerciales para FreeCAD porque impediría la vinculación con las librerías base de FreeCAD. Te puedes preguntar ¿por qué no prescindir totalmente de los módulos comerciales? En este ámbito Linux es un buen ejemplo. ¿Tendría Linux tanto éxito si la biblioteca GNU de C fuese GPL y, por tanto, incapacitada para ligarse con las aplicaciones no-GPL? Y aunque me encanta la libertad de Linux, yo también quiero ser capaz de usar el magnífico controlador gráfico NVIDIA 3D. Entiendo y acepto que NVIDIA tenga razones para no querer regalar el código de su controlador. Todos trabajamos para empresas y necesitamos el sueldo, o por lo menos comer. Por todo lo anterior, para mí, una coexistencia de software de código abierto y de código cerrado no es algo malo, cuando obedece a las reglas de la LGPL. Me gustaría ver a alguien escribiendo un módulo de importación/exportación de formato Catia para FreeCAD, y que se distribuyese, ya fuera gratis o por dinero. No me gusta obligar a nadie a que ceda más de lo que quiere. Eso no sería bueno ni para él, ni para FreeCAD.

No obstante, esta decisión se ha tomado sólo para el sistema básico de FreeCAD. Todo escritor de un módulo de aplicación puede tomar su propia decisión.


{{Quote|Jürgen Riegel|15 October 2006}}


<div class="mw-translate-fuzzy">


{{docnav/es|Dialog creation/es|Tracker/es}}


</div>



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > License/es
