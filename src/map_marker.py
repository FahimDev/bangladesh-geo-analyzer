import folium


class MapMarker:
    """
    -- --
    """
    
    def create_map(self, geojson_data: dict, payload: dict = None):
        border_stule= {
            'color': 'green',
            'weight': 2,
            'fillColor': 'blue',
            'fillOpacity': 0.3
        }
        map_obj = folium.Map(location=[23.6850, 90.3563], zoom_start=8)
        folium.GeoJson(geojson_data, name= 'Bangladesh', style_function = lambda x: border_stule).add_to(map_obj)
        map_obj.save("index.html")
        
    
    def save_map(self):
        pass