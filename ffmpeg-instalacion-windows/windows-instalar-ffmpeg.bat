
@echo off
setlocal

set "BASE=%USERPROFILE%\.desarrollo"
set "DESTINO=%BASE%\ffmpeg"
set "ZIP=%~dp0ffmpeg-master-latest-win64-gpl-shared.zip"

echo ==========================================
echo Instalacion de FFmpeg
echo ==========================================

if not exist "%ZIP%" (
    echo ERROR: No se encuentra el ZIP:
    echo "%ZIP%"
    pause
    exit /b 1
)

if not exist "%BASE%" mkdir "%BASE%"
if not exist "%DESTINO%" mkdir "%DESTINO%"

echo.
echo Extrayendo ZIP con PowerShell nativo de Windows...
echo Destino: "%DESTINO%"
echo.

powershell -NoProfile -ExecutionPolicy Bypass -Command ^
 "$ErrorActionPreference = 'Stop'; Expand-Archive -LiteralPath $env:ZIP -DestinationPath $env:DESTINO -Force"

if errorlevel 1 (
    echo.
    echo ERROR: No se pudo extraer el ZIP.
    pause
    exit /b 1
)

echo Buscando ffmpeg.exe...

set "BIN="

for /r "%DESTINO%" %%F in (ffmpeg.exe) do (
    if /i "%%~dpF"=="%DESTINO%\bin\" set "BIN=%%~dpF"
)

if not defined BIN (
    for /r "%DESTINO%" %%F in (ffmpeg.exe) do (
        if exist "%%~dpFffprobe.exe" (
            set "BIN=%%~dpF"
            goto :ENCONTRADO
        )
    )
)

:ENCONTRADO
if not defined BIN (
    echo ERROR: No se encontro ffmpeg.exe y ffprobe.exe.
    echo Revisa la estructura del ZIP.
    pause
    exit /b 1
)

echo.
echo Carpeta bin encontrada: "%BIN%"
echo Agregando al PATH del usuario...

powershell -NoProfile -ExecutionPolicy Bypass -Command ^
 "$ErrorActionPreference = 'Stop';" ^
 "$bin = [IO.Path]::GetFullPath($env:BIN).TrimEnd('\');" ^
 "$old = [Environment]::GetEnvironmentVariable('Path','User');" ^
 "$parts = @($old -split ';' | Where-Object { $_.TrimEnd('\') -ine $bin });" ^
 "$new = (@($parts | Where-Object { $_ }) + $bin) -join ';';" ^
 "[Environment]::SetEnvironmentVariable('Path', $new, 'User')"

if errorlevel 1 (
    echo ERROR: No se pudo actualizar el PATH.
    pause
    exit /b 1
)

echo.
echo ==========================================
echo FFmpeg instalado correctamente.
echo ==========================================
echo Ubicacion: "%DESTINO%"
echo Ejecutable: "%BIN%ffmpeg.exe"
echo.
echo Cierra y abre CMD nuevamente y ejecuta:
echo ffmpeg -version
echo.

pause
exit /b 0