## Установить пути к функциям построения интервальной регрессии
addpath(genpath('./IntLinInc3D'))
# Чтение координат поворота из файла
data = dlmread("gold_turn_00_0_4.txt", " ")

x = data(:,1)                             # координата поворота по х
y = data(:,2)                             # координата поворота по у
eps = data(:,3)                           # верхняя граница ошибки для y_i

# x^2 + x^1 + x^0
X_up = [ x.^0 x x.^2 ]       
X_down = [ x.^0 x x.^2 ] 

y_up = [y+eps]
y_down = [y-eps]

OrientPoints = 1
transparency = 1
EqnTol3D(X_down,X_up,y_down,y_up,OrientPoints,transparency)