def gen_actor_info(actorlist: list) -> str:
    actor_info = ''
    for actor in actorlist:
        actor_info += f'''  <actor>
  <name>{actor['name']}</name>
  <type>Actor</type>
  <thumb>{actor['thumb']}</thumb>
  <profile>{actor['profile']}</profile>
  </actor>
'''
    return actor_info


def gen_tag_info(taglist: list) -> str:
    tag_info = ''
    for tag in taglist:
        tag_info += f'''  <tag>{tag}</tag>
'''
    return tag_info


def gen_genre_info(genrelist: list) -> str:
    genre_info = ''
    for genre in genrelist:
        genre_info += f'''  <genre>{genre}</genre>
'''
    return genre_info


def gen_nfo(nfo_dict: dict) -> str:
    title = nfo_dict['title']
    originaltitle = nfo_dict['originaltitle']
    sorttitle = nfo_dict['sorttitle']
    year = nfo_dict['year']
    releasedate = nfo_dict['releasedate']
    country = nfo_dict['country']
    countrycode = nfo_dict['countrycode']
    bvid = nfo_dict['bvid']
    poster = nfo_dict['poster']
    plot = nfo_dict['plot']
    actor_info = gen_actor_info(nfo_dict['actor'])
    tag_info = gen_tag_info(nfo_dict['tag'])
    genre_info = gen_genre_info(nfo_dict['genre'])
    original_filename = nfo_dict['original_filename']
    nfo_temp = f'''<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<movie>
  <plot><![CDATA[{plot}]]></plot>
  <outline />
  <lockdata>false</lockdata>
  <title>{title}</title>
  <originaltitle>{originaltitle}</originaltitle>
{actor_info}
  <year>{year}</year>
  <sorttitle>{sorttitle}</sorttitle>
  <mpaa>PG</mpaa>
  <releasedate>{releasedate}</releasedate>
  <country>{country}</country>
  <countrycode>{countrycode}</countrycode>
{tag_info}
{genre_info}
  <id>{bvid}</id>
  <art>
    <poster>{poster}</poster>
  </art>
  <isuserfavorite>false</isuserfavorite>
  <playcount>0</playcount>
  <watched>false</watched>
  <original_filename>{original_filename}</original_filename>
</movie>'''
    return nfo_temp