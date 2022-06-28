
function enable_info() {
    for (var i = 1; i <= 8; i++){
      if(i ==3 || i==4)
        continue;
      document.getElementsByTagName("input")[i].disabled = false;
    }
  }
  
function showPassword()
{
  document.getElementById('pass').type="text";
  setTimeout(() => {
    document.getElementById('pass').type="password";
  },2000);
}