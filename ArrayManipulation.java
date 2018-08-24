
//https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

  // Complete the arrayManipulation function below.
  static long arrayManipulation(int n, int[][] queries) {
    Map<Integer, Integer> map = new TreeMap<Integer, Integer>();
    for (int i = 0; i < queries.length; i++) {
      map.put(queries[i][0], map.getOrDefault(queries[i][0], 0) + queries[i][2]);
      map.put(queries[i][1] + 1, map.getOrDefault(queries[i][1] + 1, 0) - queries[i][2]);
    }
    long max = 0;
    long sum = 0;
    for (Integer key : map.keySet()) {
      sum += map.get(key);
      if (sum > max) {
        max = sum;
      }
    }
    return max;
  }

  private static final Scanner scanner = new Scanner(System.in);

  public static void main(String[] args) throws IOException {
    BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

    String[] nm = scanner.nextLine().split(" ");

    int n = Integer.parseInt(nm[0]);

    int m = Integer.parseInt(nm[1]);

    int[][] queries = new int[m][3];

    for (int i = 0; i < m; i++) {
      String[] queriesRowItems = scanner.nextLine().split(" ");
      scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

      for (int j = 0; j < 3; j++) {
        int queriesItem = Integer.parseInt(queriesRowItems[j]);
        queries[i][j] = queriesItem;
      }
    }

    long result = arrayManipulation(n, queries);

    bufferedWriter.write(String.valueOf(result));
    bufferedWriter.newLine();

    bufferedWriter.close();

    scanner.close();
  }
}
