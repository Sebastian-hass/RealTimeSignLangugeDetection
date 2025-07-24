@echo off
cd /d "%~dp0Tensorflow\models\research"
echo Compilando archivos .proto...

for %%F in (object_detection\protos\*.proto) do (
    echo Compilando %%F
    protoc %%F --python_out=.
)

echo ¡Listo! Verifica la carpeta object_detection\protos
pause