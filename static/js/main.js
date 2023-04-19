function displayTime() {
        var date = new Date();
        var hours = date.getHours();
        var minutes = date.getMinutes();
        var seconds = date.getSeconds();
        var meridian = "AM";

        if (hours > 12) {
            hours -= 12;
            meridian = "PM";
        }

        if (hours === 0) {
            hours = 12;
        }

        if (minutes < 10) {
            minutes = "0" + minutes;
        }

        if (seconds < 10) {
            seconds = "0" + seconds;
        }

        var time = hours + ":" + minutes + ":" + seconds + " " + meridian;
        document.getElementById("clock").innerHTML = time;
    }

    setInterval(displayTime, 1000);
