from flask import Flask, render_template, request, Response
import flickrphoto 
import mdparser
import requests
import mykey
from functools import wraps

app = Flask(__name__)

# for basic authentication
def check_auth(username, password):
   return username == mykey.name and password == mykey.pwd

def authenticate():
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/')
def home():
  iname, intro = mdparser.getLtstFile()
  return render_template('home.html', iname=iname, intro=intro)

@app.route('/secret')
@requires_auth
def secret_page():

  md_personals = mdparser.convert_prs()
  return render_template('personal.html', md_personals=md_personals)

@app.route('/board')
def board():
  
  pages = mdparser.getPages('posts')
  page_n = (pages // 5) + 1
  page_r = pages % 5
  
  md_posts = mdparser.convert('1')
  return render_template('post.html', md_posts=md_posts, pages=pages, page_n=page_n, page_r=page_r, page_num=1)

@app.route('/board/<string:page_num>')
def board_page(page_num):
 
  # exception handling
  if page_num == None:
    return board()
  elif not page_num.isdigit():
    return render_template('error.html')

  else:
    # total page numbers
    pages = mdparser.getPages('posts')
    page_n = (pages // 5) + 1
    page_r = pages % 5
 
    if (int(page_num) > 0) and (int(page_num) <= pages):
      md_posts = mdparser.convert(page_num)
      return render_template('post.html', md_posts=md_posts, pages=pages, page_n=page_n, page_r=page_r, page_num=int(page_num))
    else:
      return render_template('error.html')

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

  # exception handling
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

@app.route('/review/<string:page_num>')
def review_item(page_num):

  # exception handling
  if page_num == None:
    return board()
  elif not page_num.isdigit():
    return render_template('error.html')

  else:
    # total page numbers
    pages = mdparser.getPages_rev()
    page_n = (pages // 5) + 1
    page_r = pages % 5
 
    if (int(page_num) > 0) and (int(page_num) <= pages):
      md_reviews = mdparser.convert_rev(page_num)
      md_images = mdparser.convert_rev_img(page_num)
      return render_template('review_item.html', md_reviews_pair=zip(md_images, md_reviews), pages=pages, page_n=page_n, page_r=page_r, page_num=int(page_num))
    else:
      return render_template('error.html')

@app.route('/review')
def review():

  pages = mdparser.getPages_rev()
  page_n = (pages // 5) + 1
  page_r = pages % 5

  md_images = mdparser.convert_rev_img('1')
  md_reviews = mdparser.convert_rev('1')
  return render_template('review_item.html', md_reviews_pair=zip(md_images, md_reviews), pages=pages, page_n=page_n, page_r=page_r, page_num=1)

@app.route('/article/<string:aname>')
def article(aname):

  article = mdparser.getArticle(aname)

  return render_template('article_item.html', article=article, aname=aname) 

if __name__ == '__main__':
  app.run(debug=True)
  
