public class test {
    public test()
    {
        System.out.print("testing 123 ");
    }
}

public class childtest extends test {
    public child()
    {
            System.out.print("testing 321 ");
    }
}


public class Program {
    public static void main(String[] args){
        childtest a = new childtest();
    }
}

