from compile_sass import compile_sass
compile_sass()

from app import app
app.run(debug=False)