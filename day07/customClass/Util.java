package customClass;

public class Util {

    public static Edge[] IncreaseSize(Edge[] Array, int currentSize) {
        Edge[] tmp = new Edge[currentSize*2];
        System.arraycopy(Array, 0, tmp, 0, currentSize);
        return tmp;
    }
    
    public static Node[] IncreaseSize(Node[] Array, int currentSize) {
        Node[] tmp = new Node[currentSize*2];
        System.arraycopy(Array, 0, tmp, 0, currentSize);
        return tmp;
    }
    public static String[] IncreaseSize(String[] Array, int currentSize) {
        String[] tmp = new String[currentSize*2];
        System.arraycopy(Array, 0, tmp, 0, currentSize);
        return tmp;
    }
}
