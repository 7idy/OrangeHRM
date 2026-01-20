:: echo off is used to don't show the command being executed
@echo off

:: Activate the virtual environment
call .venv\Scripts\activate

:: Run pytest with different options
pytest -s -v -m "sanity"
rem pytest -s -v -m "regression"
rem pytest -s -v -m "sanity and regression"
rem pytest -s -v -m "sanity or regression"
rem pytest -s -v -m "sanity" --html reports/report_sanity_edge.html --browser edge
rem pytest -s -v -m "sanity" --html reports/report_sanity_firefox.html --browser firefox

:: Pause the command prompt to see the results
pause