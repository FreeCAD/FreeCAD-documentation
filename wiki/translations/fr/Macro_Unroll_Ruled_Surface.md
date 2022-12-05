# Macro Unroll Ruled Surface/fr
{{Macro/fr
|Name=Macro Unroll Ruled Surface
|Description=La macro permet de dérouler la surface d'une forme et la placer dans une page.
|Author=Hervé B., heda
|Version=1.1
|Date=2022-07-24
|Download=[https://www.freecadweb.org/wiki/images/b/ba/Macro_Unroll_Ruled_Surface.png Icône de la barre d'outils]
}}

## Description

La macro permet de dérouler des surfaces réglées et de les dessiner sur une page.

<img alt="" src=images/Macro_unrollRuledSurface_00.png  style="width:480px;"> 
*Macro Unroll Ruled Surface*

## Installation

Disponible dans le [Gestionnaire des extensions](Std_AddonMgr/fr.md).

Voir aussi : [Macro for unrolling ruled surfaces](http://forum.freecadweb.org/viewtopic.php?f=17&t=4563&p=35737#p35737).

## Options

-   Nombre de génératrices.
-   Échelle manuelle ou automatique.
-   Format de page : A4/A3, cartouche (cf. modèles FreeCAD).
-   Regrouper les dessins sur une même page si possible.

![Macro_unrollRuledSurface](images/Macro_UnrollRuledSurface_start_form.png )

## Utilisation

1.  Sélectionnez les surfaces réglées.
2.  [Draft Désagrégez](Draft_Downgrade/fr.md) les.
3.  Sélectionnez les faces.
4.  Exécutez la macro.

## Script

La dernière version de la macro se trouve ici sur le wiki. Une version antérieure se trouve à l\'adresse [UnrollRuledSurface.FCMacro](https://github.com/FreeCAD/FreeCAD-macros/blob/master/Drawing/UnrollRuledSurface.FCMacro), mais le moyen le plus simple d\'installer cette macro est de passer par le <img alt="Std_AddonMgr" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire des extensions](Std_AddonMgr/fr.md).

Icône de la barre d\'outils ![](images/Macro_Unroll_Ruled_Surface.png )

**Macro_unrollRuledSurface.py**

    # -*- coding: utf-8 -*-
    #***************************************************************************
    #*                                                                         *
    #*   Copyright (c) 2013 - DoNovae/Herve BAILLY <hbl13@donovae.com>         *
    #*   Copyright (c) 2022 - heda <heda@fc-forum>                             *
    #*                                                                         *
    #*   This program is free software; you can redistribute it and/or modify  *
    #*   it under the terms of the GNU Lesser General Public License (LGPL)    *
    #*   as published by the Free Software Foundation; either version 2 of     *
    #*   the License, or (at your option) any later version.                   *
    #*   for detail see the LICENCE text file.                                 *
    #*                                                                         *
    #*   This program is distributed in the hope that it will be useful,       *
    #*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
    #*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
    #*   GNU Library General Public License for more details.                  *
    #*                                                                         *
    #*   You should have received a copy of the GNU Library General Public     *
    #*   License along with this program; if not, write to the Free Software   *
    #*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
    #*   USA                                                                   *
    #*                                                                         *
    #***************************************************************************
    __Name__ = 'Unroll Ruled Surface'
    __Comment__ = 'Unroll of a ruled surface and draw it on a page.'
    __Author__ = 'Hervé B., heda'
    __Version__ = '1.1'
    __Date__ = '2022-07-24'
    __License__ = 'LGPL-2.0-or-later'
    __Web__ = 'https://wiki.freecad.org/Macro_Unroll_Ruled_Surface'
    __Wiki__ = 'https://wiki.freecad.org/Macro_Unroll_Ruled_Surface'
    __Icon__ = ''
    __Help__ = ('Select ruled surfaces, Explode them (cf Draft menu), '
                'Select the surfaces, Execute the macro')
    __Status__ = ''
    __Requires__ = ''
    __Communication__ = ''
    __Files__ = ''

    __doc__ = """
    select a face, or several and run the macro.
    a shell/solid needs to be draft/downgraded to get the faces as separate objects

    the macro is intended to unroll lofted faces,
    function beyond that is (in current version) a bonus

    settings are not context aware, all settings not applicable are ignored.
    as example, using autoscaling ignores the scale-value in the form


    v1.1   (2022-07-24) py3/qt5 compat, cosmetic code changes, minor code tweaks,
           used gridlayout for form, added option to skip drawing,
           made new layout engine with techdraw,
           the drawing wb layout engine is now called "legacy"
    v1.0.1 (2019-02-01) - on git
    v1.0   (2013-09-14) - on wiki

    note:
    - unfolding sometimes works and sometimes not
    - not all surfaces are theoretically possible to unroll

    """

    import os
    from PySide import QtGui, QtCore
    import FreeCAD, FreeCADGui
    import Part, Draft

    Vector = FreeCAD.Base.Vector
    PrintMessage = FreeCAD.Console.PrintMessage
    PrintError = FreeCAD.Console.PrintError

    settings = dict()
    unroll_l = []
    dwgtpllegacy = 'Mod/Drawing/Templates'
    dwgtpl = 'Mod/TechDraw/Templates'


    #####################################
    ###   Functions
    #####################################

    def errorDialog(msg):
        diag = QtGui.QMessageBox(QtGui.QMessageBox.Critical, "Error Message", msg)
        diag.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        diag.exec_()

    def ending():
        PrintMessage("UnrollRuledSurface: end.\n")
        PrintMessage("===========================================\n")
        FreeCAD.ActiveDocument.recompute()


    def proceed():
        QtGui.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)

        PrintMessage("===========================================\n")
        PrintMessage("UnrollRuledSurface: start.\n")
        try:
            sts = lambda s: settings.get(s)

            file_name = sts("fname").text()
            pts_nbr = float(sts("dpts").text())
            makedwg = sts("mkdwg").isChecked()
            leglay = sts("legacylayout").isChecked()
            scale = float(sts("scale").text()) # ignored if autoscale is set
            scale_auto = sts("autoscale").isChecked()
            edge0 = sts("edge").checkedId() == -2
            a3 = sts("papersize").checkedId() == -3
            cartridge = sts("cartridge").isChecked()
            onedrawing = sts("groupdwg").isChecked()

            PrintMessage("UnrollRuledSurface.file_name: {}\n".format(file_name))
            PrintMessage("UnrollRuledSurface.pts_nbr: {}\n".format(pts_nbr))
            PrintMessage("UnrollRuledSurface.edge0: {}\n".format(edge0))
            PrintMessage("UnrollRuledSurface.makedwg: {}\n".format(makedwg))
            PrintMessage("UnrollRuledSurface.leglay: {}\n".format(leglay))
            PrintMessage("UnrollRuledSurface.scale_check: {}\n".format(scale_auto))
            PrintMessage("UnrollRuledSurface.scale: {}\n".format(scale))
            PrintMessage("UnrollRuledSurface.a3_check: {}\n".format(a3))
            PrintMessage("UnrollRuledSurface.cartridge: {}\n".format(cartridge))
            PrintMessage("UnrollRuledSurface.onedrawing: {}\n".format(onedrawing))
        except:
            msg = "UnrollRuledSurface: wrong inputs...\n"
            PrintError(msg)
            errorDialog(msg)
            QtGui.QApplication.restoreOverrideCursor()
            DialogBox.hide()
            ending()
            return

        QtGui.QApplication.restoreOverrideCursor()
        DialogBox.hide()
        unrollRS = unrollRuledSurface(file_name, pts_nbr, edge0)

        ## Get selection
        sel = FreeCADGui.Selection.getSelection()
        if not sel:
            PrintMessage("UnrollRuledSurface: no selection...\n")
            ending()
            return

        faceid = 0
        objnames_l, objnames0_l = [], []
        grp = FreeCAD.ActiveDocument.addObject("App::DocumentObjectGroup",
                                               "{}_objs".format(file_name))

        for objid, obji in enumerate(sel):
            shape = obji.Shape
            faces = shape.Faces
            for idx in range(len(faces)):
                msg = "UnrollRuledSurface.proceed: ObjId = {}, faceId = {}\n"
                PrintMessage(msg.format(objid, faceid))
                name = obji.Name
                if len(faces) > 1:
                    name = "{}.face_{}".format(name, idx)
                obj = unrollRS.unroll(faces[idx], name)
                obj.ViewObject.Visibility = not makedwg
                grp.addObject(obj)

            objnames_l.append([obj, name])
            objnames0_l.append([obji, name])
            faceid += 1

        if not makedwg:
            ending()
            return

        if leglay:
            idx = 0
            while len(objnames_l) > 0:
                draw = Drawing2dLegacy(scale, scale_auto, a3,
                                       cartridge, onedrawing,
                                       "{}_page{:02}".format(file_name, idx))
                objnames_l = draw.all2d(objnames_l)
                idx += 1
                msg = "UnrollRuledSurface: obj_l = {}\n"
                PrintMessage(msg.format(len(objnames_l)))

        else:
            draw = Drawing2d(scale, scale_auto, a3, cartridge)
            n = 4 if onedrawing else 1
            chunks = [objnames_l[i:i + n] for i in range(0, len(objnames_l), n)]
            for i, chunk in enumerate(chunks, start=1):
                draw.drawpage(chunk, "{}_page{:02}".format(file_name, i))

        ending()


    def close():
        DialogBox.hide()

    def getType(obj):
        return type(obj).__name__


    class unrollRuledSurface:
        """
        unroll ruled surfaces
        :file_name: ouput file
        :pts_nbr: nbr point of discretization
        """
        def __init__(self, file_name, pts_nbr, edge0):
            self.doc = FreeCAD.ActiveDocument
            self.file_name = file_name
            self.pts_nbr = int(pts_nbr)
            self.edge0 = edge0
            msg = "UnrollRuledSurface.unroll - file_name: {}, pts_nbr: {}\n"
            PrintMessage(msg.format(file_name, pts_nbr))


        def discretize(self, curve):
            """discretize a curve"""
            if getType(curve) in ('GeomLineSegment', 'GeomCircle'):
                sd = curve.discretize(self.pts_nbr)
            elif getType(curve) == 'GeomBSplineCurve':
                nodes = curve.getPoles()
                spline = Part.BSplineCurve()
                spline.buildFromPoles(nodes)
                sd = spline.discretize(self.pts_nbr)
            else:
                sd = curve.discretize(self.pts_nbr)
            return sd

        def nbpoles(self, curve):
            """find number of poles for a curve"""
            if getType(curve) == 'GeomLineSegment':
                nbpol=1
            elif getType(curve) == 'GeomBSplineCurve':
                nbpol=curve.NbPoles
            elif getType(curve) == 'GeomCircle':
                nbpol=2
            elif getType(curve) == 'GeomBezierCurve':
                nbpol=4
            else:
                nbpol=0

            msg = "UnrollRulrdSurface.nbpole {:s} = {:d}\n"
            PrintMessage(msg.format(getType(curve), nbpol))
            return nbpol

        def unroll(self, face, name):
            """unrolls a face composed of 2 to 4 edges"""
            nbredges = len(face.Edges)
            msg = "UnrollRuledSurface.unroll: Edge Nbr = {}\n"
            PrintMessage(msg.format(nbredges))

            if nbredges == 2:
                e1, e2 = face.Edges
                sd1 = e1.Curve.discretize(self.pts_nbr)
                sd2 = e2.Curve.discretize(self.pts_nbr)

            elif nbredges == 3:
                e1, _, e2 = face.Edges
                sd1 = e1.Curve.discretize(self.pts_nbr)
                sd2 = e2.Curve.discretize(self.pts_nbr)

            else:
                E0, E1, E2, E3, *_ = face.Edges
                ## Choose more complexe curve as edge
                nbpol0 = self.nbpoles(E0.Curve)
                nbpol1 = self.nbpoles(E1.Curve)
                nbpol2 = self.nbpoles(E2.Curve)
                nbpol3 = self.nbpoles(E3.Curve)
                msg = ("UnrollRuledSurface.unroll: nbpol0= {:d}, nbpol1= {:d},"
                       " nbpol2= {:d}, nbpol3= {:d}\n")
                PrintMessage(msg.format(nbpol0, nbpol1, nbpol2, nbpol3))

                if self.edge0:
                    e1, e2 = E0, E2
                    v = self.discretize(E1)
                    v0, v1 = v[0], v[self.pts_nbr-1]
                else:
                    e1, e2 = E1, E3
                    v = self.discretize(E2)
                    v0, v1 = v[0], v[self.pts_nbr-1]

                sd1 = self.discretize(e1)
                sd2 = self.discretize(e2)
                ## Reverse if curves cross over
                if not (sd2[0].__eq__(v0) or not sd2[0].__eq__(v1)):
                    sd2.reverse()

            ## Create a polygon object and set its nodes
            devlxy_l = self.devlxyz(sd1, sd2)
            msg = "UnrollRuledSurface.unroll: size devlxy_l: {}\n"
            PrintMessage(msg.format(len(devlxy_l)))
            p = self.doc.addObject("Part::Polygon", name)
            p.Nodes = devlxy_l
            self.doc.recompute()
            FreeCADGui.ActiveDocument.ActiveView.fitAll()
            return p

        def vect_copy(self, vect):
            """returns copy of vector"""
            return vect.add(Vector())

        def vect_cos(self, vect1, vect2):
            """returns cosine angle between 2 vectors"""
            return vect1.dot(vect2) / vect1.Length / vect2.Length

        def vect_sin(self, vect1, vect2):
            """returns absolute sinus angle between 2 vectors"""
            v = Vector()
            v.x = vect1.y * vect2.z - vect1.z * vect2.y
            v.y = vect1.z * vect2.x - vect1.x * vect2.z
            v.z = vect1.x * vect2.y - vect1.y * vect2.x
            return v.Length / vect1.Length / vect2.Length

        def devlxyz(self, vect1, vect2):
            """
            unrolls a face composed of 4 edges
            args: vect1, vect2 --> 2 edges of the shape
            returns: dvlxy
            """
            lenv1, lenv2 = len(vect1), len(vect2)
            if lenv1 != lenv2 or lenv1 != self.pts_nbr or lenv2 != self.pts_nbr:
                msg = ("UnrollRuledSurface.devlxyz: incompatility of sizes vect1,"
                       " vect2, pts_nbr: ({}, {}, {})\n")
                PrintError(msg.format(lenv1, lenv2, self.pts_nbr))
                errorDialog(msg)

            devlxy_l, devl1xy_l, devl2xy_l = [], [], []
            errormax = 0.0
            ## Init unroll
            ## AB
            a1b1 = vect2[0].sub(vect1[0])
            oa1 = Vector(0, 0, 0)
            devl1xy_l.append(oa1) #A1
            ob1 = Vector(a1b1.Length, 0, 0)
            devl2xy_l.append(ob1) #B1
            #self.draw_line(devl1xy_l[0], devl2xy_l[0])
            #self.draw_line(vect1[0], vect2[0])
            for j in range(1, self.pts_nbr):

                ## AB
                ab = vect2[j-1].sub(vect1[j-1])
                #self.draw_line(vect1[j-1], vect2[j-1])

                ## AC
                ac = vect1[j].sub(vect1[j-1])

                ## BD
                bd = vect2[j].sub(vect2[j-1])

                ## CD
                cd = vect2[j].sub(vect1[j])

                ## A1B1 in unroll plan
                a1b1 = devl2xy_l[j-1].sub(devl1xy_l[j-1])
                a1b1n = self.vect_copy(a1b1)
                a1b1n.normalize()
                a1b1on = Vector(-a1b1n.y, a1b1n.x, 0)

                ## A1C1
                cosalp = self.vect_cos(ab, ac)
                sinalp = self.vect_sin(ab, ac)
                a1c1 = self.vect_copy(a1b1n)
                a1c1.multiply(cosalp * ac.Length)
                v = self.vect_copy(a1b1on)
                v.multiply(sinalp * ac.Length)
                a1c1 = a1c1.add(v)
                oa1 = self.vect_copy(devl1xy_l[j-1])
                oc1 = oa1.add(a1c1)
                devl1xy_l.append(oc1)

                ## B1D1
                cosalp = self.vect_cos(ab, bd)
                sinalp = self.vect_sin(ab, bd)
                b1d1 = self.vect_copy(a1b1n)
                b1d1.multiply(cosalp * bd.Length)
                v = self.vect_copy(a1b1on)
                v.multiply(sinalp * bd.Length)
                b1d1 = b1d1.add(v)
                ob1 = self.vect_copy(devl2xy_l[j-1])
                od1 = ob1.add(b1d1)
                devl2xy_l.append(od1)

                ## Draw generatrice
                #self.draw_line(devl1xy_l[j], devl2xy_l[j])
                c1d1 = devl2xy_l[j].sub(devl1xy_l[j])
                if ab.Length != 0:
                    abl = ab.Length
                    errormax = max(errormax, abs(abl - c1d1.Length) / abl)

            msg = "UnrollRuledSurface Error cd,c1d1: {:.1f} %\n"
            PrintMessage(msg.format(errormax*100))

            ## Close polygone
            devlxy_l = devl1xy_l
            devl2xy_l.reverse()
            devlxy_l.extend(devl2xy_l)
            v = Vector()
            devlxy_l.append(v)

            return devlxy_l


        def draw_line(self, vect0, vect1):
            """draws a Part.Line between vect0 & vect1"""
            l = Part.LineSegment()
            l.StartPoint = vect0
            l.EndPoint = vect1
            self.doc.addObject("Part::Feature", "Line").Shape = l.toShape()


    class Scale:
        """keeps autoscaling to integers"""
        def __init__(self, scale):
            self.scale = scale if scale >= 1 else 1 / scale
            self.scale = int(self.scale)
            self.inverted = scale >= 1

        def get(self):
            if self.inverted:
                return self.scale, '{}:1'.format(self.scale)
            else:
                return 1/self.scale, '1:{}'.format(self.scale)


    class Drawing2d:
        """
        TechDraw wb layout engine, diffeent logic compared to drawing wb layout.
        serves basic purpose...
        """
        def __init__(self, scale, scale_auto, a3, cartridge):

            self.a3 = a3
            self.scale = scale
            self.scale_auto = scale_auto
            self.cartridge = cartridge
            if a3:
                self.WH = 420, 297
            else:
                self.WH = 297, 210
            self.doc = FreeCAD.ActiveDocument


        def _mkquadrants(self, nbr):
            """centers of quadrants w/o margin"""
            w, h = self.WH
            w2, h2 = w/2, h/2
            w4, h4 = w/4, h/4

            q = {1: [[w, h], [[w2, h2]]],
                 2: [[w2, h], [[w2 - w4, h2], [w2 + w4, h2]]],
                 3: [[w2, h2], [[w2 - w4, h2 + h4], [w2 + w4, h2 + h4],
                                [w2 - w4, h2 - h4]]],
                 4: [[w2, h2], [[w2 - w4, h2 + h4], [w2 + w4, h2 + h4],
                                [w2 - w4, h2 - h4], [w2 + w4, h2 - h4]]]}
            return q.get(nbr)


        def newPage(self, doc, page_name):
            freecad_dir = os.path.join(FreeCAD.getResourceDir(), dwgtpl)
            page = doc.addObject('TechDraw::DrawPage', page_name)
            template = self.doc.addObject('TechDraw::DrawSVGTemplate', 'Template')
            size = 'A3' if self.a3 else 'A4'
            frame = 'TD' if self.cartridge else '_blank'
            template.Template = freecad_dir + '/{}_Landscape{}.svg'.format(size, frame)
            page.Template = template
            return page

        def drawpage(self, faces, page_name):
            """max 4 per page, simple layout with halfs or quadrants"""
            page = self.newPage(self.doc, page_name)
            [W, H], ll = self._mkquadrants(len(faces))
            for [face, name], [x0, y0] in zip(faces, ll):
                bb = face.Shape.BoundBox
                xr, yr = W / bb.XLength, H / bb.YLength
                adjust = 0.7 if self.cartridge else 0.85
                scale = min(xr, yr) * adjust if self.scale_auto else self.scale
                scale, scr = Scale(scale).get()
                bb.scale(scale, scale, 1) # unrolled faces in xy-plane

                TopView = self.doc.addObject('TechDraw::DrawViewPart', name + ' view')
                page.addView(TopView)
                TopView.Source = face
                TopView.Direction = (0, 0, 1)
                TopView.XDirection = (1, 0, 0)
                TopView.Scale = scale
                TopView.X = x0
                TopView.Y = y0

                Text = self.doc.addObject('TechDraw::DrawViewAnnotation', name + ' txt')
                page.addView(Text)
                Text.Text = '{} [{}]'.format(name, scr)
                Text.recompute() # for size
                Text.X = x0
                yt = y0 - bb.YLength / 2 - Text.TextSize.Value * 1.5
                Text.Y = max(1, yt)

            self.doc.recompute()
            page.ViewObject.doubleClicked()
            FreeCADGui.runCommand('TechDraw_ToggleFrame', 0)


    class Drawing2dLegacy:
        """
        makes 2d drawing with Drawing wb (original layout engine, now legacy)
        - obj_l: list of objects
        """
        ## untouched logic in v1.1
        def __init__(self, scale, scale_auto, a3, cartridge, onedrawing, page_str):
            self.TopX_H = self.TopY_H = 0
            self.TopX_V = self.TopY_V = 0
            self.TopX_Hmax = self.TopY_Hmax = 0
            self.TopX_Vmax = self.TopY_Vmax = 0
            self.a3 = a3
            self.scale = scale
            self.scale_auto = scale_auto
            self.cartridge = cartridge
            self.onedrawing = onedrawing
            self.marge = 6
            if self.a3:
                self.L, self.H = 420, 297
            else:
                self.L, self.H = 297, 210
            self.name = page_str

        def newPage(self):
            freecad_dir = os.path.join(FreeCAD.getResourceDir(), dwgtpllegacy)
            doc = FreeCAD.ActiveDocument
            page = doc.addObject('Drawing::FeaturePage', self.name)
            size = 'A3' if self.a3 else 'A4'
            frame = '' if self.cartridge else '_plain'
            page.Template = freecad_dir + '/{}_Landscape{}.svg'.format(size, frame)
            return page


        def all2d(self, objname_l):
            obj1_l = []
            for objid in range(len(objname_l)):
                if objid == 0 or not self.onedrawing:
                    page = self.newPage()
                obj1_l.extend(self.done(objid, objname_l[objid]))
            return obj1_l

        def done(self, idx, objname):
            obj_l = []
            obj, objname = objname
            marge = self.marge
            bb = obj.Shape.BoundBox
            xmax = bb.XMax - bb.XMin
            ymax = bb.YMax - bb.YMin

            if ymax > xmax:
                Draft.rotate(obj, 90)
            Draft.move(obj, Vector(-bb.XMin, -bb.YMin, 0))
            xmax = bb.XMax - bb.XMin
            ymax = bb.YMax - bb.YMin

            scale = min((self.L-4 * marge) / xmax, (self.H-4 * marge) / ymax)

            if (not self.scale_auto) or self.onedrawing:
                scale = self.scale

            PrintMessage("UnrollRuledSurface.drawing: scale= {:.2f}\n".format(scale))


            if idx == 0 or not self.onedrawing:
                PrintMessage("Drawing2d: init\n")
                TopX = self.TopX_H = marge * 2
                TopY = self.TopY_H = marge * 2
                self.TopX_H = self.TopX_H + xmax * scale + marge
                self.TopY_H = self.TopY_H
                self.TopX_Hmax = max(self.TopX_Hmax, self.TopX_H)
                self.TopY_Hmax = max(self.TopY_Hmax,
                                     self.TopY_H + ymax * scale + marge)
                self.TopX_Vmax = max(self.TopX_Vmax, self.TopX_Hmax)
                self.TopX_V = max(self.TopX_Vmax, self.TopX_V)
                self.TopY_V = marge * 2

            elif self.onedrawing:
                if self.TopX_H + xmax * scale < self.L:
                    if self.TopY_H + ymax * scale + marge * 2 < self.H:
                        ## H Add at right on same horizontal line
                        PrintMessage("Drawing2d: horizontal\n")
                        TopX, TopY = self.TopX_H, self.TopY_H
                        self.TopX_H = self.TopX_H + xmax * scale + marge
                        self.TopX_Hmax = max(self.TopX_Hmax, self.TopX_H)
                        self.TopY_Hmax = max(self.TopY_Hmax,
                                             self.TopY_H + ymax * scale + marge)
                        self.TopX_Vmax = max(self.TopX_Hmax, self.TopX_Vmax)
                        self.TopX_Vmax = max(self.TopX_Vmax, self.TopX_Hmax)
                        self.TopX_V = max(self.TopX_Vmax, self.TopX_V)

                    else:
                        ## V Add at right on same horizontal line
                        PrintMessage("Drawing2d: vertival\n")
                        if (self.TopX_V + ymax * scale + 2 * marge < self.L
                            and self.TopY_V + xmax * scale + 2 * marge < self.H):
                            Draft.rotate(obj, 90)
                            Draft.move(obj, Vector(-bb.XMin, -bb.YMin, 0))
                            x0 = xmax; xmax = ymax; ymax = x0
                            self.TopX_V = max(self.TopX_Vmax, self.TopX_V)
                            TopX, TopY = self.TopX_V, self.TopY_V
                            self.TopX_V = self.TopX_V + xmax * scale + marge
                            self.TopY_Vmax = max(self.TopY_Vmax,
                                                 self.TopY_V + ymax * scale + marge)

                        else:
                            obj_l.append([obj, self.name])
                            return obj_l

                else:
                    ## H Carriage return
                    if self.TopY_Hmax + ymax * scale + self.marge*2 < self.H:
                        msg = "Drawing2d: carriage return: {} > {}\n"
                        PrintMessage(msg.format(self.TopY_H + ymax * scale, self.H))
                        TopX = self.marge * 2
                        TopY = self.TopY_Hmax
                        self.TopX_H = TopX + xmax * scale + self.marge
                        self.TopY_H = TopY
                        self.TopX_Hmax = max(self.TopX_Hmax, self.TopX_H)
                        self.TopY_Hmax = self.TopY_Hmax + ymax * scale + self.marge
                        self.TopX_Vmax = max(self.TopX_Vmax, self.TopX_Hmax)
                        self.TopX_V = max(self.TopX_Vmax, self.TopX_V)
        
                    else:
                        ## V Add at right on same horizontal line
                        msg = "Drawing2d: vertival: {} , {}\n"
                        PrintMessage(msg.format(self.TopX_V, self.TopX_Vmax))
                        if (self.TopX_V + ymax * scale + 2 * marge < self.L
                            and self.TopY_V + xmax * scale + 2 * marge < self.H):
                            Draft.rotate(obj, 90)
                            Draft.move(obj, Vector(-bb.XMin, -bb.YMin, 0))
                            x0 = xmax; xmax = ymax; ymax = x0
                            TopX, TopY = self.TopX_V, self.TopY_V
                            self.TopX_V = self.TopX_V + xmax * scale + marge
                            self.TopY_Vmax = max(self.TopY_Vmax,
                                                 self.TopY_V + ymax * scale + marge)
        
                        else:
                            obj_l.append([obj, objname])
                            return obj_l

            doc = FreeCAD.ActiveDocument
            page = doc.getObject(self.name)

            Text = doc.addObject('Drawing::FeatureViewAnnotation', f"{objname}_txt")
            Text.Text = objname
            Text.X = TopX + xmax * scale / 2
            Text.Y = TopY + ymax * scale / 2
            Text.Scale = 2

            TopView = doc.addObject('Drawing::FeatureViewPart', objname)
            TopView.Source = obj
            TopView.Direction = (0, 0, 1)
            TopView.Rotation = 0
            TopView.X = TopX
            TopView.Y = TopY
            TopView.ShowHiddenLines = False
            TopView.Scale = scale
            page.addObject(TopView)
            page.addObject(Text)
            doc.recompute()
            page.ViewObject.doubleClicked()
            return obj_l



    #####################################
    ###   Dialog Box
    #####################################

    DialogBox = QtGui.QDialog()
    DialogBox.setWindowTitle("UnrollRuledSurface")
    la = QtGui.QGridLayout(DialogBox)
    la.setSpacing(7)
    buttonGrpEdge = QtGui.QButtonGroup(DialogBox)
    buttonGrpFormat = QtGui.QButtonGroup(DialogBox)

    cols = 4
    la.addWidget(QtGui.QLabel("File Name"), 0, 0, 1, cols)
    fname = QtGui.QLineEdit("UnrollSurface")
    la.addWidget(fname, 1, 0, 1, cols)

    la.addWidget(QtGui.QLabel("Discretization Points Nbr"), 2, 0, 1, cols)
    dpts = QtGui.QLineEdit("30")
    la.addWidget(dpts, 3, 0, 1, 2)

    ###
    la.addWidget(QtGui.QLabel("Generatrices from edge:"), 4, 0, 1, 2)
    edgezero = QtGui.QRadioButton("0 to 3")
    la.addWidget(edgezero, 4, 2)
    edgeone = QtGui.QRadioButton("1 to 4")
    la.addWidget(edgeone, 4, 3)
    buttonGrpEdge.addButton(edgezero); buttonGrpEdge.addButton(edgeone)
    edgezero.setChecked(True)

    ###
    mkdwg = QtGui.QCheckBox("Make drawing")
    mkdwg.setChecked(True)
    la.addWidget(mkdwg, 5, 0, 1, 2)

    legacylayout = QtGui.QCheckBox("Legacy layout")
    legacylayout.setChecked(False)
    la.addWidget(legacylayout, 5, 2, 1, 2)


    ###
    autoscale = QtGui.QCheckBox("Auto scale")
    autoscale.setChecked(True)
    la.addWidget(autoscale, 6, 0, 1, 2)

    la.addWidget(QtGui.QLabel("Scale"), 6, 2)
    scale = QtGui.QLineEdit("1")
    la.addWidget(scale, 6, 3)

    ###
    la.addWidget(QtGui.QLabel("Paper size:"), 7, 0, 1, 2)
    rba4 = QtGui.QRadioButton("A4")
    la.addWidget(rba4, 7, 2)
    rba3 = QtGui.QRadioButton("A3")
    la.addWidget(rba3, 7, 3)
    buttonGrpFormat.addButton(rba4); buttonGrpFormat.addButton(rba3)
    rba4.setChecked(True)

    ###
    cartridge = QtGui.QCheckBox("Cartridge")
    cartridge.setChecked(False)
    la.addWidget(cartridge, 8, 0, 1, 2)

    groupdwg = QtGui.QCheckBox("Group drawings in page")
    groupdwg.setChecked(True)
    la.addWidget(groupdwg, 8, 2, 1, 2)

    ###
    box = QtGui.QDialogButtonBox(DialogBox)
    box.setOrientation(QtCore.Qt.Horizontal)
    box.setStandardButtons(QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
    la.addWidget(box, 9, 0, 1, cols)

    ###
    settings.update(dict(fname=fname, dpts=dpts, edge=buttonGrpEdge,
                         mkdwg=mkdwg, legacylayout=legacylayout,
                         autoscale=autoscale, scale=scale,
                         papersize=buttonGrpFormat,
                         cartridge=cartridge, groupdwg=groupdwg))

    QtCore.QObject.connect(box, QtCore.SIGNAL("accepted()"), proceed)
    QtCore.QObject.connect(box, QtCore.SIGNAL("rejected()"), close)
    QtCore.QMetaObject.connectSlotsByName(DialogBox)
    DialogBox.show()



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Unroll Ruled Surface/fr
