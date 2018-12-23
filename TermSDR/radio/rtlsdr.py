from rtlsdr import RtlSdr

class RTLsdr(object):
	def __init__(self, rate, freq, correction, gain):
		
		# Set up sdr
		self.sample_rate     = rate
		self.center_freq     = freq
		self.freq_correction = correction
		self.gain            = gain
	
	def loadDevice(self):
		try:
			self.radio = RtlSdr()
			
			self.radio.sample_rate     = self.sample_rate
			self.radio.center_freq     = self.center_freq
			self.radio.freq_correction = self.freq_correction
			self.radio.gain            = self.gain
			return True
		except:
			return False
	
	def read(self,width:int):
		cut = (512 - width) // 2
		return self.radio.read_samples(512).tolist()[cut:-cut]