import customClass.*;

public class Test {

    public static void main(String[] args) {
        Rules rules = new Rules();
        rules.addBags("a","b",3);
        rules.addBags("a","c",1);
        rules.addBags("a","d",2);
        rules.addBags("d","e",2);

        int c = rules.containedIn("e");
        System.out.println(c);
        System.out.println(rules);

        System.out.print("The Solution to part Two is: " + rules.howManyBags("a"));
    }


    
    
}
