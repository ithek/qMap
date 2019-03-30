#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "../")

from qOSM.common import QOSM

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


if __name__ == '__main__':

    def goCoords():
        def resetError():
            coordsEdit.setStyleSheet('')

        try:
            latitude, longitude = coordsEdit.text().split(",")
        except ValueError:
            coordsEdit.setStyleSheet("color: red;")
            QTimer.singleShot(500, resetError)
        else:
            map.centerAt(latitude, longitude)
            # map.moveMarker("MyDragableMark", latitude, longitude)


    def onMarkerMoved(key, latitude, longitude):
        print("Moved!!", key, latitude, longitude)
        coordsEdit.setText("{}, {}".format(latitude, longitude))


    def onMarkerRClick(key, latitude, longitude):
        print("RClick on ", key)
        # map.setMarkerOptions(key, draggable=False)


    def onMarkerLClick(key, latitude, longitude):
        print("LClick on ", key)


    def onMarkerDClick(key, latitude, longitude):
        print("DClick on ", key)
        # map.setMarkerOptions(key, draggable=True)

    def onMapMoved(latitude, longitude):
        print("Moved to ", latitude, longitude)


    def onMapRClick(latitude, longitude):
        print("RClick on ", latitude, longitude)


    def onMapLClick(latitude, longitude):
        print("LClick on ", latitude, longitude)


    def onMapDClick(latitude, longitude):
        print("DClick on ", latitude, longitude)


    app = QApplication(sys.argv)
    w = QDialog()
    h = QVBoxLayout(w)
    l = QFormLayout()
    h.addLayout(l)
    coordsEdit = QLineEdit()
    l.addRow('Coords:', coordsEdit)
    coordsEdit.editingFinished.connect(goCoords)
    map = QOSM(w)

    map.mapMovedCallback = onMapMoved
    map.markerMovedCallback = onMarkerMoved
    map.mapClickedCallback = onMapLClick
    map.mapDoubleClickedCallback = onMapDClick
    map.mapRightClickedCallback = onMapRClick
    map.markerClickedCallback = onMarkerLClick
    map.markerDoubleClickedCallback = onMarkerDClick
    map.markerRightClickedCallback = onMarkerRClick

    h.addWidget(map)
    map.setSizePolicy(
        QSizePolicy.MinimumExpanding,
        QSizePolicy.MinimumExpanding)
    w.show()

    map.waitUntilReady()

    map.centerAt(-12.0464, -77.0428)
    map.setZoom(12)
    # Many icons at: https://sites.google.com/site/gmapsdevelopment/
    #coords = map.center()
    coords = -12.0464, -77.0428 + 0.1
    map.addMarker("MyDragableMark", *coords, **dict(
        icon="http://maps.gstatic.com/mapfiles/ridefinder-images/mm_20_gray.png",
        draggable=True,
        title="Move me MyDragableMark!"
    ))

    coords = -12.0464 + 0.1, -77.0428 + 0.1
    map.addMarker("MyDragableMark2", *coords, **dict(
        icon="http://maps.gstatic.com/mapfiles/ridefinder-images/mm_20_red.png",
        draggable=True,
        title="Move me MyDragableMark2"
    ))

    sys.exit(app.exec_())
