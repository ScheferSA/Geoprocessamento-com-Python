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

# Deletar atributos usando o índice (posição)
layer.startEditing()
layer.deleteAttribute(17)
layer.commitChanges()


# outra forma de DELETAR - Usando o nome do campo
layer.startEditing()
layer.addAttribute(QgsField('regioes', QVariant.String))
layer.commitChanges()

layer.startEditing()
name_columns_table = layer.fields().names()
layer.deleteAttribute(name_columns_table.index('regioes'))
layer.commitChanges()

#########################################################################

# Iterando sobre get features
count = 0
for feature in layer.getFeatures():
    while count < 5:
        print(feature.attributes())
        count += 1


count = 0
for feature in layer.getFeatures():
    while count < 5:
        print(feature.attributes()[3])
        count += 1

# Alterando e update de campo
layer.startEditing()
name_columns_table = layer.fields().names()
layer.deleteAttribute(name_columns_table.index('area'))
layer.commitChanges()


# Update (criando campo)
layer.startEditing()
layer.addAttribute(QgsField('x', QVariant.Double))
layer.commitChanges()


count = 0
for feature in layer.getFeatures():
    while count < 5:
        print(feature.geometry().asPoint()[0])
        count += 1
        
        
# Atribuindo valor X (latitude) a todos os campos
layer.startEditing()
for feature in layer.getFeatures():
    id = feature.id()
    x = feature.geometry().asPoint()[0]
    attr_value = {14:x}
    layer.changeAttributeValues(id, attr_value)

layer.commitChanges()



layer.startEditing()
layer.addAttribute(QgsField('y', QVariant.Double))
layer.commitChanges()

layer.startEditing()
for feature in layer.getFeatures():
    id = feature.id()
    y = feature.geometry().asPoint()[1]
    attr_value = {15:y}
    layer.changeAttributeValues(id, attr_value)

layer.commitChanges()


