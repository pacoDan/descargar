@echo off
setlocal

set "AUDIO=audio.mp3"

if not exist "%AUDIO%" (
    echo ERROR: No se encuentra audio.mp3
    pause
    exit /b 1
)

for %%F in (*.mp4 *.avi *.mkv *.mov *.wmv *.flv *.webm *.m4v) do (
    if exist "%%F" (
        if /i not "%%~nF"=="%%~nF_con_audio" (
            echo.
            echo Procesando: %%F

            ffmpeg -hide_banner -loglevel error -y ^
            -i "%%F" -i "%AUDIO%" ^
            -map 0:v:0 -map 1:a:0 ^
            -c:v copy -c:a aac -b:a 192k ^
            -shortest "%%~nF_con_audio%%~xF"
        )
    )
)

echo.
echo Todos los videos han sido procesados.
pause