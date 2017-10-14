package com.oleast;


import java.util.ArrayList;

/**
 * Created by oleast on 29.09.17.
 */
public class MyLinkedList<T> {
    private Node<T> head;

    public MyLinkedList(T t) {
        this.head = new Node<T>(t);
    }

    public Node<T> getTail() {
        Node<T> tail = head;
        while(tail.hasNext()) {
            tail = tail.getNext();
        }
        return tail;
    }

    public void add(T t) {
        Node<T> tail = getTail();
        tail.push(new Node<T>(t));
    }

    public ArrayList<T> toArrayList() {
        Node<T> current = this.head;
        ArrayList<T> al = new ArrayList<>();
        al.add(current.getValue());
        while(this.head.hasNext()) {
            current = current.getNext();
            al.add(current.getValue());
        }
        return al;
    }

    public int getLength() {
        int i = 1;
        Node<T> current = this.head;
        while(current.hasNext()) {
            current = current.getNext();
            i++;
        }
        return i;
    }
    public int size() {
        return getLength();
    }
}
