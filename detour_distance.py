from collections import namedtuple
from math import radians, cos, sin, asin, sqrt
 
def haversine_distance((lat1, lon1, lat2, lon2)):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    referenced from: http://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
 
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
 
    # 3958.75 miles is the radius of the Earth
    distance = 3958.75 * c
    return distance 
 
def consecutive_points(points):
  """
  returns consecutive elements of a list as tuple
  for example, if list has elements [A, B, C, D] it returns (A, B), (B, C), (C, D)
  """
  i = 0
  j = i + 1
  while j < len(points):
    yield points[i].lat, points[i].lon, points[j].lat, points[j].lon
    i += 1
    j += 1
 
def total_distance(points):
  return reduce(lambda x, y: x + y, map(haversine_distance, [x for x in consecutive_points(points)]))
 
def shorter_detour(tourA, tourB):
  # there are 2 possible cases 
  # (i) Driver A pickes up Driver B
  d1 = total_distance((tourA.start, tourB.start, tourB.end, tourA.end ))
  # (ii) Driver B picks up Driver A
  d2 = total_distance((tourB.start, tourA.start, tourA.end, tourB.end ))
 
  if d1 < d2:
    print "Shorter Detour if Driver A picks up Driver B, total distance : %f compared to : %f and path is: %s%s%s%s" % (d1, d2, tourA.start.point, tourB.start.point, tourB.end.point, tourA.end.point)
  else: 
    print "Shorter Detour if Driver B picks up Driver A, total distance : %f compared to : %f and path is: %s%s%s%s" % (d2, d1, tourB.start.point, tourA.start.point, tourA.end.point, tourB.end.point)
     
def main():
  Point = namedtuple('Point', 'point lat lon')
  pointA = Point("A", 37.776685, -122.394259) # caltrain station
  pointB = Point("B", 37.760568, -122.412705) # Lyft office
  pointC = Point("C", 37.766387, -122.398820) # 16th and Berry
  pointD = Point("D", 37.757430, -122.412381) # 21st and Harrison
   
  Tour = namedtuple('Tour', 'start end')
  tourA = Tour(pointA, pointB)
  tourB = Tour(pointC, pointD)
  shorter_detour(tourA, tourB)
 
if __name__ == "__main__":
  main()
