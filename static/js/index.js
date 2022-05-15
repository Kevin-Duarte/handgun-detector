var dropZone = document.getElementById('window-image');

dropZone.addEventListener('dragover', function(e) {
    e.stopPropagation();
    e.preventDefault();
    e.dataTransfer.dropEffect = 'copy';
});

dropZone.addEventListener('drop', function(e) {
    e.stopPropagation();
    e.preventDefault();
    document.getElementById('analysis-text').value = '';

    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function(){
        if (xhr.readyState == XMLHttpRequest.DONE){
            if (xhr.status == 200)
            {
                var detected = JSON.parse(xhr.responseText)['detection'];
                if (detected == 'true')
                    document.getElementsByTagName('img')[0].style.setProperty('filter', 'grayscale(100%) brightness(40%) sepia(100%) hue-rotate(-50deg) saturate(600%) contrast(0.8)','');
                else
                    document.getElementsByTagName('img')[0].style.setProperty('filter', 'grayscale(100%) sepia(100%) hue-rotate(90deg)','');
                document.getElementById('analysis-text').value = xhr.responseText;
            }
            else
            {
                
                document.getElementById('analysis-text').value = xhr.responseText;
            }
            
        }
    }


    var files = e.dataTransfer.files; // Array of all files
    if (files[0].type.match(/image.*/)) {
        var reader = new FileReader();
        reader.onload = function(e2) {
            var img = document.createElement('img');
            img.src= e2.target.result;
            img.style.width= '100%';
            img.style.maxHeight = '60vh';
            
            document.getElementById('window-image').innerHTML = '';
            document.getElementById('window-image').appendChild(img);
        }

        reader.readAsDataURL(files[0]); // start reading the file data.
    }


    var formData = new FormData()
    formData.append('image', files[0])
    xhr.open("POST", "/anon/gun-check", true);
    xhr.send(formData);
});