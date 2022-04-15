class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        # write code here
        try:
           del self.vals[e]
        except:
           pass

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        # write code here
        try:
           if self.vals[e] !=0:
              return True
           else :
              return False
        except :
           return False

