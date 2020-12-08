package customClass;

import java.util.Stack;

public class Rules {
    private Node[] nodes;
    private int nodesCurrent;
    private int nodesSize;

    private Edge[] edges;
    private int edgesCurrent;
    private int edgesSize;

    public Rules() {
        nodesSize = 2;
        nodesCurrent = 0;
        nodes = new Node[nodesSize];

        edgesSize = 2;
        edgesCurrent = 0;
        edges = new Edge[edgesSize];
    }

    public void addBags(String extern, String intern, int contains) { 
        
        boolean extFound = false;
        boolean intFound = false;
        int toIndex = 0;
        int fromIndex = 0;
        // Search thorough nodes[] for extern
        // if !found --> add extern to nodes
        // Search thorough nodes[] for intern
        // if !found --> add intern to nodes
        for(int i=0; i<nodesCurrent; i++) {
            if(nodes[i].getName().equals(extern)) {
                extFound = true;
                fromIndex = i;
            }
            if(nodes[i].getName().equals(intern)) {
                intFound = true;
                toIndex =i;
            }
        }

        if (nodesCurrent +1 >= nodesSize) {
            nodes = Util.IncreaseSize(nodes, nodesSize);
            nodesSize *= 2;
        }
        if (!extFound) {
            nodes[nodesCurrent++] = new Node(extern);
            fromIndex = nodesCurrent-1;
        }
        if (!intFound) {
            nodes[nodesCurrent++] = new Node(intern);
            toIndex = nodesCurrent-1;
        }

        // Create edge (extern --[contains]--> intern) in edges[]
        if (edgesCurrent +1 >= edgesSize) {
            edges = Util.IncreaseSize(edges, edgesSize);
            edgesSize *= 2;
        }
        edges[edgesCurrent++] = new Edge(nodes[fromIndex], nodes[toIndex], contains);
        
    }

    public String toString() {
        String str = "GRAPH:\n";
        
        for(int i=0; i<nodesCurrent; i++) {
            str += nodes[i] + "\n";
            for (int j=0; j<edgesCurrent; j++) {
                if (edges[j].getFrom().getName().equals(nodes[i].getName())) {
                    str += "|-" + edges[j] +"\n";
                }
            }
        }
        
        return str;
    }

    public int containedIn(String start) {
        // Function for Part One Question
        int counter = 0;
        Stack<String> saves = new Stack<String>();
        boolean found = false;
        int lookedSize = 2;
        int lookedCurrent = 0;
        String[] looked = new String[lookedSize];

        saves.push(start);
        // Search for @param start

        while(!saves.isEmpty()) {
            String current = saves.pop();
            for(int i=0; i<edgesCurrent; i++) {
                if (edges[i].getTo().getName().equals(current)) {
                    found = false;
                    for (int j=0; j<lookedSize;j++) {
                        // Check if already looked at Node getFrom()
                        if (edges[i].getFrom().getName().equals(looked[j])) found = true;
                    }

                    if (!found) {
                        // If first time for this target, than save it to looked array
                        counter++;
                        saves.push(edges[i].getFrom().getName());
                        if (lookedCurrent +1 >= lookedSize) {
                            //Classic check to see if have to increase arrraySize
                            looked = Util.IncreaseSize(looked, lookedSize);
                            lookedSize *= 2;
                        }
                        looked[lookedCurrent++] = edges[i].getFrom().getName();
                    }
                    
                }
            }
        }
        return counter;
    }


    public int howManyBags(String start) {
        
        return howManyBags(start, 1) -1;
    }

    private int howManyBags(String start, int value) {
        int ret =0;
        for (int i=0; i<edgesCurrent; i++) {
            if (start.equals(edges[i].getFrom().getName())) {
                //When i find an edge that starts from start
                ret += howManyBags(edges[i].getTo().getName(), value * edges[i].getContains());
                
            }
        }
        value += ret;
        return value;
    }

}
