/*
 Given an array of integers, return a new array such that,
 each element at index i of the new array is the product of 
 all the numbers in the original array except the one at i
 Note :- Don't use division..	
*/
import java.util.*;
class Problem4 {
	public static void main(String[] args) {
		// Scanner kb = new Scanner(System.in);
		int []arr = new int[]{1, 2, 3, 4, 5};
		// 1 2 3 4 5 
		// 1
		int []ans = new int[5];
		for (int i = 0; i < arr.length; i++) {
			int prod = 1;
			for (int j = 0; j < arr.length; j++) {
				if (i!=j)
					prod = prod * arr[j];
			}
			ans[i] = prod;
		}
		for (int i : ans) System.out.print(i + " ");
 	}
}