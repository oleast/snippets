package com.oleast;

/**
 * Created by oleast on 29.09.17.
 */
public class Node<T> {

    private T value;
    private Node<T> next;

    public Node(T value) {
        this.value = value;
        this.next = null;
    }

    public boolean hasNext() {
        if (this.next == null) {
            return false;
        } else {
            return true;
        }
    }

    public Node<T> getNext() {
        if (hasNext()) {
            return this.next;
        } else {
            throw new IllegalArgumentException("");
        }
    }

    public void push(Node<T> t) {
        this.next = t;
    }

    public T getValue() {
        return this.value;
    }
}