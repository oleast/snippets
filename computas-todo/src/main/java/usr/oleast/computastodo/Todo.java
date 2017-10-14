package usr.oleast.computastodo;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.concurrent.atomic.AtomicInteger;

import java.lang.String;

/**
 * Created by oleast on 25.09.17.
 */

@RestController
@CrossOrigin
@RequestMapping("/api/todo")
public class Todo {
    private static AtomicInteger counter = new AtomicInteger();
    public int id;
    public String text;

    public Todo() {
        this.id = counter.getAndIncrement();
    }

    public Todo(String text) {
        this();
        this.text = text;
    }

    public int getId() {
        return this.id;
    }
}
