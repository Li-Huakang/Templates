@echo off
for %%i in (*.svg) do (
echo %%i
inkscape --export-type="emf" %%i
rem inkscape %%i -M %%~ni.emf
rem inkscape %%i -A %%~ni.pdf
)
@echo Finished