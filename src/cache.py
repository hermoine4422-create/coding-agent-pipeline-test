from collections import deque
import time

class SimpleCache:
  def __init__(self, max_size=5):
    self.items = deque(maxlen=max_size) 
    
    def add(self, value): 
      self.items.append((time.time(), value)) 
      
      def latest(self): 
      if not self.items:
        return None 
        return self.items[-1][1]
