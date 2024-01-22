from shapely.geometry import Polygon

# Задайте координаты полигона
coordinates = [[[53.97930, 78.36354], [52.86596, 78.46006], [52.89925, 81.67985], [55.05971, 81.58333], [54.99648, 80.07340], [54.54308, 78.94958], [53.97930, 78.36354]]]

# Создайте объект полигона с помощью Shapely
polygon = Polygon(coordinates[0])

# Получите координаты внешнего контура полигона
external_coordinates = list(polygon.exterior.coords)

# Получите координаты внутренних контуров (дырок), если они есть
internal_coordinates = [list(interior.coords) for interior in polygon.interiors]
print(f"Это координаты внутренних контуров: {internal_coordinates}")

# Объедините внешние и внутренние координаты
all_coordinates = external_coordinates + internal_coordinates

# Выведите результат
print(all_coordinates)
