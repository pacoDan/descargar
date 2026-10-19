$extensiones = @(".mp4", ".mkv", ".avi", ".mov", ".webm", ".wmv", ".flv", ".m4v", ".mpeg", ".mpg")

Get-ChildItem -File |
    Where-Object {
        $_.Extension.ToLowerInvariant() -in $extensiones -and
        $_.BaseName -notlike "*_amplificado"
    } |
    ForEach-Object {
        $video = $_
        $salida = Join-Path $video.DirectoryName "$($video.BaseName)_amplificado.wav"

        if (Test-Path $salida) {
            Write-Host "OMITIDO: ya existe $salida" -ForegroundColor Yellow
            return
        }

        Write-Host "`nProcesando: $($video.Name)" -ForegroundColor Cyan

        ffmpeg -n -i $video.FullName `
            -map 0:a:0 `
            -vn `
            -af "volume=6dB" `
            -c:a pcm_s16le `
            $salida

        if ($LASTEXITCODE -eq 0) {
            Write-Host "Correcto: $salida" -ForegroundColor Green
        } else {
            Write-Host "ERROR al procesar: $($video.Name)" -ForegroundColor Red
        }
    }

Write-Host "`nProceso terminado."