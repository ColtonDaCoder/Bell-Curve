
import math
class bellcurve:
  def function(x, mean) :
    std_deviation = 1
    y = math.e * (1/(std_deviation * math.sqrt(2*math.pi)))
    exp = -1 * ((x - mean)**2)/(2*std_deviation**2)
    return y**exp
  print(function(6,6))
