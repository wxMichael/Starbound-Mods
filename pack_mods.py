import os
import subprocess

if not os.path.isdir('_packed'):
	os.mkdir('_packed')

for item in os.scandir():
	if item.is_dir() and not item.name.startswith(('.', '_')):
		subprocess.call([r'C:\Program Files (x86)\Steam\steamapps\common\Starbound\win32\asset_packer.exe', item.name, '_packed\\' + item.name + '.pak'])

os.system('pause')
