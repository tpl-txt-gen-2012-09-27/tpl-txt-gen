# -*- mode: python; coding: utf-8 -*-
#
# Copyright 2012, 2013 Andrej A Antonov <polymorphm@gmail.com>.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

assert str is not bytes

import argparse
from . import tpl_txt_gen

DESCRIPTION = '`tpl-txt-gen` is utility for massive generate text files on a template.'

class UserError(Exception):
    pass

def main():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    
    parser.add_argument('tpl_path', metavar='TPL-FILE-PATH',
            help='template file path for define task\'s process')
    parser.add_argument('out_path', metavar='OUT-DIR-PATH',
            help='output directory path for text new files')
    parser.add_argument('count', metavar='COUNT', type=int,
            help='count of output files')
    
    args = parser.parse_args()
    
    tpl_path = args.tpl_path
    out_path = args.out_path
    count = args.count
    
    if count < 0:
        raise UserError('invalid `count` argument')
    
    tpl_txt_gen.tpl_txt_gen(tpl_path, out_path, count)
