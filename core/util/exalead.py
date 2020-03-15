# -*- coding : u8 -*-
"""
OWASP Maryam!

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import re
import time

class main:

    def __init__(self, framework, q, limit):
        self.framework = framework
        self.q = q
        self._pages = ""
        self.exalead = 'www.exalead.com'
        self.limit = limit

    def run_crawl(self):
        urls = ["https://%s/search/web/results/?q=%s&element_per_page=50&start_index=%d" % (self.exalead, self.q.replace(" ","%20"), x*10) for x in range(self.limit+1)]
        max_attempt = len(urls)
        for url in urls:
            try:
                req = self.framework.request(url=url)
            except Exception as e:
                self.framework.error(str(e.args))
                max_attempt -= 1
                if max_attempt == 0:
                    self.framework.error("exalead is missed!")
                    break
            else:
                self._pages += req.text
                time.sleep(2)
    @property
    def pages(self):
        return self._pages

    @property
    def dns(self):
        return self.framework.page_parse(self._pages).get_dns(self.q)

    @property
    def emails(self):
        return self.framework.page_parse(self._pages).get_emails(self.q)

    @property
    def docs(self):
        return self.framework.page_parse(self._pages).get_docs(self.q)
    