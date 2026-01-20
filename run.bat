:: echo off is used to don't show the command being executed
@echo off
title Pytest Automation Script (OrangeHRM Project)

:: Check if virtual environment exists and activate it
echo Checking and activating virtual environment...
if exist .venv\Scripts\activate.bat (
    call .venv\Scripts\activate
    echo Virtual environment activated from .venv
) else if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate
    echo Virtual environment activated from venv
) else (
    echo Virtual environment not found!
    echo Please create a virtual environment and install the required packages.
    pause
    exit /b     rem /b to exit the batch script without closing the command prompt
)

:: Select the test type
:SELECT_TEST_TYPE     rem Label for test type selection
echo.
echo SELECT TEST TYPE:
echo =============================================
echo 0. Exit
echo 1. Run All Test files
echo 2. Run Tests by Marker Sanity
echo 3. Run Tests by Marker Regression
echo 4. Run Tests by Marker Sanity and Regression
echo =============================================
set /p testType=Enter your choice (0 ~ 4):

if "%testType%" == "0" goto EXIT
if "%testType%" == "1" (
    set MARKER=
    goto SELECT_BROWSER
)
if "%testType%" == "2" (
    set MARKER=sanity
    goto SELECT_BROWSER
)
if "%testType%" == "3" (
    set MARKER=regression
    goto SELECT_BROWSER
)
if "%testType%" == "4" (
    set MARKER=sanity and regression
    goto SELECT_BROWSER
)
:: back to test type selection on invalid input
echo.
echo Invalid selection! Please try again.
pause
goto SELECT_TEST_TYPE

:: Select the browser
:SELECT_BROWSER     rem Label for browser selection
echo.
echo SELECT BROWSER:
echo =============================================
echo 0. Back to Test Type Selection
echo 1. Chrome
echo 2. Edge
echo 3. Firefox
echo =============================================
set /p browserChoice=Enter your choice (1 ~ 3):

if "%browserChoice%" == "0" goto SELECT_TEST_TYPE
if "%browserChoice%" == "1" (
    set BROWSER=chrome
    goto RUN_TESTS
)
if "%browserChoice%" == "2" (
    set BROWSER=edge
    goto RUN_TESTS
)
if "%browserChoice%" == "3" (
    set BROWSER=firefox
    goto RUN_TESTS
)
:: back to browser selection on invalid input
echo.
echo Invalid selection! Please try again.
pause
goto SELECT_BROWSER

:: Run the tests based on user selections
:RUN_TESTS     rem Label for running tests
echo.
echo Running tests with:
if "%MARKER%" == "" (
    echo Test Type: All
) else (
    echo Marker: %MARKER%
)
echo Browser: %BROWSER%
echo.

if "%MARKER%" == "" (
    pytest -s -v --browser %BROWSER% --html "reports\report_all_%BROWSER%.html"
) else (
    pytest -s -v --browser %BROWSER% --html "reports\report_%MARKER%_%BROWSER%.html" -m "%MARKER%"
)

pause
goto SELECT_TEST_TYPE   rem After running tests, go back to test type selection

:: Exit
:EXIT   rem Label for exit
echo.
echo Exiting Pytest Automation Script (OrangeHRM Project)...
pause
exit /b