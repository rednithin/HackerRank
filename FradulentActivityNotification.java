import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {
  // Complete the activityNotifications function below.
  public static void addToHeap(int number, PriorityQueue<Integer> lower, PriorityQueue<Integer> higher) {
    if (lower.size() == 0 || number < lower.peek()) {
      lower.add(number);
    } else {
      higher.add(number);
    }
  }

  public static void rebalance(PriorityQueue<Integer> lower, PriorityQueue<Integer> higher) {
    PriorityQueue<Integer> smaller = lower.size() < higher.size() ? lower : higher;
    PriorityQueue<Integer> bigger = lower.size() >= higher.size() ? lower : higher;

    if (bigger.size() - smaller.size() >= 2) {
      smaller.add(bigger.poll());
    }
  }

  public static double getMedian(PriorityQueue<Integer> lower, PriorityQueue<Integer> higher) {
    PriorityQueue<Integer> smaller = lower.size() < higher.size() ? lower : higher;
    PriorityQueue<Integer> bigger = lower.size() >= higher.size() ? lower : higher;

    if (bigger.size() == smaller.size()) {
      return ((double) bigger.peek() + smaller.peek()) / 2;
    } else {
      return bigger.peek();
    }
  }

  public static void deleteFromHeap(int number, PriorityQueue<Integer> lower, PriorityQueue<Integer> higher) {
    if (number <= lower.peek()) {
      lower.remove(number);
    } else {
      higher.remove(number);
    }
  }

  static int activityNotifications(int[] expenditure, int d) {
    PriorityQueue<Integer> lower = new PriorityQueue<Integer>(new Comparator<Integer>() {
      @Override
      public int compare(Integer a, Integer b) {
        return b - a;
      }
    });
    PriorityQueue<Integer> higher = new PriorityQueue<Integer>();
    int notifications = 0;

    for (int i = 0; i < d; i++) {
      addToHeap(expenditure[i], lower, higher);
      rebalance(lower, higher);
    }

    for (int i = d; i < expenditure.length; i++) {
      double median = getMedian(lower, higher);
      if (expenditure[i] >= 2 * median) {
        notifications++;
      }
      deleteFromHeap(expenditure[i - d], lower, higher);
      rebalance(lower, higher);
      addToHeap(expenditure[i], lower, higher);
      rebalance(lower, higher);
    }

    return notifications;
  }

  private static final Scanner scanner = new Scanner(System.in);

  public static void main(String[] args) throws IOException {
    BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

    String[] nd = scanner.nextLine().split(" ");

    int n = Integer.parseInt(nd[0]);

    int d = Integer.parseInt(nd[1]);

    int[] expenditure = new int[n];

    String[] expenditureItems = scanner.nextLine().split(" ");
    scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

    for (int i = 0; i < n; i++) {
      int expenditureItem = Integer.parseInt(expenditureItems[i]);
      expenditure[i] = expenditureItem;
    }

    int result = activityNotifications(expenditure, d);

    bufferedWriter.write(String.valueOf(result));
    bufferedWriter.newLine();

    bufferedWriter.close();

    scanner.close();
  }
}
