from queue_file import Queue

class AnimalShelter:
    def __init__(self):
        """Initialize the animal shelter with an empty queue for cats and dogs."""
        self.shelter = Queue()


    def enqueue(self, animal):
        """Add an animal to the animal shelter."""
        if animal["species"] == "cat" or animal["species"] == "dog":
            self.shelter.enqueue(animal)
        else:
            return ("Invalid species")


    def dequeue(self, pref=None):
        """Remove and return the first cat or dog in the animal shelter"""
        if pref == "cat" or pref == "dog":
            current = self.shelter.front
            previous = None


            # find preferred species
            while current is not None and current.value["species"] != pref:
                previous = current
                current = current.next

            if current is not None:
                if previous is None:
                    self.shelter.front = current.next

                # The preferred animal is not at the front of the queue.
                elif previous is not None:
                    previous.next = current.next

                    
                return current.value
            
        # Invalid preference, return None. 
        return None
        

    def __str__(self):
        """Return a string representation of the animal shelter."""
        output = ""
        current = self.shelter.front
        while current is not None:
            output += f"{current.value} ---> "
            current = current.next
        output += "None"
        return output
