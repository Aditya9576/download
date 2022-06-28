var mi;
window.onload =function(){mi = 0;}
function myFlip(i)
{
  var comp = document.getElementsByClassName('comp');
  if(mi == 0)
    {
      comp[i].style.transform= "rotateY(180deg)";
      mi = 1;
    }
  else
    {
      comp[i].style.transform= "rotateY(0deg)";
      mi = 0;
    }
}

function payment()
{
  window.open('http://localhost/cgi-bin/authenticate2.py')
}

