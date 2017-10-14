package usr.stokkers.no;

public class Main {
    public static void main(String[] args) {
        Hotel hotel = new Hotel("Hotel22");
        System.out.print(hotel.createRoom(101, 4, RoomType.FAMILY));
    }
}
