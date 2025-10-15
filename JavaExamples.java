import java.util.*;

// example - iterate through HashMap in java using for each loop
public class JavaExamples {
    public static void main(String[] args) {
        System.out.println("Running HashMapIteration!");

        HashMap<String, Integer> map = new HashMap<>();
        map.put("a", 1);
        map.put("b", 2);
        map.put("c", 3);
        
        //entrySet method is used get both key and values in a HashMap
        for(var entry : map.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }
}

// New class to run different code
class ListDS {
    public static void main(String[] args) {
        System.out.println("Running ListDS!");
        
        // ArrayList - index-centric
        ArrayList<String> arrList = new ArrayList<>();
        arrList.add("A");
        arrList.set(0, "B");    // replace by index
        String item = arrList.get(0);   // get by index
        System.out.println("arrList at index 0: " + item);
        System.out.println("arrList: " + arrList);
        System.out.println("--------------");

        // LinkedList - front/back-centric
        LinkedList<String> linkedList = new LinkedList<>();
        linkedList.addFirst("A");    // add to front
        linkedList.addLast("B");    // add to back
        String first = linkedList.getFirst();   // get from front
        System.out.println("LL first: " + first); 
        linkedList.removeFirst();   // remove from front
        System.out.print("LL after remove from front: " + linkedList);
    }
}