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

from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'babab_nl.views.index', name='index'),
    url(r'^dispass/$', 'babab_nl.views.dispass', name='dispass'),
    url(r'^springwhiz/$', 'babab_nl.views.springwhiz', name='springwhiz'),
    url(r'^rot13/$', 'babab_nl.tools.views.rot13', name='rot13'),
    url(r'^md5/$', 'babab_nl.tools.views.md5', name='md5'),
    url(r'^sha1/$', 'babab_nl.tools.views.sha1', name='sha1'),
    url(r'^strgen/$', 'babab_nl.tools.views.strgen', name='strgen'),
    url(r'^admin/', include(admin.site.urls)),
)