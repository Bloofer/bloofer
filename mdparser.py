import routes
import os

def convert(page_num):

  import markdown
  import codecs

  code_list = []

  # p_num is a variable used for sorting the order (latest first)
  p_num = getPages() - int(page_num) + 1

  # last page file number (latest)
  lp_fnum = getFileNum(str(getPages()))

  # if having 8 posts on latest page, originally renders 8 posts per page
  if lp_fnum == 8:
    for n in range(getFileNum(str(p_num)),0,-1):
      md_file = routes.app.open_resource('static/posts/'+str(p_num)+'/post'+str(n)+'.md')
      u_mdfile = md_file.read().decode('utf-8')
      code_list.append(markdown.markdown(u_mdfile))

    return code_list

  # if not, on the latest page, pulls and gauges the lacking number of files to 8 posts per page
  else:
    # on the latest page
    if int(p_num) == getPages():

      # case total page num is 1
      if getPages() == 1:
        for n in range(getFileNum(str(p_num)),0,-1):
          md_file = routes.app.open_resource('static/posts/'+str(p_num)+'/post'+str(n)+'.md')
          u_mdfile = md_file.read().decode('utf-8')
          code_list.append(markdown.markdown(u_mdfile))

        return code_list

      # normal case
      else:
        for n in range(getFileNum(str(p_num)),0,-1):
          md_file = routes.app.open_resource('static/posts/'+str(p_num)+'/post'+str(n)+'.md')
          u_mdfile = md_file.read().decode('utf-8')
          code_list.append(markdown.markdown(u_mdfile))

        for n in range(getFileNum(str(p_num-1)),lp_fnum,-1):
          md_file = routes.app.open_resource('static/posts/'+str(p_num-1)+'/post'+str(n)+'.md')
          u_mdfile = md_file.read().decode('utf-8')
          code_list.append(markdown.markdown(u_mdfile))

        return code_list

    # pages neither first(latest), nor last(oldest). (middle pages)
    elif (int(p_num) < getPages()) and (int(p_num) > 1):
      for n in range((lp_fnum+1),0,-1):
        md_file = routes.app.open_resource('static/posts/'+str(p_num)+'/post'+str(n)+'.md')
        u_mdfile = md_file.read().decode('utf-8')
        code_list.append(markdown.markdown(u_mdfile))

      for n in range(getFileNum(str(p_num)),lp_fnum,-1):
        md_file = routes.app.open_resource('static/posts/'+str(p_num-1)+'/post'+str(n)+'.md')
        u_mdfile = md_file.read().decode('utf-8')
        code_list.append(markdown.markdown(u_mdfile))

      return code_list

    # on the oldest page
    else:
      for n in range((lp_fnum),0,-1):
        md_file = routes.app.open_resource('static/posts/'+str(p_num)+'/post'+str(n)+'.md')
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
 

