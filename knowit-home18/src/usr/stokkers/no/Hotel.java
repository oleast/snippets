package usr.stokkers.no;

import java.util.HashMap;

/**
 *
 */
public class Hotel {
    private HashMap<Integer, Room> rooms = new HashMap<>();
    private String name;

    /**
     * Creates a Hotel
     * *Is supposed to check that the name is valid? Throw exception?*
     * @param name Name of the Hotel that is created.
     */
    public Hotel(String name) throws IllegalArgumentException {
        if (name.toLowerCase().matches("^[a-zA-Z0-9_\\-\\s]*$")) {
            this.name = name;
        } else {
            for (char c : name.toCharArray()) {
                if (!Character.isAlphabetic(c)) {
                    throw new IllegalArgumentException("Hotel name illegal character: " + c);
                }
            }
            throw new IllegalArgumentException("Hotel name contains illegal characters, please only use characters in the latin alphabet");
        }
    }

    /**
     * Creates a Room with given parameters.
     * Adds the created Room to this hotels' catalogue.
     * Returns the created Room.
     * @param roomNumber Room number given to the Hotel Room.
     * @param maxOccupants Maximal number of occupants the room can have
     * @param roomType The Room Categorization.
     * @return the created Room.
     */
    public Room createRoom(int roomNumber, int maxOccupants, RoomType roomType) throws IllegalArgumentException {
        if (!rooms.containsKey(roomNumber)) {
            Room room = new Room(roomNumber, maxOccupants, roomType, this);
            rooms.put(room.getRoomNumber(), room);
            return room;
        }
        throw new IllegalArgumentException("This Hotel already has a Room with the given roomNumber");
    }

    /**
     * Gets the amount of rooms this Hotel has.
     * @return this hotels' room count.
     */
    public int getRoomCount() {
        return rooms.size();
    }

    /**
     * Gets a Room with the given room number.
     * @param roomNumber
     * @return Room with given room number.
     * @throws IllegalArgumentException if this Hotel does not have Room with that number.
     */
    public Room getRoom(int roomNumber) throws IllegalArgumentException {
        if (rooms.containsKey(roomNumber)) {
            return rooms.get(roomNumber);
        }
        throw new IllegalArgumentException("This hotel does not contain a Room with room number: " + roomNumber);
    }

    /**
     * Gets the name of this Hotel.
     * @return this hotels' name.
     */
    public String getName() {
        return this.name;
    }

    /**
     * Overrides standard object toString to print the Object.
     * @return String describing the Object.
     */
    @Override
    public String toString() {
        String s = "Hotel Name: " + this.name + "\n"
                 + "Number of Rooms: " + this.getRoomCount() + "\n";
        return s;
    }
}
