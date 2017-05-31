


    /* global documnet */

    "use strict";
var ctx;
var canvas;
var imgData;
var keepBottom;
var keepTop;


    function textChangeListener (evt) {
      var id = evt.target.id;
      var text = evt.target.value;

      if (id === "topLineText") {
        window.topLineText = text;
      } else {
        window.bottomLineText = text;
      }
      redrawMeme(window.topLineText, window.bottomLineText);
    }



    function redrawMeme(topLine, bottomLine) {
      // Get Canvas2DContex
      ctx.putImageData(imgData,0,0);
      keepTop = topLine;
      keepBottom = bottomLine;
      if(keepTop !== null) {
        textDrawer(topLine, canvas.width /2, 40);}
      if(keepBottom !== null) {
        textDrawer(bottomLine, canvas.width /2, canvas.height-20);}
    }

    function textDrawer (text, x , y) {
        ctx.font = "36px Impact";
        ctx.textAlign = 'center';
        ctx.strokeStyle = "black";
        ctx.lineWidth = 3;
        ctx.strokeText(text, x, y);
        ctx.fillStyle = "white";
        ctx.fillText(text, x, y);
    }


    function saveFile() {
      window.open(document.querySelector('canvas').toDataURL());
    }


    function handleFileSelect(evt) {

      var file = evt.target.files[0];



      var reader = new FileReader();
      reader.onload = function(fileObject) {
        var data = fileObject.target.result;

        // Create an image object
        var image = new Image();
        image.onload = function() {
          window.imageSrc = this;
          canvas = document.querySelector('canvas');
          ctx = canvas.getContext("2d");
          ctx.drawImage(window.imageSrc, 0, 0, canvas.width, canvas.height);
          imgData = ctx.getImageData(0,0, canvas.width, canvas.height);
          redrawMeme(null, null);
        };

        // Set image data to background image.
        image.src = data;

      };
      reader.readAsDataURL(file);
    }

    function colorChange() {

        for (var i=0;i<imgData.data.length;i+=4) {
            var red = imgData.data[i];
            var green = imgData.data[i+1];
            var blue = imgData.data[i+2];
            var grey =  0.2126 * red + 0.7152 * green + 0.0722 * blue;
            imgData.data[i] = grey;
            imgData.data[i+1] = grey;
            imgData.data[i+2] = grey;
        }
        redrawMeme(keepTop, keepBottom);

    }

    function resetClick() {
          ctx.drawImage(window.imageSrc, 0, 0, canvas.width, canvas.height);
          imgData = ctx.getImageData(0,0, canvas.width, canvas.height);
          input1.value = "";
          input2.value = "";
          window.topLineText = "";
          window.bottomLineText = "";
          redrawMeme(null, null);
    }

    window.topLineText = "";
    window.bottomLineText = "";
    var input1 = document.getElementById('topLineText');
    var input2 = document.getElementById('bottomLineText');
    input1.oninput = textChangeListener;
    input2.oninput = textChangeListener;
    document.getElementById('file').addEventListener('change', handleFileSelect, false);
    document.querySelector('button#saveBtn').addEventListener('click', saveFile, false);
    document.querySelector('button#colorXhange').addEventListener('click', colorChange, false);
    document.querySelector('button#reset').addEventListener('click', resetClick, false);