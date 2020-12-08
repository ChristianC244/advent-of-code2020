package customClass;

public class Edge {
    private Node from;
    private Node to;
    private int canContain;

    public Edge(Node from, Node to, int contains){
        this.from = from;
        this.to = to;
        this.canContain = contains;
    }

    public int getContains() {
        return canContain;
    }

    public Node getFrom() {
        return from;
    }
    
    
    public Node getTo() {
        return to;
    }

    public String toString() {
        return from + " ---[" + canContain + "]---> " + to;
    }
}
