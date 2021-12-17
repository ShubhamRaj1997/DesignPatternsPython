"""
A class/method/function should have only 1 reason to change!!!
It should have single responsibility

eg. book movie for a theatre
"""
class BookMovie(object):
    """
    Bad code
    """
    def book_movie_seat(self, movie, seat):
        if self.is_seat_available(seat):
            return False
        self.book_seat()

    def is_seat_available(self, seat):
        pass

    def book_seat(self):
        pass

"""
In above class if we change how the seat availability is defined, it will change,
if booking seat process changes it will be changed so, move it to somthing like SeatValidator class 
give it seat and ask if the seat is available
"""

