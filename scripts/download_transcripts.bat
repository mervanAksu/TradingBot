@echo off
REM Downloads English subtitles (no video) for every playlist on the ICT channel.
REM Run from Anaconda Prompt:  cd "%USERPROFILE%\OneDrive\Masaüstü\ICT-bot"  then  scripts\download_transcripts.bat
REM Safe to re-run: already downloaded videos are skipped (transcripts\_archive.txt).
chcp 65001 >nul
cd /d "%~dp0.."
yt-dlp --skip-download --write-subs --write-auto-subs --sub-langs en --sub-format vtt ^
  --ignore-errors --sleep-requests 1 --sleep-interval 3 --max-sleep-interval 6 ^
  --download-archive "transcripts\_archive.txt" ^
  -o "transcripts\%%(playlist_title)s\%%(playlist_index)03d - %%(upload_date)s - %%(title)s.%%(ext)s" ^
  "https://www.youtube.com/@InnerCircleTrader/playlists"
echo.
echo Bitti. Simdi temizleme:  python scripts\clean_vtt.py transcripts transcripts\_clean
pause
