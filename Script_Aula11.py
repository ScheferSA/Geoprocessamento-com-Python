print(os.getcwd())

path = os.getcwd() + '\\Curso_PyGis\\BD\\dados'
print(path)

for root, directory, files in os.walk(path):
    for file in files:
        if file.endswith('.shp'):
            print(file)
            path_vector = os.path.join(path, file)
            layer = QgsVectorLayer(path_vector, file [0:-4], "ogr")
            QgsProject.instance().addMapLayer(layer)
    
