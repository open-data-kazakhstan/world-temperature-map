import ee
import geemap

# Аутентификация и инициализация Earth Engine
ee.Initialize()

# Загрузка границ Казахстана
kazakhstan = ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017') \
    .filter(ee.Filter.eq('country_na', 'Kazakhstan'))

# Функция для получения идентификаторов изображений из коллекции
def get_image_ids(collection):
    image_ids = collection.aggregate_array('system:index')
    return image_ids

# Функция для создания мозаичного изображения для заданного года
def generate_mosaic(year):
    # Выбор продукта MODIS Land Surface Temperature
    modis_col = 'MODIS/061/MOD11A2'
    modis_collection = ee.ImageCollection(modis_col) \
        .filterBounds(kazakhstan) \
        .filterDate(str(year) + '-01-01', str(year) + '-12-31')

    # Вызов функции для получения идентификаторов изображений MODIS
    modis_image_ids = get_image_ids(modis_collection)

    # Создание мозаичного изображения на территории Казахстана
    mosaic_image = modis_collection.mosaic()

    # Вывод списка идентификаторов изображений MODIS в консоль
    print('MODIS Image IDs for year', year, ':', modis_image_ids.getInfo())

    # Отображение мозаичного изображения на карте
    vis_params = {
        'min': 13000.0,
        'max': 16500.0,
        'palette': ['040274', '040281', '0502a3', '0502b8', '0502ce', '0502e6',
                    '0602ff', '235cb1', '307ef3', '269db1', '30c8e2', '32d3ef',
                    '3be285', '3ff38f', '86e26f', '3ae237', 'b5e22e', 'd6e21f',
                    'fff705', 'ffd611', 'ffb613', 'ff8b13', 'ff6e08', 'ff500d',
                    'ff0000', 'de0101', 'c21301', 'a71001', '911003']
    }
    
    # Подгоните мозаичное изображение на территории Казахстана
    Map.addLayer(mosaic_image.select('LST_Day_1km'), vis_params, 'Image - ' + str(year))

    # Сохранение мозаичного изображения в файл
    # Закомментируйте этот блок при выборе подходящих изображений на карте для ускорения загрузки
    filename = "mosaic_" + str(year) + ".png"
    geemap.get_image_thumbnail(mosaic_image.select('LST_Day_1km'), filename, vis_params, dimensions=2000)
    geemap.show_image(filename)

# Создание карты
Map = geemap.Map()
Map.centerObject(kazakhstan, 4)
Map.setCenter(65.5, 47, 4)  # Уточнение центра карты
Map.addLayer(kazakhstan, {}, 'Kazakhstan')  # Добавление границ Казахстана на карту

# Итерация по годам и создание мозаичных изображений для каждого года
for year in range(2000, 2021):
    generate_mosaic(year)

Map.addLayerControl()  # Добавление элемента управления слоями на карту
Map
