#wget -r -nH --level=0 --cut-dirs=6 --user=getprod --password=getprod -q \
#ftp://product.scm.baidu.com:/data/prod-64/jpaas/demos/demos_1-0-0_BL/output/app-demo-python-flask-standalone
jpaas login \
          -u daiwenkai@baidu.com \
          -p WAW8BDfSp2ZTsJ30eWeJahwlhfZfB50eigXnw085 \
          -o idea-show \
          -s artist-at-ease \
          -a http://api2.jpaas-idea.baidu.com
cd app-demo-python-flask-standalone
tag="0-0-0-1" #tag
pushname="artist-at-ease_${tag}"
jpaas push ${pushname} -i 2 -m 2G
jpaas app ${pushname}
