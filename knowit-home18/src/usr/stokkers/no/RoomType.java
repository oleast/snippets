package usr.stokkers.no;

public enum RoomType {
    SINGLE("Single"), DOUBLE("Double"), FAMILY("Family");

    private final String typeName;

    private RoomType(String typeName) {
        this.typeName = typeName;
    }
}
