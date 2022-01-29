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
}
<?php
$target_dir = "uploads/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));

// Check if image file is a actual image or fake image
if(isset($_POST["submit"])) {
  $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);
  if($check !== false) {
    echo "File is an image - " . $check["mime"] . ".";
    $uploadOk = 1;
  } else {
    echo "File is not an image.";
    $uploadOk = 0;
  }
}

// Check if file already exists
if (file_exists($target_file)) {
  echo "Sorry, file already exists.";
  $uploadOk = 0;
}

// Check file size
if ($_FILES["fileToUpload"]["size"] > 500000) {
  echo "Sorry, your file is too large.";
  $uploadOk = 0;
}

// Allow certain file formats
if($imageFileType != "jpg" && $imageFileType != "png" && $imageFileType != "jpeg"
&& $imageFileType != "gif" ) {
  echo "Sorry, only JPG, JPEG, PNG & GIF files are allowed.";
  $uploadOk = 0;
}

// Check if $uploadOk is set to 0 by an error
if ($uploadOk == 0) {
  echo "Sorry, your file was not uploaded.";
// if everything is ok, try to upload file
} else {
  if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
    echo "The file ". htmlspecialchars( basename( $_FILES["fileToUpload"]["name"])). " has been uploaded.";
  } else {
    echo "Sorry, there was an error uploading your file.";
  }
}
?>
