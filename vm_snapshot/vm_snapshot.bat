REM author      : @g0vandS, Govand Sinjari
REM # license           : MIT

@ECHO OFF
CLS
rem **********************************************************************************************
rem List/Create/Remove VM snapshots
rem Govand Sinjari
rem Ver 1.0 date 2016-10-19
rem Need VMware vSphere CLI 
rem **********************************************************************************************
echo ****************************************************
echo   This script will List/Create/Remove VM snapshot
echo ****************************************************
echo *
rem create getpwd.ps1 to hide password input
echo $password = Read-Host "*  Please enter ESXi password" -AsSecureString > getpwd.ps1
echo $password = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($password) >> getpwd.ps1
echo $password = [Runtime.InteropServices.Marshal]::PtrToStringAuto($password) >> getpwd.ps1
echo echo $password  >> getpwd.ps1

:MENU
SET /P ip=*  Please enter ESXi IP :
SET /P user=*  Please enter ESXi username :
for /f "delims=" %%i in ('powershell -file getpwd.ps1') do set pass=%%i
echo *
echo *  Available Functions: 
echo *  Please press 0 to list VMs with snapshots
echo *  Please press 1 to Create VM snapshot
echo *  Please press 2 to Remove ALL VM's snapshots
echo *
SET /P action=*  Please select 0 or 1 or 2 or Any other key to EXIT:

IF "%ip%"=="" GOTO ERROR
IF "%user%"=="" GOTO ERROR
IF "%pass%"=="" GOTO ERROR
IF "%action%"=="" GOTO ERROR

IF %action% GTR 2 GOTO END
IF %action% LSS 0 GOTO END

echo ..... Getting VM list
vmware-cmd.pl --server %ip% -U %user% -P %pass% -l > vm.txt
echo ..... Done getting VM list

IF %action%==0 GOTO LISTVM
IF %action%==1 GOTO CREATE
IF %action%==2 GOTO REMOVE

GOTO END

rem for /f %%j in (vm.txt) do @echo %%j
:LISTVM
REM List VMs with snapshots
for /f %%j in (vm.txt) do ( 
echo %%j
vmware-cmd.pl --server %ip% -U %user% -P %pass% %%j hassnapshot
)
GOTO END

:CREATE
REM Create snapshots
set hh=%time:~-11,2%
set /a hh=%hh%+100
set hh=%hh:~1%
Set DATEX=%date:~10,4%_%date:~4,2%_%date:~7,2%_%hh%:%time:~3,2%:%time:~6,2%
REM createsnapshot  <name> <description> <quiesce> <memory>
for /f %%j in (vm.txt) do vmware-cmd.pl --server %ip% -U %user% -P %pass% "%%j" createsnapshot "Snapshot_%DATEX%" "Snapshot by Script" 1 0

GOTO END


:REMOVE
REM Remove snapshots
for /f %%j in (vm.txt) do vmware-cmd.pl --server %ip% -U %user% -P %pass% "%%j" removesnapshots

GOTO END

:ERROR
ECHO *  IP or Username or Password or Function can't be NULL !!
pause
GOTO MENU

:END
REM delete getpwd.ps1 & vm.txt
del getpwd.ps1
del vm.txt

echo ..... Done