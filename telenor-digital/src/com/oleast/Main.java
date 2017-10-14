package com.oleast;

public class Main {

    public static void main(String[] args) {
        int[] a = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
        MyLinkedList<Integer> ll = new MyLinkedList<>(a[0]);
        for (int i = 1; i < a.length; i++) {
            ll.add(a[i]);
        }
        System.out.println(ll.size());

        String s = "Hei, jeg er en String!";
        String sr = new StringBuilder(s).reverse().toString();

        System.out.print(StringUtils.reverse(sr));
    }
}
