# -*- coding: utf-8 -*- 
# Time: 2022-03-01 11:23
# Copyright (c) 2022
# author: Euraxluo


from .conftest import register
from unittest import TestCase, skip

from .conftest import *
from amap_distance_matrix.services.geo import *
from amap_distance_matrix.services.navigation import *
from amap_distance_matrix.services.osrm import *


async def async_geo_addr_city_test():
    res = await async_geo_addr_city([("春熙路", "成都")])
    print(res)


def get_map(route):
    import folium
    folium.folium._default_js = [
        ('leaflet',
         'https://cdn.bootcdn.net/ajax/libs/leaflet/1.6.0/leaflet.js'),
        ('jquery',
         'https://cdn.bootcdn.net/ajax/libs/jquery/1.12.4/jquery.min.js'),
        ('bootstrap',
         'https://cdn.bootcdn.net/ajax/libs/twitter-bootstrap/2.0.0/bootstrap.min.js'),
        ('awesome_markers',
         'https://cdn.bootcdn.net/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js'),  # noqa
        ('iso8601',
         'https://cdn.jsdelivr.net/npm/iso8601@1.1.1/lib/iso8601.min.js'),
        ('timedimension',
         'https://cdn.jsdelivr.net/npm/leaflet-timedimension@1.1.1/dist/leaflet.timedimension.min.js')
    ]
    
    folium.folium._default_css = [
        ('leaflet_css',
         'https://cdn.bootcdn.net/ajax/libs/leaflet/1.6.0/leaflet.css'),
        ('bootstrap_css',
         'https://cdn.bootcdn.net/ajax/libs/twitter-bootstrap/3.2.0/css/bootstrap.min.css'),
        ('bootstrap_theme_css',
         'https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css'),  # noqa
        ('awesome_markers_font_css',
         'https://cdn.bootcdn.net/ajax/libs/font-awesome/4.6.3/css/font-awesome.min.css'),  # noqa
        ('awesome_markers_css',
         'https://cdn.bootcdn.net/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css'),  # noqa
        ('awesome_rotate_css',
         'https://birdage.github.io/Leaflet.awesome-markers/dist/leaflet.awesome.rotate.css'),  # noqa
        ('timedimension',
         'https://cdn.jsdelivr.net/npm/leaflet-timedimension@1.1.1/dist/leaflet.timedimension.control.min.css')
    ]
    
    print(route)
    m = folium.Map(location=[(route['start_point'][0] + route['end_point'][0]) / 2,
                             (route['start_point'][1] + route['end_point'][1]) / 2],
                   zoom_start=13)
    
    folium.PolyLine(
        route['route'],
        weight=8,
        color='blue',
        opacity=0.6
    ).add_to(m)
    
    # folium.Marker(
    #     location=route['start_point'],
    #     icon=folium.Icon(icon='play', color='green')
    # ).add_to(m)
    
    folium.Marker(
        location=route['end_point'],
        icon=folium.Icon(icon='stop', color='red')
    ).add_to(m)
    
    return m


class TestAMap(TestCase):
    def test_geo_url(self):
        res = geo_url("春熙路", "成都", "4396fb03833e27e6438dde36c7457cf3")
        print(res)
    
    def test_geo_addr_city(self):
        res = geo_addr_city([("春熙路", "成都")])
        print(res)
    
    def test_async_geo_addr_city(self):
        asyncio.run(async_geo_addr_city_test())
    
    def test_navigation(self):
        res = geo_addr_city([("天安门", "北京"), ("黑桥公园", "北京"), ("北宫镇", "北京"), ("大兴机场", "北京")])
        print(res)
        urls = navigating_url(res[0], res[-1], res[1:-1], strategy=1, batch_size=2)
        print("urls", urls)
        assert len(urls) == 2
        res = driving_batch(res[0], res[-1], res[1:-1], autonavi_config={"strategy": 1, "batch_size": 2})
        print(res)
    

    def test_osrm(self):
        res = geo_addr_city([("天安门", "北京"),  ("大兴机场", "北京")])  # ,
        # res = geo_addr_city([("春熙路", "成都"), ("双流国际机场", "成都")])  # ,
        # res = geo_addr_city([("天安门", "北京"), ("天安门", "北京")])  # ,
        print(res)
        # res = [gcj2wgs(Lon=loc[0], Lat=loc[1]) for loc in res]
        print(res)
        urls = osrm_url(res[0], res[-1], res[1:-1], batch_size=100,profile='bike')
        print("urls", urls)
        res = osrm_batch(res[0], res[-1], res[1:-1], batch_size=10,profile='bike')
        print(res)
