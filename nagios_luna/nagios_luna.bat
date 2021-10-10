REM author			: @g0vandS, Govand Sinjari
REM license           : MIT


@echo off
setlocal EnableDelayedExpansion
rem **********************************************************************************************
rem This scrip will check LUNA label using lunacm command, the bad luna returns no label 
rem Ver 1.2 date 03/21/2012 By Govand Sinjari
rem **********************************************************************************************
rem How to install:
rem 1- Add luna.bat to NSClient scripts folder
rem 2- Add this entry to NSC.ini: nrpe_luna=scripts\luna.bat
rem 3- Restart NSClient Services
rem 4- Add the check to Nagios
rem **********************************************************************************************

lunacm -c hsm showinfo | find "CKR_DEVICE_ERROR" /c >lunaTmpFile
SET /p lunacmvar=<lunaTmpFile
DEL lunatmpFile
if %lunacmvar% NEQ 0 (goto :LunaError)
lunacm -c hsm showinfo | find "HSM Label"  >lunaTmpFile
SET /p lunacmvar=<lunaTmpFile
DEL lunatmpFile

rem echo Result of: "%lunacmvar%"

set result=OK: LUNA is GOOD
set badluna="  HSM Label ->"
if %badluna% == %lunacmvar% (goto :LunaError)
lunacm -c hsm showinfo | find "HSM Label" >lunaTmpFile
SET /p lunacmvar=<lunaTmpFile
DEL lunaTmpFile
echo OK: LunaCM shows no errors
echo %lunacmvar%
exit /b 0

:LunaError
echo CRITICAL: LUNA is BAD, please run "lunacm -c hsm reset " and restart apps service
exit /b 2