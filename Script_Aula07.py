# Projetos do Qgis

project = QgsProject.instance()
project.read('C:/Curso_PyGis/BD/dados/dados_sig.qgs')

print(project.fileName())

print(project.absolutePath())

print(project.absoluteFilePath())

print(project.annotationManager())

print(project.backgroundColor())

print(project.crs())

project.write('C:/Curso_PyGis/BD/dados/dados_sig.qgs')

