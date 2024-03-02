lc = 0.01;
//+
Point(1) = {0, 0, 0,lc};
//+
Point(2) = {1.5, 0, 0,lc};
//+
Point(3) = {1.5, .5, 0,lc};
//+
Point(4) = {0, .5, 0,lc};
//+
Line(1) = {1, 2};
//+
Line(2) = {2, 3};
//+
Line(3) = {3, 4};
//+
Line(4) = {4, 1};
//+
Point(5) = {.6, .25, 0,lc};
//+
Point(6) = {.55, .25, 0,lc};
//+
Point(7) = {.5, .25, 0,lc};
//+
Point(8) = {.55, .3, 0,lc};
//+
Point(9) = {.55, .2, 0,lc};
//+
Circle(5) = {8, 6, 7};
//+
Circle(6) = {7, 6, 9};
//+
Circle(7) = {9, 6, 5};
//+
Circle(8) = {5, 6, 8};
//+
Curve Loop(7) = {5, 6, 7, 8};
//+
Curve Loop(8) = {4, 1, 2, 3};
//+
Plane Surface(2) = {8,7};
//+
Transfinite Surface {1};
Recombine Surface {1};

Extrude {0, 0, 0.01} {
  Surface{2}; Layers{5}; Recombine; 
}
Transfinite Volume {1};
//+
Physical Surface("inlet", 25) = {21};
//+
Physical Surface("outlet", 27) = {29};
//+
Physical Volume("interior", 28) = {1};
//+
Physical Surface("sides", 29) = {50, 2};
//+
Physical Surface("Wall", 30) = {25, 33, 37, 41, 45, 49};
//+
Field[1] = Box;

Field[1].VIn = 0.01;

Field[1].XMin = 0.45;

Field[1].XMax = 1.5;

Field[1].YMin = 0.15;

Field[1].YMax = 0.35;

Field[1].ZMin = 0;

Field[1].ZMax = 0.01;

Background Field = 1;

Mesh 3;
