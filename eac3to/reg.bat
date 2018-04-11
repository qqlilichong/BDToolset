@echo off
rem Registra ASAudioHD.ax en DirectShow
regsvr32.exe ASAudioHD.ax
rem desRegistra ASAudioHD.ax de DirectShow (quitar el 'rem' siguiente)
rem regsvr32.exe /u ASAudioHD.ax