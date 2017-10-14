package usr.stokkers.no;

import org.junit.*;

import static org.junit.Assert.fail;

public class HotelTest {

    String correctHotelName = "Scandic Lerkendal";
    String wrongHotelName = "?";

    @Test
    public void wrongHotelNameTest() {
        try {
            new Hotel(wrongHotelName);
            fail("Hotel created with illegal character");
        } catch(IllegalArgumentException e) {
        }
    }

    @Test
    public void correctHotelNameTest() {
        try {
            new Hotel(correctHotelName);
        } catch(IllegalArgumentException e) {
            throw e;
        }
    }
}