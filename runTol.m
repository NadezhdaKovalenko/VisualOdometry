## ���������� ���� � �������� ���������� ������������ ���������
addpath(genpath('./IntLinInc3D'))
# ������ ��������� �������� �� �����
data = dlmread("gold_turn_00_0_4.txt", " ")

x = data(:,1)                             # ���������� �������� �� �
y = data(:,2)                             # ���������� �������� �� �
eps = data(:,3)                           # ������� ������� ������ ��� y_i

# x^2 + x^1 + x^0
X_up = [ x.^0 x x.^2 ]       
X_down = [ x.^0 x x.^2 ] 

y_up = [y+eps]
y_down = [y-eps]

OrientPoints = 1
transparency = 1
EqnTol3D(X_down,X_up,y_down,y_up,OrientPoints,transparency)