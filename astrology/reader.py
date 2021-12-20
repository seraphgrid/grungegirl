# Set datetime and position
import flatlib
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
date = Datetime('2015/03/13', '17:00', '+00:00')
pos = GeoPos('38n32', '8w54')

# Finally create the chart
from flatlib.chart import Chart
chart = Chart(date, pos)
