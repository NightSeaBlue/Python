import folium

#위도와 경도값을 준다
map_osm = folium.Map(location=[37.572807,126.975918],
                     zoom_start=17)

#위 지도에 마커를 붙혀주기
folium.Marker(location=[37.572807,126.975918],
              popup='세종문화회관',
              icon=folium.Icon(color='red',icon='info-sign')).add_to(map_osm)

map_osm.save('./map/map4.html')