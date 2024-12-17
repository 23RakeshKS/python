Abstract:
The Hotel Management System is a Python-based application designed to manage hotel orders and user authentication. Using a graphical user interface (GUI) built with Tkinter, it allows users to sign up, log in, and place orders for South Indian food items. The system handles user data storage in a CSV file and displays an attractive menu with prices. Users can add items to their order, view the total price, and proceed with checkout. The program provides an easy-to-use interface for both guests and administrators to manage orders effectively.
Overview:
This Hotel Management System is designed to simulate a restaurant ordering system, with the following main functionalities:
•	User Authentication: Users can sign up with a username and password and log in using their credentials.
•	Menu Management: The application offers a South Indian food menu, displaying item names along with their prices.
•	Order System: Users can add items to their order, and the total price is dynamically updated based on selections.
•	Checkout: After placing the order, the user can proceed to checkout and view the total amount to pay.
•	Data Storage: User credentials are stored in a CSV file for persistence across sessions.
Features:
1.	User Authentication:
o	Sign Up: New users can create an account with a unique username and password.
o	Login: Existing users can log in to the system using their credentials (username and password).
o	CSV Data Storage: All user data (username and password) is stored in a CSV file for long-term storage.
2.	Food Menu:
o	South Indian Food Items: The application displays a list of South Indian food items such as Idli, Dosa, Sambar Vada, Pongal, and Uttapam, along with their respective prices.
o	Menu Buttons: Each food item has a button associated with it, allowing users to add items to their order.
3.	Order Management:
o	Dynamic Total Calculation: As users select items from the menu, the total cost is calculated and displayed dynamically.
o	Checkout: Once the user completes their order, they can view the order summary and proceed to checkout, which displays the total price.
4.	User-Friendly Interface:
o	Tkinter GUI: The application uses Tkinter to create an interactive and visually appealing user interface. Colors like lightgreen, lightyellow, and lightblue are used to differentiate between screens and enhance the visual experience.
o	Smooth Navigation: The application offers smooth transitions between screens for login, sign-up, and order placement.
5.	Error Handling:
o	Invalid Username or Password: If the user enters incorrect credentials, the system shows an error message.
o	Username Already Exists: During sign-up, if the user attempts to register with a username that already exists, the system will notify them.
6.	Checkout Summary:
o	Order Summary: After completing the order, the total price is displayed in a popup message, ensuring that the user knows the amount to be paid.
________________________________________
This system provides a simple but functional restaurant order management solution, with the addition of user authentication, a menu system, and the ability to manage orders in a user-friendly environment. It is ideal for learning purposes and can be further expanded with more features, such as an admin interface for managing items and viewing order history.

# python
