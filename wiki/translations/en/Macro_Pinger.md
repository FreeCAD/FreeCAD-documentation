# Macro Pinger/en
{{Macro
|Name=Macro Pinger
|Icon=Pinger_Icon.svg
|Description=Use this macro to easily ping users on the FreeCAD forum. Select the user from the combo box, click Ping, paste code into the forum post. You may add new users.
|Author=TheMarkster
|Version=1.81
|Date=2022.03.28
|FCVersion=0.19
|Download=[https://wiki.freecadweb.org/images/6/67/Pinger_Icon.svg ToolBar Icon]
|SeeAlso=[Macro Snip](Macro_Snip.md)
}}

## Description

Use this macro to ping another user on the forum so that user gets a notification. Pinging requires knowing the username exactly and the user id number. You also must know the syntax required to produce the ping. It\'s very user-unfriendly, to say the least. In comes the Pinger macro to save the day. Run the macro, select the user you wish to ping, click the **Ping** button, copy-paste the code into the forum post.

<img alt="" src=images/Pinger_scr.png  style="width:600px;"> 
*Pinger screenshot*

## Parameters

The Macro supports user parameters, which are used for the added users list. It is in User parameter:Plugins/Pinger as \"AddedUsers\", a string containing the string representation of a Python dictionary.

## Script

ToolBar icon ![](images/Pinger_Icon.svg )

**Macro_Snip.FCMacro**


{{MacroCode|code=
# -*- coding: utf-8 -*-
## Pinger macro v1.8
## By: TheMarkster
#  2022.03.28
## Aids in pinging users on the forum
## Select the user from the list and paste clipboard contents into the forum
__version__ = "1.81"
from PySide import QtGui,QtCore
import FreeCADGui as Gui
import FreeCAD
import json

#werner's code to get about info
class AboutInfo(QtCore.QObject):
    def __init__(self):
        super(AboutInfo, self).__init__()

    def eventFilter(self, obj, ev):
        if obj.metaObject().className() == "Gui::Dialog::AboutDialog" and\
        ev.type() == ev.ChildPolished and\
        hasattr(obj, 'on_copyButton_clicked'):
            obj.on_copyButton_clicked()
            QtGui.QApplication.instance().postEvent(obj, QtGui.QCloseEvent())
        return False

class PingerDlg:
    def __init__(self,parent=Gui.getMainWindow()):
        self.dict1 = {}
        self.setupDict1()
        self.pg = FreeCAD.ParamGet("User parameter:Plugins/Pinger")
        self.addedDict = {}
        self.fetchAdded() #updates self.addedDict
        self.fullDict = {}
        self.recentDict = {}
        self.cbUsers = QtGui.QComboBox()
        self.cbUsers.setEditable(True)
        self.cbUsers.lineEdit().returnPressed.connect(self.onReturnPressed)
        self.cbUsers.setToolTip("Type in a new name to add a new user, then click Ping/Add or press Enter.")
        self.form = QtGui.QDialog(parent, QtCore.Qt.Tool)
        self.form.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        self.form.setWindowTitle("Pinger v"+__version__)
        self.form.setWindowIcon(QIconFromXPMString(__icon__))
        self.layout = QtGui.QVBoxLayout()
        self.form.setLayout(self.layout)
        topLine = QtGui.QHBoxLayout()
        iconBtn = QtGui.QPushButton()
        iconBtn.setIcon(QIconFromXPMString(__icon__))
        iconBtn.clicked.connect(self.information)
        topLine.addWidget(iconBtn)
        iconBtn.setMaximumWidth(48)
        self.layout.addLayout(topLine)
        usersLabel = QtGui.QLabel("Users: ")
        usersLabel.setMaximumWidth(100)
        topLine.addWidget(usersLabel)
        topLine.addWidget(self.cbUsers)
        self.pingBtn = QtGui.QPushButton("Ping/Add")
        self.pingBtn.setToolTip("Ping this user or add the user if not already in database.")
        topLine.addWidget(self.pingBtn)
        self.pingBtn.clicked.connect(self.onPingBtnClicked)
        secondLine = QtGui.QHBoxLayout()
        self.layout.addLayout(secondLine)
        self.aboutBtn = QtGui.QPushButton("About info")
        self.aboutBtn.setToolTip("Copy FreeCAD about information to clipboard")
        self.aboutBtn.clicked.connect(self.getAboutInfo)
        secondLine.addWidget(self.aboutBtn)
        self.editBtn = QtGui.QPushButton("Edit user id")
        self.editBtn.clicked.connect(self.onEditBtnClicked)
        secondLine.addWidget(self.editBtn)
        self.delBtn = QtGui.QPushButton("Remove user")
        self.delBtn.setToolTip("Remove user from added user list")
        self.delBtn.clicked.connect(self.onDelBtnClicked)
        secondLine.addWidget(self.delBtn)
        self.sortCheckBox = QtGui.QCheckBox("Sorted")
        secondLine.addWidget(self.sortCheckBox)
        self.sortCheckBox.stateChanged.connect(self.populateUsers)
        self.msgBox = QtGui.QPlainTextEdit()
        self.layout.addWidget(self.msgBox)
        recentLine = QtGui.QHBoxLayout()
        self.recentList = QtGui.QComboBox()
        self.recentList.setMinimumWidth(175)
        recentLine.addWidget(QtGui.QLabel("Recents:"))
        recentLine.addWidget(self.recentList)
        self.layout.addLayout(recentLine)
        self.recentPingBtn = QtGui.QPushButton("Ping")
        self.recentPingBtn.clicked.connect(self.onRecentPingBtnClicked)
        recentLine.addWidget(self.recentPingBtn)
        self.removeUserFromRecentBtn = QtGui.QPushButton("Remove user")
        self.removeUserFromRecentBtn.clicked.connect(self.onRemoveUserFromRecentBtnClicked)
        self.removeUserFromRecentBtn.setToolTip("Remove this user from recent list")
        recentLine.addWidget(self.removeUserFromRecentBtn)
        self.removeAllUsersFromRecentBtn = QtGui.QPushButton("Remove all")
        self.removeAllUsersFromRecentBtn.setToolTip("Remove all users from recent list")
        self.removeAllUsersFromRecentBtn.clicked.connect(self.onRemoveAllUsersFromRecentBtnClicked)
        recentLine.addWidget(self.removeAllUsersFromRecentBtn)
        self.populateUsers()

    def onRecentPingBtnClicked(self, arg1):
        curRecent = self.recentList.currentText()
        if not curRecent:
            self.msg("Recent users is empty","Error")
            return
        self.cbUsers.setCurrentText(curRecent)
        self.onPingBtnClicked(True)

    def onRemoveUserFromRecentBtnClicked(self, arg1):
        curRecent = self.recentList.currentText()
        if not curRecent:
            self.msg("Recent users is empty","Error")
            return
        self.recentDict.pop(curRecent)
        jstring = json.dumps(self.recentDict)
        self.pg.SetString("RecentUsers",jstring)
        self.populateUsers()

    def onRemoveAllUsersFromRecentBtnClicked(self, arg1):
        self.recentDict = {}
        self.pg.SetString("RecentUsers","{}")
        self.populateUsers()

    def msg(self, txt, msgType="Message"):
        if msgType == "Message":
            self.msgBox.setStyleSheet("color:black")
        elif msgType == "Error":
            self.msgBox.setStyleSheet("color:red")
        elif msgType == "Warning":
            self.msgBox.setStyleSheet("color:yellow")
        self.msgBox.setPlainText(txt)

    def buildFullDict(self):
        self.fullDict = {}
        defaultUsers = [k for k in self.dict1.keys()]
        self.fetchAdded()
        self.fetchRecent()
        addedUsers = [k for k in self.addedDict.keys()]
        for k,v in self.addedDict.items():
            self.fullDict[k] = v
        for k,v in self.dict1.items():
            self.fullDict[k] = v



    def populateUsers(self):
        self.buildFullDict()
        self.cbUsers.clear()
        self.cbUsers.addItem('--select user--')
        if self.sortCheckBox.checkState():
            self.cbUsers.addItems(sorted(self.fullDict))
        else:
            self.cbUsers.addItems(list(self.fullDict))
        self.fetchRecent()
        self.recentList.clear()
        self.recentList.addItems(list(self.recentDict))

    def fetchAdded(self):
        addedStr = self.pg.GetString("AddedUsers","{}")
        self.addedDict = json.loads(addedStr)

    def fetchRecent(self):
        recentStr = self.pg.GetString("RecentUsers","{}")
        self.recentDict = json.loads(recentStr)

    def addUser(self, username):
        self.fetchAdded()
        self.fetchRecent()
        curId =""
        if username in self.addedDict:
            curId = self.addedDict[username]
        id,ok = QtGui.QInputDialog.getText(self.form,"Add/Edit user",f"Enter user id for {username}:",text=curId)
        if not ok:
            return False
        try:
            id_int = int(id)
        except ValueError as ve:
            self.msg(f"{ve}","Error")
            return False
        self.addedDict[username] = id
        self.recentDict[username] = id
        jstring = json.dumps(self.addedDict)
        self.pg.SetString("AddedUsers",jstring)
        jstring = json.dumps(self.recentDict)
        self.pg.SetString("RecentUsers",jstring)
        self.buildFullDict()
        self.populateUsers()
        return True

    def information(self):
        self.msg("Pinger macro is to help in pinging users on the FreeCAD forum.\n\
Usage: select a user, click Ping/Add button, paste text from clipboard into forum\n\n\
To add a new user: type in the new name, click Ping/Add button.\n\n\
Click About info button to copy your FreeCAD version information to the clipboard.\n\n\
Only added users may be edited or removed.\n\n\
Sorted checkbox sorts the users alphabetically.  \
Added users are at the top of the list when not sorted, then according to number of posts.\n\n\
Only users with 100+ posts (at the time the database was updated) are guaranteed to appear in the list.\n\
")

    def onDelBtnClicked(self, arg1):
        username = self.cbUsers.currentText()
        if not username in self.addedDict:
            self.msg(f"{username} is not an added user, cannot be deleted","Error")
            return
        self.addedDict.pop(username)
        jstring = json.dumps(self.addedDict)
        self.pg.SetString("AddedUsers",jstring)
        if username in self.recentDict:
            self.recentDict.pop(username)
            jstring = json.dumps(self.recentDict)
            self.pg.SetString("RecentUsers",jstring)
        self.cbUsers.clear()
        self.populateUsers()
        self.msg(f"{username} has been removed from added users","Message")

    def onReturnPressed(self):
        self.onPingBtnClicked(True)

    def onEditBtnClicked(self, arg1):
        username = self.cbUsers.currentText()
        if not username in self.dict1: #adding edits addedusers only
            if not self.addUser(username):
                return
        else:
            self.msg(f"{username} is in default dictionary, cannot be edited","Error")
            return

    def onPingBtnClicked(self, arg1):
        username = self.cbUsers.currentText()
        if username == '--select user--':
            return
        if not username in self.fullDict:
            if not self.addUser(username):
                return
        ping = "[quote="+username+" user_id="+self.fullDict[username]+"]\npinged by pinger macro\n[/quote]"
        self.setClipText(ping)
        self.msg("Success!\n\nNow copied to clipboard: \n\n"+ping)
        self.form.setFocus()
        self.fetchRecent()
        if not username in self.recentDict:
            self.recentDict[username] = self.fullDict[username]
            jstring = json.dumps(self.recentDict)
            self.pg.SetString("RecentUsers",jstring)
            self.populateUsers()
        #self.form.close()

    def getClipText(self):
        clip = QtGui.QClipboard()
        return clip.text(QtGui.QClipboard.Clipboard)

    def setClipText(self,txt):
        clip = QtGui.QClipboard()
        clip.setText(txt)

    def getAboutInfo(self):
        ai=AboutInfo()
        QtGui.QApplication.instance().installEventFilter(ai)
        Gui.runCommand("Std_About")
        QtGui.QApplication.instance().removeEventFilter(ai)
        del ai
        clipText = self.getClipText()
        self.msg(f"Success!  Following now copied to clipboard:\n\n{clipText}")
        self.form.setFocus()

    def setupDict1(self):
        self.dict1 = {'chrisb': '5646', 'NormandC': '202', 'wmayer': '69', 'yorik': '68', 'bernd': '2069', 'Kunda1': '12229', 'jmaustpc': '611', 'triplus': '782', 'DeepSOIC': '3888', 'freecad-heini-1': '2598', 'openBrain': '22265', 'sgrogan': '4252', 'bejant': '1940', 'thomas-neemann': '29293', 'vocx': '21943', 'drmacro': '2867', 'microelly2': '2364', 'Roy_043': '22936', 'abdullah': '3232', 'papyblaise': '25808', 'wandererfan': '1375', 'TheMarkster': '19292', 'paullee': '8738', 'kisolre': '22435', 'mario52': '1058',
'quick61': '2030', 'looo': '2349', 'Vincen': '5772', 'uwestoehr': '23505', 'Shalmeneser': '38754', 'PrzemoF': '3666', 'jriegel': '67', 'GeneFC': '8180', 'ickby': '686', 'easyw-fc': '6387', 'meme2704': '14145', 'shoogen': '765', 'sliptonic': '708', 'renatorivo': '918', 'thschrader': '15166', 'kkremitzki': '7997', 'freedman': '19098', 'Bance': '5418', 'herbk': '4353', 'keithsloan52': '930', 'Jee-Bee': '6234', 'r-frank': '1529', 'realthunder': '12167', 'carlopav': '23005', 'Chris_G': '2561',
'onekk': '5245', 'ulrich1a': '1928', 'Joel_graff': '14673', 'chennes': '11959', 'Forthman': '19652', 'rockn': '681', 'freman': '22524', 'adrianinsaval': '19302', 'saso': '3305', 'Zolko': '22794', 'Willem': '9760', 'mlampert': '10163', 'tanderson69': '208', 'bitacovir': '3136', 'Syres': '21041', 'hammax': '12483', 'HakanSeven12': '23711', 'roerich_64': '6075', 'UR_': '12184', 'Dirk.B': '23630', 'HoWil': '6222', 'user1234': '9411', '-alex-': '23825', 'HarryGeier': '15774', 'freecadjam': '20736',
'flachyjoe': '984', 'bambuko': '27936', 'jeno': '3508', 'HarryvL': '18062', 'kbwbe': '19380', 'peterl94': '1819', 'RatonLaveur': '24547', 'johnwang': '23504', 'cox': '4523', 'M4x': '13711', 'reox': '9769', 'pablogil': '4517', 'domad': '33963', 'david69': '2566', 'edwilliams16': '36484', 'leoheck': '19003', 'Russ4262': '20523', 'heda': '7350', 'ppemawm': '1807', 'ArminF': '11953', 'jp-willm': '7776', 'Pauvres_honteux': '2803', 'regis': '6401', 'vejmarie': '7506', 'Gift': '6611',
'ian.rees': '3449', 'pperisin': '356', 'emills2': '5929', 'dubstar-04': '1642', 'ezzieyguywuf': '6058', 'mrlukeparry': '607', 'fc_tofu': '29038', 'logari81': '270', 'FaDa3D': '16107', 'jpg87': '13810', 'NewJoker': '36858', 'eivindkvedalen': '1546', 'damian': '6134', 'oliveroxtoby': '11950', 'Vagulus': '35139', 'jtm2020hyo': '35626', 'Cobraschock': '25890', 'jrheinlaender': '997', 'cappy0815': '4130', 'kaktus': '26846', 'Jimidi': '15956', 'vanuan': '22024', 'davidosterberg': '36295', 'ebrahi': '21433', 'kwahoo': '2441',
'Joyas': '3582', 'r.tec': '4264', 'dcapeletti': '3651', 'drei': '3278', 'schupin': '18259', 'mariwan': '39136', 'agryson': '11337', 'JoshM': '16808', 'jnxd': '5734', 'Cekuhnen': '43243', 'manuelkrause': '20592', 'Mar': '14191', 'aapo': '22095', 'blue0cean': '23920', 'fandaL': '3658', 'Fran': '16427', 'teobo': '2833', 'paddle': '29478', 'OficineRobotica': '23938', 'Giuli': '9935', 'danielfalck': '689', 'makkemal': '5932', 'apeltauer': '16146', 'shaise': '6188', 'bavariaSHAPE': '3425',
'ragohix769': '35209', 'galou_breizh': '334', 'garya': '22407', 'fcaduser': '2823', 'jaisejames': '10269', 'bill': '5185', 'blacey': '7328', 'fosselius': '8591', 'herrdeh': '3918', 'jruiz': '4299', 'edi': '29214', 'Sudhanshu': '21878', 'fran6t': '3600', 'wsteffe': '3846', 'nemesis': '2986', 'holdi': '11560', 'piffpoof': '4556', 'mnesarco': '30314', 'f3nix': '6125', 'furti': '17491', 'balrobs': '30989', 'amrit3701': '9146', 'jbe': '2330', 'Roland': '6638', 'rynn': '20919',
'jreinhardt': '2072', 'koluna': '21576', 'chakkree': '6331', 'RedBaron': '36427', 'memfis': '11177', 'Evgeniy': '43393', 'plgarcia': '6249', 'arturromarr': '15598', 'Sura': '21412', 'Lauri': '13429', 'joha2': '10551', 'cad1234': '22955', 'lemonbug': '4228', 'C4e': '49784', 'MRx': '35035', 'Claud': '29138', 'clintonsam75': '3470', 'Repman': '3536', 'Moult': '23100', 'OldDraftsman': '16332', 'LHC': '36255', 'usbhub': '24632', 'efyx': '4074', 'catman': '23210', 'JMG': '2538',
'polymer': '3974', 'Miq58': '46857', 'hobbes1069': '725', 'dxp.dev': '22713', 'wega': '2347', 'mendy': '19994', 'Konstantin': '3649', 'Renat': '3315', 'davecoventry': '2481', 'gsandy': '23521', 'blonblon': '10279', 'Drederwisch': '11726', 'Aleks': '30029', 'oldmachine': '15343', 'salp': '2409', 'FBXL5': '26761', 'Marco_T': '7564', 'bgoodr': '3447', 'dimitar': '25801', 'CharlieMAC': '3179', 'Markymark': '28078', 'HBC0': '6833', 'obelisk79': '36480', 'ceremcem': '18069', 'arcol': '2320',
'qingfeng.xia': '6825', 'MaurinoWeb': '15573', 'hhassey': '6158', 'Brutha': '5971', 'lainegates': '1295', 'FC-Architecter': '19079', 'papy': '21427', 'chrisf': '2578', 'nahshon': '1973', 'MSOlsen65': '29727', 'ediloren': '1783', 'dan-miel': '21478', 'jean.thil': '6498', 'pl7i92LCNC': '24265', 'falviani': '25270', 'foxint': '7589', 'project4': '1944', 'j-dowsett': '652', 'un1corn': '7434', 'kwahooo': '254', 'qwerty_f': '36471', 'drum22': '40830', 'Luixx': '18322', 'paul18': '3622', 'serrepattes': '15169',
'cram': '11546', 'a3bksll47': '19044', 'joel': '12631', 'yoshimitsuspeed': '1337', 'heron': '30887', 'HartmutG': '10744', 'Smiling_user': '35383', 'josegegas': '13017', 'gdo35': '858', 'spanner888': '25590', 'dprojects': '13594', 'ProBowlUk': '4171', 'C_h_o_p_i_n': '25037', 'JussyAD': '41661', 'rentlau_64': '4246', 'Do': '11781', 'Piero69': '26052', 'tonyaimer': '27612', 'AR795': '20058', 'heilo': '12525', 'iplayfast': '27301', 'hardeeprai': '255', 'Turro75': '9800', 'Wsk8': '22665', 'Fat-Zer': '4325',
'Grub': '37710', 'Sam': '8192', 'TomB19': '25136', 'agima2': '12024', 'jmarie3D': '31172', 'Norus': '6964', 'S.N.A.L': '3080', 'PeterSD': '48559', 'Olav': '11423', 'Renato': '5905', 'kanagan': '5980', 'Routerworks': '19363', 'tom': '5727', 'Spindoctor': '6848', 'm42kus': '3911', 'freecc': '18704', 'ikua': '14240', 'grandcross': '6949', 'JellyPalm': '30355', 'TopDown': '20410', 'babaroga': '9780', 'Leatherman': '12789', 'cblt2l': '251', 'psicofil': '789', 'japie': '3493',
'turn211': '39797', 'crobar': '3893', 'christi': '22009', 'gbroques': '29296', 'industromatic': '2997', 'clytle374': '2207', 'nyholku': '12058', 'doia': '42412', 'ajoeiam': '24132', 'ABeton': '27254', 'CrashedAgain': '29187', 'wvmarle': '4214', 'run_the_race': '39789', 'derschutzhund': '3592', 'ToniTen': '36030', 'sanguinariojoe': '574', 'perot': '16372', '1D_Inc': '23696', 'etrombly': '28581', 'cadcam': '30470', 'TedM': '30824', 'crashfridh': '1483', 'Anderl': '17746', 'Chaospilot': '22486', 'Eric': '25272',
'ektus': '1283', 'Eric': '25272', 'xbit': '36362', 'bhs67': '5322', 'hyarion': '34430', 'Mongrel_Shark': '10595', 'zbigg': '17804', '2cv001': '28971', 'oddtopus': '10205', 'exsolvespacer': '39536', 'jakob': '3595', 'FemUser': '16291', 'luggw1': '13046', 'Cyril': '16289', 'jmcornil': '37409', 'kcleung': '512', 'm0n5t3r': '12818', 'Galahad': '20671', 'schnebeck': '15579', 'Crossleyuk': '20393', 'Hannu': '6761', 'HardRock': '18990', 'IzzY': '14602', 'maker': '19242', 'waebbl': '21119',
'bmsaus4ax': '37689', 'rebeltaz': '24648', 'Koemi': '17917', 'nic': '24865', 'xibinke': '5703', 'ifohancroft': '25644', 'albertdela': '16540', 'lot': '25410', 'jonasthomas': '873', 'Jos': '31258', 'jonasb': '38748', 'Ukacor': '24411', 'jmplonka': '11876', 'JiPe38': '28975', 'mfasano': '19405', 'KAP': '28935', 'scrungy_doolittle': '20416', 'doubters': '8165', 'smktec': '29984', 'eason': '5803', 'OakLD': '18151', 'brjhaverkamp': '6838', 'zohozer': '3684', 'roivai': '12794', 'prrvchr': '4119',
'hds': '13102', 'hholgi': '21563', 'bbear123': '2465', 'xf3qc': '16073', 'kreso-t': '20975', 'more11': '4079', 'alex::freecad': '3892', 'aerospaceweeb': '41416', 'cnirbhay': '9824', 'IanP': '7957', 'heideachim': '18226', 'felixlee868': '26041', 'seppelw': '18203', 'aguseguedre': '535', 'frecd': '5116', 'R23D': '29332', 'F_Rosa': '7885', 'Petrikas': '38333', 'freecadlzh': '30003', 'mrdic': '14954', 'Petert': '7290', 'duckmug': '42568', 'Gauthier': '3532', 'czinehuba': '21877', 'm.cavallerin': '20120',
'Gauthier': '3532', 'wagnerlip': '29985', 'abasel': '21318', 'NC3D': '10606', 'sibelius': '29023', 'mack5': '15924', 'Linden': '6627', 'manos': '37638', 'EkaitzEsteban': '21473', 's-light': '5425', 'NateM': '2390', 'kaih': '28962', 'julieng': '22492', 'Sidemountyucatan': '24853', 'django013': '5218', 'Bertel': '37383', 'lhagan': '108', 'PMac': '16406', 'MrRossi': '11492', 'spikey': '7624', 'Daniel84': '13510', 'Andr': '7655', 'PunyTune': '23110', 'bzb.dev001': '25224', 'godblessfq': '6436',
'godblessfq': '6436', 'DrBwts': '4281', 'neondata': '1573', 'mikeprice99': '34491', 'watsug': '36528', 'balazs': '4211', 'atzensepp': '5514', 'foadsf': '5587', 'onesz': '729', 'Gregor': '30570', 'Rost': '37043', 'oldestfox': '1910', 'Magnum56': '19253', 'hinckel': '4480', 'jmh': '4317', 'Serchu': '5411', 'miniellipse': '19613', 'Enyalios': '13094', 'Quaoar': '15966', 'Xav-83': '3750', 'A_3': '7639', 'andre': '2370', 'iogui': '24401', 'dulouie': '16780', 'j9lemmon': '2018',
        #add new users and userids here
        #some examples:
        #'Enyalios': '13094',
        #'agima2': '12024'

        }
def QIconFromXPMString(xpm_string):
    xpm = xpm_string.replace("\"","").replace(',','').splitlines()[4:-1]
    pixmap = QtGui.QPixmap(xpm)
    icon = QtGui.QIcon(pixmap)
    return icon

__icon__ = """
/* XPM */
static char *_648433055688[] = {
/* columns rows colors chars-per-pixel */
"64 64 4 1 ",
"  c black",
". c #FD8711",
"X c #FFC90E",
"o c None",
"oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo",
"oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo",
"oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo",
"oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo",
"oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo",
"oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo",
"oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo",
"oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo",
"oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo",
"oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo",
"oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo",
"oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo",
"oooooooooooooooooooooooooooXXXXXXXoooooooooooooooooooooooooooooo",
"ooooooooooooooooooooooooXXXXXXXXXXXXoooooooooooooooooooooooooooo",
"oooooooooooooooooooooooXXXXX     XXXXooooooooooooooooooooooooooo",
"ooooooooooooooooooooooXXXX         XXXXooooooooooooooooooooooooo",
"oooooooooooooooooooooXXX            XXXXoooooooooooooooooooooooo",
"oooooooooooooooooooooXX      XXX      XXXooooooooooooooooooooooo",
"ooooooooooooooooooooXXX     XXXXX      XXXoooooooooooooooooooooo",
"oooooooooooooooooooXXX    XXXXXXXXX     XXoooooooooooooooooooooo",
"ooooooooooooooooooXXX    XXXXXXXXXXX    XXoooooooooooooooooooooo",
"oooooooooooooooooXXX    XXXXXoooXXXXX   XXXooooooooooooooooooooo",
"ooooooooooooooooXXX     XXXXoooooXXXX    XXXoooooooooooooooooooo",
"ooooooooooooooooXX     XXXXooo.oooXXXX    XXoooooooooooooooooooo",
"oooooooooooooooXXX    XXXXooo...oooXXXX   XXoooooooooooooooooooo",
"oooooooooooooooXXX    XXXXoo.....oooXXX   XXXooooooooooooooooooo",
"oooooooooooooooXXX   XXXXoo.......ooXXXX   XXooooooooooooooooooo",
"oooooooooooooooXXX   XXXXoo.......ooXXXX   XXooooooooooooooooooo",
"oooooooooooooooXX    XXXXoo.......ooXXXX   XXXoooooooooooooooooo",
"ooooooooooooooXXX    XXXooo.......oooXXX    XXoooooooooooooooooo",
"oooooooooooooXXX     XXXoo.........ooXXX    XXXooooooooooooooooo",
"oooooooooooooXXX    XXXXoo.........ooXXXX    XXooooooooooooooooo",
"oooooooooooooXXX   XXXXooo.........oooXXX    XXooooooooooooooooo",
"oooooooooooooXX    XXXXoo...........ooXXX    XXXoooooooooooooooo",
"oooooooooooooXX    XXXooo...........ooXXXX   XXXoooooooooooooooo",
"ooooooooooooXXX    XXXoo............ooXXXX    XXXooooooooooooooo",
"ooooooooooooXX    XXXooo............ooXXXXX    XXooooooooooooooo",
"ooooooooooooXX    XXXoo.............ooXXXXX    XXooooooooooooooo",
"oooooooooooXXX    XXXoo.............oooXXXX    XXooooooooooooooo",
"ooooooooooXXXX    XXooo..............oooXXX    XXooooooooooooooo",
"oooooooooXXX     XXXoo................oooXXX   XXXXooooooooooooo",
"ooooooooXXX      XXXoooooooooooooooooooooXXX    XXXXoooooooooooo",
"oooooooXXXX     XXXXXoooooooooooooooooooooXXX     XXXooooooooooo",
"oXXXXXXXX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    XXXXXXXXXXooo",
"oXXXXXXX      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX     XXXXXXXXXooo",
"oXX                                                        XXooo",
"oXX                                                        XXooo",
"oXX                                                        XXooo",
"oXX                                                        XXooo",
"oXX                                                        XXooo",
"oXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXooo",
"oXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXooo",
"oXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXooo",
"oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo",
"oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo",
"oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo",
"oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo",
"oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo",
"oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo",
"oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo",
"oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo",
"oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo",
"oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo",
"oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo"
};
"""
#pinger = Pinger()
dlg = PingerDlg()

if __name__ == "__main__":
#    pinger.run()
    dlg.form.show()
}}

## Link

The forum discussion [Pinger macro](https://forum.freecadweb.org/viewtopic.php?f=22&t=48872)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Pinger/en
