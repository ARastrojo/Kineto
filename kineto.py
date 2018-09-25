#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kineto.py
#  
#  Copyright 2018 Alberto Rastrojo <arastrojo@cbm.csic.es>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from __future__ import division
import sys
import os
import argparse
from time import time

__version_info__ = ('0','0','1')
__version__ = '.'.join(__version_info__)

def main():
	
	##########################################################################################
	description = """
		These program...... pipeline for transcriptome building (kinetoplastidia)

	"""

	##########################################################################################
	#--Argument
	parser = argparse.ArgumentParser(description=description)
	parser.add_argument('-g', dest = 'genome', type = str, required = True, help = 'Fasta file containing genome sequence')
	parser.add_argument('-a', dest = 'annotations', type = str, required = True, help = 'Annotation file (GTF/GFF format)')
	parser.add_argument('-1', dest = 'read_1', type = str, required = True, help = 'R1 Reads file (Fastq)')
	parser.add_argument('-2', dest = 'read_2', type = str, required = True, help = 'R2 Reads file (Fastq)')
	parser.add_argument('-f', dest = 'annotations', type = str, default = "GTF", help = 'Annotation file format: GTF/GFF. Default: GTF')

	parser.add_argument('-V', '--version', action='version', version='kineto v' + __version__)

	parser.add_argument('-x', dest = 'debug', action='store_true', default = False, help = 'for debugging')	
	args = parser.parse_args()
	
	if args.debug: d = 1

	print ('%(prog)s')
	##########################################################################################



##########################################################################################
if __name__ == "__main__":

	main()


