import subprocess
from pathlib import Path


local_folder=Path.cwd()


print(f'CWD: {local_folder}')

fiji_path = "/Applications/Fiji.app/Contents/MacOS/ImageJ-macosx"

SetFilePaths=local_folder / 'SetFilePathsMacro.ijm'

RunQAMacro = local_folder / 'RunQAMacro.ijm'
print(f'Macro_file: {RunQAMacro}')

# fiji_cmd = " ".join([str(fiji_path), "--headless", "-macro", str(macro_file)])
fiji_cmd_setup = ' '.join([str(fiji_path), "--headless", '-macro', str(SetFilePaths)])
#fiji_cmd_setup = ' '.join([str(fiji_path), '-macro', str(SetFilePaths)])
print(f'fiji_cmd_setup: {fiji_cmd_setup}')



fiji_cmd_run = ' '.join([str(fiji_path), '-macro', str(RunQAMacro)])
print(f'fiji_cmd_run: {fiji_cmd_run}')



subprocess.call(fiji_cmd_setup, shell=True)
subprocess.call(fiji_cmd_run, shell=True)
