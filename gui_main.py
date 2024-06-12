import tkinter as tk
from tkinter import simpledialog, ttk, messagebox
from datetime import datetime

class AirlineReservationSystem(tk.Tk):
    @staticmethod
    def locate_username(username):
        with open("customerdata2.txt", "r") as file:
            for idx, line in enumerate(file, start=1):
                if line.startswith(username):
                    return idx

    def __init__(self):
        super().__init__()
        self.title("Airline Reservation System")
        self.geometry("600x400")

        # Initialize frames as None
        self.search_airline_frame = None
        self.signup_frame = None
        self.login_frame = None
        self.customer_login_frame = None
        self.admin_login_frame = None
        self.regis_cus_frame = None
        self.show_airline_frame = None
        self.available_destinations_frame = None
        self.my_account_frame = None
        self.booking_frame = None
        self.add_flight_frame = None
        self.search_results_frame = None
        self.payment_details_frame = None
        self.confirm_booking_frame = None
        self.confirm_booking_two_way_frame = None
        self.points_frame = None
        self.admin_menu_frame = None
        self.display_records_frame = None
        self.by_flight_number_frame = None
        self.booked_by_customer_frame = None
        self.summary_total_ticket_sold_frame = None

        self.create_widgets()

    def create_widgets(self):
        # Main Menu
        self.main_menu_frame = tk.Frame(self)
        self.main_menu_frame.pack()

        self.label = tk.Label(self.main_menu_frame, text="Airline Reservation System Main Menu", font=("Arial", 16))
        self.label.pack(pady=20)

        self.show_airline_button = tk.Button(self.main_menu_frame, text="Show Airline Schedules", command=self.show_airline, width=20, bg='gray')
        self.show_airline_button.pack(pady=10)

        self.search_airline_button = tk.Button(self.main_menu_frame, text="Search Airline Schedules", command=self.search_airline, width=20, bg='gray')
        self.search_airline_button.pack(pady=10)

        self.signup_button = tk.Button(self.main_menu_frame, text="Signup Membership", command=self.signup, width=20, bg='gray')
        self.signup_button.pack(pady=10)

        self.login_button = tk.Button(self.main_menu_frame, text="Login", command=self.login, width=20, bg='gray')
        self.login_button.pack(pady=10)

        self.exit_button = tk.Button(self.main_menu_frame, text="Exit Program", command=self.quit, width=20, bg='gray')
        self.exit_button.pack(pady=10)

    def show_airline(self):
        self.main_menu_frame.pack_forget()
        self.show_airline_frame = tk.Frame(self)

        # Create a canvas widget and configure it to allow scrolling
        canvas = tk.Canvas(self.show_airline_frame)
        scrollbar = tk.Scrollbar(self.show_airline_frame, orient="vertical", command=canvas.yview)
        frame = tk.Frame(canvas)

        # Configure the canvas and scrollbar
        canvas.create_window((0, 0), window=frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Add widgets to the frame
        totalrow = sum(1 for _ in open('Available_Flight_Schedules.txt'))
        header = tk.Label(frame, text="Air Malaysia Group (AMG) All Airlines", font=("Arial", 16))
        header.grid(row=0, column=0, columnspan=14, pady=14)

        cols = ["No.", "Flight Number", "From", "From_Country", "To", "To_Country", "Depart Date", "Return Date",
                "Depart Time", "Return Time", "Price", "Flight Duration (in hours)"]
        for col in cols:
            tk.Label(frame, text=col, borderwidth=1, relief="solid").grid(row=1, column=cols.index(col), sticky="nsew")

        for row in range(totalrow):
            with open('Available_Flight_Schedules.txt', 'r') as file:
                line = file.readlines()[row]
                data = list(line.replace("\n", "").split(";"))
                tk.Label(frame, text=f"{row + 1}", borderwidth=1, relief="solid").grid(row=row + 2, column=0,
                                                                                       sticky="nsew")
                for col in range(1, len(cols)):
                    tk.Label(frame, text=data[col - 1], borderwidth=1, relief="solid").grid(row=row + 2, column=col,
                                                                                            sticky="nsew")

        back_button = tk.Button(frame, text="Back to Main Menu", command=self.back_to_main_menu, bg='gray')
        back_button.grid(row=totalrow + 2, column=0, columnspan=14, pady=14)

        # Pack the canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Configure the frame to adjust to the content
        frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        self.show_airline_frame.pack(fill="both", expand=True)

        # Adjust window size
        self.geometry("1000x800")

    def flight_header_ui(self):
        header = tk.Label(self.search_airline_frame, text="Air Malaysia Group (AMG)", font=("Arial", 16))
        header.pack(pady=14)
        cols = ["No.", "Flight Number", "From", "Country", "To", "Country", "Depart Date", "Return Date", "Depart Time",
                "Return Time", "Price", "Flight Duration (in hours)"]
        for col in cols:
            tk.Label(self.search_airline_frame, text=col, borderwidth=1, relief="solid").pack()

    def available_destinations_ui(self):
        self.main_menu_frame.pack_forget()
        self.available_destinations_frame = tk.Frame(self)
        self.available_destinations_frame.pack(fill="both", expand=True)

        header = tk.Label(self.available_destinations_frame, text="Air Malaysia Group (AMG) Available Destinations",
                          font=("Arial", 16))
        header.pack(pady=10)

        destinations = [
            "Kuala Lumpur (Malaysia)", "Penang (Malaysia)", "Johor Bahru (Malaysia)", "Dhaka (Bangladesh)",
            "Shanghai (China)", "Bali (Indonesia)", "Vientiane (Laos)", "Choibalsan (Mongolia)",
            "Manila (Philippines)", "Taipei (Taiwan)", "Bandar Seri Begawan (Brunei)", "Batumi (Georgia)",
            "Tokyo (Japan)", "Mandalay (Myanmar)", "Singapore (Singapore)", "Bangkok (Thailand)",
            "Phnom Penh (Cambodia)", "Chennai (India)", "Seoul (South Korea)", "Dharavandhoo (Maldives)",
            "Bhadrapur (Nepal)", "Colombo (Sri Lanka)", "Ho Chi Minh City (Vietnam)", "Melbourne (Australia)",
            "Wellington (New Zealand)", "New York City (United States)", "London (United Kingdom)"
        ]
        for destination in destinations:
            tk.Label(self.available_destinations_frame, text=destination, borderwidth=1, relief="solid").pack()

        back_button = tk.Button(self.available_destinations_frame, text="Back to Main Menu",
                                command=self.back_to_main_menu, bg='gray')
        back_button.pack(pady=10)

    def search_airline(self):
        self.main_menu_frame.pack_forget()
        self.search_airline_frame = tk.Frame(self)
        self.search_airline_frame.pack()

        self.label = tk.Label(self.search_airline_frame, text="Search Airline Schedules", font=("Arial", 16))
        self.label.pack(pady=20)

        self.flight_num_button = tk.Button(self.search_airline_frame, text="Search by Flight Number",
                                           command=self.search_by_flight_number, width=25, bg='gray')
        self.flight_num_button.pack(pady=10)

        self.departure_arrival_button = tk.Button(self.search_airline_frame, text="Search by Departure & Arrival",
                                                  command=self.search_by_departure_arrival, width=25, bg='gray')
        self.departure_arrival_button.pack(pady=10)

        self.date_button = tk.Button(self.search_airline_frame, text="Search by Date", command=self.search_by_date,
                                     width=25, bg='gray')
        self.date_button.pack(pady=10)

        self.back_button = tk.Button(self.search_airline_frame, text="Back to Main Menu",
                                     command=self.back_to_main_menu, width=25, bg='gray')
        self.back_button.pack(pady=10)

    def perform_search(self, search_option, *args):
        if search_option == "Date":
            departure_date, return_date = args

            # Perform search based on the dates provided
            with open("Available_Flight_Schedules.txt", "r") as file:
                lines = file.readlines()

            # Preprocess lines to match user input
            lines = [line.upper().replace(" ", "").strip() for line in lines]

            # Initialize variables
            flag = False
            search_results = []

            # Search for flights with matching departure and return dates
            for line in lines:
                if departure_date in line and return_date in line:
                    flag = True
                    search_results.append(line)

            # If no matching flights found, display a message
            if not flag:
                messagebox.showinfo("Flight Search",
                                    f"Sorry, there are no flights on {departure_date} to {return_date}.")
            else:
                messagebox.showinfo("Flight Search",
                                    f"Flights on {departure_date} to {return_date} are available! Schedules are shown below.")
                for flight_details in search_results:
                    self.display_search_results(flight_details)

    def search_by_flight_number(self):
        flight_number = simpledialog.askstring("Search by Flight Number", "Enter Flight Number: (Only Number)")
        if flight_number:
            # Perform search and display results
            with open("Available_Flight_Schedules.txt", "r") as file:
                lines = file.readlines()

            # Preprocess lines to match user input
            lines = [line.upper().replace(" ", "").strip() for line in lines]

            # Initialize variables
            flag = False
            search_flight_details = None

            # Search for the flight number
            for index, line in enumerate(lines):
                if flight_number in line:
                    flag = True
                    search_flight_details = lines[index].split(";")  # Split the line into individual details
                    break

            # If flight not found, display a message
            if not flag:
                messagebox.showinfo("Flight Search", f"Sorry, the flight number {flight_number} is unavailable in AMG.")
            else:
                messagebox.showinfo("Flight Search", f"{flight_number} is available! Schedules are shown below.")
                self.display_search_results(search_flight_details)

    def display_search_results(self, search_flight_details):
        # Check if the flight details list has at least the required number of elements
        if len(search_flight_details) >= 11:  # Assuming there should be at least 11 elements
            # Display flight details in a new window
            result_window = tk.Toplevel(self)
            result_window.title("Search Results")
            result_window.geometry("600x600")  # Set the geometry to 600x600

            # Create Treeview widget
            tree = ttk.Treeview(result_window)

            # Define columns
            tree["columns"] = ("1", "2")

            # Format columns
            tree.column("#0", width=150, minwidth=150)
            tree.column("1", anchor="w", width=150)
            tree.column("2", anchor="w", width=150)

            # Add headings
            tree.heading("#0", text="Field")
            tree.heading("1", text="Value")

            # Add flight details to the treeview
            labels = ["Flight Number", "From", "To", "Depart Date", "Return Date", "Depart Time", "Return Time",
                      "Price", "Duration"]
            for i, label in enumerate(labels):
                tree.insert("", i, text=label, values=(search_flight_details[i],))

            # Pack the treeview
            tree.pack(expand=True, fill="both")

            # Add a button to go back to the search airline screen
            back_button = tk.Button(result_window, text="Back to Search Airline", command=result_window.destroy, bg='gray')
            back_button.pack(pady=10)

        else:
            messagebox.showerror("Error", "Invalid flight details found.")

    def search_by_departure_arrival(self):
        from_place = simpledialog.askstring("Search by Departure & Arrival", "From:")
        to_place = simpledialog.askstring("Search by Departure & Arrival", "To:")

        if from_place and to_place:
            # Remove spaces from the input
            from_place = from_place.upper().replace(" ", "")
            to_place = to_place.upper().replace(" ", "")

            # Perform search and display results
            with open("Available_Flight_Schedules.txt", "r") as file:
                lines = file.readlines()

            # Preprocess lines to match user input
            lines = [line.upper().replace(" ", "").strip() for line in lines]

            # Initialize variables
            flag = False
            search_results = []

            # Search for flights with matching departure and arrival places
            for line in lines:
                if from_place in line and to_place in line:
                    flag = True
                    search_results.append(line)

            # If no matching flights found, display a message
            if not flag:
                messagebox.showinfo("Flight Search", f"Sorry, {from_place} to {to_place} is unavailable in AMG.")
            else:
                messagebox.showinfo("Flight Search",
                                    f"{from_place} to {to_place} is available! Schedules are shown below.")

                # Display search results
                for flight_details in search_results:
                    # Split the line into individual details
                    search_flight_details = flight_details.split(";")
                    # Display search results in the same format as search_by_flight_number
                    self.display_search_results(search_flight_details)

    def search_by_date(self):
        # Step by step input for departure date
        departure_day = simpledialog.askstring("Search by Date", "Depart Day (DD):")
        departure_month = simpledialog.askstring("Search by Date", "Depart Month (e.g., JANUARY):")
        departure_year = simpledialog.askstring("Search by Date", "Depart Year (YYYY):")

        # Step by step input for return date
        return_day = simpledialog.askstring("Search by Date", "Return Day (DD):")
        return_month = simpledialog.askstring("Search by Date", "Return Month (e.g., JANUARY):")
        return_year = simpledialog.askstring("Search by Date", "Return Year (YYYY):")

        # Combine inputs into date strings
        departure_date = f"{departure_day}-{departure_month.upper()}-{departure_year}"
        return_date = f"{return_day}-{return_month.upper()}-{return_year}"

        if departure_date and return_date:
            # Remove spaces from the input
            departure_date = departure_date.replace(" ", "")
            return_date = return_date.replace(" ", "")

            # Perform search and display results
            with open("Available_Flight_Schedules.txt", "r") as file:
                lines = file.readlines()

            # Preprocess lines to match user input
            lines = [line.upper().replace(" ", "").strip() for line in lines]

            # Initialize variables
            flag = False
            search_results = []

            # Search for flights with matching departure and return dates
            for line in lines:
                if departure_date in line and return_date in line:
                    flag = True
                    search_results.append(line.split(";"))

            # If no matching flights found, display a message
            if not flag:
                messagebox.showinfo("Flight Search",
                                    f"Sorry, there are no flights on {departure_date} to {return_date}.")
            else:
                result_window = tk.Toplevel(self)
                result_window.title("Search Results")
                result_window.geometry("1000x600")

                # Create Treeview widget
                tree = ttk.Treeview(result_window, columns=("Flight Number", "From", "To", "Depart Date", "Return Date",
                                                             "Depart Time", "Return Time", "Price", "Duration"))

                # Define columns
                tree.column("#0", width=0, stretch=tk.NO)  # Hide the default column
                tree.column("Flight Number", anchor="w", width=120)
                tree.column("From", anchor="w", width=120)
                tree.column("To", anchor="w", width=120)
                tree.column("Depart Date", anchor="w", width=120)
                tree.column("Return Date", anchor="w", width=120)
                tree.column("Depart Time", anchor="w", width=120)
                tree.column("Return Time", anchor="w", width=120)
                tree.column("Price", anchor="w", width=120)
                tree.column("Duration", anchor="w", width=120)

                # Add headings
                tree.heading("#0", text="", anchor="w")
                tree.heading("Flight Number", text="Flight Number", anchor="w")
                tree.heading("From", text="From", anchor="w")
                tree.heading("To", text="To", anchor="w")
                tree.heading("Depart Date", text="Depart Date", anchor="w")
                tree.heading("Return Date", text="Return Date", anchor="w")
                tree.heading("Depart Time", text="Depart Time", anchor="w")
                tree.heading("Return Time", text="Return Time", anchor="w")
                tree.heading("Price", text="Price", anchor="w")
                tree.heading("Duration", text="Duration", anchor="w")

                # Add flight details to the treeview
                for details in search_results:
                    tree.insert("", tk.END, values=details)

                # Pack the treeview
                tree.pack(expand=True, fill="both")

                # Add a button to go back to the search airline screen
                back_button = tk.Button(result_window, text="Back to Search Airline", command=result_window.destroy, bg='gray')
                back_button.pack(pady=10)

    def signup(self):
        self.main_menu_frame.pack_forget()
        self.signup_frame = tk.Frame(self)
        self.signup_frame.pack()

        self.label = tk.Label(self.signup_frame, text="Signup Membership", font=("Arial", 16))
        self.label.pack(pady=20)

        self.username_label = tk.Label(self.signup_frame, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.signup_frame, width=25)
        self.username_entry.pack()

        self.password_label = tk.Label(self.signup_frame, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.signup_frame, show='*', width=25)
        self.password_entry.pack()

        self.confirm_password_label = tk.Label(self.signup_frame, text="Confirm Password:")
        self.confirm_password_label.pack()
        self.confirm_password_entry = tk.Entry(self.signup_frame, show='*', width=25)
        self.confirm_password_entry.pack()

        self.register_button = tk.Button(self.signup_frame, text="Register", command=self.register_user,
                                         width=20, bg='gray')
        self.register_button.pack(pady=10)

        self.back_button = tk.Button(self.signup_frame, text="Back to Main Menu", command=self.back_to_main_menu,
                                     width=20, bg='gray')
        self.back_button.pack(pady=10)

    def register_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return

        if len(password) <= 6:
            messagebox.showerror("Error", "Password is too short!")
            return

        with open("checkusername.txt", "r") as db:
            if f"\t{username}\n" in db:
                messagebox.showerror("Error", "Username already exists!")
                return

        with open("customerdata.txt", "a") as db:
            db.write(f"{username}\t\t{password}\n")

        with open("checkusername.txt", "a") as db2:
            db2.write(f"\t{username}\n")

        messagebox.showinfo("Success", "Successfully registered!")
        self.back_to_main_menu()

    def login(self):
        self.main_menu_frame.pack_forget()
        self.login_frame = tk.Frame(self)
        self.login_frame.pack()

        self.login_label = tk.Label(self.login_frame, text="Login Page", font=("Arial", 16))
        self.login_label.pack(pady=20)

        self.customer_button = tk.Button(self.login_frame, text="Login as Customer", command=self.login_customer,
                                         width=20, bg='gray')
        self.customer_button.pack(pady=10)

        self.admin_button = tk.Button(self.login_frame, text="Login as Administrator", command=self.login_admin,
                                      width=20, bg='gray')
        self.admin_button.pack(pady=10)

        self.back_button = tk.Button(self.login_frame, text="Back to Main Menu", command=self.back_to_main_menu,
                                     width=20, bg='gray')
        self.back_button.pack(pady=10)

    def login_customer(self):
        self.login_frame.pack_forget()
        self.customer_login_frame = tk.Frame(self)
        self.customer_login_frame.pack()

        self.label = tk.Label(self.customer_login_frame, text="Customer Login", font=("Arial", 16))
        self.label.pack(pady=20)

        self.username_label = tk.Label(self.customer_login_frame, text="Username:", width=20, anchor='w')
        self.username_label.pack()
        self.username_entry = tk.Entry(self.customer_login_frame, width=25)
        self.username_entry.pack()

        self.password_label = tk.Label(self.customer_login_frame, text="Password:", width=20, anchor='w')
        self.password_label.pack()
        self.password_entry = tk.Entry(self.customer_login_frame, show='*', width=25)
        self.password_entry.pack()

        self.login_button = tk.Button(self.customer_login_frame, text="Login", command=self.authenticate_customer,
                                      width=20, bg='gray')
        self.login_button.pack(pady=10)

        self.back_button = tk.Button(self.customer_login_frame, text="Back to Login Menu",
                                     command=self.back_to_login_menu, width=20, bg='gray')
        self.back_button.pack(pady=10)

    def authenticate_customer(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        with open("customerdata.txt", "r") as customerdb:
            for line in customerdb:
                list = line.split()
                if username == list[0] and password == list[1]:
                    messagebox.showinfo("Success", f"Logged in successful! Hi {username}")
                    get_username = username
                    self.regis_cus_menu(get_username)
                    return

        messagebox.showerror("Error", "Failed to log in! Please try again.")
        self.back_to_login_menu()

    def regis_cus_menu(self, get_username):
        if self.booking_frame is not None:
            self.booking_frame.pack_forget()
        if self.points_frame is not None:
            self.points_frame.pack_forget()
        if self.add_flight_frame is not None:
            self.add_flight_frame.pack_forget()

        self.customer_login_frame.pack_forget()
        self.regis_cus_frame = tk.Frame(self)
        self.regis_cus_frame.pack()

        self.label = tk.Label(self.regis_cus_frame, text=f"Welcome {get_username}", font=("Arial", 16))
        self.label.pack(pady=20)

        self.my_account_button = tk.Button(self.regis_cus_frame, text="My Account",
                                           command=lambda: self.show_account(get_username), width=20, bg='gray')
        self.my_account_button.pack(pady=10)

        self.my_booking_button = tk.Button(self.regis_cus_frame, text="My Booking",
                                           command=lambda: self.show_booking(get_username), width=20, bg='gray')
        self.my_booking_button.pack(pady=10)

        self.add_flight_button = tk.Button(self.regis_cus_frame, text="Add New Flight",
                                           command=lambda: self.add_new_flight(get_username), width=20, bg='gray')
        self.add_flight_button.pack(pady=10)

        self.my_points_button = tk.Button(self.regis_cus_frame, text="My Points",
                                          command=lambda: self.show_points(get_username), width=20, bg='gray')
        self.my_points_button.pack(pady=10)

        self.logout_button = tk.Button(self.regis_cus_frame, text="Log Out",
                                       command=self.back_to_main_menu, width=20, bg='gray')
        self.logout_button.pack(pady=10)

    def show_account(self, username):
        # Locate and print account details
        self.print_account_details(username)

    def print_account_details(self, username):
        with open("customerdata2.txt", "r") as file:
            index = 0
            for line in file:
                index += 1
                if username in line:
                    break
            file.seek(0)
            data = file.readlines()[index - 1].strip().split(", ")
            self.show_account_details(data)

    def show_account_details(self, data):
        account_window = tk.Toplevel(self)
        account_window.title("Account Details")
        account_window.geometry("600x600")

        details = {
            "Username": data[0],
            "Password": data[1],
            "Email Address": data[2],
            "Name": data[3],
            "Mobile Number": data[4],
            "Date of Birth": data[5],
            "Citizenship": data[6],
            "Passport ID": data[7],
            "Emergency Contact Number": data[8],
            "Relationship": data[9],
            "Credit / Debit Card ID": data[10],
            "Expiry Date": data[11]
        }

        row = 0
        for key, value in details.items():
            tk.Label(account_window, text=key, font=("Arial", 12), anchor="w").grid(row=row, column=0, sticky="w",
                                                                                    padx=10, pady=5)
            tk.Label(account_window, text=value, font=("Arial", 12), anchor="w").grid(row=row, column=1, sticky="w",
                                                                                      padx=10, pady=5)
            row += 1

        update_button = tk.Button(account_window, text="Update Profile", command=lambda: self.update_profile(data[0]),
                                  bg='gray')
        update_button.grid(row=row, column=0, pady=10)

        back_button = tk.Button(account_window, text="Back to Menu", command=account_window.destroy, bg='gray')
        back_button.grid(row=row, column=1, pady=10)

    def update_profile(self, get_username):
        update_window = tk.Toplevel(self)
        update_window.title("Update Profile")
        update_window.geometry("600x600")

        labels = [
            "Username", "Password", "Email Address", "Name", "Mobile Number", "Date of Birth (DD-MM-YYYY)",
            "Citizenship", "Passport ID", "Emergency Contact Number", "Relationship", "Credit / Debit Card No",
            "Expiry Date"
        ]
        entries = {}

        for idx, label in enumerate(labels):
            tk.Label(update_window, text=label).grid(row=idx, column=0, padx=10, pady=5)
            entry = tk.Entry(update_window)
            entry.grid(row=idx, column=1, padx=10, pady=5)
            entries[label] = entry

        def save_profile():
            data = []
            for label in labels:
                data.append(entries[label].get())
            text = (get_username + ", " + data[0] + ", " + data[1] + ", " + data[2] + ", " +
                    data[3] + ", " + data[4] + ", " + data[5] + ", " +
                    data[6] + ", " + data[7] + ", " + data[8] + ", " +
                    data[9] + ", " + data[10] + ", " + data[11] + "\n")
            text2 = (get_username + "\t\t" + data[1] + "\n")
            self.replace_line("customerdata2.txt", self.locate_username(get_username), text)
            self.replace_line("customerdata.txt", self.locate_username(get_username), text2)
            messagebox.showinfo("Success", "Your Profile is successfully updated into the system!")
            update_window.destroy()
            self.show_account_details(get_username)

        save_button = tk.Button(update_window, text="Save", command=save_profile, bg='gray')
        save_button.grid(row=len(labels), column=0, pady=10)

        cancel_button = tk.Button(update_window, text="Cancel", command=update_window.destroy, bg='gray')
        cancel_button.grid(row=len(labels), column=1, pady=10)

    @staticmethod
    def replace_line(file_path, line_number, new_text):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        lines[line_number - 1] = new_text

        with open(file_path, 'w') as file:
            file.writelines(lines)

    def submit_changes(self, username):
        # Retrieve the updated values from the Entry widgets
        email = self.email_entry.get()
        password = self.password_entry.get()
        # Repeat for other fields

        # Write the updated values to the file
        with open("customerdata2.txt", "r") as file:
            lines = file.readlines()

        # Update the specific line with the new values
        for i, line in enumerate(lines):
            if username in line:
                lines[i] = f"{username}, {password}, {email}, ..."  # Update this line with all fields

        # Write the updated content back to the file
        with open("customerdata2.txt", "w") as file:
            file.writelines(lines)

        messagebox.showinfo("Success", "Profile updated successfully!")
        self.update_profile_frame.pack_forget()  # Hide the update profile frame
        self.regis_cus_menu(username)  # Go back to the customer menu

    def back_to_menu(self, username):
        # Implement the back to menu functionality
        pass

    def show_booking(self, username):
        self.regis_cus_frame.pack_forget()
        self.booking_frame = tk.Frame(self)
        self.booking_frame.pack()

        self.label = tk.Label(self.booking_frame, text=f"Bookings for {username}", font=("Arial", 16))
        self.label.pack(pady=20)

        with open("booking_data2.txt", "r") as file:
            lines = file.readlines()

        booking_list = [line.strip().split(";") for line in lines if username in line]

        tree = ttk.Treeview(self.booking_frame,
                            columns=("No", "Flight ID", "From", "To", "Depart Date", "Return Date", "Status"))
        tree.heading("#0", text="", anchor="w")
        tree.heading("No", text="No", anchor="w")
        tree.heading("Flight ID", text="Flight ID", anchor="w")
        tree.heading("From", text="From", anchor="w")
        tree.heading("To", text="To", anchor="w")
        tree.heading("Depart Date", text="Depart Date", anchor="w")
        tree.heading("Return Date", text="Return Date", anchor="w")
        tree.heading("Status", text="Status", anchor="w")

        for index, booking in enumerate(booking_list):
            tree.insert("", "end", text="",
                        values=(index + 1, booking[1], booking[3], booking[4], booking[5], booking[6], booking[7]))

        tree.pack(expand=True, fill="both")

        back_button = tk.Button(self.booking_frame, text="Back to Menu", command=lambda: self.regis_cus_menu(username),
                                bg='gray')
        back_button.pack(pady=10)

    def add_new_flight(self, username):
        self.clear_frames()
        self.add_flight_frame = tk.Frame(self)
        self.add_flight_frame.pack()

        self.label = tk.Label(self.add_flight_frame, text=f"Add New Flight for {username}", font=("Arial", 16))
        self.label.pack(pady=20)

        self.one_way_button = tk.Button(self.add_flight_frame, text="One Way", command=lambda: self.one_way(username),
                                        width=20, bg='gray')
        self.one_way_button.pack(pady=10)

        self.two_way_button = tk.Button(self.add_flight_frame, text="Two Way", command=lambda: self.two_way(username),
                                        width=20, bg='gray')
        self.two_way_button.pack(pady=10)

        self.back_button = tk.Button(self.add_flight_frame, text="Back to Menu",
                                     command=lambda: self.regis_cus_menu(username), width=20, bg='gray')
        self.back_button.pack(pady=10)

    def one_way(self, get_username):
        self.clear_frames()
        self.one_way_frame = tk.Frame(self)
        self.one_way_frame.pack()

        from_label = tk.Label(self.one_way_frame, text="Departure Location:")
        from_label.grid(row=0, column=0, padx=10, pady=10)
        self.from_entry = tk.Entry(self.one_way_frame)
        self.from_entry.grid(row=0, column=1, padx=10, pady=10)

        to_label = tk.Label(self.one_way_frame, text="Destination Location:")
        to_label.grid(row=1, column=0, padx=10, pady=10)
        self.to_entry = tk.Entry(self.one_way_frame)
        self.to_entry.grid(row=1, column=1, padx=10, pady=10)

        depart_date_label = tk.Label(self.one_way_frame, text="Departure Date (DD-Month-YYYY):")
        depart_date_label.grid(row=2, column=0, padx=10, pady=10)
        self.depart_date_entry = tk.Entry(self.one_way_frame)
        self.depart_date_entry.grid(row=2, column=1, padx=10, pady=10)

        search_button = tk.Button(self.one_way_frame, text="Search", command=lambda: self.validate_and_search(
            get_username, self.from_entry.get(), self.to_entry.get(), self.depart_date_entry.get()), width=20,
                                  bg='gray')
        search_button.grid(row=3, columnspan=2, pady=10)

        # Button to navigate back to add_new_flight
        back_button = tk.Button(self.one_way_frame, text="Back to Add New Flight",
                                command=lambda: self.add_new_flight(get_username), width=20, bg='gray')
        back_button.grid(row=4, columnspan=2, pady=10)

    def validate_and_search(self, get_username, from_place, to_place, depart_date):
        try:
            # Validate and format the departure date
            depart_date = datetime.strptime(depart_date, "%d-%B-%Y").strftime("%d-%B-%Y")
            self.show_search_results(get_username, from_place, to_place, depart_date)
        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter a valid date in the format DD-Month-YYYY.")

    def show_search_results(self, get_username, from_place, to_place, depart_date):
        # Parse input depart_date to match the format in the file
        input_depart_date = datetime.strptime(depart_date, "%d-%B-%Y").strftime("%d-%B-%Y")

        # Read flight data from the file
        results = []
        with open("Available_Flight_Schedules.txt", "r") as file:
            for line in file:
                flight_data = line.strip().split(";")
                # Compare each flight's departure date with the parsed input depart_date
                if len(flight_data) >= 6 and flight_data[1] == from_place and flight_data[3] == to_place and \
                        flight_data[5] == input_depart_date:
                    result = {
                        "flight_id": flight_data[0],
                        "from": flight_data[1],
                        "to": flight_data[3],
                        "depart_date": flight_data[5],
                        "price": float(flight_data[7].replace("MYR", "").strip())
                    }
                    results.append(result)

        if not results:
            messagebox.showinfo("No Results", "No flights found for the selected criteria.")
            return

        self.clear_frames()
        self.search_results_frame = tk.Frame(self)
        self.search_results_frame.pack()

        summary_label = tk.Label(self.search_results_frame, text="Search Results", font=("Arial", 16), width=20,
                                 bg='gray')
        summary_label.pack(pady=10)

        self.result_vars_two_way = []
        for index, result in enumerate(results, start=1):
            var = tk.IntVar(value=0)
            self.result_vars_two_way.append(var)
            result_text = (
                f"No: {index}\n"
                f"Flight ID: {result['flight_id']}\n"
                f"From: {result['from']}\n"
                f"To: {result['to']}\n"
                f"Depart Date: {result['depart_date']}\n"
                f"Price: MYR {result['price']}\n"
            )
            result_label = tk.Label(self.search_results_frame, text=result_text, justify="left")
            result_label.pack(pady=5)
            select_button = tk.Radiobutton(self.search_results_frame, text="Select", variable=var, value=index)
            select_button.pack(pady=5)

        confirm_button = tk.Button(self.search_results_frame, text="Confirm Booking",
                                   command=lambda: self.confirm_booking(get_username, results), width=20, bg='gray')
        confirm_button.pack(pady=10)

        cancel_button = tk.Button(self.search_results_frame, text="Cancel", command=self.back_to_main_menu, width=20,
                                  bg='gray')
        cancel_button.pack(pady=10)

    def confirm_booking(self, get_username, results):
        selected_result = None
        for var, result in zip(self.result_vars, results):
            if var.get() == 1:
                selected_result = result
                break

        if selected_result is None:
            messagebox.showwarning("No Selection", "Please select a flight.")
            return

        def proceed_to_payment():
            # Get values entered by the user
            adult_count = int(adult_entry.get())
            child_count = int(child_entry.get())
            infant_count = int(infant_entry.get())
            cabin_baggage_size = int(cabin_baggage_entry.get())
            checked_baggage_size = int(checked_baggage_entry.get())

            # Calculate total passenger count and total price
            total_passenger_count = adult_count + child_count + infant_count
            total_price_in_ticket = selected_result['price'] * total_passenger_count

            # Save booking data to booking_data.txt
            with open("booking_data.txt", "a") as file:
                file.write(
                    f"{get_username};{selected_result['flight_id']};{adult_count};{child_count};{infant_count};"
                    f"{cabin_baggage_size};{checked_baggage_size};{total_passenger_count};{total_price_in_ticket}\n"
                )

            # Proceed to payment with the calculated details
            self.handle_payment_details(get_username, selected_result['flight_id'], selected_result['from'],
                                        selected_result['to'], selected_result['depart_date'], adult_count, child_count,
                                        infant_count, total_passenger_count, total_price_in_ticket)

        self.clear_frames()
        self.confirm_booking_frame = tk.Frame(self)
        self.confirm_booking_frame.pack()

        # Labels and entry fields for user input
        adult_label = tk.Label(self.confirm_booking_frame, text="Number of Adults:")
        adult_label.pack(pady=5)
        adult_entry = tk.Entry(self.confirm_booking_frame, width=25)
        adult_entry.pack(pady=5)

        child_label = tk.Label(self.confirm_booking_frame, text="Number of Children:")
        child_label.pack(pady=5)
        child_entry = tk.Entry(self.confirm_booking_frame, width=25)
        child_entry.pack(pady=5)

        infant_label = tk.Label(self.confirm_booking_frame, text="Number of Infants:")
        infant_label.pack(pady=5)
        infant_entry = tk.Entry(self.confirm_booking_frame, width=25)
        infant_entry.pack(pady=5)

        cabin_baggage_label = tk.Label(self.confirm_booking_frame, text="Cabin Baggage Size (KG):")
        cabin_baggage_label.pack(pady=5)
        cabin_baggage_entry = tk.Entry(self.confirm_booking_frame, width=25)
        cabin_baggage_entry.pack(pady=5)

        checked_baggage_label = tk.Label(self.confirm_booking_frame, text="Checked Baggage Size (KG):")
        checked_baggage_label.pack(pady=5)
        checked_baggage_entry = tk.Entry(self.confirm_booking_frame, width=25)
        checked_baggage_entry.pack(pady=5)

        confirm_button = tk.Button(self.confirm_booking_frame, text="Proceed to Payment",
                                   command=proceed_to_payment, width=20, bg='gray')
        confirm_button.pack(pady=10)

        cancel_button = tk.Button(self.confirm_booking_frame, text="Cancel", command=self.back_to_main_menu, width=20,
                                  bg='gray')
        cancel_button.pack(pady=10)

    def handle_payment_details(self, get_username, flight_id, from_place2, to_place2, full_depart_date2, adult_count,
                               child_count, infant_count, total_passenger_count, total_price_in_ticket):
        self.clear_frames()
        self.payment_details_frame = tk.Frame(self)
        self.payment_details_frame.pack()

        total_add_ons = 0  # Calculate additional costs
        final_price = total_price_in_ticket + total_add_ons
        rewards_points = final_price * 10

        payment_label = tk.Label(self.payment_details_frame, text="Payment Details", font=("Arial", 16), width=20,
                                 bg='gray')
        payment_label.pack(pady=10)

        full_name_label = tk.Label(self.payment_details_frame, text="Full Name:")
        full_name_label.pack(pady=5)
        full_name_entry = tk.Entry(self.payment_details_frame, width=25)
        full_name_entry.pack(pady=5)

        card_number_label = tk.Label(self.payment_details_frame, text="Card Number:")
        card_number_label.pack(pady=5)
        card_number_entry = tk.Entry(self.payment_details_frame, width=25)
        card_number_entry.pack(pady=5)

        cvv_label = tk.Label(self.payment_details_frame, text="CVV:")
        cvv_label.pack(pady=5)
        cvv_entry = tk.Entry(self.payment_details_frame, width=25)
        cvv_entry.pack(pady=5)

        exp_month_label = tk.Label(self.payment_details_frame, text="Expiry Month:")
        exp_month_label.pack(pady=5)
        exp_month_entry = tk.Entry(self.payment_details_frame, width=25)
        exp_month_entry.pack(pady=5)

        exp_year_label = tk.Label(self.payment_details_frame, text="Expiry Year:")
        exp_year_label.pack(pady=5)
        exp_year_entry = tk.Entry(self.payment_details_frame, width=25)
        exp_year_entry.pack(pady=5)

        process_payment_button = tk.Button(self.payment_details_frame, text="Process Payment",
                                           command=lambda: self.process_payment(
                                               get_username, flight_id, full_name_entry.get(), from_place2, to_place2,
                                               full_depart_date2,
                                               adult_count, child_count, infant_count, total_passenger_count,
                                               total_price_in_ticket, total_add_ons, final_price, rewards_points,
                                               card_number_entry.get(), cvv_entry.get(), exp_month_entry.get(),
                                               exp_year_entry.get()), width=20, bg='gray')
        process_payment_button.pack(pady=10)

    def process_payment(self, get_username, flight_id, full_name, from_place2, to_place2, full_depart_date2,
                        adult_count, child_count, infant_count, total_passenger_count, total_price_in_ticket,
                        total_add_ons, final_price, rewards_points, card_number, cvv, exp_month, exp_year):
        # Save the booking details to files as per your original code
        with open("booking_data.txt", "a") as db:
            db.write(
                get_username + ";" + flight_id + ";" + full_name + ";" + from_place2 + ";" +
                to_place2 + ";" + full_depart_date2 + ";" + "     -     " + ";" + str(adult_count) + ";" +
                str(child_count) + ";" + str(infant_count) + ";" + str(total_passenger_count) + ";" +
                str(total_price_in_ticket) + ";" + str(total_add_ons) + ";" + str(final_price) + ";" + str(
                    rewards_points) + ";" +
                card_number + ";" + cvv + ";" + exp_month + ";" + exp_year + "\n")

        with open("booking_data2.txt", "a") as db2:
            db2.write(
                get_username + ";" + flight_id + ";" + full_name + ";" + from_place2 + ";" +
                to_place2 + ";" + full_depart_date2 + ";" + "     -     " + ";" + "Check-IN OPEN" + "\n")

        messagebox.showinfo("Payment Successful",
                            f"Payment of MYR {final_price} was successful!\nRewards Points: {rewards_points}")

        # Redirect to main menu
        self.back_to_main_menu()

    def two_way(self, get_username):
        self.clear_frames()
        self.two_way_frame = tk.Frame(self)
        self.two_way_frame.pack()

        from_label = tk.Label(self.two_way_frame, text="Departure Location:")
        from_label.grid(row=0, column=0, padx=10, pady=10)
        self.from_entry = tk.Entry(self.two_way_frame)
        self.from_entry.grid(row=0, column=1, padx=10, pady=10)

        to_label = tk.Label(self.two_way_frame, text="Destination Location:")
        to_label.grid(row=1, column=0, padx=10, pady=10)
        self.to_entry = tk.Entry(self.two_way_frame)
        self.to_entry.grid(row=1, column=1, padx=10, pady=10)

        depart_date_label = tk.Label(self.two_way_frame, text="Departure Date (DD-Month-YYYY):")
        depart_date_label.grid(row=2, column=0, padx=10, pady=10)
        self.depart_date_entry = tk.Entry(self.two_way_frame)
        self.depart_date_entry.grid(row=2, column=1, padx=10, pady=10)

        return_date_label = tk.Label(self.two_way_frame, text="Return Date (DD-Month-YYYY):")
        return_date_label.grid(row=3, column=0, padx=10, pady=10)
        self.return_date_entry = tk.Entry(self.two_way_frame)
        self.return_date_entry.grid(row=3, column=1, padx=10, pady=10)

        search_button = tk.Button(self.two_way_frame, text="Search", command=lambda: self.validate_and_search_two_way(
            get_username, self.from_entry.get(), self.to_entry.get(), self.depart_date_entry.get(),
            self.return_date_entry.get()), width=20, bg='gray')
        search_button.grid(row=4, columnspan=2, pady=10)

        back_button = tk.Button(self.two_way_frame, text="Back to Add New Flight",
                                command=lambda: self.add_new_flight(get_username),
                                width=20, bg='gray')
        back_button.grid(row=5, columnspan=2, pady=10)

    def validate_and_search_two_way(self, get_username, from_place, to_place, depart_date, return_date):
        try:
            # Validate and format the departure date
            depart_date = datetime.strptime(depart_date, "%d-%B-%Y").strftime("%d-%B-%Y")
            return_date = datetime.strptime(return_date, "%d-%B-%Y").strftime("%d-%B-%Y")
            self.show_search_results_two_way(get_username, from_place, to_place, depart_date, return_date)
        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter a valid date in the format DD-Month-YYYY.")

    def show_search_results_two_way(self, get_username, from_place, to_place, depart_date, return_date):
        # Parse input departure and return dates to match the format in the file
        input_depart_date = datetime.strptime(depart_date, "%d-%B-%Y").strftime("%d-%B-%Y")
        input_return_date = datetime.strptime(return_date, "%d-%B-%Y").strftime("%d-%B-%Y")

        # Read flight data from the file
        results = []
        with open("Available_Flight_Schedules.txt", "r") as file:
            for line in file:
                flight_data = line.strip().split(";")
                # Compare each flight's departure and return dates with the parsed input dates
                if len(flight_data) >= 10 and flight_data[1] == from_place and flight_data[3] == to_place and \
                        flight_data[5] == input_depart_date and flight_data[6] == input_return_date:
                    result = {
                        "flight_id": flight_data[0],
                        "from": flight_data[1],
                        "to": flight_data[3],
                        "depart_date": flight_data[5],
                        "return_date": flight_data[6],
                        "price": float(flight_data[9].replace("MYR", "").strip())
                    }
                    results.append(result)

        if not results:
            messagebox.showinfo("No Results", "No flights found for the selected criteria.")
            return

        self.clear_frames()
        self.search_results_frame_two_way = tk.Frame(self)
        self.search_results_frame_two_way.pack()

        summary_label = tk.Label(self.search_results_frame_two_way, text="Search Results", font=("Arial", 16), width=20,
                                 bg='gray')
        summary_label.pack(pady=10)

        self.result_vars_two_way = []
        for index, result in enumerate(results, start=1):
            var = tk.IntVar(value=0)
            self.result_vars_two_way.append(var)
            result_text = (
                f"No: {index}\n"
                f"Flight ID: {result['flight_id']}\n"
                f"From: {result['from']}\n"
                f"To: {result['to']}\n"
                f"Depart Date: {result['depart_date']}\n"
                f"Return Date: {result['return_date']}\n"
                f"Price: MYR {result['price']}\n"
            )
            result_label = tk.Label(self.search_results_frame_two_way, text=result_text, justify="left")
            result_label.pack(pady=5)
            select_button = tk.Radiobutton(self.search_results_frame_two_way, text="Select", variable=var, value=index)
            select_button.pack(pady=5)

        confirm_button = tk.Button(self.search_results_frame_two_way, text="Confirm Booking",
                                   command=lambda: self.confirm_booking_two_way(get_username, results), width=20,
                                   bg='gray')
        confirm_button.pack(pady=10)

        cancel_button = tk.Button(self.search_results_frame_two_way, text="Cancel", command=self.back_to_main_menu,
                                  width=20,
                                  bg='gray')
        cancel_button.pack(pady=10)

    def confirm_booking_two_way(self, get_username, results):
        selected_result = None
        for var, result in zip(self.result_vars_two_way, results):
            if var.get() == 1:
                selected_result = result
                break

        if selected_result is None:
            messagebox.showwarning("No Selection", "Please select a flight.")
            return

        def proceed_to_payment_two_way():
            # Get values entered by the user
            adult_count = int(adult_entry.get())
            child_count = int(child_entry.get())
            infant_count = int(infant_entry.get())
            cabin_baggage_size = int(cabin_baggage_entry.get())
            checked_baggage_size = int(checked_baggage_entry.get())

            # Calculate total passenger count and total price
            total_passenger_count = adult_count + child_count + infant_count
            total_price_in_ticket = selected_result['price'] * total_passenger_count

            # Save booking data to booking_data.txt
            with open("booking_data.txt", "a") as file:
                file.write(
                    f"{get_username};{selected_result['flight_id']};{adult_count};{child_count};{infant_count};"
                    f"{cabin_baggage_size};{checked_baggage_size};{total_passenger_count};{total_price_in_ticket}\n"
                )

            # Proceed to payment with the calculated details
            self.handle_payment_details_two_way(get_username, selected_result['flight_id'], selected_result['from'],
                                                selected_result['to'], selected_result['depart_date'],
                                                selected_result['return_date'], adult_count, child_count, infant_count,
                                                total_passenger_count, total_price_in_ticket)

        self.clear_frames()
        self.confirm_booking_two_way_frame = tk.Frame(self)
        self.confirm_booking_two_way_frame.pack()

        # Labels and entry fields for user input
        adult_label = tk.Label(self.confirm_booking_two_way_frame, text="Number of Adults:")
        adult_label.pack(pady=5)
        adult_entry = tk.Entry(self.confirm_booking_two_way_frame, width=25)
        adult_entry.pack(pady=5)

        child_label = tk.Label(self.confirm_booking_two_way_frame, text="Number of Children:")
        child_label.pack(pady=5)
        child_entry = tk.Entry(self.confirm_booking_two_way_frame, width=25)
        child_entry.pack(pady=5)

        infant_label = tk.Label(self.confirm_booking_two_way_frame, text="Number of Infants:")
        infant_label.pack(pady=5)
        infant_entry = tk.Entry(self.confirm_booking_two_way_frame, width=25)
        infant_entry.pack(pady=5)

        cabin_baggage_label = tk.Label(self.confirm_booking_two_way_frame, text="Cabin Baggage Size (KG):")
        cabin_baggage_label.pack(pady=5)
        cabin_baggage_entry = tk.Entry(self.confirm_booking_two_way_frame, width=25)
        cabin_baggage_entry.pack(pady=5)

        checked_baggage_label = tk.Label(self.confirm_booking_two_way_frame, text="Checked Baggage Size (KG):")
        checked_baggage_label.pack(pady=5)
        checked_baggage_entry = tk.Entry(self.confirm_booking_two_way_frame, width=25)
        checked_baggage_entry.pack(pady=5)

        confirm_button = tk.Button(self.confirm_booking_two_way_frame, text="Proceed to Payment",
                                   command=proceed_to_payment_two_way, width=20, bg='gray')
        confirm_button.pack(pady=10)

        cancel_button = tk.Button(self.confirm_booking_two_way_frame, text="Cancel", command=self.back_to_main_menu,
                                  width=20, bg='gray')
        cancel_button.pack(pady=10)

    def handle_payment_details_two_way(self, get_username, flight_id, from_place2, to_place2, full_depart_date2,
                                       full_return_date2, adult_count, child_count, infant_count, total_passenger_count,
                                       total_price_in_ticket):
        self.clear_frames()
        self.payment_details_frame = tk.Frame(self)
        self.payment_details_frame.pack()

        total_add_ons = 0  # Calculate additional costs
        final_price = total_price_in_ticket + total_add_ons
        rewards_points = final_price * 10

        payment_label = tk.Label(self.payment_details_frame, text="Payment Details", font=("Arial", 16), width=20,
                                 bg='gray')
        payment_label.pack(pady=10)

        full_name_label = tk.Label(self.payment_details_frame, text="Full Name:")
        full_name_label.pack(pady=5)
        full_name_entry = tk.Entry(self.payment_details_frame, width=25)
        full_name_entry.pack(pady=5)

        card_number_label = tk.Label(self.payment_details_frame, text="Card Number:")
        card_number_label.pack(pady=5)
        card_number_entry = tk.Entry(self.payment_details_frame, width=25)
        card_number_entry.pack(pady=5)

        cvv_label = tk.Label(self.payment_details_frame, text="CVV:")
        cvv_label.pack(pady=5)
        cvv_entry = tk.Entry(self.payment_details_frame, width=25)
        cvv_entry.pack(pady=5)

        exp_month_label = tk.Label(self.payment_details_frame, text="Expiry Month:")
        exp_month_label.pack(pady=5)
        exp_month_entry = tk.Entry(self.payment_details_frame, width=25)
        exp_month_entry.pack(pady=5)

        exp_year_label = tk.Label(self.payment_details_frame, text="Expiry Year:")
        exp_year_label.pack(pady=5)
        exp_year_entry = tk.Entry(self.payment_details_frame, width=25)
        exp_year_entry.pack(pady=5)

        process_payment_button = tk.Button(self.payment_details_frame, text="Process Payment",
                                           command=lambda: self.process_payment_two_way(
                                               get_username, flight_id, full_name_entry.get(), from_place2, to_place2,
                                               full_depart_date2, full_return_date2,
                                               adult_count, child_count, infant_count, total_passenger_count,
                                               total_price_in_ticket, total_add_ons, final_price, rewards_points,
                                               card_number_entry.get(), cvv_entry.get(), exp_month_entry.get(),
                                               exp_year_entry.get()), width=20, bg='gray')
        process_payment_button.pack(pady=10)

    def process_payment_two_way(self, get_username, flight_id, full_name, from_place2, to_place2, full_depart_date2,
                                full_return_date2, adult_count, child_count, infant_count, total_passenger_count,
                                total_price_in_ticket, total_add_ons, final_price, rewards_points, card_number, cvv,
                                exp_month, exp_year, results):
        # Save the booking details to files as per your original code
        with open("booking_data.txt", "a") as db:
            db.write(
                f"{get_username};{flight_id};{full_name};{from_place2};{to_place2};{full_depart_date2};"
                f"{full_return_date2};{adult_count};{child_count};{infant_count};{total_passenger_count};"
                f"{total_price_in_ticket};{total_add_ons};{final_price};{rewards_points};{card_number};"
                f"{cvv};{exp_month};{exp_year}\n")

        with open("booking_data2.txt", "a") as db2:
            db2.write(
                f"{get_username};{flight_id};{full_name};{from_place2};{to_place2};{full_depart_date2};"
                f"{full_return_date2};Check-IN OPEN\n")

        # Function to handle going back to the previous screen
        def go_back():
            self.confirm_booking_two_way(get_username, results)

        # Show the payment successful message box
        messagebox.showinfo("Payment Successful",
                            f"Payment of MYR {final_price} was successful!\nRewards Points: {rewards_points}")

        # Create a back button to return to the previous screen
        back_button = tk.Button(self.payment_details_frame, text="Back", command=go_back, width=20, bg='gray')
        back_button.pack(pady=10)

        # Redirect to main menu
        self.back_to_main_menu()

    def clear_frames(self):
        for widget in self.winfo_children():
            widget.pack_forget()


    def show_points(self, username):
        # Read the booking data from the file and display it in a new window
        with open("booking_data.txt", "r") as file:
            lines = file.readlines()

        # Filter the lines that contain the username
        filtered_lines = [line for line in lines if username in line]

        if not filtered_lines:
            messagebox.showinfo("No Points", "No points found for the user.")
            return

        # Create a new window to display the points
        points_window = tk.Toplevel(self)
        points_window.title("My Points")
        points_window.geometry("800x600")

        # Create a Treeview widget
        tree = ttk.Treeview(points_window)

        # Define columns
        tree["columns"] = ("1", "2", "3", "4", "5", "6", "7")

        # Format columns
        tree.column("#0", width=50, minwidth=50)
        tree.column("1", anchor="w", width=100)
        tree.column("2", anchor="w", width=100)
        tree.column("3", anchor="w", width=100)
        tree.column("4", anchor="w", width=100)
        tree.column("5", anchor="w", width=100)
        tree.column("6", anchor="w", width=100)
        tree.column("7", anchor="w", width=100)

        # Add headings
        tree.heading("#0", text="No.")
        tree.heading("1", text="Flight ID")
        tree.heading("2", text="From")
        tree.heading("3", text="To")
        tree.heading("4", text="Depart Date & Time")
        tree.heading("5", text="Return Date & Time")
        tree.heading("6", text="Rewards Points")

        # Add data to the treeview
        for idx, line in enumerate(filtered_lines, start=1):
            data = line.strip().split(";")
            tree.insert("", "end", text=idx, values=(data[1], data[3], data[4], data[5], data[6], data[24]))

        # Pack the treeview
        tree.pack(expand=True, fill="both")

        # Add a back button
        back_button = tk.Button(points_window, text="Back to Menu", command=points_window.destroy, bg='gray')
        back_button.pack(pady=10)

    def login_admin(self):
        self.login_frame.pack_forget()
        self.admin_login_frame = tk.Frame(self)
        self.admin_login_frame.pack()

        self.label = tk.Label(self.admin_login_frame, text="Admin Login", font=("Arial", 16))
        self.label.pack(pady=20)

        self.username_label = tk.Label(self.admin_login_frame, text="Username:", width=20, anchor='w')
        self.username_label.pack()
        self.username_entry = tk.Entry(self.admin_login_frame, width=25)
        self.username_entry.pack()

        self.password_label = tk.Label(self.admin_login_frame, text="Password:", width=20, anchor='w')
        self.password_label.pack()
        self.password_entry = tk.Entry(self.admin_login_frame, show='*', width=25)
        self.password_entry.pack()

        self.login_button = tk.Button(self.admin_login_frame, text="Login",
                                      command=self.authenticate_admin, width=20, bg='gray')
        self.login_button.pack(pady=10)

        self.back_button = tk.Button(self.admin_login_frame, text="Back to Login Menu",
                                     command=self.back_to_login_menu, width=20, bg='gray')
        self.back_button.pack(pady=10)

    def authenticate_admin(self):
        username_admin = "admin"
        password_admin = "admin"
        user_name = self.username_entry.get()
        pass_word = self.password_entry.get()

        if user_name == username_admin and pass_word == password_admin:
            messagebox.showinfo("Success", f"Successfully logged in! Good day {user_name}")
            self.admin_menu()
        else:
            messagebox.showerror("Error", "Username or password was incorrect. Try again!")
            self.back_to_login_menu()

    def admin_menu(self):
        self.clear_frames()
        self.admin_menu_frame = tk.Frame(self)
        self.admin_menu_frame.pack()

        self.admin_menu_label = tk.Label(self.admin_menu_frame, text="AIRLINE ADMIN SYSTEM MENU", font=("Arial", 16))
        self.admin_menu_label.pack(pady=20)

        self.show_airline_button = tk.Button(self.admin_menu_frame, text="Show Airline Schedules",
                                             command=self.show_airline_ui)
        self.show_airline_button.pack()

        self.add_flight_button = tk.Button(self.admin_menu_frame, text="Add Flight Schedules", command=self.add_flight_ui)
        self.add_flight_button.pack()

        self.modify_flight_button = tk.Button(self.admin_menu_frame, text="Modify Flight Schedules",
                                              command=self.modify_flight_schedules_menu_ui)
        self.modify_flight_button.pack()

        self.display_records_button = tk.Button(self.admin_menu_frame, text="Display All Records",
                                                command=self.display_records_menu)
        self.display_records_button.pack()

        self.logout_button = tk.Button(self.admin_menu_frame, text="Log Out", command=self.logout)
        self.logout_button.pack()


    def show_airline_ui(self):
        self.clear_frames()
        self.show_airline_frame = tk.Frame(self)
        self.show_airline_frame.pack()

        # Interface Header
        header_label = tk.Label(self.show_airline_frame, text="Air Malaysia Group (AMG) All Airlines",
                                font=("Arial", 16))
        header_label.grid(row=0, columnspan=6, pady=10)

        # Column headers
        headers = ["No.", "Flight Number", "From", "To", "Depart Date", "Time", "Return Date", "Time", "Price",
                   "Flight Duration (hours)"]
        for col, header in enumerate(headers):
            header_label = tk.Label(self.show_airline_frame, text=header)
            header_label.grid(row=1, column=col, padx=5, pady=5)

        # Read data from file and display
        with open('Available_Flight_Schedules.txt', 'r') as file:
            row = 2
            for index, line in enumerate(file, start=1):
                data = line.strip().split(";")
                for col, value in enumerate(data, start=1):
                    label = tk.Label(self.show_airline_frame, text=value)
                    label.grid(row=row, column=col, padx=5, pady=5)
                row += 1

        # Add back button to return to admin menu
        back_button = tk.Button(self.show_airline_frame, text="Back to Admin Menu", command=self.admin_menu)
        back_button.grid(row=row, columnspan=6, pady=10)

    def add_flight_ui(self):
        self.clear_frames()
        self.add_flight_frame = tk.Frame(self)
        self.add_flight_frame.pack()

        header_label = tk.Label(self.add_flight_frame, text="Add New Flight", font=("Arial", 16))
        header_label.pack(pady=20)

        # Flight ID
        flight_id_label = tk.Label(self.add_flight_frame, text="Flight ID (AMG):")
        flight_id_label.pack()
        flight_id_entry = tk.Entry(self.add_flight_frame)
        flight_id_entry.pack()

        # From Place
        from_place_label = tk.Label(self.add_flight_frame, text="From:")
        from_place_label.pack()
        from_place_entry = tk.Entry(self.add_flight_frame)
        from_place_entry.pack()

        # To Place
        to_place_label = tk.Label(self.add_flight_frame, text="To:")
        to_place_label.pack()
        to_place_entry = tk.Entry(self.add_flight_frame)
        to_place_entry.pack()

        # Depart Date
        depart_date_label = tk.Label(self.add_flight_frame, text="Depart Date:")
        depart_date_label.pack()
        depart_date_entry = tk.Entry(self.add_flight_frame)
        depart_date_entry.pack()

        # Return Date
        return_date_label = tk.Label(self.add_flight_frame, text="Return Date:")
        return_date_label.pack()
        return_date_entry = tk.Entry(self.add_flight_frame)
        return_date_entry.pack()

        # Depart Time
        depart_time_label = tk.Label(self.add_flight_frame, text="Depart Time:")
        depart_time_label.pack()
        depart_time_entry = tk.Entry(self.add_flight_frame)
        depart_time_entry.pack()

        # Return Time
        return_time_label = tk.Label(self.add_flight_frame, text="Return Time:")
        return_time_label.pack()
        return_time_entry = tk.Entry(self.add_flight_frame)
        return_time_entry.pack()

        # Price
        price_label = tk.Label(self.add_flight_frame, text="Price (MYR):")
        price_label.pack()
        price_entry = tk.Entry(self.add_flight_frame)
        price_entry.pack()

        # Flight Duration
        duration_label = tk.Label(self.add_flight_frame, text="Flight Duration (hours):")
        duration_label.pack()
        duration_entry = tk.Entry(self.add_flight_frame)
        duration_entry.pack()

        # Add Flight Button
        add_button = tk.Button(self.add_flight_frame, text="Add Flight",
                               command=lambda: self.process_flight_data(flight_id_entry.get(),
                                                                        from_place_entry.get(),
                                                                        to_place_entry.get(),
                                                                        depart_date_entry.get(),
                                                                        return_date_entry.get(),
                                                                        depart_time_entry.get(),
                                                                        return_time_entry.get(),
                                                                        price_entry.get(),
                                                                        duration_entry.get()))
        add_button.pack(pady=10)

        # Back Button
        back_button = tk.Button(self.add_flight_frame, text="Back to Admin Menu", command=self.admin_menu)
        back_button.pack(pady=10)

    def process_flight_data(self, flight_id, from_place, to_place, depart_date, return_date,
                            depart_time, return_time, price, duration):
        # Open the database file
        with open("Available_Flight_Schedules.txt", "r") as file:
            # Read each line to check for existing flight data
            for line in file:
                data = line.strip().split(";")
                # Check if the flight data matches the provided details
                if (data[0] == flight_id and data[1] == from_place and data[2] == to_place
                        and data[3] == depart_date and data[4] == return_date
                        and data[5] == depart_time and data[6] == return_time
                        and data[7] == "MYR" + price and data[8] == duration):
                    # Display success message if the flight already exists
                    messagebox.showinfo("Flight Already Exists", "The flight already exists in the database.")
                    return
        # If no match is found, add the flight data to the database
        with open("Available_Flight_Schedules.txt", "a") as db:
            db.write(
                f"{flight_id};{from_place};{to_place};{depart_date};{return_date};{depart_time};{return_time};MYR{price};{duration}\n")
        # Display success message after adding the flight
        messagebox.showinfo("Flight Added", "The flight has been successfully added to the database.")

    def modify_flight_schedules_menu(self):
        self.admin_menu_frame.pack_forget()  # Hide the admin menu frame
        self.modify_flight_frame = tk.Frame(self)  # Create a new frame for the modify flight menu
        self.modify_flight_frame.pack()

        # Interface Header
        header_label = tk.Label(self.modify_flight_frame, text="Modify Flight Schedules", font=("Arial", 16))
        header_label.pack(pady=20)

        # Menu options
        option_label = tk.Label(self.modify_flight_frame, text="Please select an option:", font=("Arial", 12))
        option_label.pack()

        # Buttons for different options
        change_button = tk.Button(self.modify_flight_frame, text="Change Flight Schedules",
                                  command=self.change_flight_schedules)
        change_button.pack()

        cancel_button = tk.Button(self.modify_flight_frame, text="Cancel Flight Schedules",
                                  command=self.cancel_flight_schedules)
        cancel_button.pack()

        back_button = tk.Button(self.modify_flight_frame, text="Back to Admin Menu", command=self.admin_menu)
        back_button.pack()

    def change_flight_schedules_ui(self):
        self.clear_frames()  # Hide the admin menu frame
        self.change_flight_frame = tk.Frame(self)  # Create a new frame for changing flight schedules
        self.change_flight_frame.pack()

        # Interface Header
        header_label = tk.Label(self.change_flight_frame, text="Change Flight Schedules", font=("Arial", 16))
        header_label.pack(pady=20)

        # Instruction for selecting flight
        instruction_label = tk.Label(self.change_flight_frame, text="Please select the flight you wish to modify:", font=("Arial", 12))
        instruction_label.pack()

        # Entry for selecting flight
        self.flight_entry = tk.Entry(self.change_flight_frame)
        self.flight_entry.pack()

        # Button to confirm flight selection
        confirm_button = tk.Button(self.change_flight_frame, text="Confirm", command=self.confirm_flight_change)
        confirm_button.pack(pady=10)

        # Back button to return to admin menu
        back_button = tk.Button(self.change_flight_frame, text="Back to Admin Menu", command=self.admin_menu)
        back_button.pack(pady=10)

    def confirm_flight_change(self):
        flight_number = self.flight_entry.get()
        if not flight_number:
            messagebox.showwarning("Input Error", "Please enter a flight number.")
            return

        self.clear_frames()
        self.modify_flight_frame = tk.Frame(self)
        self.modify_flight_frame.pack()

        # Flight ID
        flight_id_label = tk.Label(self.modify_flight_frame, text="Flight ID (AMG):")
        flight_id_label.pack()
        flight_id_entry = tk.Entry(self.modify_flight_frame)
        flight_id_entry.pack()

        # From Place
        from_place_label = tk.Label(self.modify_flight_frame, text="From:")
        from_place_label.pack()
        from_place_entry = tk.Entry(self.modify_flight_frame)
        from_place_entry.pack()

        # To Place
        to_place_label = tk.Label(self.modify_flight_frame, text="To:")
        to_place_label.pack()
        to_place_entry = tk.Entry(self.modify_flight_frame)
        to_place_entry.pack()

        # Depart Date
        depart_date_label = tk.Label(self.modify_flight_frame, text="Depart Date:")
        depart_date_label.pack()
        depart_date_entry = tk.Entry(self.modify_flight_frame)
        depart_date_entry.pack()

        # Return Date
        return_date_label = tk.Label(self.modify_flight_frame, text="Return Date:")
        return_date_label.pack()
        return_date_entry = tk.Entry(self.modify_flight_frame)
        return_date_entry.pack()

        # Depart Time
        depart_time_label = tk.Label(self.modify_flight_frame, text="Depart Time:")
        depart_time_label.pack()
        depart_time_entry = tk.Entry(self.modify_flight_frame)
        depart_time_entry.pack()

        # Return Time
        return_time_label = tk.Label(self.modify_flight_frame, text="Return Time:")
        return_time_label.pack()
        return_time_entry = tk.Entry(self.modify_flight_frame)
        return_time_entry.pack()

        # Price
        price_label = tk.Label(self.modify_flight_frame, text="Price (MYR):")
        price_label.pack()
        price_entry = tk.Entry(self.modify_flight_frame)
        price_entry.pack()

        # Flight Duration
        duration_label = tk.Label(self.modify_flight_frame, text="Flight Duration (hours):")
        duration_label.pack()
        duration_entry = tk.Entry(self.modify_flight_frame)
        duration_entry.pack()

        # Update Flight Button
        update_button = tk.Button(self.modify_flight_frame, text="Update Flight",
                                  command=lambda: self.update_flight_data(flight_number, flight_id_entry.get(),
                                                                          from_place_entry.get(), to_place_entry.get(),
                                                                          depart_date_entry.get(), return_date_entry.get(),
                                                                          depart_time_entry.get(), return_time_entry.get(),
                                                                          price_entry.get(), duration_entry.get()))
        update_button.pack(pady=10)

        # Back Button
        back_button = tk.Button(self.modify_flight_frame, text="Back to Admin Menu", command=self.admin_menu)
        back_button.pack(pady=10)

    def update_flight_data(self, flight_number, flight_id, from_place, to_place, depart_date, return_date,
                           depart_time, return_time, price, duration):
        # Read the existing file
        with open("Available_Flight_Schedules.txt", "r") as file:
            lines = file.readlines()

        # Check if the flight number exists and update the data
        with open("Available_Flight_Schedules.txt", "w") as file:
            for line in lines:
                data = line.strip().split(";")
                if data[0] == flight_number:
                    line = f"{flight_id};{from_place};{to_place};{depart_date};{return_date};{depart_time};{return_time};MYR{price};{duration}\n"
                file.write(line)

        # Show the message box and redirect to the admin menu
        messagebox.showinfo("Flight Updated", "The flight has been successfully updated.")
        self.admin_menu()

    def cancel_flight_schedules_ui(self):
        self.clear_frames()
        self.cancel_flight_frame = tk.Frame(self)
        self.cancel_flight_frame.pack()

        # Interface Header
        header_label = tk.Label(self.cancel_flight_frame, text="Cancel Flight Schedules", font=("Arial", 16))
        header_label.pack(pady=20)

        # Instruction for selecting flight
        instruction_label = tk.Label(self.cancel_flight_frame, text="Please select the flight you wish to cancel:", font=("Arial", 12))
        instruction_label.pack()

        # List of flights
        flights = self.get_flight_list()
        self.flight_listbox = tk.Listbox(self.cancel_flight_frame)
        for index, flight in enumerate(flights):
            self.flight_listbox.insert(tk.END, f"{index + 1}. {flight}")
        self.flight_listbox.pack(pady=10)

        # Confirm button to cancel flight
        confirm_button = tk.Button(self.cancel_flight_frame, text="Cancel Flight", command=self.confirm_cancel_flight)
        confirm_button.pack(pady=10)

        # Back button to return to admin menu
        back_button = tk.Button(self.cancel_flight_frame, text="Back to Admin Menu", command=self.admin_menu)
        back_button.pack(pady=10)

    def get_flight_list(self):
        flights = []
        with open("Available_Flight_Schedules.txt", "r") as file:
            for line in file:
                flights.append(line.strip())
        return flights

    def confirm_cancel_flight(self):
        selected_index = self.flight_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Selection Error", "Please select a flight to cancel.")
            return

        flight_index = selected_index[0]

        # Read the existing file
        with open("Available_Flight_Schedules.txt", "r") as file:
            lines = file.readlines()

        # Delete the selected flight
        del lines[flight_index]

        # Write back the updated list to the file
        with open("Available_Flight_Schedules.txt", "w") as file:
            file.writelines(lines)

        # Show success message
        messagebox.showinfo("Flight Canceled", "The flight has been successfully canceled.")

        # Redirect to admin menu
        self.admin_menu()

    def display_records_menu(self):
        self.clear_frames()
        self.display_records_frame = tk.Frame(self)
        self.display_records_frame.pack()

        self.display_records_label = tk.Label(self.display_records_frame, text="Display Records Menu", font=("Arial", 16))
        self.display_records_label.pack(pady=20)

        self.by_flight_number_button = tk.Button(self.display_records_frame, text="Flight schedules by flight number",
                                                 command=self.by_flight_number_ui)
        self.by_flight_number_button.pack(pady=5)

        self.booked_by_customer_button = tk.Button(self.display_records_frame, text="Flight booked by customer",
                                                   command=self.booked_by_customer_ui)
        self.booked_by_customer_button.pack(pady=5)

        self.summary_total_tickets_sold_button = tk.Button(self.display_records_frame, text="Summary of Total tickets sold",
                                                           command=self.summary_total_ticket_sold_ui)
        self.summary_total_tickets_sold_button.pack(pady=5)

        self.back_to_main_menu_button = tk.Button(self.display_records_frame, text="Back to Admin Menu",
                                                  command=self.admin_menu)
        self.back_to_main_menu_button.pack(pady=5)

    def by_flight_number_ui(self):
        self.clear_frames()
        self.by_flight_number_frame = tk.Frame(self)
        self.by_flight_number_frame.pack()

        header_label = tk.Label(self.by_flight_number_frame, text="Search Flight by Flight Number", font=("Arial", 16))
        header_label.pack(pady=20)

        flight_id_label = tk.Label(self.by_flight_number_frame, text="Enter Flight ID (without 'AMG'):")
        flight_id_label.pack(pady=5)
        self.flight_id_entry = tk.Entry(self.by_flight_number_frame)
        self.flight_id_entry.pack(pady=5)

        search_button = tk.Button(self.by_flight_number_frame, text="Search", command=self.search_flight_by_number)
        search_button.pack(pady=10)

        self.results_frame = tk.Frame(self.by_flight_number_frame)
        self.results_frame.pack(pady=10)

        back_button = tk.Button(self.by_flight_number_frame, text="Back to Records Menu", command=self.display_records_menu)
        back_button.pack(pady=10)

    def search_flight_by_number(self):
        flight_id = self.flight_id_entry.get()
        final_user_prompt_flight_id = "AMG" + flight_id

        for widget in self.results_frame.winfo_children():
            widget.destroy()

        header = ["No.", "Flight ID", "From", "To", "Depart Date & Time", "Return Date & Time", "Price", "Flight Duration (hrs)"]
        for col, text in enumerate(header):
            label = tk.Label(self.results_frame, text=text, font=("Arial", 10, "bold"))
            label.grid(row=0, column=col, padx=5, pady=5)

        with open("Available_Flight_Schedules.txt", "r") as file:
            total_row = 0
            for line in file:
                if final_user_prompt_flight_id in line:
                    total_row += 1
                    temp2 = line.strip().split(";")
                    price_convert = int(temp2[9].strip("MYR"))
                    data = [
                        total_row, temp2[0], f"{temp2[1]}, {temp2[2]}", f"{temp2[3]}, {temp2[4]}",
                        f"{temp2[5]}|{temp2[7]}", f"{temp2[6]}|{temp2[8]}", "MYR" + str(price_convert), temp2[10]
                    ]
                    for col, value in enumerate(data):
                        label = tk.Label(self.results_frame, text=value, font=("Arial", 10))
                        label.grid(row=total_row, column=col, padx=5, pady=5)

        if total_row == 0:
            label = tk.Label(self.results_frame, text="No results found.", font=("Arial", 10))
            label.grid(row=1, columnspan=len(header), padx=5, pady=5)

    def booked_by_customer_ui(self):
        self.clear_frames()
        self.booked_by_customer_frame = tk.Frame(self)
        self.booked_by_customer_frame.pack()

        header_label = tk.Label(self.booked_by_customer_frame, text="Flights Booked by Customer", font=("Arial", 16))
        header_label.pack(pady=20)

        header = ["No.", "Username", "Full Name", "Flight ID", "From", "To", "Depart Date & Time", "Return Date & Time", "Adult", "Child", "Infant"]
        for col, text in enumerate(header):
            label = tk.Label(self.booked_by_customer_frame, text=text, font=("Arial", 10, "bold"))
            label.grid(row=0, column=col, padx=5, pady=5)

        with open("booking_data.txt", "r") as file:
            total_row = 0
            for line in file:
                total_row += 1
                temp2 = line.strip().split(";")
                data = [
                    total_row, temp2[0], temp2[2], temp2[1], f"{temp2[3]}, {temp2[4]}", f"{temp2[5]}, {temp2[6]}",
                    temp2[7], temp2[8], temp2[9], temp2[10], temp2[11]
                ]
                for col, value in enumerate(data):
                    label = tk.Label(self.booked_by_customer_frame, text=value, font=("Arial", 10))
                    label.grid(row=total_row, column=col, padx=5, pady=5)

        back_button = tk.Button(self.booked_by_customer_frame, text="Back to Records Menu", command=self.display_records_menu)
        back_button.grid(row=total_row + 1, columnspan=len(header), pady=10)

    def summary_total_ticket_sold_ui(self):
        self.clear_frames()
        self.summary_total_ticket_sold_frame = tk.Frame(self)
        self.summary_total_ticket_sold_frame.pack()

        header_label = tk.Label(self.summary_total_ticket_sold_frame, text="Summary of Total Tickets Sold", font=("Arial", 16))
        header_label.pack(pady=20)

        with open("booking_data.txt", "r") as file:
            total_adult_count = 0
            total_child_count = 0
            total_infant_count = 0
            total_total_price_in_ticket = 0
            total_total_seat_class_price = 0
            total_total_add_baggage_price = 0
            total_total_seating_price = 0
            total_total_insurance = 0
            total_income = 0
            total_rewards_points = 0

            for line in file:
                temp = line.replace("\n", "").strip("")
                temp2 = list(temp.split(";"))
                adult_count = int(temp2[9])
                total_adult_count += adult_count
                child_count = int(temp2[10])
                total_child_count += child_count
                infant_count = int(temp2[11])
                total_infant_count += infant_count
                total_price_in_ticket = float(temp2[22])
                total_total_price_in_ticket += total_price_in_ticket
                total_seat_class_price = float(temp2[14])
                total_total_seat_class_price += total_seat_class_price
                total_add_baggage_price = float(temp2[16])
                total_total_add_baggage_price += total_add_baggage_price
                total_seating_price = float(temp2[18])
                total_total_seating_price += total_seating_price
                total_insurance = float(temp2[20])
                total_total_insurance += total_insurance
                total_income = float(
                    total_total_price_in_ticket + total_total_seat_class_price + total_total_add_baggage_price + total_total_seating_price + total_total_insurance)
                rewards_points = float(temp2[24])
                total_rewards_points += rewards_points

        summary_text = (
            f'Total Passengers:\n'
            f'  Adult: {total_adult_count}      Child: {total_child_count}      Infant: {total_infant_count}\n\n'
            f'The total prices earned in tickets: {total_total_price_in_ticket}\n\n'
            f'The total seat class incomes: MYR {total_total_seat_class_price}\n'
            f'The total add baggage incomes: MYR {total_total_add_baggage_price}\n'
            f'The total seating incomes: MYR {total_total_seating_price}\n'
            f'The total insurance incomes: MYR {total_total_insurance}\n\n'
            f'UP-to-date Profit: MYR {total_income}\n'
            f'UP-to-date total rewards points given: {total_rewards_points} Points\n'
        )

        summary_label = tk.Label(self.summary_total_ticket_sold_frame, text=summary_text, justify="left")
        summary_label.pack(pady=10)

        back_button = tk.Button(self.summary_total_ticket_sold_frame, text="Back to Records Menu", command=self.display_records_menu)
        back_button.pack(pady=10)

    def logout(self):
        self.clear_frames()
        self.main_menu_frame.pack()

    def back_to_main_menu(self):
        if self.search_airline_frame is not None:
            self.search_airline_frame.pack_forget()
        if self.signup_frame is not None:
            self.signup_frame.pack_forget()
        if self.login_frame is not None:
            self.login_frame.pack_forget()
        if self.customer_login_frame is not None:
            self.customer_login_frame.pack_forget()
        if self.regis_cus_frame is not None:
            self.regis_cus_frame.pack_forget()
        if self.admin_login_frame is not None:
            self.admin_login_frame.pack_forget()
        if self.show_airline_frame is not None:
            self.show_airline_frame.pack_forget()
        if self.search_airline_frame is not None:
            self.search_airline_frame.pack_forget()
        if self.available_destinations_frame is not None:
            self.available_destinations_frame.pack_forget()
        if self.my_account_frame is not None:
            self.my_account_frame.pack_forget()
        if self.booking_frame is not None:
            self.booking_frame.pack_forget()
        if self.add_flight_frame is not None:
            self.add_flight_frame.pack_forget()
        if self.confirm_booking_frame is not None:
            self.confirm_booking_frame.pack_forget()
        if self.confirm_booking_two_way_frame is not None:
            self.confirm_booking_two_way_frame.pack_forget()
        if self.points_frame is not None:
            self.points_frame.pack_forget()
        self.main_menu_frame.pack()

        self.geometry("600x400")

    def back_to_login_menu(self):
        if self.customer_login_frame is not None:
            self.customer_login_frame.pack_forget()
        if self.admin_login_frame is not None:
            self.admin_login_frame.pack_forget()
        self.login_frame.pack()

if __name__ == "__main__":
    app = AirlineReservationSystem()
    app.mainloop()
