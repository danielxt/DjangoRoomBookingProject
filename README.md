# ABC Room booking system

Allows staff to book rooms for a given time and date and view room availability. Provides admins with additional privileges such as managing rooms, bookings and users.

## Startup

1. Set up virtual environment
   `python3 -m venv env`
2. Install requirements
   `pip install -r requirements.txt`
3. Change directory into `roomBooking`
4. Create admin user and follow instructions
   `python manage.py createsuperuser`
5. Run server
   `python manage.py runserver`
6. Login with created admin account

## Full demo

### **Admin dashboard**

After setup, login with the newly created account.

![](assets/20230718_150037_image.png)

Logging in as an admin takes the user to the admin dashboard. Here, admins can manage users, rooms, bookings as well as make bookings themselves.

![](assets/20230718_150154_image.png)

Clicking on User management allows admins to add and remove users.

![](assets/20230718_150408_image.png)

Clicking on staff/admin account takes the user to the account signup form. Admins can assign if the newly created user should be made an admin or staff account.

![](assets/20230718_150600_image.png)

Upon form submission, admins are taken back to User management:

![](assets/20230718_150729_image.png)

Now back to the dashboard by clicking Home.

![](assets/20230718_150851_image.png)

Room creation, modification and deletion is handled in Room management:

![](assets/20230718_151130_image.png)

The room creation form asks for a room name, room capacity and image.

![](assets/20230718_151212_image.png)

Upon form submission, the user is taken back to Room management.

![](assets/20230718_151252_image.png)

More rooms can be created:

![](assets/20230718_151501_image.png)

Rooms can have their name and capacity modified. For example, here Room Red has changed to Room Purple and has a new capacity of 10 people. The form is also autofilled with Room Red's old name and old capacity before editing.

![](assets/20230718_151716_image.png)

![](assets/20230718_151731_image.png)

Deleting rooms requires an additional confirmation:

![](assets/20230718_151904_image.png)

![](assets/20230718_151917_image.png)

Returning back to the dashboard shows the 'Rooms available now' counter updated from 0 to 2, since 2 new rooms have been made with no bookings happening for them right now.

![](assets/20230718_152407_image.png)

Booking creation, modification and deletion is handled in Booking management. Admins can see all bookings made by all users.

![](assets/20230718_152541_image.png)

The booking creation form asks for a room to be a selected as well as an appropriate time. Date and time inputs are handled with `django-datetime-widget` and limited so that users are only permitted to make bookings for the future. A room image carousel allows the users to preview the rooms and clicking on 'Check availability' allows users to confirm that no other bookings conflicts with theirs.

![](assets/20230718_152744_image.png)

Upon form submission, the user is taken back to Booking management.

![](assets/20230718_153128_image.png)

Creating another booking that lies on the same day as another, is valid and clicking on 'Check availability' will result in a availability confirmation message, as well as display all the current bookings for that day allowing users to adjust their bookings easily.

![](assets/20230718_153405_image.png)

Creating a booking that conflicts with another will display an error message. Ignoring the message and clicking on 'Make booking' will result in the invalid booking page.

![](assets/20230718_153539_image.png)

![](assets/20230718_153655_image.png)

Creating another valid booking and returning to the dashboard updates the 'Bookings made' counter. When a meeting begins, the 'Meetings happening now' counter increments and the 'Rooms available now' counter decrements.

![](assets/20230718_153814_image.png)

![](assets/20230718_154040_image.png)

Deleting a booking requires additional confirmation. Both staff and admin users are given an alert on their dashboard when an admin deletes their booking which can be cleared by clicking 'Ok'.

![](assets/20230718_154127_image.png)

![](assets/20230718_154224_image.png)

![](assets/20230718_154245_image.png)

![](assets/20230718_154326_image.png)

### **Staff dashboard**

Logging out and logging back in using a staff account:

![](assets/20230718_154346_image.png)

The staff dashboard only allows users to make bookings.

![](assets/20230718_154550_image.png)

Staff users can also only see their own bookings, unlike admins. See the admin booking demonstration to see the booking functionality.

![](assets/20230718_154621_image.png)

## Known bugs

**Major**

* ~Users can overlap booking time slots for the same room~
* ~Users can put end time before start time when booking room~
* ~Staff can access create room, book room, create user by hardcode entering url~

**Minor**

* Changing start time to be after end time when modifying booking after creation opens new ValidationError page instead of displaying on current page
* Creating room with non unique name prevents adding but doesn't display error message or redirect anywhere
* Header text jumps back and forth sometimes?

## Features to add

* ~~Alert users when an admin has deleted their booking / room they booked~~
* ~~Allow users to see the booking history for diferent rooms~~
* ~~Break up admin home page layout into 3 buttons - account management, room management, booking management (put tables behind them)~~
* ~~Meetings happening now counter not hooked up~~
* ~~Rooms available now counter not hooked up~~
