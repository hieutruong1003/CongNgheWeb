# CongNgheWeb

## Chào Bạn!!!
## Trương Văn Hiếu
## Phạm Trung Hoài
## Phan Thanh Lâm

#backend

sudo docker build - t backend .
sudo docker run -d --name backend --env dp_ip=10.0.2.15 -p 8080:8080 backend
sudo docker stop backend
sudo docker rm backend

#lenh kết nối csdl
sudo docker exec -it coredb bash

#postgres
//sudo docker run -d --restart unless-stopped --name coredb -e POSTGTRES_PASSWORD=postgres -e POSGRESS_DB=postgres -v ~northwind db:var/lib/postgresql/data -p 5432:5432 postgres
sudo docker run -d -p 5432:5432 --name my-postgres -e POSTGRES_PASSWORD=mysecretpassword postgres
sudo docker exec -it my-postgres bash
