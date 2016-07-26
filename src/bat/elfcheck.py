#!/usr/bin/python

## Binary Analysis Tool
## Copyright 2012-2016 Armijn Hemel for Tjaldur Software Governance Solutions
## Licensed under Apache 2.0, see LICENSE file for details

'''
This module contains methods to verify ELF files and extract data from ELF files
such as the architecture, and so on.
'''

import sys, os, subprocess, os.path, struct
import tempfile, re

## mappings of architectures to names
## info from the following places:
##
## https://en.wikipedia.org/wiki/Executable_and_Linkable_Format
## https://docs.oracle.com/cd/E19683-01/816-1386/chapter6-43405/index.html
## https://refspecs.linuxbase.org/elf/elf.pdf
## https://android.googlesource.com/platform/art/+/master/runtime/elf.h
##
architecturemapping = { 0: None
                     , 1: "AT&T WE 32100"
                     , 2: "SPARC"
                     , 3: "Intel 80386"
                     , 4: "Motorola 68000"
                     , 5: "Motorola 88000"
                     , 6: "Intel 80486"
                     , 7: "Intel 80860"
                     , 8: "MIPS R3000"
                     , 9: "IBM System/370"
                     , 10: "MIPS RS3000 Little-endian"
                     , 15: "Hewlett-Packard PA-RISC"
                     , 17: "Fujitsu VPP500"
                     , 18: "SPARC32+" # // Enhanced instruction set SPARC
                     , 19: "Intel 80960"
                     , 20: "PowerPC"
                     , 21: "PowerPC64"
                     , 22: "IBM System/390"
                     , 23: "IBM SPU/SPC"
                     , 36: "NEC V800"
                     , 37: "Fujitsu FR20"
                     , 38: "TRW RH-32"
                     , 39: "Motorola RCE"
                     , 40: "ARM"
                     , 41: "DEC Alpha"
                     , 42: "Hitachi SH"
                     , 43: "SPARC V9"
                     , 44: "Siemens TriCore"
                     , 45: "Argonaut RISC Core"
                     , 46: "Hitachi H8/300"
                     , 47: "Hitachi H8/300H"
                     , 48: "Hitachi H8S"
                     , 49: "Hitachi H8/500"
                     , 50: "Intel IA-64"
                     , 51: "Stanford MIPS-X"
                     , 52: "Motorola ColdFire"
                     , 53: "Motorola M68HC12"
                     , 54: "Fujitsu MMA Multimedia Accelerator"
                     , 55: "Siemens PCP"
                     , 56: "Sony nCPU embedded RISC processor"
                     , 57: "Denso NDR1 microprocessor"
                     , 58: "Motorola Star*Core processor"
                     , 59: "Toyota ME16 processor"
                     , 60: "STMicroelectronics ST100 processor"
                     , 61: "Advanced Logic Corp. TinyJ"
                     , 62: "AMD X86-64"
                     , 63: "Sony DSP Processor"
                     , 64: "Digital Equipment Corp. PDP-10"
                     , 65: "Digital Equipment Corp. PDP-11"
                     , 66: "Siemens FX66 microcontroller"
                     , 67: "STMicroelectronics ST9+ 8/16 bit microcontroller"
                     , 68: "STMicroelectronics ST7 8-bit microcontroller"
                     , 69: "Motorola MC68HC16 Microcontroller"
                     , 70: "Motorola MC68HC11 Microcontroller"
                     , 71: "Motorola MC68HC08 Microcontroller"
                     , 72: "Motorola MC68HC05 Microcontroller"
                     , 73: "Silicon Graphics SVx"
                     , 74: "STMicroelectronics ST19 8-bit microcontroller"
                     , 75: "Digital VAX"
                     , 76: "ETRAX CRIS"
                     , 77: "Javelin"
                     , 78: "Element 14 64-bit DSP Processor"
                     , 79: "ZSP LSI Logic 16-bit DSP Processor"
                     , 80: "MMIX (Donald Knuth's educational 64-bit processor)"
                     , 81: "Harvard University machine-independent object files"
                     , 82: "SiTera Prism"
                     , 83: "Atmel AVR 8-bit microcontroller"
                     , 84: "Fujitsu FR30"
                     , 85: "Mitsubishi D10V"
                     , 86: "Mitsubishi D30V"
                     , 87: "NEC v850"
                     , 88: "Mitsubishi M32R"
                     , 89: "Matsushita MN10300"
                     , 90: "Matsushita MN10200"
                     , 91: "picoJava"
                     , 92: "OpenRISC 32-bit embedded processor"
                     , 93: "ARC International ARCompact processor"
                     , 94: "Tensilica Xtensa Architecture"
                     , 95: "Alphamosaic VideoCore processor"
                     , 96: "Thompson Multimedia General Purpose Processor"
                     , 97: "National Semiconductor 32000 series"
                     , 98: "Tenor Network TPC processor"
                     , 99: "Trebia SNP 1000 processor"
                     , 100: "STMicroelectronics ST200"
                     , 101: "Ubicom IP2xxx"
                     , 102: "MAX Processor"
                     , 103: "National Semiconductor CompactRISC microprocessor"
                     , 104: "Fujitsu F2MC16"
                     , 105: "Texas Instruments embedded microcontroller msp430"
                     , 106: "Analog Devices Blackfin (DSP) processor"
                     , 107: "S1C33 Family of Seiko Epson processors"
                     , 108: "Sharp embedded microprocessor"
                     , 109: "Arca RISC Microprocessor"
                     , 110: "MPRC UniCore"
                     , 111: "eXcess: 16/32/64-bit configurable embedded CPU"
                     , 112: "Icera Semiconductor Inc. Deep Execution Processor"
                     , 113: "Altera Nios II soft-core processor"
                     , 114: "National Semiconductor CompactRISC CRX"
                     , 115: "Motorola XGATE embedded processor"
                     , 116: "Infineon C16x/XC16x processor"
                     , 117: "Renesas M16C series microprocessors"
                     , 118: "Microchip Technology dsPIC30F Digital Signal Controller"
                     , 119: "Freescale Communication Engine RISC core"
                     , 120: "Renesas M32C series microprocessors"
                     , 131: "Altium TSK3000 core"
                     , 132: "Freescale RS08 embedded processor"
                     , 133: "Analog Devices SHARC"
                     , 134: "Cyan Technology eCOG2 microprocessor"
                     , 135: "Sunplus S+core7 RISC processor"
                     , 136: "New Japan Radio (NJR) 24-bit DSP Processor"
                     , 137: "Broadcom VideoCore III processor"
                     , 138: "RISC processor for Lattice FPGA architecture"
                     , 139: "Seiko Epson C17"
                     , 140: "Texas Instruments TMS320C6000"
                     , 141: "Texas Instruments TMS320C2000"
                     , 142: "Texas Instruments TMS320C55x"
                     , 160: "STMicroelectronics 64bit VLIW Data Signal Processor"
                     , 161: "Cypress M8C microprocessor"
                     , 162: "Renesas R32C series microprocessors"
                     , 163: "NXP Semiconductors TriMedia"
                     , 164: "Qualcomm Hexagon processor"
                     , 165: "Intel 8051"
                     , 166: "STMicroelectronics STxP7x RISC processor"
                     , 167: "Andes Technology compact code size embedded RISC"
                     , 168: "Cyan Technology eCOG1X"
                     , 169: "Dallas Semiconductor MAXQ30 Core Micro-controllers"
                     , 170: "New Japan Radio (NJR) 16-bit DSP Processor"
                     , 171: "M2000 Reconfigurable RISC Microprocessor"
                     , 172: "Cray Inc. NV2 vector architecture"
                     , 173: "Renesas RX"
                     , 174: "Imagination Technologies META"
                     , 175: "MCST Elbrus"
                     , 176: "Cyan Technology eCOG16"
                     , 177: "National Semiconductor CompactRISC CR16"
                     , 178: "Freescale Extended Time Processing Unit"
                     , 179: "Infineon Technologies SLE9X core"
                     , 180: "Intel L10M"
                     , 181: "Intel K10M"
                     , 183: "ARM AArch64"
                     , 185: "Atmel Corporation AVR32"
                     , 186: "STMicroeletronics STM8"
                     , 187: "Tilera TILE64"
                     , 188: "Tilera TILEPro"
                     , 190: "NVIDIA CUDA architecture"
                     , 191: "Tilera TILE-Gx"
                     , 192: "CloudShield"
                     , 193: "KIPO-KAIST Core-A 1st generation"
                     , 194: "KIPO-KAIST Core-A 2nd generation"
                     , 195: "Synopsys ARCompact V2"
                     , 196: "Open8 8-bit RISC soft processor core"
                     , 197: "Renesas RL78"
                     , 198: "Broadcom VideoCore V processor"
                     , 199: "Renesas 78KOR"
                     , 200: "Freescale 56800EX"
                     }

def getArchitecture(filename, tags):
	if not 'elf' in tags:
		return
	elffile = open(filename, 'rb')
	elffile.seek(0)
	elfbytes = elffile.read(64)

	## just set some default values: little endian, 32 bit
	littleendian = True

	## then check if this is a little endian or big endian binary
	if struct.unpack('>B', elfbytes[5])[0] != 1:
		littleendian = False

	## check the machine type
	if littleendian:
		elfmachinebyte = struct.unpack('<H', elfbytes[0x12:0x12+2])[0]
	else:
		elfmachinebyte = struct.unpack('>H', elfbytes[0x12:0x12+2])[0]
	if elfmachinebyte in architecturemapping:
		architecture = architecturemapping[elfmachinebyte]
	else:
		architecture = "UNKNOWN"
	elffile.close()
	return architecture

## simplistic method to verify if a file is an ELF file
## This might not work for all ELF files and it is a conservative verification, only used to
## reduce false positives of LZMA scans.
## This does for sure not work for Linux kernel modules on some devices.
def verifyELF(filename, tempdir=None, tags=[], offsets={}, scanenv={}, debug=False, unpacktempdir=None):
	offset = 0
	if not 'binary' in tags:
		return []
	if 'compressed' in tags or 'graphics' in tags or 'xml' in tags:
		return []
	elffile = open(filename, 'rb')
	elffile.seek(offset)
	elfbytes = elffile.read(4)
	if elfbytes != '\x7f\x45\x4c\x46':
		elffile.close()
		return []

	newtags = []
	filesize = os.stat(filename).st_size

	## don't rely on output of readelf as it does not take localized systems into account
	## Instead, use specification found here: http://en.wikipedia.org/wiki/Executable_and_Linkable_Format
	elffile.seek(offset)
	elfbytes = elffile.read(64)
	if len(elfbytes) != 64:
		elffile.close()
		return []

	## just set some default values: little endian, 32 bit
	littleendian = True
	bit32 = True

	## first check if this is a 32 bit or 64 bit binary
	if struct.unpack('>B', elfbytes[4])[0] != 1:
		bit32 = False
	## then check if this is a little endian or big endian binary
	if struct.unpack('>B', elfbytes[5])[0] != 1:
		littleendian = False

	## first determine the size of the ELF header
	if bit32:
		elfunpackbytes = elfbytes[0x28:0x28+2]
	else:
		elfunpackbytes = elfbytes[0x34:0x34+2]
	if littleendian:
		elfheadersize = struct.unpack('<H', elfunpackbytes)[0]
	else:
		elfheadersize = struct.unpack('>H', elfunpackbytes)[0]

	## ELF header cannot extend past the end of the file
	if offset + elfheadersize > filesize:
		elffile.close()
		return []

	## then read the actual ELF header
	elffile.seek(offset)
	elfbytes = elffile.read(elfheadersize)

	## check the ELF type.
	if littleendian:
		elftypebyte = struct.unpack('<H', elfbytes[0x10:0x10+2])[0]
	else:
		elftypebyte = struct.unpack('>H', elfbytes[0x10:0x10+2])[0]
	if elftypebyte == 0:
		elftype = 'elftypenone'
	elif elftypebyte == 1:
		elftype = 'elfrelocatable'
	elif elftypebyte == 2:
		elftype = 'elfexecutable'
	elif elftypebyte == 3:
		elftype = 'elfdynamic'
	elif elftypebyte == 4:
		elftype = 'elfcore'
	newtags.append(elftype)

	## check the machine type
	if littleendian:
		elfmachinebyte = struct.unpack('<H', elfbytes[0x12:0x12+2])[0]
	else:
		elfmachinebyte = struct.unpack('>H', elfbytes[0x12:0x12+2])[0]
	if elfmachinebyte in architecturemapping:
		architecture = architecturemapping[elfmachinebyte]
	else:
		architecture = "UNKNOWN"

	## the start of program headers
	if bit32:
		elfunpackbytes = elfbytes[0x1C:0x20]
	else:
		elfunpackbytes = elfbytes[0x20:0x28]
	if littleendian:
		if bit32:
			startprogramheader = struct.unpack('<I', elfunpackbytes)[0]
		else:
			startprogramheader = struct.unpack('<Q', elfunpackbytes)[0]
	else:
		if bit32:
			startprogramheader = struct.unpack('>I', elfunpackbytes)[0]
		else:
			startprogramheader = struct.unpack('>Q', elfunpackbytes)[0]

	## program header cannot be outside of the file
	if offset + startprogramheader > filesize:
		elffile.close()
		return []

	## the start of section headers
	if bit32:
		elfunpackbytes = elfbytes[0x20:0x20+4]
	else:
		elfunpackbytes = elfbytes[0x28:0x28+8]
	if littleendian:
		if bit32:
			startsectionheader = struct.unpack('<I', elfunpackbytes)[0]
		else:
			startsectionheader = struct.unpack('<Q', elfunpackbytes)[0]
	else:
		if bit32:
			startsectionheader = struct.unpack('>I', elfunpackbytes)[0]
		else:
			startsectionheader = struct.unpack('>Q', elfunpackbytes)[0]

	## section header cannot be outside of the file
	if offset + startsectionheader > filesize:
		elffile.close()
		return []

	## the size of the program headers
	if bit32:
		elfunpackbytes = elfbytes[0x2A:0x2A+2]
	else:
		elfunpackbytes = elfbytes[0x36:0x36+2]
	if littleendian:
		programheadersize = struct.unpack('<H', elfunpackbytes)[0]
	else:
		programheadersize = struct.unpack('>H', elfunpackbytes)[0]

	## program header cannot extend past the file
	if offset + startprogramheader + programheadersize > filesize:
		elffile.close()
		return []

	## the amount of program headers
	if bit32:
		elfunpackbytes = elfbytes[0x2C:0x2C+2]
	else:
		elfunpackbytes = elfbytes[0x38:0x38+2]
	if littleendian:
		numberprogramheaders = struct.unpack('<H', elfunpackbytes)[0]
	else:
		numberprogramheaders = struct.unpack('>H', elfunpackbytes)[0]

	if numberprogramheaders != 0:
		## program header cannot be inside the ELF header
		if offset + startprogramheader + programheadersize < offset + elfheadersize:
			elffile.close()
			return []

	## the size of the section headers
	if bit32:
		elfunpackbytes = elfbytes[0x2E:0x2E+2]
	else:
		elfunpackbytes = elfbytes[0x3A:0x3A+2]
	if littleendian:
		sectionheadersize = struct.unpack('<H', elfunpackbytes)[0]
	else:
		sectionheadersize = struct.unpack('>H', elfunpackbytes)[0]

	## section header cannot extend past the end of the file
	if offset + startsectionheader + sectionheadersize > filesize:
		elffile.close()
		return []

	## the amount of section headers
	if bit32:
		elfunpackbytes = elfbytes[0x30:0x30+2]
	else:
		elfunpackbytes = elfbytes[0x3C:0x3C+2]
	if littleendian:
		numbersectionheaders = struct.unpack('<H', elfunpackbytes)[0]
	else:
		numbersectionheaders = struct.unpack('>H', elfunpackbytes)[0]

	## the start of section header index
	if bit32:
		elfunpackbytes = elfbytes[0x32:0x32+2]
	else:
		elfunpackbytes = elfbytes[0x3E:0x3E+2]
	if littleendian:
		sectionheaderindex = struct.unpack('<H', elfunpackbytes)[0]
	else:
		sectionheaderindex = struct.unpack('>H', elfunpackbytes)[0]

	## section header cannot be inside the ELF header
	if offset + startsectionheader + sectionheadersize < offset + elfheadersize:
		elffile.close()
		return []

	## First process the program header table
	brokenelf = False
	for i in range(0,numberprogramheaders):
		elffile.seek(offset + startprogramheader + i*programheadersize)
		elfbytes = elffile.read(programheadersize)
		if len(elfbytes) != programheadersize:
			brokenelf = True
			break
		## first the segmenttype
		if littleendian:
			segmenttype = struct.unpack('<I', elfbytes[:4])[0]
		else:
			segmenttype = struct.unpack('>I', elfbytes[:4])[0]
		## then the offset in the file
		if littleendian:
			if bit32:
				segmentoffset = struct.unpack('<I', elfbytes[4:8])[0]
			else:
				segmentoffset = struct.unpack('<Q', elfbytes[8:16])[0]
		else:
			if bit32:
				segmentoffset = struct.unpack('>I', elfbytes[4:8])[0]
			else:
				segmentoffset = struct.unpack('>Q', elfbytes[8:16])[0]

		## segment cannot be outside of the file
		if offset + segmentoffset > filesize:
			brokenelf = True
			break

		## then the virtual address in memory (skip for now) -- 4 bytes (32 bit) or 8 bytes
		## then the physical address in memory (skip for now) -- 4 bytes (32 bit) or 8 bytes
		## then the size in bytes in the file image
		if littleendian:
			if bit32:
				segmentsize = struct.unpack('<I', elfbytes[16:20])[0]
			else:
				segmentsize = struct.unpack('<Q', elfbytes[32:40])[0]
		else:
			if bit32:
				segmentsize = struct.unpack('>I', elfbytes[16:20])[0]
			else:
				segmentsize = struct.unpack('>Q', elfbytes[32:40])[0]

		## segment cannot extend past the end of the file
		if offset + segmentoffset + segmentsize > filesize:
			brokenelf = True
			break

		## then the size in bytes in memory image (skip for now) -- 4 bytes or 8 bytes
		## then the segment dependent flags (skip for now) -- 4 bytes
		## then the alignment
		if littleendian:
			if bit32:
				alignment = struct.unpack('<I', elfbytes[24:28])[0]
			else:
				alignment = struct.unpack('<I', elfbytes[52:60])[0]
		else:
			if bit32:
				alignment = struct.unpack('>I', elfbytes[24:28])[0]
			else:
				alignment = struct.unpack('>I', elfbytes[56:60])[0]

	if brokenelf:
		elffile.close()
		return []

	dynamic = False

	sections = {}

	## process the section headers
	dynamiccount = 0
	for i in xrange(0,numbersectionheaders):
		elffile.seek(offset+startsectionheader + i * sectionheadersize)
		elfbytes = elffile.read(sectionheadersize)
		if len(elfbytes) != sectionheadersize:
			elffile.close()
			return []
		if littleendian:
			sh_name = struct.unpack('<I', elfbytes[0:4])[0]
		else:
			sh_name = struct.unpack('>I', elfbytes[0:4])[0]
		if littleendian:
			sh_type = struct.unpack('<I', elfbytes[4:8])[0]
		else:
			sh_type = struct.unpack('>I', elfbytes[4:8])[0]
		if sh_type == 6:
			dynamiccount += 1
		## then the flags (4 byte or 8 byte) -- skip for now
		if littleendian:
			if bit32:
				sh_flags = struct.unpack('<I', elfbytes[8:12])[0]
			else:
				sh_flags = struct.unpack('<Q', elfbytes[8:16])[0]
		else:
			if bit32:
				sh_flags = struct.unpack('>I', elfbytes[8:12])[0]
			else:
				sh_flags = struct.unpack('>Q', elfbytes[8:16])[0]
	
		## then the virtual address (4 byte or 8 byte) -- skip for now
		if littleendian:
			if bit32:
				sh_addr = struct.unpack('<I', elfbytes[12:16])[0]
			else:
				sh_addr = struct.unpack('<Q', elfbytes[16:24])[0]
		else:
			if bit32:
				sh_addr = struct.unpack('>I', elfbytes[12:16])[0]
			else:
				sh_addr = struct.unpack('>Q', elfbytes[16:24])[0]
		## then the offset
		if littleendian:
			if bit32:
				sectionoffset = struct.unpack('<I', elfbytes[16:20])[0]
			else:
				sectionoffset = struct.unpack('<Q', elfbytes[24:32])[0]
		else:
			if bit32:
				sectionoffset = struct.unpack('>I', elfbytes[16:20])[0]
			else:
				sectionoffset = struct.unpack('>Q', elfbytes[24:32])[0]

		## section offset cannot be outside of the file
		if offset + sectionoffset > filesize:
			brokenelf = True
			break

		## then the size in bytes in the file image
		if littleendian:
			if bit32:
				sectionsize = struct.unpack('<I', elfbytes[20:24])[0]
			else:
				sectionsize = struct.unpack('<Q', elfbytes[32:40])[0]
		else:
			if bit32:
				sectionsize = struct.unpack('>I', elfbytes[20:24])[0]
			else:
				sectionsize = struct.unpack('>Q', elfbytes[32:40])[0]

		## segment cannot extend past the end of the file, except if the
		## file is debugging package on for example Fedora. TODO
		if offset + sectionoffset + sectionsize > filesize:
			brokenelf = True
			break

		sections[i] = {'sectionoffset': sectionoffset, 'sectionsize': sectionsize}

	if brokenelf:
		elffile.close()
		return []

	if dynamiccount == 1:
		dynamic = True

	sectionnames = []
	if sectionheaderindex in sections:
		elffile.seek(sections[i]['sectionoffset'])
		sectionnames = filter(lambda x: x != '',  elffile.read(sections[i]['sectionsize']).split('\x00'))

	## finally close the file
	elffile.close()

	## This does not work well, for example for Linux kernel modules
	#if elfheadersize != startprogramheader:
	#	return []

	## This does not work well for some Linux kernel modules as well as other files
	## (architecture dependent?)
	## One architecture where this sometimes seems to happen is ARM.
	totalsize = startsectionheader + sectionheadersize * numbersectionheaders
	if totalsize == filesize:
		newtags.append("elf")
	else:
		## If it is a signed kernel module then the key is appended to the ELF data
		elffile = open(filename, 'rb')
		elffile.seek(-28, os.SEEK_END)
		elfbytes = elffile.read()
		if elfbytes == "~Module signature appended~\n":
			## The metadata of the signing data can be found in 12 bytes
			## preceding the 'magic'
			## According to 'scripts/sign-file' in the Linux kernel
			## the last 4 bytes are the size of the signature data
			## three bytes before that are 0x00
			## The byte before that is the length of the key identifier
			## The byte before that is the length of the "signer's name"
			elffile.seek(-40, os.SEEK_END)
			totalsiglength = 40
			elfbytes = elffile.read(12)
			signaturelength = struct.unpack('>I', elfbytes[-4:])[0]
			totalsiglength += signaturelength
			keyidentifierlen = ord(elfbytes[4])
			signernamelen = ord(elfbytes[3])
			totalsiglength += keyidentifierlen
			totalsiglength += signernamelen
			if totalsiglength + totalsize == filesize:
				newtags.append("elf")
		elffile.close()

	if not 'elf' in newtags:
		## on some architectures we can probably look at the starting point
		## of the last section, then use the offset value there and see if the offset
		## of the last section, plus the size of the last section == file size
		p = subprocess.Popen(['readelf', '-Wt', filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
		(stanout, stanerr) = p.communicate()
		if p.returncode != 0:
			return []
		st = stanout.strip().split("\n")
		for s in st[-3:]:
			spl = s.split()
			if len(spl) == 8:
				totalsize = int(spl[2], 16) + int(spl[3], 16)
				if totalsize == os.stat(filename).st_size:
					newtags.append("elf")

	if not dynamic:
		newtags.append("static")
	else:
		newtags.append("dynamic")
	#if not "elf" in newtags:
		#newtags.append("elf")

	## check whether or not it might be a Linux kernel file or module
	p = subprocess.Popen(['readelf', '-SW', filename], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
	(stanout, stanerr) = p.communicate()
	if "There are no sections in this file." in stanout:
		pass
	else:
		st = stanout.strip().split("\n")
		for s in st[3:]:
			if "__ksymtab_strings" in s:
				newtags.append('linuxkernel')
				break
			if "oat_patches" in s:
				## Android
				newtags.append('oat')
				newtags.append('android')
				break
	return newtags
