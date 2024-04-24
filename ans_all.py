# Ans to the queition no.01

class Star_Cinema:
    hall_list = []

    def entry_hall(self,Hall):
        self.hall_list.append(Hall)


# Ans to the queition no.02
        
class Star_Cinema:
    hall_list = []

    def entry_hall(clas,hall):
        clas.hall_list.append(hall)

class Hall:
    def __init__(self,rows,cols,hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats[hall_no] = {}
        self.show_list = []
        Star_Cinema.entry_hall(self)


# Ans to the queition no.03
        
class Hall:
    def __init__(self,rows,cols,hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats[hall_no] = [[0 for _ in range(cols)] for _ in range(rows)]

    def entry_show(self,id,movie_name,time):
        show_info = (id,movie_name,time)
        self.show_list.append(show_info)

        self.seats[id] = [[0 for _ in range(self.cols)] for _ in range(self.rows)]


# Ans to the queition no.04
        
class Hall:
    def __init__(self,rows,cols,hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats[hall_no] = [[0 for _ in range(cols)] for _ in range(rows)]

    def entry_show(self,id,movie_name,time):
        show_inf = (id,movie_name,time)
        self.show_list.append(show_inf)
        self.seats[id] = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def book_seats(self,id,seat_booked):
        for seat in seat_booked:
            row,col = seat
            if 0 <= row < self.rows and 0 <= col < self.cols:
                if self.seats[id][row][col] == 0:
                    self.seats[id][row][col] = 1
                    print(f"Seat at Row {row}, Col {col} booked successfully.")
                else:
                    print(f"Seat at Row {row}, Col {col} is already booked.")
            else:
                 print(f"Invalid seat at Row {row}, Col {col}.")


# Ans to the queition no.05
                 
class Hall:
    def __init__(self,rows,cols,hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats[hall_no] = [[0 for _ in range(cols)] for _ in range(rows)]

    def entry_show(self,id,movie_name,time):
        show_info = (id,movie_name,time)
        self.show_list.append(show_info)
        self.seats[id] = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def book_seats(self,id,seat_booked):
        for seat in seat_booked:
            row,col = seat
            if 0 <= row < self.rows and 0 <= col < self.cols:
                if self.seats[id][row][col] == 0:
                    self.seats[id][row][col] = 1
                    print(f"Seat at Row {row}, Col {col} booked successfully.")
                else:
                    print(f"Seat at Row {row}, Col {col} is already booked.")
            else:
                print(f"Invalid seat at Row {row}, Col {col}.")

    def view_show_list(self):
        print("Shows running in Hall",self.hall_no)
        for show_info in self.show_list:
            print("ID:",show_info[0],"| Movie:",show_info[1],"| Time:",show_info[2])


# Ans to the queition no.06
            
class Hall:
    def __init__(self,rows,cols,hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats[hall_no] = [[0 for _ in range(cols)] for _ in range(rows)]

    def entry_show(self,id,movie_name,time):
        show_inf = (id,movie_name,time)
        self.show_list.append(show_inf)
        self.seats[id] = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def book_seats(self,id,seat_booked):
        for seat in seat_booked:
            row,col = seat
            if 0 <= row < self.rows and 0 <= col < self.cols:
                if self.seats[id][row][col] == 0:
                    self.seats[id][row][col] = 1
                    print(f"Seat at Row {row},Col {col} booked successfully.")
                else:
                    print(f"Seat at Row {row},Col {col} is already booked.")
            else:
                print(f"Invalid seat at Row {row},Col {col}.")

    def view_show_list(self):
        print("Shows running in Hall",self.hall_no)
        for show_inf in self.show_list:
            print("ID:",show_inf[0],"| Movie:",show_inf[1],"| Time:",show_inf[2])

    def view_available_seats(self,id):
        print("Available seats for show : ",id)
        for i in range(self.rows):
            for j in range(self.cols):
                if self.seats[id][i][j] == 0:
                    print(f"Row {i},Col {j} is available")


# Ans to the queition no.07
                    
class Hall:
    def __init__(self,rows,cols,hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats[hall_no] = [[0 for _ in range(cols)] for _ in range(rows)]

    def entry_show(self, id, movie_name, time):
        show_inf = (id, movie_name, time)
        self.show_list.append(show_inf)
        self.seats[id] = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def seat_books(self, id, seat_booked):
        for seat in seat_booked:
            row,col = seat
            if 0 <= row < self.rows and 0 <= col < self.cols:
                if self.seats[id][row][col] == 0:
                    self.seats[id][row][col] = 1
                    print(f"Seat at Row {row}, Col {col} booked successfully.")
                else:
                    print(f"Seat at Row {row}, Col {col} is already booked.")
            else:
                print(f"Invalid seat at Row {row}, Col {col}.")

    def view_show_list(self):
        print("Shows running in Hall", self.hall_no)
        for show_inf in self.show_list:
            print("ID:",show_inf[0],"| Movie:",show_inf[1],"| Time:",show_inf[2])

    def view_available_seats(self, id):
        print("Available seats for show", id)
        for i in range(self.rows):
            for j in range(self.cols):
                if self.seats[id][i][j] == 0:
                    print(f"Row {i},Col {j} is available")


class Ticket_counter:
    def __init__(self):
        self.halls = {}

    def add_hall(self, hall):
        self.halls[hall.hall_no] = hall

    def view_all_shows(self):
        print("All shows running:")
        for hall_no, hall in self.halls.items():
            print(f"Hall {hall_no}:")
            hall.view_show_list()
            print()

    def view_available_seats(self,hall_no,show_id):
        if hall_no not in self.halls:
            print("Invalid hall number")
            return

        hall = self.halls[hall_no]
        hall.view_available_seats(show_id)

    def book_tickets(self,hall_no,show_id,seat_booked):
        if hall_no not in self.halls:
            print("Invalid hall number")
            return

        hall = self.halls[hall_no]
        hall.seat_books(show_id, seat_booked)


# Ans to the queition no.08(a)
        
class Hall:
    def __init__(self,rows,cols,hall_no):
        self._seats_ = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._seats_[hall_no] = [[0 for _ in range(cols)] for _ in range(rows)]

    def entry_show(self,id,movie_name,time):
        show_inf = (id,movie_name,time)
        self._show_list.append(show_inf)
        self._seats_[id] = [[0 for _ in range(self._cols)] for _ in range(self._rows)]

    def book_seats_(self,id,seat_booked):
        if id not in self._seats_:
            print("Invalid show ID")
            return

        for seat in seat_booked:
            row, col = seat
            if not (0 <= row < self._rows and 0 <= col < self._cols):
                print(f"Invalid seat at Row {row}, Col {col}.")
                continue

            if self._seats_[id][row][col] == 1:
                print(f"Seat at Row {row}, Col {col} is already booked.")
            else:
                self._seats_[id][row][col] = 1
                print(f"Seat at Row {row}, Col {col} booked successfully.")

    def view_show_list(self):
        print("Shows running in Hall",self._hall_no)
        for show_inf in self._show_list:
            print("ID:",show_inf[0],"| Movie:",show_inf[1],"| Time:",show_inf[2])

    def view_available_seats_(self,id):
        if id not in self._seats_:
            print("Invalid show ID")
            return

        print("Available seats for show", id)
        for i in range(self._rows):
            for j in range(self._cols):
                if self._seats_[id][i][j] == 0:
                    print(f"Row {i}, Col {j} is available")


# Ans to the queition no.08(b)
                    
class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._seats[hall_no] = [[0 for _ in range(cols)] for _ in range(rows)]

    def entry_show(self,id,movie_name,time):
        show_inf = (id,movie_name,time)
        self._show_list.append(show_inf)
        self._seats[id] = [[0 for _ in range(self._cols)] for _ in range(self._rows)]

    def book_seats(self, id, seats_to_book):
        if id not in self._seats:
            print("Invalid show ID")
            return

        for seat in seats_to_book:
            row, col = seat
            if not (0 <= row < self._rows and 0 <= col < self._cols):
                print(f"Invalid seat at Row {row}, Col {col}.")
                continue

            if self._seats[id][row][col] == 1:
                print(f"Seat at Row {row}, Col {col} is already booked.")
            else:
                self._seats[id][row][col] = 1
                print(f"Seat at Row {row}, Col {col} booked successfully.")

    def view_show_list(self):
        print("Shows running in Hall", self._hall_no)
        for show_inf in self._show_list:
            print("ID:",show_inf[0],"| Movie:", show_inf[1],"| Time:", show_inf[2])

    def view_available_seats(self, id):
        if id not in self._seats:
            print("Invalid show ID")
            return

        print("Available seats for show", id)
        for i in range(self._rows):
            for j in range(self._cols):
                if self._seats[id][i][j] == 0:
                    print(f"Row {i}, Col {j} is available")


# Ans to the queition no.08(c)
                    
class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._seats[hall_no] = [[0 for _ in range(cols)] for _ in range(rows)]

    def entry_show(self,id,movie_name,time):
        show_info = (id,movie_name,time)
        self._show_list.append(show_info)
        self._seats[id] = [[0 for _ in range(self._cols)] for _ in range(self._rows)]

    def book_seats(self, id,seat_booked):
        if id not in self._seats:
            print("Invalid show ID")
            return

        for seat in seat_booked:
            row,col = seat
            if not (0 <= row < self._rows and 0 <= col < self._cols):
                print(f"Invalid seat at Row {row}, Col {col}.")
                continue

            if self._seats[id][row][col] == 1:
                print(f"Seat at Row {row}, Col {col} is already booked.")
            else:
                self._seats[id][row][col] = 1
                print(f"Seat at Row {row}, Col {col} booked successfully.")

    def view_show_list(self):
        print("Shows running in Hall", self._hall_no)
        for show_info in self._show_list:
            print("ID:",show_info[0],"| Movie:",show_info[1],"| Time:",show_info[2])

    def view_available_seats(self, id):
        if id not in self._seats:
            print("Invalid show ID")
            return

        print("Available seats for show",id)
        for i in range(self._rows):
            for j in range(self._cols):
                if self._seats[id][i][j] == 0:
                    print(f"Row {i},Col {j} is available")


# Ans to the queition no.09
                    
class Hall:
    def __init__(self,rows,cols,hall_no):
        self.__seats = {}
        self._show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__allocate_seats()

    def entry_show(self,show_id,movie_name,time):
        show_inf = (show_id,movie_name,time)
        self._show_list.append(show_inf)

    def book_seats(self,show_id,seat_list):
        for show in self._show_list:
            if show[0] == show_id:
                for row, col in seat_list:
                    if self.__seats[self.__hall_no][row][col] == 'free':
                        self.__seats[self.__hall_no][row][col] = 'booked'
                    else:
                        print(f"Seat ({row}, {col}) is already booked.")
                print("Seats booked successfully.")
                return
        print("Show ID unfound.")

    def show_lst(self):
        print("Show List:")
        for show in self._show_list:
            print(f"Show ID: {show[0]}, Movie Name: {show[1]}, Time: {show[2]}")

    def __allocate_seats(self):
        seats = [['free' for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__seats[self.__hall_no] = seats

