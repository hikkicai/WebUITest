from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__, template_folder='./')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        a = request.form['left']
        b = request.form['right']
        c = float(a) + float(b)
        return render_template('add.html', RESULT=str(c))
    return render_template('add.html')


if __name__ == "__main__":
    app.run()


# <!DOCTYPE html>
# <html lang="en">
#     <head>
#         <meta charset="utf-8">
#         <title>Calculator</title>
#     </head>
#     <body>
#
#         <div align="center" style="margin-top:30px">
#             <form method="POST" name = "form1">
#                 <input type="text" name = "left" placeholder = "left"/>+
#                 <input type="text" name = "right" placeholder = "right"/>=
#                 <input type="text" name = "result" placeholder = "result" readonly="readonly" value = "{{ RESULT }}"/>
#
#                 <input type="submit" value = "submit"/>
#             </form>
#         </div>
#
#     </body>
# </html>
