project = QgsProject.instance()

project.read('C:/Curso_PyGis/BD/dados/dados_sig.qgs')

project.setBackgroundColor(QColor(51, 153, 255))

project.count()

project.setCrs(QgsCoordinateReferenceSystem("EPSG:4674"))

project.setTitle('Curso_PyGis')

project.ellipsoid()

project.lastModified()