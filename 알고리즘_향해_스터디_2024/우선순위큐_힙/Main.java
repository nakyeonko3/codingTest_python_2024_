import java.util.PriorityQueue;

public class Main {
public class FindingKthElement {
    public int findKthLargest(int[] nums, int k) {
        // 최소힙(최소 값이 우선순위인 큐)으로 정렬이 된다.
        // 루트 값은 최소값으로 유지된다.
        // 삭제나 조회 시 항상 루트 노드만 반환된다.
        // 루트 노드 외에는 값은 정렬되지 않는다.
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        // 최대힙(최대 값이 우선순위인 큐)
        // PriorityQueue<Integer> priorityQueueHighest = new PriorityQueue<>(Collections.reverseOrder());
        // 예시) nums = {3, 2, 1, 4}, k=2 
        for (int num : nums) {
            // nums에 원소들을 하나씩 최소힙에 추가한다. 
            minHeap.offer(num);
            
            // nums에 원소가 k개를 넘어가면 첫 번째 값(최소값)을 제거하고  

            if (minHeap.size() > k) {
                minHeap.poll();
            }
        }
             // {3, 4}

        // 3을 리턴
        return minHeap.poll();
    }
}
}
