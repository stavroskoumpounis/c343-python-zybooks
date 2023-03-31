"""
Airport runways are numbered using a 2-digit number, like 09. The meaning generally is that planes taking off or
landing on that runway will be facing 090 or 90 degrees rotated right from north, namely facing east. Given a runway
number (integer), output the degrees followed by the closest direction indication (north, northeast, east, southeast,
south, southwest, west, or northwest). If the input is 03, the output is: 30 degrees (northeast).
"""

runway_deg = int(input()) * 10

if (runway_deg >= 337.5) or (runway_deg < 22.5):
    direction = "north"
elif (runway_deg >= 22.5) and (runway_deg < 67.5):
    direction = "northeast"
elif (runway_deg >= 67.5) and (runway_deg < 112.5):
    direction = "east"
elif (runway_deg >= 112.5) and (runway_deg < 157.5):
    direction = "southeast"
elif (runway_deg >= 157.5) and (runway_deg < 202.5):
    direction = "south"
elif (runway_deg >= 202.5) and (runway_deg < 247.5):
    direction = "southwest"
elif (runway_deg >= 247.5) and (runway_deg < 292.5):
    direction = "west"
else:
    direction = "northwest"

print(f"{runway_deg} degrees ({direction})")
