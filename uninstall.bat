@echo off
setlocal enabledelayedexpansion

for /f "delims=" %%i in (packages.txt) do (
    pip uninstall "%%i" -y
)

endlocal
