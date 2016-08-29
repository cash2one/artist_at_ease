# artist_at_ease

# start a docker container
docker pull daocloud.io/daiwk/dl-server-basic:1.0.1

nohup sh -x run_docker_dl_server_basic.sh 2>&1 &

# install mysql-server
http://wiki.baidu.com/pages/viewpage.action?pageId=187796854

# load schema & data from sql

mysql -uroot -p123456
create database artist_at_ease;

mysql -uroot -p123456 artist_at_ease < artist_at_ease.sql


# set crontab job
*/3 * * * * cd /home/work/daiwk/artist_at_ease/docker_server && sh ct_update_status.sh > ct.log 2>&1

# login docker container
sh root@180.76.146.23 -p 50002

# inside docker container, run 
cd /notebooks/daiwk/artist_at_ease/docker_server
nohup python gt_server.py 2>&1 &


# provide images download
cd /home/work/daiwk/artist_at_ease/docker_server/neural-style
nohup python -m CGIHTTPServer 8888 2>&1 &
