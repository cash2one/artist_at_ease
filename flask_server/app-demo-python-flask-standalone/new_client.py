#!/usr/bin/env python
# -*- coding: gbk -*-
########################################################################
# 
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: new_client.py
Author: root(root@baidu.com)
Date: 2016/08/26 23:55:57
"""
import os
import json
import time
import httplib


def send_file_to_gt():
    GT_SERVER_PATH = "180.76.146.23"
    host = GT_SERVER_PATH
    port = 8001 # Reserve a port for your service.
    method = "sendfile"

    filename='./static/upload/style-picasso.jpg'
    f = open(filename,'rb')
    l = f.read()
    headers = {'Content-Type': 'multipart/form-data', \
                    'Cache-Control': 'no-cache'}
    headers["method"] = method
    headers["filename"] = "style-picasso.jpg"

    #raw_body = {"content": l, "method": method, "filename": "style-picasso.jpg"}
    body = l
    conn = httplib.HTTPConnection(host, port)
    conn.request("POST", method, body, headers)
    response = conn.getresponse()
    res = response.read()
    print res
    return res

send_file_to_gt()
