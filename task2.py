#!/usr/bin/python
import urllib
import json
import psycopg2
from config import config

url = 'http://api.hostip.info/get_json.php'
info = json.loads(urllib.urlopen(url).read())
ip = info['ip']

urlFoLaction = "http://www.freegeoip.net/json/{0}".format(ip)
locationInfo = json.loads(urllib.urlopen(urlFoLaction).read())
IP=data['ip']
country=data['country_name']
country_code=data['country_code']
time_zone=data['time_zone']
latitude=data['latitude']
longitude=data['longitude']


conn = psycopg2.connect("dbname=geo_test user=devops password=devopstest")
sql = 'create table if not exists ' + geo_test + ' (id serial primary key, local_ip char, public_ip char, country char, country_code char, time_zone char, latitude char, longitude char)'
c.execute(sql)
def insert_geo_test(local_ip, public_ip, country, country_code, time_zone, latitude, longitude):
    sql = """INSERT INTO geo_test(local_ip, public_ip, country, country_code, time_zone, latitude, longitude)
             VALUES(ip, IP, country, country_code, time_zone, latitude, longitude);"""
    c.execute(sql)
conn.close()
