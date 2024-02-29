lc = 0.1;
//+
Point(1) = {0, 0, 0,lc};
//+
Point(2) = {8, 0, 0,lc};
//+
Point(3) = {8, 5, 0,lc};
//+
Point(4) = {0, 5, 0,lc};
//+
Line(1) = {1, 2};
//+
Line(2) = {2, 3};
//+
Line(3) = {3, 4};
//+
Line(4) = {4, 1};
//+
Point(5) = {2, 2.5, 0,lc};
//+
Point(6) = {1.5, 2.5, 0,lc};
//+
Point(7) = {1, 2.5, 0,lc};
//+
Point(8) = {1.5, 3, 0,lc};
//+
Point(9) = {1.5, 2, 0,lc};
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
Extrude {0, 0, 0.1} {
  Surface{2}; 
}
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
Show "*";
