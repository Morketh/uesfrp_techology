#!/usr/bin/python
##################################################################################################
#
# Copyright (C) 2014 Collective Industries
#
# AUTHOR: Andrew Malone
#
# TITLE: id-hash.py
#
# PURPOSE: servers as a back-end for the creation of ID hashes
#
# CREDITS: William Baggett for concept and original algorithm
# Cristian Năvălici for the CRC code found used below https://github.com/cristianav/PyCRC
# this code uses commit 69d47e010eecc982b3d16a794d9206bf63f12053
# 
#
##################################################################################################

## Global Settings ##

## Includes ##

from CRCModules.CRC16 import CRC16
from CRCModules.CRC16DNP import CRC16DNP
from CRCModules.CRCCCITT import CRCCCITT
from CRCModules.CRC16Kermit import CRC16Kermit

## Functions ##

def soundex(name, len=4):
    """ soundex module conforming to Knuth's algorithm
        implementation 2000-12-24 by Gregory Jorgensen
        public domain
    """

    # digits holds the soundex values for the alphabet
    digits = '01230120022455012623010202'
    sndx = ''
    fc = ''

    # translate alpha chars in name to soundex digits
    for c in name.upper():
        if c.isalpha():
            if not fc: fc = c   # remember first letter
            d = digits[ord(c)-ord('A')]
            # duplicate consecutive soundex digits are skipped
            if not sndx or (d != sndx[-1]):
                sndx += d

    # replace first digit with first alpha character
    sndx = fc + sndx[1:]

    # remove all 0s from the soundex code
    sndx = sndx.replace('0','')

    # return soundex code padded to len characters
    return (sndx + (len * '0'))[:len]

## Main program ##
if __name__ == "__main__":
	input = "BannonInterplanetarySystems"
	target = soundex(input)
	print "Soundex of "+input+": " + target
	print ("CRC-CCITT(XModem) {:10X}".format(CRCCCITT().calculate(target)))
	print ("CRC-16            {:10X}".format(CRC16().calculate(target)))
	print ("CRC-DNP           {:10X}".format(CRC16DNP().calculate(target)))
	print ("CRC-16 (Kermit)   {:10X}".format(CRC16Kermit().calculate(target)))
	
	input = "Bannon debugging"
	target = soundex(input)
	print "Soundex of "+input+": " + target
	print ("CRC-CCITT(XModem) {:10X}".format(CRCCCITT().calculate(target)))
	print ("CRC-16            {:10X}".format(CRC16().calculate(target)))
	print ("CRC-DNP           {:10X}".format(CRC16DNP().calculate(target)))
	print ("CRC-16 (Kermit)   {:10X}".format(CRC16Kermit().calculate(target)))