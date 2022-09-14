import folium


class MapMarker:
    
    def create_map(self, geojson_data: dict, payload: dict = None):
        
        loc = 'Geo Experiment Bangladesh'
        title_html = '''
             <h3 align="center" style="font-size:16px"><b>{}</b></h3>
             '''.format(loc)
        border_stule= {
            'color': 'green',
            'weight': 2,
            'fillColor': 'blue',
            'fillOpacity': 0.3
        }
        map_obj = folium.Map(location=[payload['latitude'], payload['longitude']], zoom_start=8)
        folium.GeoJson(geojson_data, name= payload['name'], style_function = lambda x: border_stule).add_to(map_obj)
        map_obj.get_root().html.add_child(folium.Element(title_html))
        map_obj.save("index.html")
        
    
    def save_map(self):
        pass
    
"""
Example of GEOJSON
object		{5}
    type	:	Feature
    id	:	test_layer_1_1.302
geometry		{2}
    type	:	MultiPolygon
	coordinates		[1]
    geometry_name	:	the_geom
properties		{9}
    ID_1	:	4
    NAME_1	:	Khulna
    ID_2	:	17
    NAME_2	:	Kushtia
    ID_3	:	45
    NAME_3	:	Kustia
    ID_4	:	302
    NAME_4	:	Mirpur
    VARNAME_4	:	Kushtia
"""