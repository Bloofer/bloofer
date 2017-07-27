from flask import Flask, render_template
import flickrphoto 

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/board')
def board():
  return render_template('board.html')

@app.route('/gallery')
def gallery():

  photos = flickrphoto.getPhotos('12', 1)

  # total page numbers
  pages = flickrphoto.getPages('12')
  page_n = (pages // 5) + 1
  page_r = pages % 5

  return render_template('photo.html', r1_photo=photos[0:4], r2_photo=photos[4:8], r3_photo=photos[8:12], pages=pages, page_n=page_n, page_r=page_r, page_num=1)

@app.route('/gallery/<string:page_num>')
def gallery_page(page_num):

  if page_num == None:
    return gallery()

  elif not page_num.isdigit():
    return render_template('error.html')

  else:
    photos = flickrphoto.getPhotos('12', int(page_num))

    # total page numbers
    pages = flickrphoto.getPages('12')
    page_n = (pages // 5) + 1
    page_r = pages % 5

    if (int(page_num) > 0) and (int(page_num) <= pages):
      return render_template('photo.html', r1_photo=photos[0:4], r2_photo=photos[4:8], r3_photo=photos[8:12], pages=pages, page_n=page_n, page_r=page_r, page_num=int(page_num))
    else:
      return render_template('error.html')

@app.route('/profile')
def profile():
  return render_template('profile.html')

@app.route('/review')
def review():
  return render_template('review.html')

if __name__ == '__main__':
  app.run(debug=True)
  
