# \Curso_PyGis\BD\dados

print(os.getcwd())
path = os.getcwd() + '\Curso_PyGis\BD\dados'
print(path)

# Abrindo camada vetorial
path_layer = path + '/aeroportos.shp'
layer = QgsVectorLayer(path_layer, "Aeroportos", "ogr")

#Adicionar camada no canvas
QgsProject.instance().addMapLayer(layer)

# Obter id
print(layer.id())

# Saber extensão
print(layer.extent())

# Criar novos atributos
layer.startEditing()
layer.addAttribute(QgsField('teste', QVariant.String))
layer.commitChanges()

layer.startEditing()
layer.addAttribute(QgsField('area', QVariant.Double))
layer.commitChanges()

# Obter informações de campos
print(layer.fields().names())
print(layer.fields().names()[3])
print(layer.fields().names()[8])

# Deletar atributos
layer.startEditing()
layer.deleteAttribute(15)
layer.commitChanges()


# outra forma de DELETAR
layer.startEditing()
layer.addAttribute(QgsField('regioes', QVariant.String))
layer.commitChanges()


layer.startEditing()
 name_columns_table = layer.fields().names()
 layer.deleteAttribute(name_columns_table.index('regioes'))
 layer.commitChanges()






