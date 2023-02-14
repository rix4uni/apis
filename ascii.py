# import pyfiglet

# fig = pyfiglet.Figlet()

# for font in fig.getFonts():
#     print(pyfiglet.figlet_format("SubDog", font=font, justify="left"))

from flask import Flask, render_template, request
import pyfiglet

app = Flask(__name__)
fig = pyfiglet.Figlet()

@app.route('/')
def font_display():
    fonts = fig.getFonts()
    return render_template('index.html', fonts=fonts)

@app.route('/display', methods=['POST'])
def display_font():
    text = request.form['text']
    font = request.form['font']
    ascii_text = pyfiglet.figlet_format(text, font=font, justify="left")
    return '''
    <pre>
    {}
    </pre>
    '''.format(ascii_text)

if __name__ == '__main__':
    app.run()
