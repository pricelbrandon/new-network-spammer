@echo off
:START
setlocal EnableDelayedExpansion
rem huehuehueLETSFUCKINGOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
rem generates random SSID, removes need for wordlists
set "chars=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
set "SSID="
for /l %%i in (1,1,8) do (
    set /a "rand=!random! %% 62"
    for %%j in (!rand!) do set "char=!chars:~%%j,1!"
    set "SSID=!SSID!!char!"
)

rem generates random password
set "chars=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%%^&*()-_+=?"
set "Password="
for /l %%i in (1,1,12) do (
    set /a "rand=!random! %% 68"
    for %%j in (!rand!) do set "char=!chars:~%%j,1!"
    set "Password=!Password!!char!"
)

echo Starting Ad-hoc Network with SSID: !SSID! and Password: !Password! 

rem start Ad-hoc network
netsh wlan set hostednetwork mode=allow ssid=!SSID! key=!Password! keyUsage=persistent > nul
netsh wlan start hostednetwork > nul

rem wait for a minnymin
timeout /t 60 /nobreak > nul

rem stop Ad-hoc network
netsh wlan stop hostednetwork > nul

echo Ad-hoc Network stopped.

goto START