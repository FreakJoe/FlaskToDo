import os, sass
from config import basedir

def compile_sass():
	for root, dirs, files in os.walk(basedir):
		for f in files:
			if f.endswith(".scss"):
				sass_file = os.path.join(root, f)
				scss = open(sass_file).read()

				css_file = sass_file.replace(".scss", ".css")
				css = ''
				if scss is not '':
					css = sass.compile(string=scss)
					
				open(css_file, 'w').write(css)