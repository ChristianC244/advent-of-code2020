import customClass.*;

import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files
import java.util.regex.*;


public class HandyHaversacks {

    public static void main(String[] args) {
        final String regexMain = "(\\d+) (\\w+\\s\\w+) bag";
        final String regexSplit = "^(.+) bags contain(.+)";

        Pattern splitter = Pattern.compile(regexSplit);
        Pattern finder = Pattern.compile(regexMain);


        Rules graph = new Rules();

        try {
            File myObj = new File("input.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();

                Matcher spl = splitter.matcher(data);
                while(spl.find()) {
                    //spl.group(1) <- Head
                    //spl.group(2) <- Tail
                    Matcher fnd = finder.matcher(spl.group(2));
                    while(fnd.find()) {
                        //fnd.group(1) <- Digits
                        //fnd.group(2) <- Bag name
                        graph.addBags(spl.group(1), fnd.group(2), Integer.parseInt(fnd.group(1)));
                    }
        
                }
                
              
            }
            myReader.close();
        }catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
          }

          System.out.println(graph);
          System.out.println("The Solution to part One is: " + graph.containedIn("shiny gold"));
          System.out.println("The Solution to part Two is: " + graph.howManyBags("shiny gold"));

    }
}
