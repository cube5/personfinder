#!/usr/bin/python2.7
# Copyright 2010 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from utils import *
from model import *


class Handler(BaseHandler):
    repo_required = False

    def get(self):
        self.env.robots_ok = True
        self.env.amp = True
        self.render('ampstart.html', cache_seconds=0, get_vars=self.get_vars)

    def get_vars(self):
        # Round off the count so people don't expect it to change every time
        # they add a record.
        person_count = Counter.get_count(self.repo, 'person.all')
        if person_count < 100:
            num_people = 0  # No approximate count will be displayed.
        else:
            # 100, 200, 300, etc.
            num_people = int(round(person_count, -2))

        return {'num_people': num_people,
                'seek_url': self.get_url('/query', role='seek'),
                'provide_url': self.get_url('/query', role='provide')}