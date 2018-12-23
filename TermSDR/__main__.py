print("TermSDR Starting..")

from graphics import display as disp
from radio import privmanager as devices
from radio import rtlsdr as rtlsdr
from radio import rtlcalculate as calculate

print("Fetching screen data")
cols = 151
rows = 34

print("Initalizing display")
display = disp.Display(rows,cols)

print("Initalizing SDR interface")
radio = rtlsdr.RTLsdr(2.048e6,70e6,60,'auto')

print("Finding SDR")
sdrs = devices.findSDR(devices.getDevices())
print(f"Found {len(sdrs)} devices")

# If not 0666 mode, do chmod
if not radio.loadDevice():
	devices.getAccess(sdrs)
	radio.loadDevice()

print("Building height map")
calculate.buildMap(rows)

print("READY")

display.clear()
try:
	while True:
		for i,point in enumerate(calculate.remap(radio.read(cols))):
			if i < cols - 1:
				display.setCol(i, int(round(point)))
except:
	print("Stopping")
	display.clear()

# Test Display
# display.clear()
# display.setCol(1,15)
# display.setCol(30,105)
# display.toolTip("Testing")
# input()