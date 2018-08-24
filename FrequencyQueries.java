
// https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dictionaries-hashmaps
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

public class Solution {

  // Complete the freqQuery function below.
  static List<Integer> freqQuery(List<List<Integer>> queries) {
    List answers = new ArrayList();
    Map<Integer, Integer> frequencies = new HashMap<Integer, Integer>();
    Map<Integer, Integer> counters = new HashMap<Integer, Integer>();
    for (List query : queries) {

      int operation = (int) query.get(0);
      int key = (int) query.get(1);
      int frequency = (int) frequencies.getOrDefault(key, 0);

      if (operation == 1) {
        if (counters.containsKey(frequency))
          counters.put(frequency, counters.getOrDefault(frequency, 0) - 1);
        frequencies.put(key, ++frequency);
        counters.put(frequency, counters.getOrDefault(frequency, 0) + 1);
      }
      if (operation == 2) {
        if (frequency > 0) {
          counters.put(frequency, counters.getOrDefault(frequency, 0) - 1);
          frequencies.put(key, --frequency);
          counters.put(frequency, counters.getOrDefault(frequency, 0) + 1);
        }
      }
      if (operation == 3) {
        if (counters.getOrDefault(key, 0) > 0) {
          answers.add(1);
        } else {
          answers.add(0);
        }
      }
    }
    return answers;
  }

  public static void main(String[] args) throws IOException {
    BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

    int q = Integer.parseInt(bufferedReader.readLine().trim());

    List<List<Integer>> queries = new ArrayList<>();

    IntStream.range(0, q).forEach(i -> {
      try {
        queries.add(Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" ")).map(Integer::parseInt)
            .collect(toList()));
      } catch (IOException ex) {
        throw new RuntimeException(ex);
      }
    });

    List<Integer> ans = freqQuery(queries);

    bufferedWriter.write(ans.stream().map(Object::toString).collect(joining("\n")) + "\n");

    bufferedReader.close();
    bufferedWriter.close();
  }
}
