from cx_Freeze import setup, Executable

base = None    

executables = [Executable("DC.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<DirCleaner",
    options = options,
    version = "1.0.0",
    description = 'Deletes all empty directories within a directory',
    executables = executables
)
