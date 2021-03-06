# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import qrcode
from django.utils.six import BytesIO

def generate_qrcode(request, data):
	img = qrcode.make(data)

	buf = BytesIO()
	img.save(buf)
	image_stream = buf.getvalue()

	response = HttpResponse(image_stream, content_type="image/png")
	return response

# Create your views here.
