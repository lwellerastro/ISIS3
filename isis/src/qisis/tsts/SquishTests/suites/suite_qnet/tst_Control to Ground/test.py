import os

def main():
    try:
        os.mkdir(os.path.expandvars('$ISISROOT/src/qisis/tsts/SquishTests/output'))
    except Exception:
        pass
    try:
        os.unlink(os.path.expandvars('$ISISROOT/src/qisis/tsts/SquishTests/output/') + 'MiniUpdate.net')
    except Exception:
        pass

    
    startApplication("qnet")
    
    # Open cube list
    activateItem(waitForObjectItem(":qnet_QMenuBar", "File"))
    activateItem(waitForObjectItem(":qnet.File_QMenu", "Open control network and cube list"))
    snooze(0.5)
    mouseClick(waitForObject(":fileNameEdit_QLineEdit"), 95, 13, 0, Qt.LeftButton)
    type(waitForObject(":fileNameEdit_QLineEdit"), "../src/qisis/tsts/SquishTests/input/Ground/Extracted_AllOverlaps.lis")
    type(waitForObject(":_QListView"), "<Return>")

    # Open control net
    snooze(0.5)
    mouseClick(waitForObject(":fileNameEdit_QLineEdit_7"), 95, 13, 0, Qt.LeftButton)

    waitForObjectItem(":stackedWidget.treeView_QTreeView_2", "Mini\\.net")
    doubleClickItem(":stackedWidget.treeView_QTreeView_2", "Mini\\.net", 58, 5, 0, Qt.LeftButton)
    
    # Open ground source file
    activateItem(waitForObjectItem(":qnet_QMenuBar", "File"))
    activateItem(waitForObjectItem(":qnet.File_QMenu", "Open Ground Source"))
    clickButton(waitForObject(":Open ground source.toParentButton_QToolButton"))
    snooze(0.5)
    mouseClick(waitForObject(":fileNameEdit_QLineEdit_2"), 95, 13, 0, Qt.LeftButton)
    type(waitForObject(":fileNameEdit_QLineEdit_2"), "src/qisis/tsts/SquishTests/input/Ground/Shade_Mola_Radius.cub")
    type(waitForObject(":fileNameEdit_QLineEdit_2"), "<Return>")
    
    # Open radius source file
    activateItem(waitForObjectItem(":qnet_QMenuBar", "File"))
    activateItem(waitForObjectItem(":qnet.File_QMenu", "Open Radius Source"))
    clickButton(waitForObject(":Open DEM.toParentButton_QToolButton"))
    snooze(0.5)
    mouseClick(waitForObject(":fileNameEdit_QLineEdit_4"), 95, 13, 0, Qt.LeftButton)
    type(waitForObject(":fileNameEdit_QLineEdit_4"), "src/qisis/tsts/SquishTests/input/Ground/Mola_Radius.cub")
    type(waitForObject(":fileNameEdit_QLineEdit_4"), "<Return>")
    
    # Filter on constrained points
    clickTab(waitForObject(":Control Network Navigator.qt_tabwidget_tabbar_QTabBar"), "Point Properties")
    clickButton(waitForObject(":Filter by Point Type(s).Free_QCheckBox"))
    clickButton(waitForObject(":Filter by Point Type(s).Constrained_QCheckBox"))
    clickButton(waitForObject(":Control Network Navigator.Filter_QPushButton"))
    waitForObjectItem(":Navigator_List", "L1470")
    
    # Bring up qnet tool dialog with given point
    doubleClickItem(":Navigator_List", "L1470", 26, 5, 0, Qt.LeftButton)
    clickButton(waitForObject(":Qnet Tool.Geom_QRadioButton"))
    
    # Click add measures
    clickButton(waitForObject(":QnetToolScroll.Add Measure(s) to Point_QPushButton"))
    scrollTo(waitForObject(":Select Files:_QScrollBar"), 177)
    scrollTo(waitForObject(":Select Files:_QScrollBar"), 126)
    clickButton(waitForObject(":Add Measures to ControlPoint.OK_QPushButton"))
    
    # Control measures
    mouseClick(waitForObject(":Right Measure_QComboBox"), 145, 6, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":Right Measure_QComboBox", "f684a63\\.lev1\\_slo\\.cub"), 147, 2, 0, Qt.LeftButton)
    clickButton(waitForObject(":QnetToolScroll.Latitude: 17.1381    Longitude:  300.307_QToolButton"))
    spinUp(waitForObject(":QnetToolScroll.Latitude: 17.1381    Longitude:  300.307_QDoubleSpinBox"))
    doubleClick(waitForObject(":QnetToolScroll.Latitude: 17.1381    Longitude:  300.307_QDoubleSpinBox"), 44, 8, 0, Qt.LeftButton)
    spinUp(waitForObject(":QnetToolScroll.Latitude: 17.1381    Longitude:  300.307_QDoubleSpinBox"))
    doubleClick(waitForObject(":QnetToolScroll.Latitude: 17.1381    Longitude:  300.307_QDoubleSpinBox"), 45, 0, 0, Qt.LeftButton)
    spinUp(waitForObject(":QnetToolScroll.Latitude: 17.1381    Longitude:  300.307_QDoubleSpinBox"))
    doubleClick(waitForObject(":QnetToolScroll.Latitude: 17.1381    Longitude:  300.307_QDoubleSpinBox"), 45, 0, 0, Qt.LeftButton)
    spinDown(waitForObject(":QnetToolScroll.Latitude: 17.1381    Longitude:  300.307_QDoubleSpinBox"))
    doubleClick(waitForObject(":QnetToolScroll.Latitude: 17.1381    Longitude:  300.307_QDoubleSpinBox"), 45, 14, 0, Qt.LeftButton)
    spinDown(waitForObject(":QnetToolScroll.Latitude: 17.1381    Longitude:  300.307_QDoubleSpinBox"))
    doubleClick(waitForObject(":QnetToolScroll.Latitude: 17.1381    Longitude:  300.307_QDoubleSpinBox"), 45, 14, 0, Qt.LeftButton)
    spinDown(waitForObject(":QnetToolScroll.Latitude: 17.1381    Longitude:  300.307_QDoubleSpinBox"))
    doubleClick(waitForObject(":QnetToolScroll.Latitude: 17.1381    Longitude:  300.307_QDoubleSpinBox"), 45, 14, 0, Qt.LeftButton)
    spinDown(waitForObject(":QnetToolScroll.Latitude: 17.1381    Longitude:  300.307_QDoubleSpinBox"))
    spinDown(waitForObject(":QnetToolScroll.Latitude: 17.1381    Longitude:  300.307_QDoubleSpinBox"))
    spinUp(waitForObject(":QnetToolScroll.Latitude: 17.1381    Longitude:  300.307_QDoubleSpinBox"))
    mouseClick(waitForObject(":QnetToolScroll_Isis::ControlPointEdit"), 602, 436, 0, Qt.LeftButton)
    type(waitForObject(":VP2"), "<Right>")
    type(waitForObject(":VP2"), "<Right>")
    type(waitForObject(":VP2"), "<Right>")
    type(waitForObject(":VP2"), "<Left>")
    type(waitForObject(":VP2"), "<Left>")
    type(waitForObject(":VP2"), "<Left>")
    type(waitForObject(":VP2"), "<Left>")
    type(waitForObject(":VP2"), "<Left>")
    type(waitForObject(":VP2"), "<Left>")
    type(waitForObject(":VP2"), "<Left>")
    type(waitForObject(":VP2"), "<Left>")
    type(waitForObject(":VP2"), "<Left>")
    type(waitForObject(":VP2"), "<Down>")
    type(waitForObject(":VP2"), "<Down>")
    type(waitForObject(":VP2"), "<Down>")
    type(waitForObject(":VP2"), "<Down>")
    type(waitForObject(":VP2"), "<Left>")
    clickButton(waitForObject(":QnetToolScroll.Save Measure_QPushButton"))
    clickButton(waitForObject(":QnetToolScroll.Save Point_QPushButton"))
    mouseClick(waitForObject(":Right Measure_QComboBox"), 229, 14, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":Right Measure_QComboBox", "f825a28\\.lev1\\_slo\\.cub"), 209, 9, 0, Qt.LeftButton)
    mouseClick(waitForObject(":VP2"), 142, 155, 0, Qt.LeftButton)
    type(waitForObject(":VP2"), "<Down>")
    type(waitForObject(":VP2"), "<Down>")
    type(waitForObject(":VP2"), "<Left>")
    type(waitForObject(":VP2"), "<Left>")
    type(waitForObject(":VP2"), "<Left>")
    type(waitForObject(":VP2"), "<Down>")
    type(waitForObject(":VP2"), "<Down>")
    type(waitForObject(":VP2"), "<Down>")
    type(waitForObject(":VP2"), "<Down>")
    type(waitForObject(":VP2"), "<Left>")
    type(waitForObject(":VP2"), "<Left>")
    clickButton(waitForObject(":QnetToolScroll.Save Measure_QPushButton"))
    clickButton(waitForObject(":QnetToolScroll.Save Point_QPushButton"))
    clickButton(waitForObject(":QnetToolScroll.Latitude: 17.1381    Longitude:  300.307_QToolButton_2"))
    
    # Save resulting network
    scrollTo(waitForObject(":_QScrollBar"), 2)
    mouseClick(waitForObject(":_QHeaderView"), 877, 11, 0, Qt.LeftButton)
    waitFor("object.exists(':0_1_QModelIndex')", 20000)
    test.compare(findObject(":0_1_QModelIndex").text, "Odyssey/THEMIS_IR/705696930.025")
    waitFor("object.exists(':1_1_QModelIndex')", 20000)
    test.compare(findObject(":1_1_QModelIndex").text, "Odyssey/THEMIS_IR/829897156.179")
    waitFor("object.exists(':2_1_QModelIndex')", 20000)
    test.compare(findObject(":2_1_QModelIndex").text, "Viking1/VISA/39046014")
    waitFor("object.exists(':3_1_QModelIndex')", 20000)
    test.compare(findObject(":3_1_QModelIndex").text, "Viking1/VISB/41759599")
    waitFor("object.exists(':4_1_QModelIndex')", 20000)
    test.compare(findObject(":4_1_QModelIndex").text, "Shade_Mola_Radius.cub")
    waitFor("object.exists(':0_1_QModelIndex')", 20000)
    test.compare(findObject(":0_1_QModelIndex").text, "Odyssey/THEMIS_IR/705696930.025")
    waitFor("object.exists(':1_1_QModelIndex')", 20000)
    test.compare(findObject(":1_1_QModelIndex").text, "Odyssey/THEMIS_IR/829897156.179")
    waitFor("object.exists(':2_1_QModelIndex')", 20000)
    test.compare(findObject(":2_1_QModelIndex").text, "Viking1/VISA/39046014")
    waitFor("object.exists(':3_1_QModelIndex')", 20000)
    test.compare(findObject(":3_1_QModelIndex").text, "Viking1/VISB/41759599")
    waitFor("object.exists(':4_1_QModelIndex')", 20000)
    test.compare(findObject(":4_1_QModelIndex").text, "Shade_Mola_Radius.cub")
    waitFor("object.exists(':0_15_QModelIndex')", 20000)
    test.compare(findObject(":0_15_QModelIndex").text, "RegisteredSubPixel")
    waitFor("object.exists(':0_1_QModelIndex')", 20000)
    test.compare(findObject(":0_1_QModelIndex").text, "Odyssey/THEMIS_IR/705696930.025")
    waitFor("object.exists(':1_1_QModelIndex')", 20000)
    test.compare(findObject(":1_1_QModelIndex").text, "Odyssey/THEMIS_IR/829897156.179")
    waitFor("object.exists(':2_1_QModelIndex')", 20000)
    test.compare(findObject(":2_1_QModelIndex").text, "Viking1/VISA/39046014")
    waitFor("object.exists(':3_1_QModelIndex')", 20000)
    test.compare(findObject(":3_1_QModelIndex").text, "Viking1/VISB/41759599")
    waitFor("object.exists(':4_1_QModelIndex')", 20000)
    test.compare(findObject(":4_1_QModelIndex").text, "Shade_Mola_Radius.cub")
    waitFor("object.exists(':0_15_QModelIndex')", 20000)
    test.compare(findObject(":0_15_QModelIndex").text, "RegisteredSubPixel")
    waitFor("object.exists(':1_15_QModelIndex')", 20000)
    test.compare(findObject(":1_15_QModelIndex").text, "RegisteredSubPixel")
    waitFor("object.exists(':0_1_QModelIndex')", 20000)
    test.compare(findObject(":0_1_QModelIndex").text, "Odyssey/THEMIS_IR/705696930.025")
    waitFor("object.exists(':1_1_QModelIndex')", 20000)
    test.compare(findObject(":1_1_QModelIndex").text, "Odyssey/THEMIS_IR/829897156.179")
    waitFor("object.exists(':2_1_QModelIndex')", 20000)
    test.compare(findObject(":2_1_QModelIndex").text, "Viking1/VISA/39046014")
    waitFor("object.exists(':3_1_QModelIndex')", 20000)
    test.compare(findObject(":3_1_QModelIndex").text, "Viking1/VISB/41759599")
    waitFor("object.exists(':4_1_QModelIndex')", 20000)
    test.compare(findObject(":4_1_QModelIndex").text, "Shade_Mola_Radius.cub")
    waitFor("object.exists(':0_15_QModelIndex')", 20000)
    test.compare(findObject(":0_15_QModelIndex").text, "RegisteredSubPixel")
    waitFor("object.exists(':1_15_QModelIndex')", 20000)
    test.compare(findObject(":1_15_QModelIndex").text, "RegisteredSubPixel")
    waitFor("object.exists(':2_15_QModelIndex')", 20000)
    test.compare(findObject(":2_15_QModelIndex").text, "Manual")
    waitFor("object.exists(':0_1_QModelIndex')", 20000)
    test.compare(findObject(":0_1_QModelIndex").text, "Odyssey/THEMIS_IR/705696930.025")
    waitFor("object.exists(':1_1_QModelIndex')", 20000)
    test.compare(findObject(":1_1_QModelIndex").text, "Odyssey/THEMIS_IR/829897156.179")
    waitFor("object.exists(':2_1_QModelIndex')", 20000)
    test.compare(findObject(":2_1_QModelIndex").text, "Viking1/VISA/39046014")
    waitFor("object.exists(':3_1_QModelIndex')", 20000)
    test.compare(findObject(":3_1_QModelIndex").text, "Viking1/VISB/41759599")
    waitFor("object.exists(':4_1_QModelIndex')", 20000)
    test.compare(findObject(":4_1_QModelIndex").text, "Shade_Mola_Radius.cub")
    waitFor("object.exists(':0_15_QModelIndex')", 20000)
    test.compare(findObject(":0_15_QModelIndex").text, "RegisteredSubPixel")
    waitFor("object.exists(':1_15_QModelIndex')", 20000)
    test.compare(findObject(":1_15_QModelIndex").text, "RegisteredSubPixel")
    waitFor("object.exists(':2_15_QModelIndex')", 20000)
    test.compare(findObject(":2_15_QModelIndex").text, "Manual")
    waitFor("object.exists(':3_15_QModelIndex')", 20000)
    test.compare(findObject(":3_15_QModelIndex").text, "Manual")
    waitFor("object.exists(':0_1_QModelIndex')", 20000)
    test.compare(findObject(":0_1_QModelIndex").text, "Odyssey/THEMIS_IR/705696930.025")
    waitFor("object.exists(':1_1_QModelIndex')", 20000)
    test.compare(findObject(":1_1_QModelIndex").text, "Odyssey/THEMIS_IR/829897156.179")
    waitFor("object.exists(':2_1_QModelIndex')", 20000)
    test.compare(findObject(":2_1_QModelIndex").text, "Viking1/VISA/39046014")
    waitFor("object.exists(':3_1_QModelIndex')", 20000)
    test.compare(findObject(":3_1_QModelIndex").text, "Viking1/VISB/41759599")
    waitFor("object.exists(':4_1_QModelIndex')", 20000)
    test.compare(findObject(":4_1_QModelIndex").text, "Shade_Mola_Radius.cub")
    waitFor("object.exists(':0_15_QModelIndex')", 20000)
    test.compare(findObject(":0_15_QModelIndex").text, "RegisteredSubPixel")
    waitFor("object.exists(':1_15_QModelIndex')", 20000)
    test.compare(findObject(":1_15_QModelIndex").text, "RegisteredSubPixel")

    waitFor("object.exists(':2_15_QModelIndex')", 20000)
    test.compare(findObject(":2_15_QModelIndex").text, "Manual")
    waitFor("object.exists(':3_15_QModelIndex')", 20000)
    test.compare(findObject(":3_15_QModelIndex").text, "Manual")
    waitFor("object.exists(':4_15_QModelIndex')", 20000)
    test.compare(findObject(":4_15_QModelIndex").text, "Candidate")
    activateItem(waitForObjectItem(":Qnet Tool_QMenuBar", "File"))
    activateItem(waitForObjectItem(":qnet.File_QMenu", "Save Control Network As..."))
    clickButton(waitForObject(":Choose filename to save under.toParentButton_QToolButton"))
    snooze(0.5)
    mouseClick(waitForObject(":fileNameEdit_QLineEdit_3"), 95, 13, 0, Qt.LeftButton)
    type(waitForObject(":fileNameEdit_QLineEdit_3"), "src/qisis/tsts/SquishTests/output/MiniUpdate.net")
    snooze(0.5)
    type(waitForObject(":fileNameEdit_QLineEdit_3"), "<Return>")
    
    # Quit
    activateItem(waitForObjectItem(":Qnet Tool_QMenuBar", "File"))
    activateItem(waitForObjectItem(":qnet.File_QMenu", "Close"))
    activateItem(waitForObjectItem(":qnet_QMenuBar", "File"))
    activateItem(waitForObjectItem(":qnet.File_QMenu", "Exit"))
    snooze(1)
