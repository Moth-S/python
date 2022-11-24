# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

numberCoordinateQuarter = int(input('Номер координатной четверти: '))

if numberCoordinateQuarter == 1:
    print('x,y -> [0, +беск.)')
elif numberCoordinateQuarter == 2:
    print('x -> (-беск., 0], y -> [0, +беск.)')
elif numberCoordinateQuarter == 3:
    print('x,y -> (-беск., 0]')
else:
    print('y -> [0, +беск.), x -> (-беск., 0]')
