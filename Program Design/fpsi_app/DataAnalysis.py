class Compute():
	def __init__(self,master=None):
		self.operate(data={},piezo_conversion=0)

	def operate(self,data,piezo_conversion):
		# Do math stuff and create dictionaries to use
		# Create a graph with axises labeled with Intensity vs. Distance Moved
		intensity = data['intensity']*data['normalize'] # Normalize the intensity for easier calculations
		distance = data['volts']*piezo_conversion # Where the piezo_conversion is in meters/volts
		wavelength = data['wavelength'] # Units are in Angstroms

		# Calculate the wavelength based on the distance between the peaks.
		graphical_analysis = {'Intensity': intensity,'Distance': distance, 'Wavelength': wavelength}
		return graphical_analysis