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
    // successful api import in html. try to figure out doing so well in java.
    
    // window.onload = function() {
        // L.mapquest.key = 'Kkulaafxam9iXADKMFedCV9JsENBp7Yc';

        // // map refers to a <div> element with the ID map
        // var map = L.mapquest.map('map', {
        //   center: [47.604325816529375, -122.1713779290056],
        //   layers: L.mapquest.tileLayer('map'),
        //   zoom: 12
        // });
    //   }

#!/usr/bin/env python

import pandas as pd

data = {"state": ["Washington", "Texas", "California", "Florida", "New York"],
        "capital": ["Olympia", "Austin", "Sacramento", "Tallahassee", "Albany"],
        "covid": [],
        "population": [7.61, 29, 39.51, 21.48, 8.42]}

frame = pd.DataFrame(data)
print(frame)

print('------------------------------')

frame.index = ["WA", "TE", "CA", "FL", "NE"]
print(frame)

//this creates their own custom index with the printed data frame 

