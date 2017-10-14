package usr.stokkers.no;

import java.util.concurrent.atomic.AtomicInteger;

public class Room {
    private static AtomicInteger counter = new AtomicInteger();
    private final int id;
    private int roomNumber;
    private int maxOccupants;
    private RoomType type;
    private final Hotel hotel;

    /**
     * Creates a Room based on the given parameters.
     * @param roomNumber Room number identifying this room in this Hotel, unique only to connected Hotel.
     * @param maxOccupants Maximum number of occupants this room can have at any given moment.
     * @param type Descriptive RoomType
     */
    public Room(int roomNumber, int maxOccupants, RoomType type, Hotel hotel) {
        this.id = counter.getAndIncrement();
        this.roomNumber = roomNumber;
        this.maxOccupants = maxOccupants;
        this.type = type;
        this.hotel = hotel;
    }

    /**
     * Overrides built in toString() method.
     * @return Formatted and descriptive string for the Room.
     */
    @Override
    public String toString() {
        String s = "Room ID: " + this.id  + "\n"
                 + "Room Number: " + this.roomNumber + "\n"
                 + "Max Occupants: " + this.maxOccupants + "\n"
                 + "Room Type: " + this.type + "\n"
                 + "Connected Hotel: " + this.hotel.getName() + "\n";
        return s;
    }

    /**
     * Gets the id of this Room.
     * @return This rooms' id.
     */
    public int getId() {
        return this.id;
    }

    /**
     * Gets the room number of this room.
     * @return this rooms' room number.
     */
    public int getRoomNumber() {
        return this.roomNumber;
    }

    /**
     * Gets the maximum number of occupants this room can have at any given moment.
     * @return this rooms' max occupants.
     */
    public int getMaxOccupants() {
        return this.maxOccupants;
    }

    /**
     * Gets ths hotel connected to this room.
     * @return this rooms' hotel.
     */
    public Hotel getHotel() { return this.hotel; }
}
