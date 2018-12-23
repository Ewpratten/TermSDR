from graphics import display as disp

cols = 151
rows = 34

display = disp.Display(rows,cols)

# Test Display
display.clear()
display.setCol(1,15)
display.setCol(30,105)
display.toolTip("Testing")
input()