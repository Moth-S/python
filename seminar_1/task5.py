# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

point_coordinates_1=input("Coordinates point 1(through space):")
point_coordinates_2=input("Coordinates point 2(through space):")

point1=point_coordinates_1.split()
point2=point_coordinates_2.split()

distance=((int(point1[0])-int(point2[0]))**2 + (int(point2[1])-int(point1[1]))**2)**0.5
print(f"distance {round(distance,2)}")