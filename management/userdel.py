# Copyright (c) 2010-2011 OpenStack, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import optparse
import keystone.db.sqlalchemy.api as db_api


def main():
    usage = "usage: %prog username"
    parser = optparse.OptionParser(usage)
    options, args = parser.parse_args()
    if len(args) != 1:
        parser.error("Incorrect number of arguments")
    else:
        username = args[0]
        try:
            u = db_api.user_get(username)
            if u == None:
                raise IndexError("User not found")
            else:
                db_api.user_delete(username)
            print 'User', username, 'deleted.'
        except Exception, e:
            print 'Error deleting user', username, ':', str(e)

if __name__ == '__main__':
    main()
