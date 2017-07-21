from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/board')
def board():
  return render_template('board.html')

@app.route('/gallery')
def gallery():
  return render_template('gallery.html')

@app.route('/profile')
def profile():
  return render_template('profile.html')

if __name__ == '__main__':
  app.run(debug=True)
