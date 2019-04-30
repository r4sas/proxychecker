@echo off
title Checking tunnels...
SET PY_PYTHON=3

for %%X in (python3.exe) do (set FOUND=%%~$PATH:X)
if defined FOUND (
	set xPy=%FOUND%
	goto RUN_CHECK
)

for %%X in (python.exe) do (set FOUND=%%~$PATH:X)
if defined FOUND (
	%FOUND% -c "import sys; print(sys.version_info[0])" | find "3" >nul && set xyes=1 || set xyes=0
	if "%xyes%" == 1 (
		set xPy=%FOUND%
		goto RUN_CHECK
	) else (
		echo Error: Python3 not found!
		pause
		exit
	)
) else (
	echo Error: Python3 not found!
	pause
	exit
)

:RUN_CHECK
%xPy% bin\checker.py

echo Done...
pause > nul