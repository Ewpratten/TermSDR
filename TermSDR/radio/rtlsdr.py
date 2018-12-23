from rtlsdr import RtlSdr

class RTLsdr(object):
	def __init__(self, ):
		self.radio = RtlSdr()
		
		# Set up sdr
		self.radio.sample_rate = 2.048e6
		