# -*- coding: utf-8 -*-
#Copyright (C) 2011 Seán Hayes
from feedback.models import Feedback

VERSION = (1, 0, 2)

__version__ = "".join([".".join(map(str, VERSION[0:3])), "".join(VERSION[3:])])
def context_processor(request):
	return {'feedback_count': Feedback.objects.filter(archived=False).count()}