#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-12-11 19:23:24
# @Author  : yml_bright@163.com

import pe_models, pc_cache, jwc_cache, data_cache, lecture_cache, card_cache, nic_cache, phylab_cache
import empty_room, lecturedb, user_detail
from db import engine, Base

Base.metadata.create_all(engine)

