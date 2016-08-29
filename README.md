# artist_at_ease

* **mkdir && git pull**
<pre><code>mkdir -p /home/work/daiwk && cd /home/work/daiwk/
git clone git@github.com:daiwk/artist_at_ease.git
</code></pre>
OR
<pre><code>mkdir -p /home/work/daiwk && cd /home/work/daiwk/
git clone https://github.com/daiwk/artist_at_ease.git
</code></pre>


* **start a docker container**
<pre><code>docker pull daocloud.io/daiwk/dl-server-basic:1.0.1
nohup sh -x run_docker_dl_server_basic.sh 2>&1 &
</code></pre>

* **install mysql-server**
<p>refer to
http://wiki.baidu.com/pages/viewpage.action?pageId=187796854
</p>
* **load schema & data from sql**
<pre><code>mysql -uroot -p123456
create database artist_at_ease;
mysql -uroot -p123456 artist_at_ease < artist_at_ease.sql
</code></pre>

* **set crontab job**
<pre><code>*/3 * * * * cd /home/work/daiwk/artist_at_ease/docker_server && sh ct_update_status.sh > ct.log 2>&1
</code></pre>

* **download mxnet model vgg**
<pre><code>cd /home/work/daiwk/artist_at_ease/docker_server/neural-style/
sh -x download.sh
</code></pre>

* **login docker container**
<pre><code>sh root@180.76.146.23 -p 50002
</code></pre>

* **inside docker container, run**
<pre><code>cd /notebooks/daiwk/artist_at_ease/docker_server
nohup python gt_server.py 2>&1 &
</code></pre>

* **provide images download**
<pre><code>cd /home/work/daiwk/artist_at_ease/docker_server/neural-style
nohup python -m CGIHTTPServer 8888 2>&1 &
</code></pre>

* **start the flask server**
<pre><code>pip install flask
cd /home/work/daiwk/artist_at_ease/flask_server/app-demo-python-flask-standalone/
nohup python app.py 2>&1 &
</code></pre>

* **REFS:**
1.[puzzle template](http://www.templatemo.com/tm-477-puzzle)
