import java.net.URI;
import java.net.URISyntaxException;
import java.lang.Object;

class solution {
    public static void main(String[] args) throws URISyntaxException {
    URI uri = new URI("mongodb+srv://readonly:readonly@covid-19.hip2i.mongodb.net/covid19");
    URI def = uri;
    System.out.print(def);
    System.out.print(def.getUserInfo());
    }
}