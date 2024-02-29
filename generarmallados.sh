#!/bin/bash
#Miguel Rosas

Re1=1000
Re2=2300
Re3=3000
Re4=4000
Re5=5000
Re6=6000

nu=0.00001562
d=5

# Calcular k utilizando bc para manejar decimales
k=$(echo "$nu / $d" | bc -l)

# Calcular v1, v2, v3, v4, v5 con bc para manejar decimales
v1=$(echo "$Re1 * $k" | bc -l)
v2=$(echo "$Re2 * $k" | bc -l)
v3=$(echo "$Re3 * $k" | bc -l)
v4=$(echo "$Re4 * $k" | bc -l)
v5=$(echo "$Re5 * $k" | bc -l)
v6=$(echo "$Re6 * $k" | bc -l)

# Lista de valores para lc
valores_lc=("$v1" "$v2" "$v3" "$v4" "$v5" "$v6")

# Verifica si se proporciona la cantidad como argumento
if [ $# -eq 0 ]; then
	echo "Uso: $0 cantidad"
	exit 1
fi

# Obtiene la cantidad desde el primer argumento
cantidad=$1

# Bucle para crear y mover carpetas, editar y genrar mallado
for ((i = 1; i <= $cantidad; i++)); do
	# Genera el nombre de la carpeta
	nombre_carpeta="Case_$i"

	# Crea la carpeta del caso
	mkdir "$nombre_carpeta"

	# Copia carpetas del caso dentro de las carpetasgeneradas
	cp -r "Case_0/0/" "$nombre_carpeta/"
	cp -r "Case_0/constant/" "$nombre_carpeta/"
	cp -r "Case_0/system/" "$nombre_carpeta/"
	cp "Case_0/script_paraview.py" "$nombre_carpeta/script_paraview_case_$i.py"
	cp "Case_0/script_paraview_PlotU1.py" "$nombre_carpeta/script_paraview_PlotU1_case_$i.py"
	cp "Case_0/script_paraview_PlotU2.py" "$nombre_carpeta/script_paraview_PlotU2_case_$i.py"
	# Utilizar sed para reemplazar todas las instancias de $i por i en el archivo
	valor_i=$i
	sed -i "s/\$i/$valor_i/g" "Case_$i/script_paraview_case_$i.py"
	sed -i "s/\$i/$valor_i/g" "Case_$i/script_paraview_PlotU1_case_$i.py"
	sed -i "s/\$i/$valor_i/g" "Case_$i/script_paraview_PlotU2_case_$i.py"

	# Copia un archivo dentro de la carpeta
	archivo_geo="Case_0/geometry.geo"
	archivo_geoi="geometry_Case_$i.geo"
	touch "$archivo_geo"
	cp "$archivo_geo" "$nombre_carpeta/$archivo_geoi"

	# Realiza el intercambio en el archivo
	valor_v="${valores_lc[i - 1]}"
	sed -i "s/\$v/$valor_v/g" "$nombre_carpeta/0/U"

	#Generar mallado gmsh
	cd "$nombre_carpeta/"
	gmsh "$archivo_geoi" -3

	#Genera mallado OpenFoam
	gmshToFoam "geometry_Case_$i.msh"

	# Utiliza grep para eliminar las líneas que contienen la palabra "physicalType" y sobrescribe el archivo original
	grep -v "physicalType" constant/polyMesh/boundary >constant/polyMesh/boundary.temp
	mv constant/polyMesh/boundary.temp constant/polyMesh/boundary

	# Reemplaza "patch" por "wall" en las líneas 35
	sed -i '35s/patch/wall/;' "constant/polyMesh/boundary"

	# Reemplaza "patch" por "empty" en las líneas 23
	sed -i '23s/patch/empty/;' "constant/polyMesh/boundary"

	decomposePar
	mpirun -np 6 icoFoam -parallel

	reconstructPar
	foamToVTK

	rm -rR processor*

	pvbatch "script_paraview_case_$i.py"
	pvbatch "script_paraview_PlotU1_case_$i.py"
	pvbatch "script_paraview_PlotU2_case_$i.py"

	mv "animation_case_$i.ogv" ".."
	mv "animation_PlotU1_case_$i.ogv" ".."
	mv "animation_PlotU2_case_$i.ogv" ".."
	mv "constant/" ".."
	mv "0/" ".."
	mv "geometry_Case_$i.geo" ".."
	mv "geometry_Case_$i.msh" ".."
	mv "system/" ".."
	mv "VTK/" ".."
	mv "script_paraview_case_$i.py" ".."
	mv "script_paraview_PlotU1_case_$i.py" ".."
	mv "script_paraview_PlotU2_case_$i.py" ".."

	cd ..

	rm -rR "Case_$i/"

	# Crea la carpeta del caso
	mkdir "$nombre_carpeta"

	mv "animation_case_$i.ogv" "$nombre_carpeta/"
	mv "animation_PlotU1_case_$i.ogv" "$nombre_carpeta/"
	mv "animation_PlotU2_case_$i.ogv" "$nombre_carpeta/"
	mv "constant/" "$nombre_carpeta/"
	mv "0/" "$nombre_carpeta/"
	mv "geometry_Case_$i.geo" "$nombre_carpeta/"
	mv "geometry_Case_$i.msh" "$nombre_carpeta/"
	mv "system/" "$nombre_carpeta/"
	mv "VTK/" "$nombre_carpeta/"
	mv "script_paraview_case_$i.py" "$nombre_carpeta/"
	mv "script_paraview_PlotU1_case_$i.py" "$nombre_carpeta/"
	mv "script_paraview_PlotU2_case_$i.py" "$nombre_carpeta/"
done

echo "Proceso completado."
