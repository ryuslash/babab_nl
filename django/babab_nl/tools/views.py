# Copyright (C) 2012-2013  Benjamin Althues
#
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the authors be held liable for any damages
# arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgment in the product documentation would be
#    appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.

import hashlib
from django.shortcuts import render_to_response
from django.template import RequestContext

from forms import strgenForm
from string_generator import stringGenerator


def rot13(request):
    data = {'text': '', 'section': 'rot13'}

    if request.POST:
        data = {'section': 'rot13',
                'text': request.POST['text'].encode('rot13')}

    context = RequestContext(request)
    return render_to_response('tools/rot13.html', data, context)


def md5(request):
    data = {'text': '', 'section': 'md5'}

    if request.POST:
        text = request.POST['text']

        if text:
            digest = hashlib.md5(text).hexdigest()
            data = {'section': 'md5', 'text': text, 'digest': digest}

    context = RequestContext(request)
    return render_to_response('tools/md5.html', data, context)


def sha1(request):
    data = {'text': '', 'section': 'sha1'}

    if request.POST:
        text = request.POST['text']

        if text:
            digest = hashlib.sha1(text).hexdigest()
            data = {'section': 'sha1', 'text': text, 'digest': digest}

    context = RequestContext(request)
    return render_to_response('tools/sha1.html', data, context)


def strgen(request):
    chars = ''
    result = ''

    if request.method == 'POST':
        form = strgenForm(request.POST)
        if form.is_valid():
            strlen = form.cleaned_data['number_of_chars']
            charOptions = form.cleaned_data['type_of_chars']
            result = stringGenerator(charOptions, strlen)
    else:
        form = strgenForm()

    data = {'section': 'strgen', 'form': form,
            'chars': chars, 'result': result}
    context = RequestContext(request)
    return render_to_response('tools/strgen.html', data, context)