function shuffleArray(array) {
    for (var i = array.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}
$( document ).ready(function() {
  $.get('buffalo.txt', function(data) {
    posts = data.split("/p")
    shuffleArray(posts)
    // console.log(data)
    body = posts[0]
    let i = 0;
    setInterval(function(){
      i = i+1
      body = posts[i]
      html_str = `<tr> <td align="center" valign="top" width="150" bgcolor="" style="word-wrap: break-word"> <div class="whitetext12"> Buffalo </div> <br> <br> <img src="http://www.ci.buffalo.ny.us/files/1_2_1/public%20art%20website/Images/David.jpg" class="comment-img"  border="0"> <div style="width:80px;height:20px;" id="UserDataNode1" class="DataPoint=OnlineNow;UserID=61789441;"></div> <br> <br> </td> <td bgcolor="white" align="left" valign="top" width="260" style="word-wrap: break-word"> <span class="blacktext10"> 3/11/2006 2:03 AM </span> <br> <br> ${body}</td> </tr> // do_something_with(data)`
      $("#comment-body").append(html_str)
    }, 40000)
  }, 'text');
});
