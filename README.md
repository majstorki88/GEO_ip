# 1. Podesavanje hard/soft limit-a pri dobijanju greske TOO MANY FILES OPEN

Pokrenuti ansible playbook task1.yml

U host fajlu ansibla za servers podesiti hostname/IP adrese servera koji će biti afektovani, i dodeliti u host fajlu sudo prava ka tim serverima


# 2. Kreiranje baze i aplikacije

Python skripta task2.py kreira bazu geo_test u koliko ne postoji, curl-uje sa adrese http://api.hostip.info/get_json.php
geo lokaciju i istu storuje u navedenu bazu.

# 3. Kreiranje okruženja

U folderu Task3 nalazi se ansible playbook-ovi koji:

- Task3a - Instalira se NGNIX sa Passenger modom playbook-om task3a.yml

- Task3b - Instalira se PostgreSQL sa userom ror_app/testpass koji ima privilegije Read, Write, Create playbook-om task3b.yml

- Task3c - Instalira se ruby-2.4.2 system wide sa playbook-om task3c.yml

- Task3d - Inicijalizuje se aplikacija test_app kojom se NGINX povezuje sa PostgreSQL playbook-om task3d.yml

- Task3d - Završno podešavanje NGINX-a kako bi bio vidljiv na javnoj IP adresi playbook-om task3d.yml
