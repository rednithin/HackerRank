import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

  // Complete the abbreviation function below.
  static String abbreviation(String a, String b) {
    Map<Character, Integer> upperA = new HashMap<Character, Integer>();
    Map<Character, Integer> upperB = new HashMap<Character, Integer>();
    for (char c : a.toCharArray()) {
      if (Character.isUpperCase(c)) {
        upperA.put(c, upperA.getOrDefault(c, 0) + 1);
      }
    }
    for (char c : b.toCharArray()) {
      upperB.put(c, upperB.getOrDefault(c, 0) + 1);
    }
    for (char key : upperA.keySet()) {
      if (upperA.get(key) > upperB.getOrDefault(key, 0)) {
        return "NO";
      }
    }

    a = a.toUpperCase();
    Set set = new HashSet();
    for (char c : b.toCharArray()) {
      set.add(c);
    }
    String newA = "";
    for (char c : a.toCharArray()) {
      if (set.contains(c)) {
        newA += c;
      }
    }
    a = newA;
    if (b.length() > a.length()) {
      return "NO";
    }
    int matrix[][] = new int[b.length() + 1][a.length() + 1];
    int length = 0;
    for (int i = 1; i <= b.length(); i++) {
      char charB = b.charAt(i - 1);
      for (int j = 1; j <= a.length(); j++) {
        char charA = a.charAt(j - 1);
        if (charA == charB) {
          matrix[i][j] = 1 + matrix[i - 1][j - 1];
          length = Math.max(length, matrix[i][j]);
        } else {
          matrix[i][j] = Math.max(matrix[i][j - 1], matrix[i - 1][j]);
        }
      }
    }
    if (b.length() == length) {
      return "YES";
    } else {
      return "NO";
    }
  }

  private static final Scanner scanner = new Scanner(System.in);

  public static void main(String[] args) throws IOException {
    BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

    int q = scanner.nextInt();
    scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

    for (int qItr = 0; qItr < q; qItr++) {
      String a = scanner.nextLine();

      String b = scanner.nextLine();

      String result = abbreviation(a, b);

      bufferedWriter.write(result);
      bufferedWriter.newLine();
    }

    bufferedWriter.close();

    scanner.close();
  }
}
