@echo off
if "%1" neq "" (
    if "%1" equ "install" (
        echo "Installing env..."
        REM create env --> activate env ---> install requirement
        call conda create --name images-excels python==3.9.0 anaconda -y
        call conda activate images-excels
        call pip install -r requirement.txt
    ) else if "%1" equ "ur" (
        echo "Updating requirement..."
        REM Just for update requirement
        call pip install -r requirement.txt
    ) else if "%1" equ "urf" (
        echo "Updating requirement file..."
        REM Just for update requirements file
        pip freeze | findstr /v "certifi" > requirements.txt
    ) else (
        if "%1" equ "run" (
            call python run.py
        ) else (
            echo "No one... %0 %1"
        )
    )
) else (
    REM Case when just want to activate environment
    echo "Activating env, to deactivate conda deactivate..."
    call conda activate images-excels
)