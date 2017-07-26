import mykey
import flickrapi

def getPhotos(photos_per_page, page_num):

  # should put your own auth_key from flickr api
  api_key = mykey.key
  api_secret = mykey.secret
  content_type = '7'

  flickr = flickrapi.FlickrAPI(api_key, api_secret, content_type, format='parsed-json')
  extras = 'url_sq,url_t,url_s,url_q,url_m,url_n,url_z,url_c,url_l,url_o'
  # should put your own user_id from flickr
  my = flickr.photos.search(user_id=mykey.u_id, per_page=photos_per_page, extras=extras, page=page_num)
  items = my['photos']

  o_photos = []
  m_photos = []
  for photo in items[u'photo']:
    o_photos.append(photo[u'url_o'])
    m_photos.append(photo[u'url_m'])

  return zip(o_photos, m_photos)


def getPages(photos_per_page):

  # should put your own auth_key from flickr api
  api_key = mykey.key
  api_secret = mykey.secret
  content_type = '7'

  flickr = flickrapi.FlickrAPI(api_key, api_secret, content_type, format='parsed-json')
  extras = 'url_sq,url_t,url_s,url_q,url_m,url_n,url_z,url_c,url_l,url_o'
  # should put your own user_id from flickr
  my = flickr.photos.search(user_id=mykey.u_id, per_page=photos_per_page, extras=extras)
  return my['photos']['pages']

