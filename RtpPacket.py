import sys
from time import time
import VideoStream
HEADER_SIZE = 12

class RtpPacket:	
	
	
	def __init__(self):
		self.header = bytearray(HEADER_SIZE)
		
	def encode(self, version, padding, extension, cc, seqnum, marker, pt, ssrc, payload):
		"""Encode the RTP packet with header fields and payload."""
		timestamp = int(time())
		self.header = bytearray(HEADER_SIZE)
		#--------------
		# TO COMPLETE
		#--------------
		# Fill the header bytearray with RTP header fields
		
		# RTP HEADER STRUCTURE (http://www.siptutorial.net/RTP/header.html)
		# --------------------
        # version - 2 bits
        # padding - 1 bit
        # extension - 1 bit
        # CSRC count (CC) - 4 bits
        # marker - 1 bit
        # payload type (PT) - 7 bits
        # sequence number (seqnum) - 16 bits
        # timestamp - 32 bits
        # synchronization source (SSRC) - 32 bits
        
        # TODO: figure out how to set bits for the header bytearray
		# version = 2
		# padding = 0
		# extension = 0
		# cc = 0
		# marker = 0
		# pt = 26 # MJPEG type
		# seqnum = frameNbr
		# ssrc = 0 
        
        # first byte (bits 0-7)
        #
        # version = 2 (2 bits)  
        # padding = 0 (1 bit)
        # extension = 0 (1 bit)
        # CSRC count (CC) = 0 (4 bits)
        # 
        #  V    P   X     CC
        # 0 1 | 2 | 3 | 4 5 6 7 (bits 0-7)
        # 1 0 | 0 | 0 | 0 0 0 0 (set the bits)
        # ---------------------------------
        
		self.header[0] = version << 6 | padding << 5 | extension << 4 | cc
        
        # second byte (bits 8-15)
        #
        # marker = 0 (1 bit)
        # payload type (PT) = 26 (7 bits)
        # ---------------------------------

		self.header[1] = marker << 7 | pt 
        
        # third and fourth bytes for seqnum (bits 16-31)
        # ---------------------------------
        
		self.header[2] = (seqnum >> 8) & 0xFF
		self.header[3] = seqnum & 0xFF
        
        # next four bytes for timestamp (bits 32-63)
        # ---------------------------------
		
		self.header[4] = (timestamp >> 24) & 0xFF
		self.header[5] = (timestamp >> 16) & 0xFF
		self.header[6] = (timestamp >> 8) & 0xFF
		self.header[7] = timestamp & 0xFF
        
        # last four bytes for ssrc (bits 64-95)
        # ---------------------------------
        
		self.header[8] = (ssrc >> 24) & 0xFF
		self.header[9] = (ssrc >> 16) & 0xFF
		self.header[10] = (ssrc >> 8) & 0xFF
		self.header[11] = ssrc & 0xFF
        
        # Get the payload from the argument
		self.payload = payload
		
	def decode(self, byteStream):
		"""Decode the RTP packet."""
		self.header = bytearray(byteStream[:HEADER_SIZE])
		self.payload = byteStream[HEADER_SIZE:]
	
	def version(self):
		"""Return RTP version."""
		return int(self.header[0] >> 6)
	
	def seqNum(self):
		"""Return sequence (frame) number."""
		seqNum = self.header[2] << 8 | self.header[3]
		return int(seqNum)
	
	def timestamp(self):
		"""Return timestamp."""
		timestamp = self.header[4] << 24 | self.header[5] << 16 | self.header[6] << 8 | self.header[7]
		return int(timestamp)
	
	def payloadType(self):
		"""Return payload type."""
		pt = self.header[1] & 127
		return int(pt)
	
	def getPayload(self):
		"""Return payload."""
		return self.payload
		
	def getPacket(self):
		"""Return RTP packet."""
		return self.header + self.payload