import routes
import os

def convert(page_num):

  import markdown
  import codecs

  code_list = []

  for n in range(getFileNum(page_num),0,-1):
    md_file = routes.app.open_resource('static/posts/'+page_num+'/post'+str(n)+'.md')
    u_mdfile = md_file.read().decode('utf-8')
    code_list.append(markdown.markdown(u_mdfile))

  return code_list


def getPages():
  path, dirs, files = next(os.walk('/home/jmyang/www/routes/static/posts/'))
  num = len(dirs)
  return num



def getFileNum(page_num):
  path, dirs, files = next(os.walk('/home/jmyang/www/routes/static/posts/'+page_num+'/'))
  num = len(files)
  return num


