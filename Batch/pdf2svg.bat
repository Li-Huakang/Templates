@echo off
for %%i in (*.pdf) do (
echo %%i
inkscape -D %%i  -o %%~ni.svg --export-latex
rem inkscape --export-type="emf" %%i
rem inkscape %%i -M %%~ni.emf
rem inkscape %%i -A %%~ni.pdf
)
@echo Finished