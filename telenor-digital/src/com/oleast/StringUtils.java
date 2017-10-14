package com.oleast;

/**
 * Created by oleast on 29.09.17.
 */
public class StringUtils {
    public static String reverse(String s) {
        char[] ca = s.toCharArray();
        StringBuilder sr = new StringBuilder();
        for (int i = ca.length-1; i >= 0; i--) {
            sr.append(ca[i]);
        }
        return sr.toString();
    }
}
