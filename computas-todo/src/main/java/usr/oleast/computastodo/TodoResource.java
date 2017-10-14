package usr.oleast.computastodo;

import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

/**
 * Created by oleast on 25.09.17.
 */

@RestController
@CrossOrigin
@RequestMapping("/api/todo")
public class TodoResource {
    private Map<Integer, Todo> todos = new HashMap<>();

    @RequestMapping(method = RequestMethod.GET, produces = MediaType.APPLICATION_JSON_VALUE)
    public Collection<Todo> getTodos() {
        return todos.values();
    }

    @RequestMapping(value = "{id}", method = RequestMethod.DELETE, produces = MediaType.APPLICATION_JSON_VALUE)
    public Collection<Todo> deleteTodo(String id) {
        todos.remove(id);
        return todos.values();
    }

    @RequestMapping(value = "{data}", method = RequestMethod.POST, produces = MediaType.APPLICATION_JSON_VALUE)
    public Todo createTodo(String data) {
        Todo t = new Todo(data);
        todos.put(t.getId(), t);
        return t;
    }
}