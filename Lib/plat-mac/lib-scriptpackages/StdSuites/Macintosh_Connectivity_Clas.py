"""Suite Macintosh Connectivity Classes: Classes relating to Apple Macintosh personal computer connectivity
Level 1, version 1

Generated from /Volumes/Moes/Systeemmap/Extensies/AppleScript
AETE/AEUT resource version 1/0, language 0, script 0
"""

import aetools
import MacOS

_code = 'macc'

class Macintosh_Connectivity_Clas_Events:

	pass


class ADB_address(aetools.ComponentItem):
	"""ADB address - Addresses a device connected via Apple Desktop Bus """
	want = 'cadb'
class _3c_inheritance_3e_(aetools.NProperty):
	"""<inheritance> - inherits some of its properties from this class """
	which = 'c@#^'
	want = 'cadr'
class ID(aetools.NProperty):
	"""ID - the Apple Desktop Bus device ID """
	which = 'ID  '
	want = 'shor'

ADB_addresses = ADB_address

class AppleTalk_address(aetools.ComponentItem):
	"""AppleTalk address - Addresses a device or service connected via the AppleTalk protocol """
	want = 'cat '
class AppleTalk_machine(aetools.NProperty):
	"""AppleTalk machine - the machine name part of the address """
	which = 'patm'
	want = 'TEXT'
class AppleTalk_zone(aetools.NProperty):
	"""AppleTalk zone - the zone part of the address """
	which = 'patz'
	want = 'TEXT'
class AppleTalk_type(aetools.NProperty):
	"""AppleTalk type - the type part of the AppleTalk address """
	which = 'patt'
	want = 'TEXT'

AppleTalk_addresses = AppleTalk_address

class Ethernet_address(aetools.ComponentItem):
	"""Ethernet address - Addresses a device by its Ethernet address """
	want = 'cen '

Ethernet_addresses = Ethernet_address

class FireWire_address(aetools.ComponentItem):
	"""FireWire address - Addresses a device on the FireWire bus """
	want = 'cfw '

FireWire_addresses = FireWire_address

class IP_address(aetools.ComponentItem):
	"""IP address - Addresses a device or service via the Internet Protocol (IP) """
	want = 'cip '
class DNS_form(aetools.NProperty):
	"""DNS form - the address in the form "apple.com" """
	which = 'pdns'
	want = 'TEXT'
class port(aetools.NProperty):
	"""port - the port number of the service or client being addressed """
	which = 'ppor'
	want = 'TEXT'

IP_addresses = IP_address

class LocalTalk_address(aetools.ComponentItem):
	"""LocalTalk address - Addresses a device by its LocalTalk address """
	want = 'clt '
class network(aetools.NProperty):
	"""network - the LocalTalk network number """
	which = 'pnet'
	want = 'shor'
class node(aetools.NProperty):
	"""node - the LocalTalk node number """
	which = 'pnod'
	want = 'shor'
class socket(aetools.NProperty):
	"""socket - the LocalTalk socket number """
	which = 'psoc'
	want = 'shor'

LocalTalk_addresses = LocalTalk_address

class SCSI_address(aetools.ComponentItem):
	"""SCSI address - Addresses a SCSI device """
	want = 'cscs'
class SCSI_bus(aetools.NProperty):
	"""SCSI bus - the SCSI bus number """
	which = 'pscb'
	want = 'shor'
class LUN(aetools.NProperty):
	"""LUN - the SCSI logical unit number """
	which = 'pslu'
	want = 'shor'

SCSI_addresses = SCSI_address

class Token_Ring_address(aetools.ComponentItem):
	"""Token Ring address - Addresses a device or service via the Token Ring protocol """
	want = 'ctok'

Token_Ring_addresses = Token_Ring_address

class USB_Addresses(aetools.ComponentItem):
	"""USB Addresses -  """
	want = 'cusb'

USB_address = USB_Addresses
class name(aetools.NProperty):
	"""name - the USB device name """
	which = 'pnam'
	want = 'TEXT'

class address_specification(aetools.ComponentItem):
	"""address specification - Unique designation of a device or service connected to this computer """
	want = 'cadr'
class properties(aetools.NProperty):
	"""properties - property that allows getting and setting of multiple properties """
	which = 'pALL'
	want = 'reco'
class conduit(aetools.NProperty):
	"""conduit - How the addressee is physically connected """
	which = 'pcon'
	want = 'econ'
class protocol(aetools.NProperty):
	"""protocol - How to talk to this addressee """
	which = 'pprt'
	want = 'epro'

address_specifications = address_specification

class bus_slot(aetools.ComponentItem):
	"""bus slot - Addresses a PC, PCI, or NuBus card """
	want = 'cbus'

bus_slots = bus_slot

class device_specification(aetools.ComponentItem):
	"""device specification - A device connected to a computer """
	want = 'cdev'
class device_type(aetools.NProperty):
	"""device type - the kind of device """
	which = 'pdvt'
	want = 'edvt'
class device_address(aetools.NProperty):
	"""device address - the address of the device """
	which = 'pdva'
	want = 'cadr'

device_specifications = device_specification
ADB_address._superclassnames = ['address_specification']
ADB_address._privpropdict = {
	'_3c_inheritance_3e_' : _3c_inheritance_3e_,
	'ID' : ID,
}
ADB_address._privelemdict = {
}
AppleTalk_address._superclassnames = ['address_specification']
AppleTalk_address._privpropdict = {
	'_3c_inheritance_3e_' : _3c_inheritance_3e_,
	'AppleTalk_machine' : AppleTalk_machine,
	'AppleTalk_zone' : AppleTalk_zone,
	'AppleTalk_type' : AppleTalk_type,
}
AppleTalk_address._privelemdict = {
}
Ethernet_address._superclassnames = ['address_specification']
Ethernet_address._privpropdict = {
	'_3c_inheritance_3e_' : _3c_inheritance_3e_,
	'ID' : ID,
}
Ethernet_address._privelemdict = {
}
FireWire_address._superclassnames = ['address_specification']
FireWire_address._privpropdict = {
	'_3c_inheritance_3e_' : _3c_inheritance_3e_,
	'ID' : ID,
}
FireWire_address._privelemdict = {
}
IP_address._superclassnames = ['address_specification']
IP_address._privpropdict = {
	'_3c_inheritance_3e_' : _3c_inheritance_3e_,
	'ID' : ID,
	'DNS_form' : DNS_form,
	'port' : port,
}
IP_address._privelemdict = {
}
LocalTalk_address._superclassnames = ['address_specification']
LocalTalk_address._privpropdict = {
	'_3c_inheritance_3e_' : _3c_inheritance_3e_,
	'network' : network,
	'node' : node,
	'socket' : socket,
}
LocalTalk_address._privelemdict = {
}
SCSI_address._superclassnames = ['address_specification']
SCSI_address._privpropdict = {
	'_3c_inheritance_3e_' : _3c_inheritance_3e_,
	'SCSI_bus' : SCSI_bus,
	'ID' : ID,
	'LUN' : LUN,
}
SCSI_address._privelemdict = {
}
Token_Ring_address._superclassnames = ['address_specification']
Token_Ring_address._privpropdict = {
	'_3c_inheritance_3e_' : _3c_inheritance_3e_,
	'ID' : ID,
}
Token_Ring_address._privelemdict = {
}
USB_Addresses._superclassnames = []
USB_Addresses._privpropdict = {
}
USB_Addresses._privelemdict = {
}
address_specification._superclassnames = []
address_specification._privpropdict = {
	'properties' : properties,
	'conduit' : conduit,
	'protocol' : protocol,
}
address_specification._privelemdict = {
}
bus_slot._superclassnames = ['address_specification']
bus_slot._privpropdict = {
	'_3c_inheritance_3e_' : _3c_inheritance_3e_,
	'ID' : ID,
}
bus_slot._privelemdict = {
}
device_specification._superclassnames = []
device_specification._privpropdict = {
	'properties' : properties,
	'device_type' : device_type,
	'device_address' : device_address,
}
device_specification._privelemdict = {
}
_Enum_econ = {
	'ADB' : 'eadb',	# 
	'printer_port' : 'ecpp',	# 
	'modem_port' : 'ecmp',	# 
	'modem_printer_port' : 'empp',	# 
	'LocalTalk' : 'eclt',	# 
	'Ethernet' : 'ecen',	# 
	'Token_Ring' : 'etok',	# 
	'SCSI' : 'ecsc',	# 
	'USB' : 'ecus',	# 
	'FireWire' : 'ecfw',	# 
	'infrared' : 'ecir',	# 
	'PC_card' : 'ecpc',	# 
	'PCI_bus' : 'ecpi',	# 
	'NuBus' : 'enub',	# 
	'PDS_slot' : 'ecpd',	# 
	'Comm_slot' : 'eccm',	# 
	'monitor_out' : 'ecmn',	# 
	'video_out' : 'ecvo',	# 
	'video_in' : 'ecvi',	# 
	'audio_out' : 'ecao',	# 
	'audio_line_in' : 'ecai',	# 
	'audio_line_out' : 'ecal',	# 
	'microphone' : 'ecmi',	# 
}

_Enum_edvt = {
	'hard_disk_drive' : 'ehd ',	# 
	'floppy_disk_drive' : 'efd ',	# 
	'CD_ROM_drive' : 'ecd ',	# 
	'DVD_drive' : 'edvd',	# 
	'storage_device' : 'edst',	# 
	'keyboard' : 'ekbd',	# 
	'mouse' : 'emou',	# 
	'trackball' : 'etrk',	# 
	'trackpad' : 'edtp',	# 
	'pointing_device' : 'edpd',	# 
	'video_monitor' : 'edvm',	# 
	'LCD_display' : 'edlc',	# 
	'display' : 'edds',	# 
	'modem' : 'edmm',	# 
	'PC_card' : 'ecpc',	# 
	'PCI_card' : 'edpi',	# 
	'NuBus_card' : 'ednb',	# 
	'printer' : 'edpr',	# 
	'speakers' : 'edsp',	# 
	'microphone' : 'ecmi',	# 
}

_Enum_epro = {
	'serial' : 'epsr',	# 
	'AppleTalk' : 'epat',	# 
	'IP' : 'epip',	# 
	'SCSI' : 'ecsc',	# 
	'ADB' : 'eadb',	# 
	'FireWire' : 'ecfw',	# 
	'IrDA' : 'epir',	# 
	'IRTalk' : 'epit',	# 
	'USB' : 'ecus',	# 
	'PC_card' : 'ecpc',	# 
	'PCI_bus' : 'ecpi',	# 
	'NuBus' : 'enub',	# 
	'bus' : 'ebus',	# 
	'Macintosh_video' : 'epmv',	# 
	'SVGA' : 'epsg',	# 
	'S_video' : 'epsv',	# 
	'analog_audio' : 'epau',	# 
	'digital_audio' : 'epda',	# 
	'PostScript' : 'epps',	# 
}


#
# Indices of types declared in this module
#
_classdeclarations = {
	'cat ' : AppleTalk_address,
	'cadr' : address_specification,
	'ctok' : Token_Ring_address,
	'cfw ' : FireWire_address,
	'cbus' : bus_slot,
	'cscs' : SCSI_address,
	'cadb' : ADB_address,
	'cusb' : USB_Addresses,
	'cip ' : IP_address,
	'clt ' : LocalTalk_address,
	'cdev' : device_specification,
	'cen ' : Ethernet_address,
}

_propdeclarations = {
	'pdns' : DNS_form,
	'pdva' : device_address,
	'patt' : AppleTalk_type,
	'pprt' : protocol,
	'pcon' : conduit,
	'patz' : AppleTalk_zone,
	'pnet' : network,
	'pdvt' : device_type,
	'pnam' : name,
	'c@#^' : _3c_inheritance_3e_,
	'ID  ' : ID,
	'pALL' : properties,
	'psoc' : socket,
	'pscb' : SCSI_bus,
	'ppor' : port,
	'patm' : AppleTalk_machine,
	'pslu' : LUN,
	'pnod' : node,
}

_compdeclarations = {
}

_enumdeclarations = {
	'econ' : _Enum_econ,
	'edvt' : _Enum_edvt,
	'epro' : _Enum_epro,
}
