
# ABC Room booking system

Allows staff to book rooms for a given time and date. Provides admins with additional privileges such as managing rooms, bookings and users.
sdasd


## Known bugs
**Major**

* Users can overlap booking time slots for the same room
* ~Users can put end time before start time when booking room~
* Staff can access create room, book room, create user by hardcode entering url

**Minor**
* Changing start time to be after end time when modifying booking after creation opens new ValidationError page instead of displaying on current page
* Creating room with non unique name prevents adding but doesn't display error message or redirect anywhere
* Header text jumps back and forth sometimes?

## Features to add
* Alert users when an admin has deleted their booking / room they booked
* Allow users to see the booking history for diferent rooms
* Break up admin home page layout into 3 buttons - account management, room management, booking management (put tables behind them)
* Meetings happening now counter not hooked up
* Rooms available now counter not hooked up







## Startup

Create django superuser and login as admin.



