import java.util.regex.*;

public class RegExTest {
    public static void main(String[] args) {
        final String t2 = "vibrant aqua bags contain 3 drab tan bags, 5 bright coral bags, 3 pale brown bags.\n";
        final String t1 = "dull aqua bags contain 2 wavy coral bags.\n";

        //final String regex = "(\\w+\\s\\w+) bag"; DEPRECATED
        final String regexMain = "(\\d+) (\\w+\\s\\w+) bag";
        final String regexSplit = "^(.+) bags contain(.+)";
        
        Pattern splitter = Pattern.compile(regexSplit);
        Matcher s = splitter.matcher(t2);
        Pattern finder = Pattern.compile(regexMain);

        String tail;

        while(s.find()) {
            System.out.println(s.group(1) + " -- " + s.group(2));
            tail = s.group(2);
            Matcher f = finder.matcher(tail);
            while(f.find()) {
                System.out.println(f.group(1) + ":" + f.group(2));
            }

        }


    }
    
}
